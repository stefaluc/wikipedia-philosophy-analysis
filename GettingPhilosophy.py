#!/usr/bin/env python2.7
import urllib2
from bs4 import BeautifulSoup
class GetPhilosophy:
    num_articles = 0
    articles = []
    def __init__(self):
        '''
        Initialize class with random article and add random article to article list
        '''
        starting_article = urllib2.urlopen('https://en.wikipedia.org/wiki/Special:Random').geturl()
        articles.append(starting_article)

    def is_valid_link(teststr):
        '''
        Check whether or not the string is a valid link for navigation
        '''
        if not teststr.startswith('/wiki/'):
            return False
        string = teststr[6:]
        if string.startswith('Help:') or string.startswith('File:') or string.endswith('.ogg') or string.startswith('Wikipedia:'):
            return False
        return True

    def is_valid_paragraph(test):
        '''
        Tests validity of paragraph object (soup.p)
        '''
        links = test.find_all('a')
        #return false if no links in paragraph
        if links is None:
            return False
        #return true if one link in the paragraph is valid
        for link in links:
            if is_valid_link(link['href']):
                return True
        return False

    def get_first_link(url):
        '''
        Returns link to the first valid wiki article of param url
        '''
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
    def find_philosophy():
        '''
        Starts at first random Wikipedia article and loops until first article is found
        '''
        while True:
            num_articles = num_articles + 1
            first_link = get_first_link(starting_article)
            articles.append(first_link)
            if first_link == 'https://en.wikipedia.org/wiki/Philosophy':
                break
            starting_article = first_link
    '''
    print("Starting search at " + starting_article[30:])
    #Navigate to each first link until philosophy is reached
    while True:
        first_link = get_first_link(random_url)
        print(first_link[30:])
        #Stop looping when philosophy is found
        if 'https://en.wikipedia.org/wiki/Philosophy' == first_link:
            num_articles = num_articles + 1
            print('Found Philosophy in ' + str(num_articles) + ' trys!')
            break
        random_url = first_link
        num_articles = num_articles + 1
    '''
