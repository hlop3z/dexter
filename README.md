# Get this Project

## Get (**pipenv**)
```sh
python -m pipenv install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

## Get (**pip**)
```sh
pip install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

## Dexter-Lab (Watchdog)
```sh
dexter-lab
```

<br /><br /><br />
---
# New Project (**Clone**)
---

## Download
```sh
git clone https://github.com/hlop3z/dexter.git
```

## Install **build**
```sh
python -m pipenv install build isort black pylint watchdog mkdocs mkdocs-material --dev --pre
```

## Build **Package**
```sh
python -m build
```

## Install **Package**
```sh
python -m pip install dist/{dexter}-0.0.1.tar.gz
```