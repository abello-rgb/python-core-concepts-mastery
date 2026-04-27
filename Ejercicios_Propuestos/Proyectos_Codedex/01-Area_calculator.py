import math

print('==================')
print('Area Calculator 📐')
print('==================')

answer = int(input('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\nPlease answer: '))

if answer == 1:
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    area = (height * base) / 2
    print(f'The area of the triangle is {area}\n')

elif answer == 2:
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    area = length * width
    print(f'The area of the rectangle is {area}\n')

elif answer == 3:
    side = float(input('Enter side: '))
    area = side ** 2
    print(f'The area of the square is {area}\n')

elif answer == 4:
    radius = float(input('Enter radius: '))
    area = math.pi * radius ** 2
    print(f'The area of the circle is {area}\n')

elif answer == 5:
    print('Ending program...')

else:
    print('INVALID ENTRY')