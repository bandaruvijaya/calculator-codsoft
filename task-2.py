def add(num1, num2):
  """Performs addition operation."""
  return num1 + num2

def subtract(num1, num2):
  """Performs subtraction operation."""
  return num1 - num2

def multiply(num1, num2):
  """Performs multiplication operation."""
  return num1 * num2

def divide(num1, num2):
  """Performs division operation, handling division by zero."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

while True:
  # Get user input
  print("\nChoose operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Enter choice(1/2/3/4/5): ")

  # Get numbers
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue
  
  # Perform operation based on choice
  if choice == '1':
    result = add(num1, num2)
    print(num1, "+", num2, "=", result)
  elif choice == '2':
    result = subtract(num1, num2)
    print(num1, "-", num2, "=", result)
  elif choice == '3':
    result = multiply(num1, num2)
    print(num1, "*", num2, "=", result)
  elif choice == '4':
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result)
  elif choice == '5':
    print("Exiting calculator.")
    break
  else:
    print("Invalid input.")