def average(numbers):
    return sum(numbers) / len(numbers)


def add_three(numbers, amount):
    return [number + amount for number in numbers]


def main():
    print('testing average')
    numbers = [15, 12, 10, 9, 8, 7, 6]
    calculate_average = average(numbers)
    print(int(calculate_average))
    print('testing Adding 3')
    adding_three = add_three(numbers)
    print(adding_three)


if __name__ == "__main__":
    main()
