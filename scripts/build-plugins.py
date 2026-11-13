#!/usr/bin/env python3
"""Build self-contained plugin distributions from the canonical skill sources."""
import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    'saas': 'https://slimweb-mcp-aakwcbp2ca-de.a.run.app/mcp',
    'lujiu': 'https://slimweb-standalone-mcp-27587628711.asia-east1.run.app/mcp?domain=lujiu.com.tw',
}
MARKER = '.slimweb-generated.json'

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def validate(name, url):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError('name must be lowercase kebab-case')
    parsed = urlsplit(url)
    if (parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password
            or parsed.fragment or any(c.isspace() or ord(c) < 32 for c in url)):
        raise ValueError('provide an exact HTTPS MCP URL without credentials, whitespace or fragment')
    if any(re.search(r'token|secret|password|api.?key|client.?id', key, re.I) for key, _ in parse_qsl(parsed.query)):
        raise ValueError('credentials and fixed client IDs must not be packaged')
    try:
        parsed.port
    except ValueError as exc:
        raise ValueError('invalid HTTPS port') from exc

def generate(output, name, url, refresh=False):
    validate(name, url)
    output = Path(output).absolute()
    identity = {'generator': 'slimweb-plugin-v1', 'name': name, 'url': url}
    if output.exists() or output.is_symlink():
        try:
            previous = json.loads((output / MARKER).read_text())
        except (OSError, ValueError):
            previous = None
        if output.is_symlink() or not refresh or previous != identity:
            raise FileExistsError('refusing to overwrite an existing or unrelated directory: ' + str(output))
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.slimweb-build-', dir=output.parent) as temp:
        staging = Path(temp) / 'plugin'
        skill = staging / 'skills/slimweb-mcp'
        skill.mkdir(parents=True)
        shutil.copyfile(ROOT / 'SKILL.md', skill / 'SKILL.md')
        shutil.copytree(ROOT / 'references', skill / 'references')
        metadata = {'name': name, 'version': '1.0.1', 'description': 'SlimWeb MCP and complete ecommerce workflow skill', 'author': {'name': 'SlimWeb'}, 'homepage': 'https://slimweb.tw', 'repository': 'https://github.com/ericchen1972/slimweb-skill'}
        dump(staging / 'plugin.json', {'$schema': 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', **metadata})
        dump(staging / '.claude-plugin/plugin.json', metadata)
        dump(staging / 'mcp.json', {'$schema': 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json', 'mcpServers': {'slimweb': {'type': 'streamable-http', 'url': url}}})
        dump(staging / '.mcp.json', {'mcpServers': {'slimweb': {'type': 'http', 'url': url}}})
        dump(staging / MARKER, identity)
        if output.exists():
            # Only replace recognized generated files; preserve unknown user files.
            for item in staging.rglob('*'):
                if item.is_file():
                    dest = output / item.relative_to(staging)
                    if dest.is_symlink() or any(p.is_symlink() for p in dest.parents if p.is_relative_to(output)):
                        raise FileExistsError('refusing symlink in output')
            shutil.copytree(staging, output, dirs_exist_ok=True)
        else:
            staging.rename(output)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', help='Exact standalone HTTPS MCP URL, including domain query')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--name')
    parser.add_argument('--refresh-generated', action='store_true')
    args = parser.parse_args()
    if any([args.url, args.output, args.name]):
        if not all([args.url, args.output, args.name]):
            parser.error('--url, --output and --name are required together')
        generate(args.output, args.name, args.url, args.refresh_generated)
    else:
        for target, url in TARGETS.items():
            generate(ROOT / 'plugins' / target, 'slimweb-' + target, url, args.refresh_generated)
        entries = [{'name': 'slimweb-' + target, 'source': {'source': 'local', 'path': './plugins/' + target}, 'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, 'category': 'Productivity'} for target in TARGETS]
        dump(ROOT / '.agents/plugins/marketplace.json', {'name': 'slimweb', 'plugins': entries})
        dump(ROOT / '.claude-plugin/marketplace.json', {'name': 'slimweb', 'owner': {'name': 'SlimWeb'}, 'plugins': [{'name': 'slimweb-' + target, 'source': './plugins/' + target, 'description': 'SlimWeb ' + target + ' MCP and Skill'} for target in TARGETS]})

if __name__ == '__main__':
    main()
