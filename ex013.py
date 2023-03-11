# Make an algorithm that reads the salary of an employee, and their new salary with a 15% raise

original_salary = float(input("How much is the employee salary before the raise? R$"))
new_salary = original_salary + (original_salary * 15 / 100)

print("The employee's new salary is R${:.2f}".format(new_salary))
