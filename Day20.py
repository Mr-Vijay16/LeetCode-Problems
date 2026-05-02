def is_good(num):
    valid = {0, 1, 8, 2, 5, 6, 9}
    change = {2, 5, 6, 9}

    has_change = False

    for d in str(num):
        d = int(d)

        # invalid digit
        if d not in valid:
            return False

        # must change to be "good"
        if d in change:
            has_change = True

    return has_change


def rotatedDigits(n):
    count = 0
    for i in range(1, n + 1):
        if is_good(i):
            count += 1
    return count



n = int(input("Enter value of n: "))

# Output
print("Number of Good Integers:", rotatedDigits(n))

#sample output
#Enter value of n: 10
#Number of Good Integers: 8
