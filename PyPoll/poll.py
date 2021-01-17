#import python imports
import csv
import os

#read the csv and convert into a list
with open('Resources/election_data.csv') as csvfile:
    data_reader = csv.reader(csvfile)
#read the header
    header = next(data_reader)
    data = list(data_reader)

#calculate the number of votes
votes = len(data)
#define the candidates 
candidate = 'Khan'
candidate = 'Li'
candidate = 'Correy'
candidate =  'O_Tooley'
##fix this 
#count candidates
Khan = int(candidate.count("Khan"))
Li = int(candidate.count("Li"))
Correy = int(candidate.count("Correy"))
O_Tooley = int(candidate.count("O_Tooley"))

##this is correct need to fix the define the candidate section

#percentage of votes each candidate won
Khan_percent = (Khan/votes)*100
Li_percent = (Li/votes)*100
Correy_percent = (Correy/votes)*100
O_Tooley_percent = (O_Tooley/votes)*100

#total number of votes each candidate won




        