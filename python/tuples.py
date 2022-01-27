# # Preparing array for q1
# sentence = 'Life is what happens when you\'re busy making other plans'
# sentenceSplit = sentence.split()
# tarr = [(i, w) for i, w in enumerate(sentenceSplit)]
# import random
# random.shuffle(tarr)
# print(tarr)
# tarr_rev = [(b,a) for a,b in tarr]
# print(tarr_rev)

# 1.a Given an array of tuple (example tarr below), sort the array according to first element of each tuple.

tarr = [(0, 'Life'), (9, 'plans'), (2, 'what'), (4, 'when'), (6, 'busy'), (7, 'making'), (5, "you're"), (8, 'other'), (3, 'happens'), (1, 'is')]


# 1.b What if we want to sort tarr_rev below according to the second element of each tuple

tarr_rev = [('busy', 6), ('what', 2), ('making', 7), ('is', 1), ('plans', 9), ('other', 8), ('Life', 0), ('when', 4), ('happens', 3), ("you're", 5)]


# 2. Give two arrays of tuples, implement an inner join of those arrays. Example:

arr1 = [('Hello', 'Beatiful'), (1, 2), ("Cats", "Love"), ("Cats", "hate"), (0, "collapse")]
arr2 = [('Hello', 'World'), (1, 3), ("null", "bye"), (1, "3 4"), ("Cats", "Dogs")]

result = [('Hello', 'Beatiful', 'World'), (1, 2, 3), (1, 2, '3 4'), ('Cats', 'Love', 'Dogs'), ('Cats', 'hate', 'Dogs')]

# 3. No need to code. Regarding tq2. Given that arr1 and arr2 are huge lists (let's say in two files in file system), how would you implement the inner join
