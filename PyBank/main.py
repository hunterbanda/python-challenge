# Import modules
import os
import csv
import pandas as pd # Import pandas

# Capture path in variable
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Use pandas to read data
df = pd.read_csv('budget_data.csv')

# Count number of months
number_of_months = len(df)
print("Total months: ", number_of_months)

# Get total amount of profit/losses
total_amount = sum(df["Profit/Losses"])
print("Total: ", total_amount)

# Calculate average change profit/losses
average_change = total_amount / number_of_months
print("Average Change: ", average_change)

# Calculate greatest increase in profit
greatest_increase = max(df["Profit/Losses"])
print("Greatest Increase in Profit: ", greatest_increase)

# Calculate greatest decrease in profit
greatest_decrease = min(df["Profit/Losses"])
print("Greatest Decrease in Profit: ", greatest_decrease)
                  







