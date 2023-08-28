sum = 0
count = 0
while True:
    i = int(input("Enter a number: "))
    if i == -1:
        break
    sum += i
    count += 1
    print("Sum:", sum)
    print("Count:", count)
    #print("Average:", sum / count)
    print("Average: {:.2f}".format(sum / count))

