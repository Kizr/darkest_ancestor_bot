import quote_list
import praw
import config
import time
import ast
import os

def login_reddit():
	run = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = config.user_agent) 
	return run
				
def run_darkest_bot(run, comment_list):
	bot = "darkest_ancestor_bot"
	print("Fetching 10 comments...")
	for key, value in quote_list.quote.items():
		for comment in run.subreddit('darkestdungeon').comments(limit=10):
			if key in comment.body and comment.id not in comment_list and bot != comment.author:	
				print("Matching comment criteria found! Posted by: " + comment.author.name)
				comment.reply("#[" + key + "](" + value + ")" + "\n\n ^^I ^^am ^^a ^^bot, ^^and ^^this ^^action ^^was ^^performed ^^automatically. ^^Please ^^contact ^^/u/Frozen_Aurora ^^if ^^you ^^have ^^any ^^questions ^^or ^^concerns.")
				print("Writing reply and updating comment_list")
				comment_list.append(comment.id)
			
				with open("comment_list.txt", "a") as f:
					f.write(comment.id + "\n")
			
def replies_list():
	if not os.path.isfile("comment_list.txt"):
		comment_list = []
	else:
		with open("comment_list.txt", "r") as f:
			comment_list = f.read()
			comment_list = comment_list.split("\n")
			comment_list = list(filter(None, comment_list))
	
	return comment_list


run = login_reddit()	
comment_list = replies_list()


while True:
	run_darkest_bot(run, comment_list)

