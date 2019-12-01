#!/usr/local/bin/bash
#echo "Enter the list of fonts found";
#read -d "\`" value;
#echo "$value" > input.txt;
readarray -t websites < allsites.txt
for website in "${websites[@]}"
	do
	./css_extractor.py $website;
	#echo EOF >> input.txt;
	cat input.txt | tr '\n' '\r\n' | cat > output.csv;
	#truncate -s-4 output.csv ;
	#truncate -s -4 input.txt;
	clear;
	./font2csv.py;
	let num_of_nl=$(wc fonts.csv | gawk {'print $1'});
	let lines=$num_of_nl+1;
	echo -e "there are $lines lines";
	rm input.txt output.csv
	#./input_formatter.sh;
done