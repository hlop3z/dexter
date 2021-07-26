# Welcome to Dexter
```
/project_root
├── /builds         -->  Move the <releases> here.
├── /data           -->  Any <data> for the project.
├── /dist           -->  Source <distribution>.
├── /docs           -->  Write the <documentation> here.
├── /src            -->  Write the <code> here.
|   |
|   └── /project_name       -->  (Library).
|       |
|       └── /pkg1           -->  (Package).
|       |   ├── __init__.py -->  (Constructor).
|       |   ├── creator.py  -->  (Module).
|       |   └── details.py  -->  (Module).
|       |
|       └── /pkg2           -->  (Package).
|           ├── __init__.py -->  (Constructor).
|           ├── creator.py  -->  (Module).
|           └── details.py  -->  (Module).
|
├── /tests      -->  Testing the <code>.
└── watcher.py  -->  Code style enforcer & rating.
```

<br />

# New Project (**Clone**)
---

## Download
```sh
git clone https://github.com/hlop3z/dexter.git
```

## Install **Dev-Packages**
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
---

<br /><br /><br />
# Get this Project

## Get (**pipenv**)
```sh
python -m pipenv install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```