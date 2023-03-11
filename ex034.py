# Write a program that asks an employee's salary and calculates their raise.
# For salaries over R$1.250,00, give the employee a 10% raise. For salaries below or equal to that, a 15% raise.

salary = float(input('How much does the employee make? R$'))

if salary > 1250:
    new_salary = salary + (salary * 10 / 100)
    print("With a 10% raise, the employee will make R${:.2f}.".format(new_salary))
elif salary <= 1250:
    new_salary = salary + (salary * 15 / 100)
    print("With a 15% raise, the employee will make R${:.2f}.".format(new_salary))
