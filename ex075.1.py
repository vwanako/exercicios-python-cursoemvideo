# Develop a program that reads 5 values and stores them in a tuple. a) how many times did 9 show up b) the position that
# the number 3 was first typed c) the even numbers

counter = even = 0
position = 1

nums = (int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')),
        int(input('Type a number: ')), int(input('Type a number: ')))

print(f'Number 9 showed up {nums.count(9)} times, there are {even} even numbers', end=' ')
print(f'the number 3 showed up in the {nums.index(3)+1}ª position first')

# , the number 3 showed up in the 'f'{nums.index(3)} position first

print(nums)
