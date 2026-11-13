import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

// Run from any directory. Only explicitly selected consumers are written.
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const check = args.includes('--check');
function option(name) {
  const index = args.indexOf(name);
  if (index < 0) return null;
  if (!args[index + 1] || args[index + 1].startsWith('--')) throw new Error(`${name} requires a path`);
  return resolve(args[index + 1]);
}
const guide = await readFile(resolve(root, 'references/capability-map.md'), 'utf8');
const marketing = await readFile(resolve(root, 'references/marketing-campaigns.md'), 'utf8');
const entry = await readFile(resolve(root, 'guides/overview.md'), 'utf8');
const start = '<!-- BEGIN GENERATED CAPABILITY REFERENCE -->';
const end = '<!-- END GENERATED CAPABILITY REFERENCE -->';
let failures = 0;
async function output(path, content) {
  let current = null;
  try { current = await readFile(path, 'utf8'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
  if (current === content) return;
  if (check) { console.error(`Out of sync: ${path}`); failures++; return; }
  await mkdir(dirname(path), { recursive: true });
  await writeFile(path, content);
  console.log(`Updated: ${path}`);
}
const knowledgePath = resolve(root, 'chatgpt-knowledge/slimweb-mcp-ai-guide.md');
const knowledge = await readFile(knowledgePath, 'utf8');
const startIndex = knowledge.indexOf(start);
const endIndex = knowledge.indexOf(end);
if ((startIndex < 0) !== (endIndex < 0) || (startIndex >= 0 && endIndex < startIndex)) {
  throw new Error('Malformed generated reference markers; preserve the knowledge file and repair its markers first.');
}
const prefix = startIndex >= 0 ? knowledge.slice(0, startIndex).trimEnd() : knowledge.trimEnd();
const suffix = endIndex >= 0 ? knowledge.slice(endIndex + end.length) : '\n';
await output(knowledgePath, `${prefix}\n\n${start}\n\n${guide}\n\n${marketing}\n${end}${suffix}`);
const core = option('--core-root');
if (core) await output(resolve(core, 'src/merchant-capabilities.md'), guide);
for (const name of ['--webless-root', '--standalone-root']) {
  const consumer = option(name);
  if (!consumer) continue;
  await output(resolve(consumer, 'resources/ai/slimweb-mcp-skill.md'), `${entry.trimEnd()}\n\n${start}\n\n${guide}\n\n${marketing}\n${end}\n`);
  await output(resolve(consumer, 'docs/SLIMWEB_CAPABILITIES.md'), guide);
}
const installed = option('--installed-root');
if (installed) {
  // Installed clients receive the stable bootstrap only. Existing user files stay intact.
  for (const file of ['SKILL.md']) {
    await output(resolve(installed, file), await readFile(resolve(root, file), 'utf8'));
  }
}
if (failures) process.exitCode = 1;
else console.log(check ? 'Capability guide copies match.' : 'Capability guide synchronization complete.');
