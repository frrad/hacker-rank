#!/bin/bash

for x in `seq 9`; do python input.py > $x.in; done
for x in `seq 9`; do python output.py < $x.in > $x.out; done
