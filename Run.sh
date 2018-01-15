#!/bin/bash

# Use the below code to generate a list of URLs of a playlist/channel from command line
# youtube-dl --get-url https://www.youtube.com/watch?v=V-mP3VU0DCg&list=PLRBp0Fe2GpgnIh0AiYKh7o7HnYAej-5ph |& tee -a /home/guest/Documents/Programs/SPD/links.txt

value=$(</home/guest/Documents/Programs/SPD/nowplaying.txt)
youtube-dl -o - $value | cvlc -