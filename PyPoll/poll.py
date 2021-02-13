# import python imports
import csv
import os

# read the csv and convert into a list
with open('Resources/election_data.csv') as csvfile:
    data_reader = csv.reader(csvfile)
# read the header
    header = next(data_reader)
    data = list(data_reader)

# calculate the number of votes
total_votes = len(data)
vote_counter = {}
# create a list of candidates and then a dictionary with the candidate
candidate_list = []
for row in data:
    candidate_name = row[2]
    if candidate_name not in candidate_list:
        #candidate_name = row[2] 
        candidate_list.append(candidate_name)
        vote_counter[candidate_name] = 0
    vote_counter[candidate_name] = vote_counter[candidate_name] +1

# total number of votes and percentage of votes each candidate won
Correy_votes = vote_counter.get("Correy")  
Khan_votes = vote_counter.get("Khan")  
Li_votes = vote_counter.get("Li")  
OTooley_votes = vote_counter.get("O'Tooley")  
Correy_percentage = float(Correy_votes) / float(total_votes) * 100    
Khan_percentage = float(Khan_votes) / float(total_votes) * 100  
Li_percentage = float(Li_votes) / float(total_votes) * 100  
OTooley_percentage = float(OTooley_votes) / float(total_votes) * 100 

# figure out the winner
poll_winner = max(vote_counter)
poll_loser = min(vote_counter)
## keep getting error for the winner. Khan should be the winner he has the most votes.


Analysis = f"""Election Results
#----------------------------
#Total Votes: {total_votes}
#Candidates: {candidate_list}
#Correy Votes: {Correy_votes}
#Khan Votes: {Khan_votes}
#Li Votes: {Li_votes}
#O'Tooley Votes: {OTooley_votes}
#Correy Percentage: {Correy_percentage}
#Khan Percentage: {Khan_percentage}
#Li Percentage: {Li_percentage}
#O'Tooley Percentage: {OTooley_percentage}
#Poll Winner: {poll_winner }
#Poll Loser: {poll_loser}"""
print(Analysis)