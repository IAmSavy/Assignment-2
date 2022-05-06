a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

result = ((a+b > c) & (a+c > b) & (b+c > a)) ==1

print(str(result).replace('True','Yes').replace('False','No')) 