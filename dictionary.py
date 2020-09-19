import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def multipleTranslations(translations):
    for meaning in translations:
        print(meaning)

def translate(word):
    word = word.lower()
    if word in data:
       multipleTranslations(data[word])
    elif (len(get_close_matches(word,data.keys()))>0):
        print("Are you trying to say",get_close_matches(word,data.keys())[0] )
        check = input("please enter Y or N")
        if check == "Y":
            translate(get_close_matches(word,data.keys())[0])
        else:
            word = input("please enter word again:")
            translate(word)
    else:
       print("please enter a vaild word")

word = input("enter word:")
translate(word)