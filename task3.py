
products = ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"]

search = input("Enter product name: ")

if search in products:
    print(search, "is available")
else:
    print(search, "is not available")
