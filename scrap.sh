#! /bin/bash

SEED="https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/css3-modsel-1.html"

# curl -o /myrep/first.html $SEED

TEST=$(cat css3test.html | grep "<a href" | grep "==&gt" | cut -d '"' -f2 | cut -d '"' -f1 )

curl -o second.html https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/$TEST
echo $TEST
# if [ $TEST == "" ]
# then echo "hi"

# curl -o test https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/#
# fi