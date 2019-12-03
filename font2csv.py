#!/usr/bin/env python3

import sys
import urllib.request
import pdb

if __name__ == '__main__':

	undesireables = ["arial", "arial-black", "avant-garde", "bookman", "candara", "century-schoolbook", "comic-sans-ms", "courier", "courier-new", "garamond", "georgia", "helvetica", "helvetica-neue", "impact", "palatino", "roboto", "tahoma", "times", "times-new-roman", "trebuchet-ms", "verdana", "serif", "sans-serif", "sans", "monospace", "simple-social-icons"]
	
	infile = open("output.csv", "r")  # Opens csv source file
	if infile.mode == 'r':
		URL = infile.readline().replace('\n', "").replace('\r',"").replace(" ", "")  #  Removes any whitespace and newline characters
		URL = URL.replace("\n", "")
		contents = infile.readline() # Reads in data from source file
	infile.close()
	contents = contents.replace('\"', " ").replace('\'', " ")  # removes all single and double quotes from fonts found
	lst = contents.split(",")
	lst.pop()
	already_used =[]
	with open("_fonts.csv", "a+") as outfile:
		#outfile.write("\r")
		for element in lst:
			if ("w0" in element.lower()):
				element = element.lower().split("w0")[0]
			#for char in element:
				#if char.isnumeric() and char == element[-1]:  # removes gratuitous versions of fonts found
					#element = element[:-2]
			element = element.strip()  # removes whitespace and newline characters
			element = element.lower()  # lowercases all the results
			element = element.replace(" ", "-")
			element_parts = element.split("-")
			if(element_parts[-1].isnumeric()):
				element = element[:-2]
			
			for value in element_parts:
				try:
					if((urllib.request.urlopen(f"http://fonts.adobe.com/fonts/{value}").getcode() == 200) and (value not in undesireables)):
						isConnected = True

				except:
					isConnected = False

				if (value not in already_used) and (value.isspace() == False) and (isConnected == True):
					outfile.write(URL + "," + element + "," + f"http://fonts.adobe.com/fonts/{value}" + "\n")
					print("entry: "+ URL + "," + element + "," + f"http://fonts.adobe.com/fonts/{value}")
					already_used.append(value)
					already_used.append(element)

			if (element not in already_used) and (element not in undesireables) and (element.isspace() == False):  # discards any fonts that are undesireable
				fonturl = (f"http://fonts.adobe.com/fonts/{element}")
				try:
					if urllib.request.urlopen(fonturl).getcode() == 200:   # adds adobe font along with adobe font url after checking that the adobe font url is functional
						outfile.write(URL + "," + element + "," + fonturl + "\n")
						print("entry: "+ URL + "," + element + "," + fonturl)
				except:
					outfile.write(URL + "," + element + "\n")  #adds non-adobe font if adobe url does not exist
					print("entry: "+ URL + "," + element)
				already_used.append(element)