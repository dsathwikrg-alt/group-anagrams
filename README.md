# group-anagrams
Group anagrams together from a word list.

How it works:::

Loop each word from the input list.

Normalize the word:

word.lower() makes it lowercase.

sorted(...) sorts the characters alphabetically.

''.join(...) joins them back to a string.

Example: "Tea" → "aet".

Use this normalized string ("aet") as the dictionary key.

Group all words with the same key in a list.

#########################################################################

Step by Step

word.lower()

Converts the word to lowercase (so “Eat” and “Tea” are treated the same).

word = "Tea"
word.lower()   # "tea"


sorted(word.lower())

sorted() takes an iterable (like a string) and returns a list of characters in sorted order.

sorted("tea")   # ['a', 'e', 't']


👉 Notice: the result is a list, not a string.

''.join([...])

''.join(list) glues the list of characters back into a single string.

The empty string '' means "put nothing between them."

''.join(['a', 'e', 't'])   # "aet"

######################################################################
Context

In the dictionary-based solution:

anagrams: Dict[str, List[str]] = {}
for word in input_list:
    sorted_word = ''.join(sorted(word.lower()))
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]   # 👈 this line

What’s happening in that line?

anagrams → is a dictionary (dict).

sorted_word → is a string created by sorting the letters of word.
Example: "eat" → "aet", "Tea" → "aet", "tan" → "ant".

anagrams[sorted_word] → means “the value stored in the dictionary under the key sorted_word”.

= [word] → creates a new list containing the current word as its first element.

So that line creates a new dictionary entry when we see a new "pattern" of letters for the first time.

Example Walkthrough

Input:

words = ["eat", "Tea", "tan", "ate", "nat", "bat"]


Loop step 1:

word = "eat"

sorted_word = "aet"

"aet" not in anagrams, so we do:

anagrams["aet"] = ["eat"]


Now dictionary is:

{"aet": ["eat"]}


Loop step 2:

word = "Tea"

sorted_word = "aet"

"aet" already exists → append instead of replace.

Loop step 3:

word = "tan"

sorted_word = "ant"

"ant" not in anagrams, so we create:

anagrams["ant"] = ["tan"]


Dictionary now:

{"aet": ["eat", "Tea"], "ant": ["tan"]}


…and so on.

✅ In short:
anagrams[sorted_word] = [word] means
“📌 create a new dictionary entry for this anagram pattern, and start its value as a list with the current word inside.”

#########################################################################################

Analogy 🪣

Think of anagrams as a set of buckets (dictionary values).

Each bucket is labeled with a sorted_word (dictionary key).

= [word] → create a new empty bucket and drop the word in it.

.append(word) → find the bucket that already exists, and toss another word into it.