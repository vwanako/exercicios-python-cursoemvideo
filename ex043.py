# Develop an app that reads a person's height and weight, calculates and displays their BMI. (underweight,
# ideal weight, overweight, obese, morbid obese)

print('-=+=-' * 4)
print('BMI calculator (kg/m)')
print('-=+=-' * 4)

weight = float(input('\nWeight: '))
height = float(input('Height: '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = '\033[1;31munderweight'
elif 18.5 <= bmi <= 24.9:
    status = '\033[1;32mideal weight'
elif 25 <= bmi <= 29.9:
    status = '\033[1;33moverweight'
elif 30 <= bmi <= 39.9:
    status = '\033[1;31mobese'
elif bmi >= 40:
    status = '\033[1;31mmorbidly obese'

print('At {}m and {}kg, you have a BMI of {:.1f}. Classifying you as {}.'.format(height, weight, bmi, status))
