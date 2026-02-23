def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 2. Lambda function to check if a number is even
even_filter = lambda x: x % 2 == 0

# 3. Taking user inputs
try:
    # Factorial input
    num = int(input("Enter a number to compute its factorial: "))
    print(f"Factorial of {num}: {factorial(num)}")

    # List input for filtering even numbers
    raw_list = input("Enter numbers separated by spaces to filter evens: ")
    numbers = list(map(int, raw_list.split()))

    even_numbers = list(filter(even_filter, numbers))
    print("Even numbers in the list:", even_numbers)

except ValueError:
    print("Invalid input! Please enter numeric values.")