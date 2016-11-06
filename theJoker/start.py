import random

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
	print(storage[pickme])

def main():
	storage = dadstantiate('input.txt')
	dadifyMe(storage)

if __name__ == "__main__":
    main()
