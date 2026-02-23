def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        
        max_num = find_max(num1, num2, num3)
        print("Maximum number:", max_num)
    except ValueError:
        print("Invalid input: Please enter numeric values.")

if __name__ == "__main__":
    main()