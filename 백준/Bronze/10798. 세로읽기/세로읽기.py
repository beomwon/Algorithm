text = [''] * 15
for i in range(5):
    for index, word in enumerate(input()):
        text[index] += word

print(''.join(text))