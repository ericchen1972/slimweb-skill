import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PluginTests(unittest.TestCase):
    def setUp(self):
        script = ROOT / 'scripts/build-plugins.py'
        self.assertTrue(script.exists(), 'plugin generator must exist')
        spec = importlib.util.spec_from_file_location('plugins', script)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name) / 'plugin'

    def test_targets_manifests_and_complete_skill(self):
        for target, url in self.module.TARGETS.items():
            out = self.out / target
            self.module.generate(out, 'slimweb-' + target, url)
            portable = json.loads((out / 'mcp.json').read_text())['mcpServers']['slimweb']
            self.assertEqual(portable['url'], url)
            self.assertEqual(portable['type'], 'streamable-http')
            self.assertEqual(portable['extensions']['com.openai']['auth'], {'type':'oauth','client':{'mode':'dcr'}})
            self.assertEqual(json.loads((out / '.mcp.json').read_text())['mcpServers']['slimweb'], {'type':'http','url':url})
            self.assertEqual(json.loads((out / 'plugin.json').read_text())['name'], 'slimweb-' + target)
            self.assertEqual((out / 'skills/slimweb-mcp/SKILL.md').read_bytes(), (ROOT / 'SKILL.md').read_bytes())
            for source in (ROOT / 'references').rglob('*'):
                if source.is_file():
                    self.assertEqual((out / 'skills/slimweb-mcp/references' / source.relative_to(ROOT / 'references')).read_bytes(), source.read_bytes())

    def test_exact_custom_url_and_determinism(self):
        url = 'https://merchant.example/mcp?domain=shop.example&tenant=a%2Fb'
        self.module.generate(self.out, 'slimweb-custom', url)
        before = {str(p.relative_to(self.out)):p.read_bytes() for p in self.out.rglob('*') if p.is_file()}
        self.module.generate(self.out, 'slimweb-custom', url, refresh=True)
        self.assertEqual(before, {str(p.relative_to(self.out)):p.read_bytes() for p in self.out.rglob('*') if p.is_file()})
        self.assertEqual(json.loads((self.out / '.mcp.json').read_text())['mcpServers']['slimweb']['url'], url)

    def test_rejects_unsafe_urls_and_names(self):
        for url in ['http://example.com/mcp','https://user:pass@example.com/mcp','https://example.com/mcp#x','https://','https://example.com/mcp?token=secret','https://example.com/ mcp']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.module.generate(self.out, 'slimweb-test', url)
        with self.assertRaises(ValueError):
            self.module.generate(self.out, '../escape', 'https://example.com/mcp')

    def test_never_overwrites_arbitrary_directory(self):
        self.out.mkdir()
        marker = self.out / 'user-file'
        marker.write_text('keep')
        for refresh in [False, True]:
            with self.assertRaises(FileExistsError):
                self.module.generate(self.out, 'slimweb-test', 'https://example.com/mcp', refresh=refresh)
        self.assertEqual(marker.read_text(), 'keep')

    def test_refresh_preserves_extra_files_and_rejects_target_change(self):
        self.module.generate(self.out, 'slimweb-test', 'https://example.com/mcp')
        extra = self.out / 'user-notes.txt'
        extra.write_text('preserve')
        self.module.generate(self.out, 'slimweb-test', 'https://example.com/mcp', refresh=True)
        self.assertEqual(extra.read_text(), 'preserve')
        with self.assertRaises(FileExistsError):
            self.module.generate(self.out, 'slimweb-test', 'https://other.example/mcp', refresh=True)

    def test_rejects_symlink_in_generated_tree(self):
        self.module.generate(self.out, 'slimweb-test', 'https://example.com/mcp')
        external = Path(self.temp.name) / 'external.json'
        external.write_text('keep')
        destination = self.out / 'plugin.json'
        destination.unlink()
        destination.symlink_to(external)
        with self.assertRaises(FileExistsError):
            self.module.generate(self.out, 'slimweb-test', 'https://example.com/mcp', refresh=True)
        self.assertEqual(external.read_text(), 'keep')

if __name__ == '__main__':
    unittest.main()
