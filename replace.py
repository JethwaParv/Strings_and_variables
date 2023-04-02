# Sentence saved as a single string
sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog!.'

# Sentence printed replacing the exclamation mark with a blank space
print(sentence.replace('!', ' '))

# Reprinted the sentence using upper function.
new_sentence = sentence.upper()
print(new_sentence)
print(new_sentence.replace('!', ' '))

# Sentence printed in reverse.
sentence = 'The quick brown fox jumps over the lazy dog'
position = sentence[::-1]
print(position)
