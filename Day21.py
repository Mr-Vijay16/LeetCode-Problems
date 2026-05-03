def rotateString(s, goal):
   
    if len(s) != len(goal):
        return False

    # check rotation
    return goal in (s + s)



s = input("Enter string s: ")
goal = input("Enter goal string: ")

# Output
result = rotateString(s, goal)

print("Output:", result)

#Sample Output
#Enter string s: abcde
#Enter goal string: cdeab
#Output: True