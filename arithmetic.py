# Accept two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2
mod_result = num1 % num2
exp_result = num1 ** num2
floor_div_result = num1 // num2

# Display results
print("Arithmetic Operations:")
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("Modulus:", mod_result)
print("Exponentiation:", exp_result)
print("Floor Division:", floor_div_result)

# Explore type conversion
print("\nType Conversion:")
print("int to float:", float(num1))
print("int to str:", str(num1))
print("int to complex:", complex(num1))
print("float to int:", int(10.5))
print("float to str:", str(10.5))
print("float to complex:", complex(10.5))
print("str to int:", int('10'))
print("str to float:", float('10.5'))
print("list to tuple:", tuple([1, 2, 3]))
print("tuple to list:", list((1, 2, 3)))
print("set to list:", list({1, 2, 3}))
print("dict to list:", list({'a': 1, 'b': 2}.items()))

# Explore memory management
print("\nMemory Management:")
print("Memory address of num1:", id(num1))
print("Memory address of num2:", id(num2))