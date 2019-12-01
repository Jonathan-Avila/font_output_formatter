#!/usr/bin/env python3
import sys
import urllib.request

if __name__ == '__main__':

	infile = open("output.csv", "r")
	if infile.mode == 'r':
		URL = infile.readline().replace('\n', "").replace('\r',"").replace(" ", "")
		URL = URL.replace("\n", "")
		#(URL + "\n")
		contents = infile.readline()
		#print(contents)
	infile.close()
	'''
	num_of_args = len(sys.argv)
	i = 1
	string = ""

	while(i < num_of_args):
			string = string + sys.argv[i]
			i = i + 1



	delimeters = ["\t", "\n", "\r"]
	for dl in delimeters:
		string = string.replace(dl,"")


	list = string.split(",")
	'''
	contents = contents.replace('\"', " ").replace('\'', " ")
	lst = contents.split(",")
	lst.pop()
	already_used =[]
	outfile = open("fonts.csv", "a+")
	#outfile.write("\r")
	for element in lst:
		#(element)
		if ("w0" in element.lower()):
			element = element.lower().split("w0")[0]
		for char in element:
			if char.isnumeric() and char == element[-1]:
				element = element[:-2]
				#element = element.replace(char, "")
				#element = element.replace("-", "")
		element = element.strip()
		element = element.lower()
		undesireables = ["arial", "arial black", "avant garde", "bookman", "candara", "century schoolbook", "comic sans ms", "courier", "courier new", "garamond", "georgia", "helvetica", "helvetica neue", "impact", "palatino", "roboto", "tahoma", "times", "times new roman", "trebuchet ms", "verdana", "serif", "sans-serif", "sans"]
		if (element not in already_used) and (element not in undesireables) and (element.isspace() == False) :
			fonturl = (f"http://fonts.adobe.com/fonts/{element}")
			try:
				if urllib.request.urlopen(fonturl).getcode() == 200:
					outfile.write(URL + "," + element + "," + fonturl + "\n")
					print("entry: "+ URL + "," + element + "," + fonturl)
			except:
				outfile.write(URL + "," + element + "\n")
				print("entry: "+ URL + "," + element)
			already_used.append(element)
	outfile.close()
