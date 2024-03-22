print('Python Functions :')
print('------------------')
print("")

print("**Key word argument function**")
print('------------------------------')
print('')


def data(name,age):
    print(name," age is ", age)

print('Python For Loop : ')
print("------------------")
print("")

array = []

for i in range (2):
    
    a = input('Enter your name : ')
    
    b  = int(input('Enter your age :'))
    
    array.append((a,b))

    print("")
    

print('------------------------------------------------')

for a,b in array:
    data(age = a,name = b)
