def average(lst):
    return sum(lst) / len(lst)

numbers = []
while True:
    number = input("Enter a number or 'done': ")
    if number.lower() == 'done':
        break
    try:
        number = int(number)
        numbers.append(number)
        print(f"The average is: {average(numbers)}")
    except ValueError:
        print("That's not a valid number. Please try again.")