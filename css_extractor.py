#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from time import sleep
from sys import argv
from os import path
import re
import subprocess
if __name__ == '__main__':
	url = argv[1]   # loads website from command line arguments
	url = url.replace("\n", "").replace("\r", "")  # removes whitespace characters
	chrome_options = Options()
	chrome_options.add_argument("--headless")  # makes the Chrome browser headless
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f"http://{url}/")
	sleep(5)  # allows time for selenium to render the Javascript on the sites
	html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")  # returns rendered site
	outfile = open("full_site.html", "w+")
	outfile.write(html)
	outfile.close()
	outfile_path = path.abspath("full_site.html")
	driver.get('file://' + outfile_path)  # Opens loaded site locally
	sleep(5)
	elems = driver.find_elements_by_xpath("//link[@href]")  # acquires all embedded css links found within html site
	css_hyperlinks = []
	font_file = open("input.txt", "w+") 
	font_file.write(url + "\n")  # writes out url into txt file
	font_file.close()
	for css_lk in elems:
		if (("css" in css_lk.get_attribute("href")) and (css_lk.get_attribute("href") not in css_hyperlinks)):  # opens all css sites found in html site and makes sure its not already saved in the list
			css_hyperlinks.append(css_lk.get_attribute("href"))
	for elem in css_hyperlinks:
		lst_of_fonts = []
		try:
			css = requests.get(elem)  # opens css link to acquire fonts from
		except:
			print(elem + ": hyperlink is not a valid http link")
		css_file = css.text
		result = re.compile('font-family\s*?:\s*?(.*?)\s*?[;\}]')  # uses a regular expression function to extract the required font data
		result = re.findall(result, css_file)
		if result:
			for lst in result:
				lst = lst.replace("font-family", "").replace("}", "").replace(";", "").replace("{", "").replace(":", "")
				lst = lst.split(",")
				for font in lst:
					font_file = open("input.txt", "a")  # adds font data to txt file
					font_file.write(font + ",")
	font_file.close()
	driver.close()
