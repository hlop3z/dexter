# Variables
REPO="https://github.com/hlop3z/dexter"
ISVALID=true

# Command-Line <Arguments>
while getopts n: flag
do
    case "${flag}" in
        n) name=${OPTARG};;
    esac
done

if [ -z "$name" ]
    then
        ISVALID=false
        printf "\nPlease enter a name for the project. \n\n"
        printf "For example: \n"
        printf "\tclone_repo -n project_name\n"
fi


# Do something with the <Arguments>
if [ "$ISVALID" = true ] ; then
    git clone $REPO $name
    cd $name
    rm -rf .git/
    rm -rf builds/
    mkdir builds
    mv src/project_name src/$name
fi