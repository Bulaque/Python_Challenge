import os
import csv
import pandas as pd

election_datacsv = os.path.join("..", "Resources","election_data.csv").replace('\\','/')

print(f"current working dir: {os.getcwd()}")
print(f"csv path: {election_datacsv}")
with open(election_datacsv) as election_sheet:
    
    electiondata_reader = csv.reader(election_sheet)
    heading = next(electiondata_reader)

election_df = pd.read_csv(election_datacsv)


print("Election Results")
print("-------------------------------")

# The total number of votes cast

total_votes = election_df["Ballot ID"].nunique()
print(f"Total Votes: {total_votes}")
print("--------------------------------")

# A complete list of candidates who recieved votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

Full_amount_votes = election_df.groupby("Candidate")["Ballot ID"].nunique()

# For Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane

# The winner of the election based on popular vote