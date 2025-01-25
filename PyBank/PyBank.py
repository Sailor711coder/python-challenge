# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
#file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open('PyBank/budget_data.csv', 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)   
    months = []
    profit_losses = []
    changes = []
    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
# Calculate the total number of months
total_months = len(months)
# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)
# Calculate the changes in profit/losses and store them in a list
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)
# Calculate the average change
average_change = sum(changes) / len(changes)
# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]
# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")   
# Generate the output summary
output= (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    
)

# Print the output
file_to_output="PyBank/output.txt"

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
