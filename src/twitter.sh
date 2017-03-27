#!/bin/sh

usr=$1
python get-twitter.py $usr > ../watson-text/twitter.txt
echo "Twitter data downloaded for $usr!"