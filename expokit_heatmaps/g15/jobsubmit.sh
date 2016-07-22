#!/bin/bash 
for FILE in *.job; do 
echo "Processing $FILE " 
 qsub ${FILE}
sleep 3
done