# Develop a program that reads the name, age and gender of 4 people. Then show:
# The average age of the group, the name of the oldest man, how many women have less than 20 years of age.

age_sum = 0
avg_age = 0

oldest_man = 0
o_m_name = ''

under_20_f = 0

for i in range(1, 5):
    print('----PERSON {}----'.format(i))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]: ')).upper().strip()

    age_sum += age

    if i == 1 and gender in 'Mm':
        oldest_man = age
        o_m_name = name
    if gender in 'Mm' and age > oldest_man:
        oldest_man = age
        o_m_name = name

    if gender in "Ff" and age < 20:
        under_20_f += 1

avg_age = age_sum / 4
print('The average age in the group is {}'.format(avg_age))
print('The oldest man is {} years old and his name is {}'.format(oldest_man, o_m_name))
print('There are {} women under 20 years old.'.format(under_20_f))
