# Welcome to Dexter
```
project_root/
├── builds/         -->  Move the <releases> here. 
├── data/           -->  Any <data> for the project.
├── dist/           -->  Source <distribution>.
├── docs/           -->  Write the <documentation> here.
├── scripts/        -->  Write the <shell/bash> here.
├── src/            -->  Write the <code> here.
|   |
|   └── project_name/       -->  (Library).
|       ├── __init__.py     -->  (Library: __init__) import [pkg1, pkg2, etc...] in this file.
|       ├── __main__.py     -->  (Library: __main__) any function you want to run as a <script> with "python -m project_name".
|       ├── script.py       -->  Script to use in --> setup.cfg --> [options.entry_points] <console_scripts>.
|       |
|       └── pkg1/           -->  (Package).
|       |   ├── __init__.py -->  (Constructor).
|       |   ├── creator.py  -->  (Module).
|       |   └── details.py  -->  (Module).
|       |
|       └── pkg2/           -->  (Package).
|           ├── __init__.py -->  (Constructor).
|           ├── creator.py  -->  (Module).
|           └── details.py  -->  (Module).
|
├── tests/      -->  Testing the <code>.
└── watcher.py  -->  Code style enforcer & rating.
```

<br />

# New Project (**Clone**)
[Clone Repo Script](https://raw.githubusercontent.com/hlop3z/dexter/main/scripts/clone_repo.sh).

## Usage:
```sh
sh clone_repo.sh -n example_lib
```

<br />

## Install **Packages**
```sh
python -m pipenv install <package>
```

## Install **Dev-Packages**
```sh
python -m pipenv install build isort black pylint watchdog mkdocs mkdocs-material --dev --pre
```

## Build **My - Package**
```sh
python -m build
```

## Install **My - Package**
```sh
python -m pip install dist/{project_name}-0.0.1.tar.gz
```
---

<br /><br />
# Get this Project

## Get (**pipenv**)
```sh
python -m pipenv install https://github.com/hlop3z/dexter/raw/main/data/builds/dexter-0.0.1.tar.gz
```