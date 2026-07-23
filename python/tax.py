salary = int(input('Enter your salary:'))
tax = 0

salary = salary - 500000

tax += 500000 *10/100
salary = salary - 500000

tax += 500000 *20/100
salary = salary - 500000

tax += salary *30/100

print("Total Tax: ",tax)