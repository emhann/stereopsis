import random
import os
import pymsgbox as pmb
import sys


#os.system("mkdir ~/util")
#os.system("cp start.py ~/util")
#os.system("python ~/util/start.py")

def dadstantiate(fileName):
	storage = []
	with open(fileName) as f:
		for line in f:
			line = line.strip('\n')
			storage.append(line.split(','))
	f.close()
	return storage



def dadifyMe(storage):
	pickme = random.randrange(0,len(storage)-1)
	return storage[pickme]

def dadHelp(joke):
    for i in joke:
        pmb.alert(text=i, title='The Joker', button='CLOSE')

def listen():
	for line in sys.stdin:
		if "dad" in line:
			leggo()
			return

def leggo():
	storage = dadstantiate('input.txt')
	joke = dadifyMe(storage)
	dadHelp(joke)

def main():
	while(True):
		leggo()
		pmb.alert(text="Here's another joke for you!", title='The Joker', button="I CAN'T WAIT!!!")

if __name__ == "__main__":
    main()
