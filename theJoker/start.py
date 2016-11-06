import random
import os
import pymsgbox as pmb

def dadstantiate(fileName):
	storage = []
	with open(fileName) as f:
		for line in f:
			line = line.strip('\n')
			storage.append(line.split(','))
	f.close
	return storage

def dadifyMe(storage):
	pickme = random.randrange(0,len(storage))
	return storage[pickme]

def dadHelp(joke):
    for i in joke:
        pmb.alert(text=i, title='The Joker', button='CLOSE')

def main():
	storage = dadstantiate('input.txt')
	joke = dadifyMe(storage)
	dadHelp(joke)

if __name__ == "__main__":
    main()
