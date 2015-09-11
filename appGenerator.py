import tweepy, time, sys, random
from random import randint

CONSUMER_KEY = 'insertkey'
CONSUMER_SECRET = 'insertsecret'
ACCESS_KEY = 'insertkey'
ACCESS_SECRET = 'insertsecret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open('handles.txt') as f:
	handleslines = f.readlines()

with open('apps.txt') as f:
	applines = [line.strip() for line in f.readlines()]

with open('animalList.txt') as f:
	animallines = [line.strip() for line in f.readlines()]

with open('numbers.txt') as f:
	numberlines = [line.strip() for line in f.readlines()]

with open('largeNumbers.txt') as f:
	largelines = [line.strip() for line in f.readlines()]

with open('end.txt') as f:
	endlines = [line.strip() for line in f.readlines()]

while True:

	username = random.choice(handleslines).strip()
	m = "{} How about {} for {}. It's a {} {} dollar {}".format(username, random.choice(applines), random.choice(animallines), random.choice(numberlines), random.choice(largelines), random.choice(endlines))
	print m
	api.update_status(status=m)
	nap = randint(86400, 604800)
	time.sleep(nap)
	print line 