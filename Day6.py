# Function to reverse a number
def reverse_num(n):
    return int(str(n)[::-1])

# Take input
n = int(input("Enter a number: "))

# Calculate mirror distance
reversed_n = reverse_num(n)
result = abs(n - reversed_n)

# Output
print("Mirror Distance:", result)

#output:
#Enter a number: 25
#Mirror Distance: 27