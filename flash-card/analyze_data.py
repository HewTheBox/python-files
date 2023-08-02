import pandas
from random import randint, choice


data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict()
to_learn = data.to_dict(orient="records")


def generate_eng_word():
    
    words = choice(to_learn)
    # data_dict["French"][randint(0,100)]
    print(words["French"])
    return words["English"]

print(generate_eng_word())