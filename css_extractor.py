#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import sys
import os
if __name__ == '__main__':
	url = sys.argv[1]
	url = url.replace("\n", "").replace("\r", "")
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f"http://{url}/")
	time.sleep(5)
	html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
	outfile = open("full_site.html", "w+")
	outfile.write(html)
	outfile.close()
	outfile_path = os.path.abspath("full_site.html")
	driver.get('file://' + outfile_path)
	time.sleep(5)
	elems = driver.find_elements_by_xpath("//link[@href]")
	css_links = []
	font_list = []
	font_file = open("input.txt", "w+")
	font_file.write(url + "\n")
	font_file.close()
	for elem in elems:
		if (("css" in elem.get_attribute("href")) and (elem.get_attribute("href") not in css_links)):
			css_links.append(elem.get_attribute("href"))
	#print(css_links)
	for elem in css_links:
		#print(elem)
		driver.get(elem)
		time.sleep(5)
		lst_of_fonts = []
		html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
		result = re.compile('font-family\s*?:\s*?(.*?)\s*?[;\}]')
		result = re.findall(result, html)
		if result:
			#print(result)
			for element in result:
				element = element.replace("font-family", "").replace("}", "").replace(";", "").replace("{", "").replace(":", "")
				element = element.split(",")
				for font in element:
					#print(font)
					font_file = open("input.txt", "a")
					font_file.write(font + ",")
				#print(font + "\n")
	font_file.close()
	driver.close()



				
				

