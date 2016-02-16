#!/usr/bin/env python2.7
import urllib2
from bs4 import BeautifulSoup
class GetPhilosophy:
    '''
    Object that is assigned a random article from Wikipedia and webcrawls until it reaches the Wikipedia
    article Philosophy. Stores data based on its journey to Philosophy.
    '''
    def __init__(self):
        '''
        Initialize class
        '''
        self.num_articles = 0
        self.starting_article = urllib2.urlopen('https://en.wikipedia.org/wiki/Special:Random').geturl()
        self.articles = [self.starting_article]
        self.philosophy = False

    def is_valid_link(self, teststr):
        '''
        Check whether or not the string is a valid link for navigation
        '''
        if not teststr.startswith('/wiki/') or teststr == '/wiki/Latin':
            return False
        string = teststr[6:]
        if string.startswith('Help:') or string.startswith('File:') or string.endswith('.ogg') or string.startswith('Wikipedia:'):
            return False
        return True

    def is_valid_paragraph(self, test):
        '''
        Tests validity of paragraph object (soup.p)
        '''
        links = test.find_all('a')
        #return false if no links in paragraph
        if links is None:
            return False
        #return true if one link in the paragraph is valid
        for link in links:
            if self.is_valid_link(link['href']):
                return True
        return False

    def get_first_link(self, url):
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
            if self.is_valid_paragraph(child):
                #search through every link in first valid paragraph and find first valid link
                for childlink in child.find_all('a'):
                    if self.is_valid_link(childlink['href']):
                        return 'https://en.wikipedia.org' + childlink['href']

    def find_philosophy(self):
        '''
        Starts at first random Wikipedia article and loops until Philosophy article is found
        '''
        try:
            curr_article = self.starting_article
            while True:
                self.num_articles = self.num_articles + 1
                first_link = self.get_first_link(curr_article)
                print(first_link[30:])
                #Skips over article if it has already been traveled to
                if first_link not in self.articles:
                    self.articles.append(first_link)
                    #Stop looking when Philosophy is found
                    if first_link == 'https://en.wikipedia.org/wiki/Philosophy':
                        self.philosophy = True
                        break
                curr_article = first_link
        except Exception as ex:
            print('A ' + str(ex) + ' error occured while web crawling.')
            print('This error occured on the article: ' + curr_article)
            
    def get_articles(self):
        '''
        Print traveled to articles in instance of class
        '''
        for article in self.articles:
            print(article[30:])

    def get_info(self):
        '''
        Print information about the current instance
        '''
        if self.philosophy:
            print('\nThis object started at the article "' + self.starting_article[30:] + 
                 '" and reached Philosophy in ' + str(self.num_articles) + ' tries.')
        else:
            print('This object has not yet reached philosophy.')
            
phil = GetPhilosophy()
phil.find_philosophy()
phil.get_info()
