__all__ = ['path_to_dockq_py']
from pathlib import Path

path_to_dockq_py = Path(__file__).parent.joinpath('DockQ.py').absolute()
assert path_to_dockq_py.exists()