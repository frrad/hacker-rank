#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
for f in $DIR/*.in
do
    output=`echo $f | sed 's/in$/out/'`	
	python $DIR/output.py < $f > $output
done

