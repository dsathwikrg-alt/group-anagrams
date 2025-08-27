from typing import List, Any
import ast

# Approach ::

# words = ['Dog', 'God', 'Listen', 'Sentil', 'Apple']
# 1. Define a function that accepts list of words
# 2. Convert the list of words to lower case
# 3. 

def group_anagrams(input_list: List[Any]):

    anagram_dict = {}

    for word in input_list:

        sorted_word = ''.join(sorted(word.lower()))

        # anagram_dict.setdefault(key, []).append(word)  # shorter form instead of if/else

        if sorted_word in anagram_dict:

            anagram_dict[sorted_word].append(word)

        else:
            anagram_dict[sorted_word] = [word]

    return anagram_dict.values()       


def main():

    user_input = input("Enter the List of words :")

    input_list = ast.literal_eval(user_input)

    anagrams_group = group_anagrams(input_list)

    print(f'The group of anagrams is {anagrams_group}')

if __name__ == '__main__':
    main()  

    
