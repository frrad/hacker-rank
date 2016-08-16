#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SIZE=10

for x in `seq $SIZE`; do python $DIR/input.py > $DIR/$x.in; done
for x in `seq $SIZE`; do python $DIR/output.py < $DIR/$x.in > $DIR/$x.out; done
