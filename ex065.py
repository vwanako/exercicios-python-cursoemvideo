# make a program that reads multiple whole numbers. in the end, show the average, biggest and lowest values.
# the program must ask the user if they want to continue or not

reply = 'Yy'
avg = total = soma = biggest = smallest = 0

while reply in 'Yy':
    num = int(input('Type a value: '))
    reply = input('Would you like to continue? [Y/N] ')
    total += 1
    soma += num
    if total == 1:
        smallest = biggest = num
    else:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num

avg = soma / total
print('The average is: {:.2f}, the biggest number is: {} and the smallest number is: {}'.format(avg, biggest, smallest))
