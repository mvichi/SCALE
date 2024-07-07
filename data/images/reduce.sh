#!/bin/sh
for i in *JPG; 
do 
	convert -resize 800 $i small/_$i;
done
