def minimumEffort(tasks):
    
    tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

    energy = 0
    current = 0

    for actual, minimum in tasks:

       
        if current < minimum:
            energy += (minimum - current)
            current = minimum

        
        current -= actual

    return energy



n = int(input("Enter number of tasks: "))

tasks = []

print("Enter actual and minimum energy for each task:")

for _ in range(n):
    actual, minimum = map(int, input().split())
    tasks.append([actual, minimum])


result = minimumEffort(tasks)

print("Minimum Initial Energy Required:", result)

#sample input:
#Enter number of tasks: 3
#Enter actual and minimum energy for each task:
#1 2
#2 3
#3 4
#Minimum Initial Energy Required: 3