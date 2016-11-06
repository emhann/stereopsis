import os
import pymsgbox as pmb

joke1=["knock knock!", "who's there?", "boo", "boo who?", "Don't cry, it's only a joke!"]


#os.system("mkdir ~/util")
#os.system("cp vir.py ~/util")
print("we ran the thingy!!!")


def tellJoke(joke):
    for i in joke:
        pmb.alert(text=i, title='The Joker', button='CLOSE')


tellJoke(joke1)