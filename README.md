# Get this Project

## Get (**pipenv**)
```sh
python -m pipenv install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

## Get (**pip**)
```sh
pip install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

---
# New Project (**Clone**)
---

## Download
```sh
git clone https://github.com/hlop3z/dexter.git
```

## Install **build**
```sh
python -m pipenv install build isort black pylint mkdocs mkdocs-material --dev
```

## Build **Package**
```sh
python -m build
```

## Install **Package**
```sh
python -m pip install dist/{dexter}-0.0.1.tar.gz
```