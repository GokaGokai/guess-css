#!/bin/bash

# REPINPUT=$1
REPINPUT="scrapped-html"

# shell.py creates scrapped-html folder
CSSDIR="scrapped-css"
ERRORDIR="error-css"

mkdir $CSSDIR
mkdir $ERRORDIR 

for HTML in $REPINPUT/*
do
    NAME=$(echo $HTML | cut -d '/' -f2| cut -d '.' -f1)
    echo "Extracting" $NAME
    python3 shell.py $NAME

    errormessage=$(sass $CSSDIR/$NAME.css $ERRORDIR/temp.css 2>&1)
    if [[ $errormessage == *"Error"* ]]; then
        echo "Error found"
        echo $errormessage >> error-css/$NAME.txt
    else
        echo "No Error"
    fi

done

rm error-css/temp.css
rm error-css/temp.css.map

echo "Done"

# ---
# BASH VER ONLY, DOESNT FULLY WORK
# ---
# for CSS in scrapped-html/* 
# do 
#     HTML=$(echo $CSS | cut -d '/' -f2)
#     CSS=$(echo $CSS | cut -d '/' -f2 | cut -d '.' -f1).css

#     LINE=$(grep "<style" scrapped-html/$HTML)

#     if [[ $LINE == *"</style>"* ]]; then
#         echo "It's there!"
#         sudo grep "<style" scrapped-html/$HTML | cut -d '>' -f2 | cut -d '<' -f1 >> testt/$CSS
#     else
#         echo "no"
#         sudo sed -n '/<style/,/style>/p' scrapped-html/$HTML | cut -d '>' -f2 | cut -d '<' -f1 >> testt/$CSS
#     fi
# done

