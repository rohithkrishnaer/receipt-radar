# Receipt Radar

A command-line expense auditor in pure Python. It checks **every** transaction - so nothing slips through.

## Why audit expenses?

A person skimming a spreadsheet skims: they sample, they get tired, and they miss things. Duplicate invoices get paid twice. A £450 "taxi" hides in the middle of a long list and nobody blinks. Receipt Radar reads 100% of the rows, every time, and flags exactly the two things a human eye slides past: **payments made twice**, and **spend that doesn't belong**.

## What it does

- **Total spend** - sums every expense
- **Spend by category** - groups totals per category, so drift is visible
- **Outlier detection** - flags any expense above a set threshold
- **Duplicate detection** - flags identical entries (same date, category, and amount) — i.e. money paid twice

## Example

    Total spend: 1284.50

    By category:
      groceries   412.30
      travel      610.00
      coffee       62.20

    Outliers (over 200):
      2025-01-14  travel  450.00

    Possible duplicates:
      2025-01-09  groceries  42.10  (x2)

## Run it

    python receipt_radar.py

## Roadmap

- Read real expense CSVs instead of an in-script list
- Configurable outlier threshold
- Export the audit report to JSON
