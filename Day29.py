def separateDigits(nums):
    result = []

    for num in nums:
        digits = list(str(num))
        
        for digit in digits:
            result.append(int(digit))

    return result



nums = list(map(int, input("Enter array elements: ").split()))


answer = separateDigits(nums)


print("Separated Digits:", answer)

#sample output
#Enter array elements: 12345
#Separated Digits: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]