def input_float():
    while True:
        try:
            num = float(input("Enter a real number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")
input_float()