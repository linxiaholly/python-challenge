import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    totalvote = 0
    candidate = []
    number_vote = [0, 0, 0, 0]
    for row in csvreader:
        totalvote += 1
        if row[2] not in candidate:
            candidate.append(row[2])
        vote_index = candidate.index(row[2])
        number_vote[vote_index]+=1
    maxvote = max(number_vote)
    winner = candidate[number_vote.index(maxvote)]

                          
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(totalvote))
    print("-----------------------------")
    for a in range(len(candidate)):
        name = str(candidate[a])
        vote = str(number_vote[a])
        portion = str("{0:.3f}%".format(number_vote[a]/totalvote *100))

        print(name+": "+portion+ " ("+vote+")")
    print("-----------------------------")
    print("Winner: " +winner)
    print("-----------------------------")
    
    
        
        
       
