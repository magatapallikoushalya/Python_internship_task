account = {
    "name": "Kaushalya",
    "balance": 1000
}

print("Account Holder:", account["name"])
print("Initial Balance:", account["balance"])

deposit = int(input("Enter deposit amount: "))
account["balance"] += deposit

print("Balance After Deposit:", account["balance"])

withdraw = int(input("Enter withdrawal amount: "))
account["balance"] -= withdraw

print("Balance After Withdrawal:", account["balance"])

interest = int(input("Enter interest percentage: "))

account["balance"] += (account["balance"] * interest / 100)

print("Balance After Interest:", account["balance"])

print("Final Balance:", account["balance"])
