#!/bin/bash

# Input
REPINPUT=$1

# Input Temp
# REPINPUT="scrapped-html"

mkdir $REPINPUT
SEED="https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/"

curl -o $REPINPUT/index $SEED
INDEX=$(cat $REPINPUT/index | grep "a href" | grep "css3" | cut -d '"' -f2 | cut -d '"' -f1)

rm $REPINPUT/index

for PAGE in $INDEX
do
    DIR=$REPINPUT/$PAGE
    echo "curl -o $DIR $SEED$PAGE"
    curl -o $DIR $SEED$PAGE
    sleep 2
done

# Giving permissions
chmod -R 711 .
chmod -R og+r .

echo "Done"