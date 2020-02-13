from functools import reduce

def read_numbers():
    numbers = []

    while True:
        try:
            new_number = float(input("Enter a floating-point number:"))
            if new_number < 0 and len(numbers) > 0:
                break
            elif new_number >= 0:
                numbers.append(new_number)
        except ValueError:
            print("Invalid input, please ensure you are entering floating-point numbers")

    return numbers

def get_sum(numbers):
    return reduce(lambda a,b: a + b, numbers)

def get_average(numbers):
    return get_sum(numbers) / len(numbers)

def get_min(numbers):
    return reduce(lambda a,b: b if a > b else b, numbers)

def get_max(numbers):
    return reduce(lambda a,b: a if a > b else b, numbers)

def main():
    numbers = read_numbers()
    print()
    print("The sum of the numbers is:", get_sum(numbers))
    print("The average of the numbers is:", get_average(numbers))
    print("The min value of the numbers is:", get_min(numbers))
    print("The max value of the numbers is:", get_max(numbers))


if __name__ == "__main__":
    main()
