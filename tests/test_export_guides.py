import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ExportGuideTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('guides', ROOT / 'scripts/export-guides.py')
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name) / 'export'

    def test_all_topics_hashes_and_determinism(self):
        self.module.export(self.out)
        manifest = json.loads((self.out / 'manifest.json').read_text())
        self.assertEqual(manifest['schema_version'], 1)
        topics = manifest['topics']
        self.assertEqual([t['topic'] for t in topics], sorted(['overview'] + [p.stem for p in (ROOT / 'references').glob('*.md')]))
        for topic in topics:
            content = (self.out / topic['file']).read_bytes()
            self.assertEqual(hashlib.sha256(content).hexdigest(), topic['sha256'])
            self.assertEqual(len(content), topic['bytes'])
        expected = hashlib.sha256(json.dumps(topics, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(manifest['guide_version'], 'sha256:' + expected)
        before = {p.name:p.read_bytes() for p in self.out.iterdir()}
        second = Path(self.temp.name) / 'second'
        self.module.export(second)
        self.assertEqual(before, {p.name:p.read_bytes() for p in second.iterdir()})
        overview = (self.out / 'overview.md').read_text()
        self.assertFalse(overview.startswith('---'))
        self.assertIn('Tailwind-first Responsive Safety Contract', overview)

    def test_refuses_existing_directory_and_symlink(self):
        self.out.mkdir()
        (self.out / 'user-file').write_text('keep')
        with self.assertRaises(FileExistsError): self.module.export(self.out)
        self.assertEqual((self.out / 'user-file').read_text(), 'keep')
        link = Path(self.temp.name) / 'link'
        link.symlink_to(self.out)
        with self.assertRaises(FileExistsError): self.module.export(link)

    def test_rejects_path_traversal_topic_and_symlink_source(self):
        for topic in ['../secret', 'a/b', '..', 'A', 'token.json', '']:
            with self.subTest(topic=topic), self.assertRaises(ValueError):
                self.module.validate_topic(topic)
        sources = Path(self.temp.name) / 'source'
        (sources / 'guides').mkdir(parents=True)
        (sources / 'references').mkdir()
        (sources / 'guides/overview.md').write_text('# Guide')
        secret = Path(self.temp.name) / 'secret'
        secret.write_text('private token')
        (sources / 'references/secret.md').symlink_to(secret)
        with self.assertRaises(ValueError): self.module.export(self.out, sources)
        self.assertFalse(self.out.exists())

    def test_only_canonical_markdown_is_exported(self):
        sources = Path(self.temp.name) / 'source'
        (sources / 'guides').mkdir(parents=True)
        (sources / 'references').mkdir()
        (sources / 'guides/overview.md').write_text('# Overview')
        (sources / 'references/topic.md').write_text('# Topic')
        (sources / 'references/.env').write_text('SECRET=private')
        (sources / 'credentials.json').write_text('private')
        self.module.export(self.out, sources)
        self.assertEqual({p.name for p in self.out.iterdir()}, {'overview.md','topic.md','manifest.json'})
