string = 'Hola, mi nombre es Peyman y amo a Lana'
counter = dict()
for letter in string:
    if letter.isalpha():
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

for letter, count in sorted_counter:
    print(f"{letter}: {count} time")
