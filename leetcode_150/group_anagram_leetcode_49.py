# Analgrams can be grouped by sorting but they have a time complexity of O(n log n) * O(m) 
# where n is the number of words and m is the length of the longest word

from collections import defaultdict

def group_anagram(anagram_str):

    result = defaultdict(list)

    for word in anagram_str:
        count = [0] * 26

        for character in word:
            count[ord(character) - ord("a")]+=1

        result[tuple(count)].append(word)

    return result.values()

anagram_strings = ['eat', 'tan', 'tea', 'ate', 'nat', 'bat']
result = group_anagram(anagram_strings)
print(result)
