# works on the test cases, but not random cases https://www.codewars.com/kata/51e056fe544cf36c410000fb
import re


def top_3_words(text):
    ntext = []
    text_array = []
    unique_dict = {}
    count = 1
    # remove every character there is in the string
    text = text.translate({ord(i): None for i in '!"#¤%&/()=@£€?´`+<>\,.;:-_^¨|{}[]'})
    # if it finds any characters in the alphabet
    if any(re.findall(r'[a-zA-Z]', text)):
        # lower because it doesn't need to be case-sensitive
        text = text.lower()
        text = text.split(' ')
        for word in text:
            if word != '':
                # gets every word into a array
                ntext.append(word)
                # separates the "words" that have a \n character in them, so array in array
                seperated_text = [w.split('\n') for w in ntext]
                # gets the array down to 1 - for loop in for loop
                text_array = [char for sublist in seperated_text for char in sublist]
        # sorting the array
        sorted_text = sorted(text_array)
        # for loop to get every unique item into a dict, and updates the count of how many times it has appeared
        for x in sorted_text:
            if x not in unique_dict:
                unique_dict.update({x: 1})
                count = 1
            else:
                count += 1
                unique_dict.update({x: count})

        # sorts the dict by the value of the keys, and adds them into a array
        sorted_list = sorted(unique_dict.items(), key=lambda x: x[1], reverse=True)
        # searches for a '' in the list, and removes it
        sorted_list = [item for item in sorted_list if item[0] != '']

        # only 1 word
        if len(sorted_list) == 1:
            return [sorted_list[0][0]]
        # only 2 words
        elif len(sorted_list) == 2:
            return [sorted_list[0][0], sorted_list[1][0]]
        # 3 words
        else:
            return [sorted_list[0][0], sorted_list[1][0], sorted_list[2][0]]
    # nothing in the string
    else:
        return []

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))

# another solution, but still only works on the test cases and not random from re import findall
from collections import Counter


def another_top_3_words(text):
    cnt = Counter()
    text = text.translate({ord(i): None for i in '''!"#¤%&/()=@£€?´`+<>\,.;:-_^¨|{}[]'''})
    text = text.lower()
    if any(re.findall(r'[a-zA-Z]', text)):
        for word in text.split():
            cnt[word] += 1
        return [x[0] for x in cnt.most_common(3)]
    else:
        return []




print(another_top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))
