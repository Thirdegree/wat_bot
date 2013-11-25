import praw 
import re
from time import sleep
from collections import deque

r = praw.Reddit("Wat_bot v1.0 by /u/Thirdegree")

done = deque(maxlen=200)

success = False
while not success:
	try:
		USERNAME = raw_input("Username\n>")
		PASSWORD = raw_input("Password\n>")
		r.login(USERNAME, PASSWORD)
		success = True
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

def main():
	comments = r.get_comments("thirdegree")
	for post in comments:
		if post.id not in done:
			done.append(post.id)
			if re.search("(?i)^[what?]+$", post.body) and post.parent.author.name:
				print post.body
				post.reply(">**"+post.parent.body+"**") #i have no idea if this works. Stupid internet won't give me an ip address
				sleep(2)
		
running = True
while running:
	try:	
		print "here"
		main()
		sleep(10)
	except praw.errors.RateLimitExceeded:
		print "Rate limit exceeded, sleeping 1 min"
