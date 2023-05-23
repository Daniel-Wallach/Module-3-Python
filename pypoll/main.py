import os
import csv

# Set base directory path
dir = r"D:\Data_Analytics_Bootcamp\Module-3-Python\PyPoll"

# Set file paths for election data and analysis results file
election_data = os.path.join(dir, r"Resources\election_data.csv")
analysis_file = os.path.join(dir, r"analysis\election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read election data
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader)
    
    # Loop through rows in dataset
    for row in csvreader:
    
        # Calculate total votes and candidate votes
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

# Calculate percentage of votes for each candidate
results = []
for candidate in candidates:
    votes = candidate_votes[candidate]
    percent = (votes / total_votes) * 100
    results.append({"candidate": candidate, "votes": votes, "percent": percent})

# Find winner
winner = ""
max_votes = 0
for result in results:
    if result["votes"] > max_votes:
        max_votes = result["votes"]
        winner = result["candidate"]

# Format analysis results with line breaks between each line
analysis = f"""Election Results

----------------------------

Total Votes: {total_votes}

----------------------------

"""

analysis += "\n\n".join([f"{result['candidate']}: {result['percent']:.3f}% ({result['votes']})" for result in results])
analysis += f"""

----------------------------

Winner: {winner}

----------------------------"""

# Print analysis to terminal
print(analysis)

# Export the analysis results to text file
with open(analysis_file, "w") as file:
    file.write(analysis)

# Print message indicating the successful export
print(f"""
Analysis results saved to: {analysis_file}
""")