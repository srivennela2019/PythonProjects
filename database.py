import mysql.connector
import numpy
from difflib import get_close_matches

con = mysql.connector.connect(
user ="****",
password = "****",
host = "****",
database = "******"
)

cursor = con.cursor()

def multipleTranslations(translations):
    for meaning in translations:
        print(meaning[0])

def translate(word):
    word = word.lower()
    meanings = cursor.execute("SELECT Expression FROM Dictionary")
    data = numpy.asarray(cursor.fetchall())
    finaldata = []
    for w in data:
        finaldata.append(w[0])
    print(data)
    print(type(data))
    if word in finaldata:
       print("word in data")
       query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
       results = numpy.asarray(cursor.fetchall())
       multipleTranslations(results)
    elif (len(get_close_matches(word,finaldata)>0)):
        print("Are you trying to say",get_close_matches(word,finaldata)[0] )
        check = input("please enter Y or N")
        if check == "Y":
            translate(get_close_matches(word,finaldata)[0])
        else:
            word = input("please enter word again:")
            translate(word)
    else:
       print("please enter a vaild word")

word = input("enter word:")
translate(word)