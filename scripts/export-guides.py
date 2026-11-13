#!/usr/bin/env python3
"""Export canonical server guidance into an explicit new output directory."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate_topic(topic):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', topic):
        raise ValueError('topic must be lowercase kebab-case')
    if topic == 'index':
        raise ValueError('index is reserved for the server manifest')

def export(output, source_root=ROOT):
    output = Path(output).absolute()
    if output.exists() or output.is_symlink():
        raise FileExistsError('output must be a new directory: ' + str(output))
    source_root = Path(source_root)
    references = source_root / 'references'
    overview = source_root / 'guides/overview.md'
    if not references.is_dir():
        raise ValueError('canonical references directory is required')
    if references.is_symlink() or overview.is_symlink() or overview.parent.is_symlink():
        raise ValueError('canonical guide sources must not be symlinks')
    sources = [overview, *references.glob('*.md')]
    content = {}
    for source in sources:
        topic = source.stem
        validate_topic(topic)
        if topic in content:
            raise ValueError('duplicate topic: ' + topic)
        if source.is_symlink() or not source.is_file():
            raise ValueError('guide must be a regular canonical Markdown file: ' + str(source))
        content[topic] = source.read_bytes()
        content[topic].decode('utf-8')
    topics = [{'topic': topic, 'file': topic + '.md', 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)} for topic, data in sorted(content.items())]
    version_bytes = json.dumps(topics, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    manifest = {'schema_version': 1, 'guide_version': 'sha256:' + hashlib.sha256(version_bytes).hexdigest(), 'topics': topics}
    # mkdir is the exclusive-create boundary; no existing file or directory is replaced.
    output.mkdir(parents=True, exist_ok=False)
    for topic, data in sorted(content.items()):
        (output / (topic + '.md')).write_bytes(data)
    (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path, help='Explicit output directory; must not already exist')
    args = parser.parse_args()
    manifest = export(args.output)
    print(json.dumps({'output': str(args.output.absolute()), 'guide_version': manifest['guide_version'], 'topics': len(manifest['topics'])}))

if __name__ == '__main__':
    main()
