#!/bin/bash

mkdir $1
SEED="https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/"

curl -o $1/index $SEED
INDEX=$(cat $1/index | grep "a href" | grep "css3" | cut -d '"' -f2 | cut -d '"' -f1)

rm $1/index

for PAGE in $INDEX
do
    DIR=$1/$PAGE
    curl -o $DIR $SEED$PAGE
    sleep 2
done

echo "Done"