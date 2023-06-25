# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Variable set up

ballot_id=[]
county=[]
candidate=[]
candidate_unique=[]
candidate_votes=[]
total_votes=0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #Store Headers
        headers=next(csvreader)
        #Place CSV data into lists
        for row in csvreader:
            ballot_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        candidate_unique.append(candidate[0])
        #Produces list of unique candidates
        for i in range(len(candidate)):
            total_votes=total_votes+1
            if candidate[i] in candidate_unique:
                pass
            else:
                candidate_unique.append(candidate[i])
        #Populates a list of unique vote counters
        for i in range(len(candidate_unique)):
            candidate_votes.append(0)
        for i in range(len(candidate)):
            for j in range(len(candidate_unique)):
                if candidate[i]==candidate_unique[j]:
                    candidate_votes[j]=candidate_votes[j]+1
winner=""
winner_votes=0
for j in range(len(candidate_unique)):
    if candidate_votes[j]>winner_votes:
        winner=candidate_unique[j]
        winner_votes=candidate_votes[j]
str_winner="Winner: "+winner
title=("Election Results")
linebreak=("-------------------------")
str_total_votes="Total Votes: "+str(total_votes)
output=[title,linebreak,str_total_votes,linebreak]
for line in range(len(output)):
    print(output[line])
for j in range(len(candidate_unique)):
    print(f"{candidate_unique[j]}: {round(candidate_votes[j]/total_votes*100,3)}% ({candidate_votes[j]})")
print(linebreak)
print(str_winner)
print(linebreak)
#Txt File Outupt
output_file = os.path.join("analysis","output.txt")
with open(output_file, "w") as datafile:
    
        for line in range(len(output)):
            datafile.write(output[line])
            datafile.write('\n')
        for j in range(len(candidate_unique)):
            datafile.write(f"{candidate_unique[j]}: {round(candidate_votes[j]/total_votes*100,3)}% ({candidate_votes[j]})")     
            datafile.write('\n') 
        datafile.write(linebreak)
        datafile.write('\n')     
        datafile.write(str_winner)
        datafile.write('\n')  
        datafile.write(linebreak)
        datafile.write('\n')       