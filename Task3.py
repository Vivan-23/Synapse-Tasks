request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance": 5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati": {
        "balance": 3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}


def total_spending(Name):
    print(f'The expenses made by {Name} are:')
    for i in range(len(request_spending[Name]["transactions"])):
        if request_spending[Name]["transactions"][i]["amount"] <= 0:
            print(request_spending[Name]["transactions"][i]["amount"],
                  request_spending[Name]["transactions"][i]["category"])

def account_balance(Name):
    sum = request_spending[Name]["balance"]
    for i in range(len(request_spending[Name]["transactions"])):
        sum = sum + request_spending[Name]["transactions"][i]["amount"]
    print(f'The final balance of {Name} is: {sum}')
def money_owed(Name):
    summ = 0
    for i in range(len(request_spending[Name]["transactions"])):
        if request_spending[Name]["transactions"][i]["amount"] <= 0:
            summ += request_spending[Name]["transactions"][i]["amount"]
    print(f"The committee owes {Name} {-summ} ")

if __name__ == '__main__':
    Name = input("Enter Admin Name:")
    if Name == 'Arham' or Name == 'Gaurang' or Name == 'Unnati' or Name == 'Mahek':
        total_spending(Name)
        account_balance(Name)
        money_owed(Name)
        print("**\'-\' sign denotes removal**")
    else:
        print("Enter Correct Admin Name")