import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index,row) in alphabets.iterrows()}

word_input = input("enter a word: ")
word_list = [char.upper() for char in word_input]


phonetic = [alpha_dict[letter] for letter in word_list]
print(phonetic)
