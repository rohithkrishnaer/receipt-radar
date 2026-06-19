expenses = [
    {"date": "2026-06-01", "category": "food", "amount":12.50},
    {"date": "2026-06-02", "category": "software", "amount":30.20},
    {"date": "2026-06-01", "category": "food", "amount":12.50},
    {"date": "2026-06-04", "category": "travel", "amount":400.50},
    {"date": "2026-06-05", "category": "software", "amount":20.10},
    {"date": "2026-06-06", "category": "food", "amount":55.55}
]



def total_spend(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total

def spend_by_category(expenses):
    category_total = {}
    for expense in expenses:
        if expense["category"] in category_total:
            category_total[expense["category"]] += expense["amount"]
        else:
            category_total[expense["category"]] = expense["amount"]
    return category_total

def find_outliers(expenses, limit):
    outliers = []
    for expense in expenses:
        if expense["amount"] > limit:
            outliers.append(expense)
    return outliers

def find_duplicates(expenses):
    seen = set()
    duplicate = []
    for expense in expenses:
        key = (expense["date"], expense["category"], expense["amount"])
        if(key in seen):
            duplicate.append(expense)
        else:
            seen.add(key)
    return duplicate


def report():
    print()
    print("===== RECEIPT RADAR - MONTHLY REPORT =====")
    print(f"Total spend: £{total_spend(expenses):.2f}")
    print()

    print("Spend by category:")
    by_cat = spend_by_category(expenses)
    for category in by_cat:
        print(f"{category}: £{by_cat[category]:.2f}")
    print()
    
    print("Outliers (over £100):")
    by_out = find_outliers(expenses, 100)
    for outliers in by_out:
        print(f"{outliers['date']} | {outliers['category']} | {outliers['amount']:.2f}")
    print()
    
    print("Duplicates found:")
    by_dup = find_duplicates(expenses)
    for duplicate in by_dup:
        print(f"{duplicate['date']} | {duplicate['category']} | {duplicate['amount']:.2f}")
    print()


report()
