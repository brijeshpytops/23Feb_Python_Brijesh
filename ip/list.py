# words = ['milk', 'chocolate', 'monky', 'dudhi', 'god', 'pani']

# # [
# #     ['milk', 4],
# #     ['chocolate', 9],
# #     .,
# #     .,
# #     ['pani', 4]
# # ]

# # [
# #     ['milk', 4, vowels, consonent],
# #     ['chocolate', 9, , vowels, consonent],
# #     .,
# #     .,
# #     ['pani', 4, , vowels, consonent]
# # ]

# words = input("Enter a string: ").split(" ") 

# for index, word in enumerate(words):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     words[index] = [word, len(word), len([ch for ch in word if ch in vowels]), len(word) - len([ch for ch in word if ch in vowels])]

# print(words)

