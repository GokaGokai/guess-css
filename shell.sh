#! bin/bash

python3 shell.py css3-modsel-d4

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

