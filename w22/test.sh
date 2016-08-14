NAME=6
for input in ${NAME}_test/*.in; do python ${NAME}.py < $input > /tmp/output; diff /tmp/output `echo $input | sed 's/in$/out/'` ; done
