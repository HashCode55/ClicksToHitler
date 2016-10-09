"""
Lets go to the United States.
This script tells you how you are gonna reach the USA if you 
start from some given wikipedia article.
"""
import re 
import utilities
#pattern to clean the urls 
PATTERN = re.compile('^/wiki/*[^:]*(?<!\.jpg)(?<!\.svg)$')
end_url = 'https://en.wikipedia.org/wiki/United_States'

start_url = input("Enter the starting URL")
#Lets make the call!
utilities.bfs(start_url, end_url, PATTERN)