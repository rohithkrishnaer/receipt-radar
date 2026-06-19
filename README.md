# Receipt Radar

A command-line expense auditor written in pure Python (no libraries). It takes a list of expense records and produces a monthly audit report.

## What it does
- **Total spend** — sums all expenses
- **Spend by category** — groups totals per category
- **Outlier detection** — flags expenses above a set limit
- **Duplicate detection** — flags identical entries (same date, category, amount)

## How to run

python receipt_radar.py

## Concepts used
Lists, dictionaries, tuples, sets (hashing for O(1) duplicate detection), functions, and string formatting.

## Author
Rohith K