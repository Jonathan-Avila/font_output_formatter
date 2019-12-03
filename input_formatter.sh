#!/usr/local/bin/bash

readarray -t websites < allsites.txt
for website in "${websites[@]}"   # cycles through every site listed in allsites.txt
	do
	if [[ $website == "" ]]; then
		break;
	fi
	./css_extractor.py $website;
	cat input.txt | tr '\n' '\r\n' | cat > output.csv;  # creates csv copy of input.txt, with formatting
	./font2csv.py;
	let num_of_nl=$(wc _fonts.csv | gawk {'print $1'});  # prints total number of lines after entry additions are performed
	let lines=$num_of_nl+1;
	echo -e "there are $lines lines";
	rm input.txt output.csv  # deletes unnecessary files
done
