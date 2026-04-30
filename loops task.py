# Write a program that displays a numbers 1 to 50 inside a list
numbers = list(range(1, 51))
print(numbers)
# From 1 above display the ones divisible by 7 or 5 inside a list.
divisible = [n for n in numbers if n % 7 == 0 or n % 5 == 0]
print(divisible)
# Find sum and average of values in the range between 10 to 40.
values = list(range(10, 41))
total = sum(values)
average = total / len(values)
print("Sum:", total)
print("Average:", average)
# Put in a list the first 10 odd numbers between 10 to 50.
odd_numbers = []
for n in range(10, 51):
    if n % 2 != 0:
        odd_numbers.append(n)
    if len(odd_numbers) == 10:
        break
print(odd_numbers)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    # write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count = 0
for n in range(1, 51):
    if n % 2 == 0:
        count += 1
print("Even numbers count:", count)
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ] Display the total quantity of the 3 above.
ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32')]
total_quantity=0
for i in ls1:
    for i in ls1:
        quatity=int(i[1])
        total_quantity=total_quantity+quatity
        print(total_quantity)