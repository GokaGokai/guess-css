#!/bin/bash
# This shell script calls tranf.py

# Input
REPINPUT=$1
REPOUTPUT=$2

# Input Temp
# REPINPUT="scrapped-html"
# REPOUTPUT="trans-html"

mkdir $REPOUTPUT
mkdir $REPOUTPUT/css
mkdir $REPOUTPUT/sass

bash scrap.sh $REPINPUT

# # Going through the scrappped html folder with transf.py
for TRANS in $REPINPUT/*
do
    NAME=$(echo $TRANS | cut -d '/' -f2 | cut -d '.' -f1)
    python3 transf.py $REPINPUT $REPOUTPUT $NAME
    echo Trans $NAME
done

# Add main.css
cp skeleton-html/css/main.css $REPOUTPUT/css

# Convert SASS into CSS for focused styling
for SASS in $REPOUTPUT/sass/*
do 
    NAMECSS=$(echo $SASS | cut -d '/' -f3 | cut -d '.' -f1)
    echo "Executing sass $SASS $REPOUTPUT/css/$NAMECSS.css"
    sass $SASS $REPOUTPUT/css/$NAMECSS.css
done

bash css.sh $REPINPUT

echo "Done"