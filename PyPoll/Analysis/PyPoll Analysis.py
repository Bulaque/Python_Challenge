import csv
import os

election_datacsv = os.path.join("..", "Resources","election_data.csv").replace('\\','/')

with open(election_datacsv) as election_sheet:
    
    electiondata_reader = csv.reader(election_sheet)
    heading = next(electiondata_reader)

Winner = []
Total_votes = 0

with open(election_datacsv) as final_data:
    reader = csv.reader(final_data)

    heading = next(reader)

    first_row = next(reader)
    Total_votes += 1

    for row in reader:

        
        Total_votes += 1


        

    

# The total number of votes cast
Total_votes

# A complete list of candidates who recieved votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

# Return the winner based on popular vote

# Answer
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
#print(f"Charles Casper Stockham: {}")
#print(f"Diana DeGette: {}")
#print(f"Raymon Anthony Doane: {}")
print("-------------------------")
#print(f"Winner: {}")




#Answer is in a dictionary that you will make