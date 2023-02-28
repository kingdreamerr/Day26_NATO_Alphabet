import pandas

data = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter:row.code for (key,row) in data.iterrows() }

word = input("Enter word: ").upper()

nato_code = [nato_alphabet[letter] for letter in word]
