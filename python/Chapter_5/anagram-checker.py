print("Enter two strings and I'll tell you if they are anagrams: ")
word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")

def anagram_checker(a, b):
    a = list(a)
    if len(word1) == len(word2):
        for i in word1:
            if i not in word2:
                return False
            return True

print(anagram_checker(word1, word2))
