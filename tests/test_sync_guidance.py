import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SyncGuidanceTests(unittest.TestCase):
    def test_embedded_uses_full_overview_installed_receives_only_bootstrap(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'source'
            for folder in ['scripts','references','guides','chatgpt-knowledge']:
                (root / folder).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / 'scripts/sync-capability-guide.mjs', root / 'scripts/sync-capability-guide.mjs')
            (root / 'SKILL.md').write_text('THIN BOOTSTRAP')
            (root / 'guides/overview.md').write_text('FULL SERVER OVERVIEW')
            (root / 'references/capability-map.md').write_text('CURRENT CAPABILITIES')
            (root / 'references/marketing-campaigns.md').write_text('CURRENT MARKETING')
            (root / 'chatgpt-knowledge/slimweb-mcp-ai-guide.md').write_text('KNOWLEDGE')
            embedded = Path(temporary) / 'embedded'
            installed = Path(temporary) / 'installed'
            (installed / 'references').mkdir(parents=True)
            sentinel = installed / 'references/capability-map.md'
            sentinel.write_text('USER MODIFIED REFERENCE')
            subprocess.run(['node',str(root / 'scripts/sync-capability-guide.mjs'),'--webless-root',str(embedded),'--installed-root',str(installed)], check=True, capture_output=True)
            result = (embedded / 'resources/ai/slimweb-mcp-skill.md').read_text()
            self.assertIn('FULL SERVER OVERVIEW', result)
            self.assertNotIn('THIN BOOTSTRAP', result)
            self.assertEqual((installed / 'SKILL.md').read_text(),'THIN BOOTSTRAP')
            self.assertEqual(sentinel.read_text(),'USER MODIFIED REFERENCE')
            self.assertFalse((installed / 'chatgpt-knowledge').exists())
