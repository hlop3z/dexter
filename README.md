# Clone this Project

## Clone < **pipenv** >
```sh
python -m pipenv install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

## Clone < **pip** >
```sh
pip install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```

---
# New Project
---

## Install **build**
```sh
python -m pipenv install build isort black pylint --dev
```

## Build **Package**
```sh
python -m build
```

## Install **Package**
```sh
python -m pip install dist/{dexter}-0.0.1.tar.gz
```