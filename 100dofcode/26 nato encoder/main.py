import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}

word = "MEABC"

natoed = [phonetic_dict[letter] for letter in word]
print(natoed)
