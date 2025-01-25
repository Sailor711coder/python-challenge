# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
#file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open('PyPoll/election_data.csv','r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    votes=[]
    candidates=[]
    # Loop through each row of the dataset and process it
    for row in reader:
        candidates.append(row[2])
        votes.append(row[0])
        # Print a loading indicator (for large datasets)
total_votes = len(votes)
total_candidates = []
for val in candidates:
    if val not in total_candidates:
        total_candidates.append(val)
print("the total votes "+ str(total_votes))
winner="" 
max=0    # Increment the total vote count for each row
for can in total_candidates:
    per=candidates.count(can)
    percapital =per/total_votes * 100
    print(percapital)
    print(per)
    if per > max:
        winner=can
        max=per
print("the winner is "+winner)
        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
