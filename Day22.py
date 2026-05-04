def isAnagram(s, t):
    return sorted(s) == sorted(t)


s = input("Enter first string: ")
t = input("Enter second string: ")

result = isAnagram(s, t)

print("Output:", result)

#sample output
#Enter first string: anagram
#Enter second string: nagaram
#Output: True