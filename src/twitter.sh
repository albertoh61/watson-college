#!/bin/sh

usr=$1
python get-twitter.py $usr > ../college-watsonready/twitter.txt
echo "Twitter data downloaded for $usr!"