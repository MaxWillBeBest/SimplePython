
print('I will learn python well')
print('100+200=', 100+200)

print(ord('A'), chr(66))

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0])

classmates.append('Adam')
print(classmates[-1])

classmates.insert(1,'Jack')
print(classmates[1])

classmates.pop(1)
print(classmates[1])

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

s = input('Age: ')
age = int(s)
if age > 20:
    print("true")
else:
    print('false')
