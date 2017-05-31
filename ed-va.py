import requests
from time import sleep

count = 0
while True:
	requests.get('https://edforvirginia.com/meet-ed/?utm_source=justinlhiggins&utm_campaign=direct&utm_medium=banner&utm_content=300x250-A4')
	sleep(3)
	count = count=+1
	print('Ping. . . ' + str(count))