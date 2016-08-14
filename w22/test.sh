#!/bin/bash

NAME=6
for input in ${NAME}_test/*.in
do
	python ${NAME}.py < $input > /tmp/output
	output=`echo $input | sed 's/in$/out/'`
	cmp -s "/tmp/output" "$output" 
	if [[ $? -ne 0 ]]
	then
		echo "$input"
		diff "/tmp/output" "$output"
	fi
done
