#!/bin/sh

declare -a img=("test.jpg")
declare -a qsn=("what is the vehicle")

for i in "${!img[@]}"; do 
  python demo.py -image_file_name ${img[$i]} -question ${qsn[$i]}
done
