## Importing modules from sibling packages using setuptools

#### Add a basic setup script in the root folder

```python
from setuptools import setup, find_packages
setup(name="package", version="1.0", packages=find_packages())
```

#### Install your project

```
path\to\project\root> pip install -e .
```

#### Project Tree

```
├── _pycache_
├── package
│       ├── _pycache_.py
│       ├── subpackage1
│       │         ├── _pycache_.py
│       │         ├── __init__.py
│       │         └── subpackage1.py
│       ├── subpackage2
│       │         ├── _pycache_.py
│       │         ├── __init__.py
│       │         └── subpackage2.py
│       ├── __init__.py
│       └── package.py
├── package.egg-info
│       ├── dependency_links.txt
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       └── top_level.txt
├── app.py
├── README.md
└── setup.py
```
