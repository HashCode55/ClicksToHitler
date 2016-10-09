"""
Module implementing the basic BFS for exploring the 
wikipedia space.
"""
import urlhelper
import queue
import re

#initialise the queue for the bfs
que = queue.Queue()
#dict to maintain the parents 
parent_keeper = {}

def bfs(start_url, end_url, pattern):
	"""
	Explore the space baby...
	The actual bfs code
	:param start_url: the starting url 
	:param end_url: the ending url
	:param pattern: the regex pattern used 
	"""
	print (urlhelper.fetch(start_url, pattern))
	que.put(start_url)
	parent_keeper[start_url] = None
	while not que.empty():
		curr_link = que.get()
		print ("Current visiting link is " + curr_link)
		if curr_link == end_url:
			print_path(parent_keeper, curr_link)
			return ("Found the path")
		curr_page_links = urlhelper.fetch(curr_link, pattern)	
		for link in curr_page_links:
			#print (link)
			if link == end_url:
				print_path(parent_keeper, curr_link)
				return ("Found the path")
			else:
				if link not in parent_keeper:
					parent_keeper[link] = curr_link
					que.put(link)

def print_path(parent_keeper, link):
	"""
	Move up the tree to the root tracing back the path
	:param parent_keeper: Dictionary to maintain the parents
	:link: The link we want to traceback 
	"""
	print ("FINALLY WE ARE HERE!! Heres the path we followed - ")
	if link is None:
		return
	print_path(parent_keeper, parent_keeper[link])	
	print (link.split('/')[-1])
	return 
