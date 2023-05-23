import os
import csv

# Set base directory path
dir = r"D:\Data_Analytics_Bootcamp\Module-3-Python\PyBank"

# Set file paths for budget data and analysis results file
budget_data = os.path.join(dir, r"Resources\budget_data.csv")
analysis_file = os.path.join(dir, r"analysis\financial_analysis.txt")

# Initialize variables
total_mon = 0
total_prof = 0
prof_changes = []
greatest_incr = {
    "date": "",
    "amount": 0
    }
greatest_decr = {
    "date": "",
    "amount": 0
    }

# Read budget data
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skip header
    next(csvreader)

    # Loop through rows in dataset
    for row in csvreader:
    
        # Extract date and profit/loss values
        date = row[0]
        prof = int(row[1])

        # Calculate total number of months
        total_mon += 1

        # Calculate net total amount of profit/losses
        total_prof += prof

        # Calculate change in profit/loss since previous month
        if total_mon > 1:
            prof_change = prof - prev_prof
            prof_changes.append(prof_change)

            # Find greatest increase and decrease in profits
            if prof_change > greatest_incr["amount"]:
                greatest_incr["date"] = date
                greatest_incr["amount"] = prof_change
            if prof_change < greatest_decr["amount"]:
                greatest_decr["date"] = date
                greatest_decr["amount"] = prof_change

        prev_prof = prof

# Calculate average change in profit/losses
avg_change = sum(prof_changes) / len(prof_changes)

# Format analysis results with line breaks between each line
analysis = f"""Financial Analysis

----------------------------

Total Months: {total_mon}

Total: ${total_prof}

Average Change: ${avg_change:.2f}

Greatest Increase in Profits: {greatest_incr["date"]} (${greatest_incr["amount"]})

Greatest Decrease in Profits: {greatest_decr["date"]} (${greatest_decr["amount"]})"""

# Print analysis to terminal
print(analysis)

# Export analysis results to text file
with open(analysis_file, "w") as txtfile:
    txtfile.write(analysis)

# Print message indicating the successful export
print(f"""
----------------------------

Analysis results saved to to: {analysis_file}.
""")