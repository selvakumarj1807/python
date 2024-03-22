# Example of using break, pass, and continue with a while loop

# Using break
print("Using break:")
num = 0
while num < 10:
    if num == 5:
        break  # exits the loop when num equals 5
    print(num)
    num += 1

# Using pass
print("\nUsing pass:")
num = 0
while num < 10:
    if num == 5:
        pass  # does nothing when num equals 5
    else:
        print(num)
    num += 1

# Using continue
print("\nUsing continue:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # skips even numbers
    print(num)
