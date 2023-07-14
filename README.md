# banger names

Generate marketable PtX component names

## How to install
```bash
pip install git+https://github.com/mihsamusev/banger_names
```

## How to verify
Check that `pip` has the package installed
```bash
pip list | findstr banger-names # on Windows
pip list | grep banger-names # on Windows
```

Alternatively:
```bash
python -c "import banger_names" # should not crash
```

## Getting started
```python
from banger_names.name_generator import generate_names


for name in generate_names(10):
    print(name)
```