# Welcome to **Dexter**
```
project_root/
├── archived/       -->  Move the <releases> here. 
├── data/           -->  Any <data> for the project.
├── dist/           -->  Source <distribution>.
├── docs/           -->  Write the <documentation> here.
├── scripts/        -->  Write the <shell/bash> here.
|   └── watcher.py  -->  Code style enforcer & rating.
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
└── tests/ -->  Testing the <code>.
```

<br />


## New Project (**Clone**)
```sh
touch clone_repo.sh
nano clone_repo.sh
```

## Clone Repo Script:
```sh
# Variables
REPO="https://github.com/hlop3z/dexter"

if [ "$1" != "" ]; then
    # Do Cloning
    git clone $REPO $name
    cd $name
    mv src/project_name src/$name
else
    # Return Error
    printf "\nPlease enter a name for the project. \n\n"
    printf "For example: \n"
    printf "\tclone_repo project_name\n"
fi
```


## Usage:
```sh
sh clone_repo.sh -n example_lib
```

# Go to [**PipEnv**](./PIPENV.md)
