#!/bin/bash

for ST in $(git diff --name-only --cached)
do	
for BR in $(git branch -a | sed -e's/*//')
do
count=$(git ls-tree -r $BR --name-only | grep ST | wc -l)
#echo $count
if [ $count == 0 ]
then
echo "$ST is present in $BR"
else
echo "$ST is not present in $BR"
fi
done
done
