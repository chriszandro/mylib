#!/bin/bash 
for FILE in g*/*.job; do 
echo "Processing $FILE " 
 qsub ${FILE}
sleep 3
done
