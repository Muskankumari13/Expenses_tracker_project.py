# -*- coding: utf-8 -*-
"""Expense_Tracker_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wukUgW_nc6H4ZalV3AtEvkxMlyWw77tl
"""

# -------------------- User Profile Setup --------------------
# Ask the user for their name and profession
name=input("Enter your Name:")
profession=input("Enter your profession:")

# Display a personalized welcome message
print(f"Welcome {name} Let's analyze your financial health as a {profession}.")

# -------------------- Income and Expense Management --------------------
# Get user's monthly income and expenses
monthlyIncome=int(input(name+ " Enter your monthly income:"))
monthlyExpenses=int(input(name+ " Enter you monthly expenses:"))

# Calculate total savings and savings percentage
TotalSavings=monthlyIncome-monthlyExpenses
percentageOfSaving=int((TotalSavings/monthlyIncome)*100)
print(name+ " Your total saving =",TotalSavings)
print("Total saving percentage=",percentageOfSaving)

# -------------------- Financial Health Check --------------------
# Use nested if-else to analyze user's financial habits
if percentageOfSaving>=20:
  print(f"Great job, {name} You have a strong savings habit.")
elif 10 <= percentageOfSaving < 20:
  print(f"Great, {name} but you could save a bit more.")
else:
  print(f"Warning, {name} Your savings are too low.Consider cutting expenses!")

# -------------------- Categorize Expenses --------------------
# Ask the user to categorize expenses into Essentials, Wants, and Savings/Investments
Essential=int(input("How much do you spend on Essentials((e.g., rent, utilities, groceries):"))
want=int(input("How much do you spend on Wants(e.g., dining out, entertainment) :"))
SavingOrInvestment=int(input("How much do you save or invest:"))

# Calculate percentage of each category
PerofEssential=int((Essential/monthlyIncome)*100)
PerofWant=(want/monthlyIncome)*100
PerofSavingOrInvestment=(SavingOrInvestment/monthlyIncome)*100

# Display expense breakdown summary
print("Expense Breakdown: ")
print("Essentials:",PerofEssential)
print("Wants:",PerofWant)
print("Saving / Investment:",PerofSavingOrInvestment)

# -------------------- Custom Savings Goal --------------------
# Ask the user to enter a custom savings goal in percentage
SavingGoals=int(input("Enter Your Saving Goals:"))
x=SavingGoals-percentageOfSaving
# Compare current savings with the goal
if PerofSavingOrInvestment>SavingGoals:
  print(f"Congratulations, {name}! You’ve achieved your savings goal." )
else:
  print(f"Keep working on your savings, {name}. You're {x}% away from your goal.")

# -------------------- Export Summary --------------------
# Display a final summary of the user's financial health
print(f"Financial Health Summary for {name}:")
print("Monthly Income:",monthlyIncome)
print(f"Monthly Expenses:{monthlyExpenses}")
print(f"Total Savings:{TotalSavings}({percentageOfSaving}%)")
print("Expense Breakdown:")
print(f"\tEssentials:{PerofEssential}%")
print(f"\tWants:{PerofWant}%")
print(f"\tSaving / Investment:{PerofSavingOrInvestment}%")
print(f"Saving Goals:{SavingGoals}%")
print(f"Status: {x}% away from your goal.")
