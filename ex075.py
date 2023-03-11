# Develop a program that reads 5 values and stores them in a tuple. a) how many times did 9 show up b) the position that
# the number 3 was first typed c) the even numbers

nums = ()
counter = even = 0
position = 1

for i in range(0, 5):
    number = input('Type a number: ')
    nums += tuple(number)
    i += 1

    if int(number) == 9:
        counter += 1

    if int(number) % 2 == 0:
        even += 1

if 3 in nums:
    var = position == 1
    for n in nums:
        if n == 3:
            break
        else:
            position += 1
else:
    print('The number 3 does not appear')

print(f'Number 9 showed up {counter} times, there are {even} even numbers, the number 3 showed up in the {position} position first')
print(nums)
