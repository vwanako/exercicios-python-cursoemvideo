# Make a program that shows the weight of five people and shows the highest and lowest weights recorded.

w_list = []

for i in range(1, 6):
    weight = float(input('Weight {} (kg): '.format(i)))
    w_list += [weight]

largest = w_list[0]
smallest = w_list[0]

for w in w_list:
    if w > largest:
        largest = w
    if w < smallest:
        smallest = w

print('The biggest weight is {}kg.'.format(largest))
print('The smallest weight is {}kg.'.format(smallest))
