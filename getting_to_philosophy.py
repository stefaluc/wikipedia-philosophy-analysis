#!/usr/bin/env python2.7
import urllib2
from bs4 import BeautifulSoup
random_url = 'https://en.wikipedia.org/wiki/Special:Random' #Random Wikipedia article to start from
#Check whether or not the string is a valid link for navigation
def is_valid_link(teststr):
    if not teststr.startswith('/wiki/'):
        return False
    string = teststr[6:]
    if string.startswith('Help:') or string.startswith('File:') or string.endswith('.ogg') or string.startswith('Wikipedia:'):
        return False
    return True

#Tests validity of paragraph object (soup.p)
def is_valid_paragraph(test):
    links = test.find_all('a')
    #return false if no links in paragraph
    if links is None:
        return False
    #return true if one link in the paragraph is valid
    for link in links:
        if is_valid_link(link['href']):
            return True
    return False

#Returns link to the first valid wiki article of param url
def get_first_link(url):
    #Open param url
    page = urllib2.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html, 'lxml')
    #Loop through all paragraph tags in page
    for child in soup.find_all('p'):
        #check for validity of paragraph
        if is_valid_paragraph(child):
            #search through every link in first valid paragraph and find first valid link
            for childlink in child.find_all('a'):
                if is_valid_link(childlink['href']):
                    return 'https://en.wikipedia.org' + childlink['href']

print("Starting search at: " + urllib2.urlopen(random_url).geturl()[30:])
numtrys = 0
#Navigate to each first link until philosophy is reached
while True:
    first_link = get_first_link(random_url)
    print(first_link[30:])
    #Stop looping when philosophy is found
    if 'https://en.wikipedia.org/wiki/Philosophy' == first_link:
        numtrys = numtrys + 1
        print('Found Philosophy in ' + str(numtrys) + ' trys!')
        break
    random_url = first_link
    numtrys = numtrys + 1
