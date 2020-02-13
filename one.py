def read_numbers():
    numbers = []

    for i in range(5):
        while len(numbers) != i + 1:
            try:
                new_number = int(input("Enter an integer:"))
                numbers.append(new_number)
            except ValueError:
                print("Invalid input, please ensure you are entering integers")

    return numbers

def print_sorted_numbers(numbers, reverse):
    print(sorted(numbers, reverse=reverse))

def main():
    numbers = read_numbers()
    print_sorted_numbers(numbers, False)
    print_sorted_numbers(numbers, True)

if __name__ == "__main__":
    main()
