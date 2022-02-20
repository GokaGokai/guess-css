#!/bin/bash
# This shell script calls css.py

# Input
REPINPUT=$1

# Input Temp
# REPINPUT="scrapped-html"

# No arguments required for theses folder names, the default names could be change if wanted by change the variables below
CSSDIR="scrapped-css"
ERRORDIR="error-css"

mkdir $CSSDIR
mkdir $ERRORDIR 

for HTML in $REPINPUT/*
do
    # Extracting CSS into CSSDIR
    NAME=$(echo $HTML | cut -d '/' -f2| cut -d '.' -f1)
    echo "Extracting" $NAME
    python3 css.py $REPINPUT $CSSDIR $NAME

    # Extracting Errors into ERRORDIR
    errormessage=$(sass $CSSDIR/$NAME.css $ERRORDIR/temp.css 2>&1)
    if [[ $errormessage == *"Error"* ]]; then
        echo "Error found"
        echo $errormessage >> $ERRORDIR/$NAME.txt
    else
        echo "No Error"
    fi

done

python3 error-report.py $ERRORDIR

# Removing temp.css created by sass
rm $ERRORDIR/temp.css
rm $ERRORDIR/temp.css.map

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

