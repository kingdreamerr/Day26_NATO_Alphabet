import pandas

data = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter:row.code for (key,row) in data.iterrows() }
print(nato_alphabet)