"""Выполнить ноутбук и сохранить его HTML-версию: python run.py."""
from pathlib import Path
import sys
import tempfile
import json
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parent
notebook_path = ROOT / 'Practice_1.ipynb'
notebook = nbformat.read(notebook_path, as_version=4)
# Ядро использует тот же Python, которым запущен скрипт, в том числе внутри venv.
with tempfile.TemporaryDirectory() as temp:
    kernel_dir = Path(temp) / 'python3'
    kernel_dir.mkdir()
    (kernel_dir / 'kernel.json').write_text(json.dumps({
        'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        'display_name': 'Python 3', 'language': 'python',
    }), encoding='utf-8')
    manager = KernelManager(kernel_name='python3', kernel_spec_manager=KernelSpecManager(kernel_dirs=[temp]))
    try:
        NotebookClient(notebook, km=manager, timeout=180,
                       resources={'metadata': {'path': str(ROOT)}}).execute()
    finally:
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
nbformat.write(notebook, notebook_path)
html, _ = HTMLExporter().from_notebook_node(notebook)
(ROOT / 'Practice_1.html').write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding='utf-8')
print('Готово: Practice_1.ipynb и Practice_1.html')
for cell in notebook.cells:
    for output in cell.get('outputs', []):
        if output.output_type == 'stream' and 'Для этой выборки' in output.text:
            print(output.text)
