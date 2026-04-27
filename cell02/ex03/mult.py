num = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
total = (num * num2)
print (total)
print(num, " x ", num2, " = ", total )
if total > 0:
    print ('The result is positive.')
elif total < 0:
    print("The result is negative.")
else:
    print('The result is positive and negative.')
