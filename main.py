with open('books/frankenstein.txt') as f:
    file_contents = f.read()

words = file_contents.split()
print(len(words))

def count_letters():
    count_dict = {}
    for word in words:
        for letter in word:
            if letter[0].isalpha():
                if letter.lower()[0] not in count_dict:
                    count_dict[letter.lower()[0]] = 1
                else:
                    count_dict[letter.lower()[0]] += 1
    return count_dict

letter_count = count_letters()
report_list = []
for key in letter_count:
    report_list.append((key, letter_count[key]))

report_list.sort(key = lambda x: x[1], reverse = True)
print(report_list)
