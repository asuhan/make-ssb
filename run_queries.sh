#!/bin/bash

for i in {11,12,13,21,22,23,31,32,33,34,41,42,43};
do
  for j in {1..5};
  do 
    /home/ubuntu/mapd-core/build/bin/mapdql -p HyperInteractive < queries/$i.sql
    echo "Iteration $i $j"
  done
done
