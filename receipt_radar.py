import csv
import json

class InvalidExpenseError(Exception):
    pass

def load_expense(path):
    expenses = []

    try:
        with open (path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["amount"] = float(row["amount"])
                    if row["amount"] <= 0:
                        raise InvalidExpenseError(f"Non-positive amount: {row}")
                    expenses.append({"date" : row["date"], "category" : row["category"], "amount" : row["amount"]})
                except (ValueError, InvalidExpenseError):
                    print(f"⚠ Skipping malformed row: {row}")
                    continue
    except FileNotFoundError:
        expenses = []

    return expenses

expenses = load_expense("expenses.csv")


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


def save_summary(expenses, path):
    summary = {
        "total" : total_spend(expenses),
        "by_category" : spend_by_category(expenses)
    }
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)


report()
save_summary(expenses, "summary.json")