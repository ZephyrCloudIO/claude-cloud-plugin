"""Package only the Zephyr Cloud Claude plugin's distribution files."""
from pathlib import Path
import json
import zipfile

root = Path(__file__).resolve().parents[1]
plugin = root / 'plugins/zephyr-cloud'
manifest = json.loads((plugin / '.claude-plugin/plugin.json').read_text())
assert manifest['name'] == 'zephyr-cloud'
assert manifest['displayName'] == 'Zephyr Cloud'
connector = json.loads((plugin / '.mcp.json').read_text())
assert connector['mcpServers'] == {
    'Zephyr Cloud': {
        'type': 'http',
        'url': 'https://mcp.zephyr-cloud.io/sites/content/mcp',
    }
}
assert manifest.get('license')
assert len((plugin / 'README.md').read_text().split()) >= 40
files = [
    '.claude-plugin/plugin.json',
    '.mcp.json',
    'skills/deploy-site/SKILL.md',
    'README.md',
    'assets/zephyr-cloud-icon.png',
]
output = root / 'dist/zephyr-cloud-claude.zip'
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in files:
        path = plugin / name
        assert path.is_file() and not path.is_symlink(), name
        archive.write(path, name)
print(f'Created {output} ({len(files)} files, plugin v{manifest["version"]}).')
