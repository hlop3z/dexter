# Variables
REPO="https://github.com/hlop3z/dexter"

# Command-Line <Arguments>
if [ "$1" != "" ]; then
    git clone $REPO $name
    cd $name
    mv src/project_name src/$name
else
    printf "\nPlease enter a name for the project. \n\n"
    printf "For example: \n"
    printf "\tclone_repo project_name\n"
fi
