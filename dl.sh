#!/bin/bash

a=1
b=".mp3"
name=$a$b

cd /home/guest/Music/Downloaded

for a in {1..500}; do
	ls $a$b
	if [[ $? -ne 0 ]]; then
		name=$a$b
		break
	fi
done

value=$(</home/guest/Documents/Programs/SPD/nowplaying.txt)
youtube-dl -i -c -w -o $name $value

mv $name ~/Music/Downloaded/