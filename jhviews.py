import requests
from time import sleep

count = 0
views = True
while views == True:
	page = requests.get("https://pubs.acs.org/doi/abs/10.1021/acschemneuro.8b00148")
	print(page)
	print("Yessir. Viewed: " + str(count) + " times.")
	count = count + 1
	sleep(3)