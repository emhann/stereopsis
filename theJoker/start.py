import random
import os
import pymsgbox as pmb

#os.system("mkdir ~/util")
#os.system("cp vir.py ~/util")

def dadstantiate(fileName):
	storage = []
	with open(fileName) as f:
		for line in f:
			line = line.strip('\n')
			storage.append(line.split(','))
	f.close
	return storage


def tellJoke(joke):
    for i in joke:
        pmb.alert(text=i, title='The Joker', button='CLOSE')

def dadifyMe(storage):
	pickme = random.randrange(0,len(storage)-1)
	tellJoke(storage[pickme])

def main():
	storage = dadstantiate('input.txt')
	dadifyMe(storage)

if __name__ == "__main__":
    main()
