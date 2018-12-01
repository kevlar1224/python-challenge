import os
import csv

filepath = os.path.join("..","Files","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

voter = []
county = []
candidate = []

with open(filepath,newline = "") as voterfile:
    voterdata = csv.reader(voterfile, delimiter = ",")
    for row in voterdata:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_votes = len(voter)

candidates_list = []
for i in range(1,len(candidate)):
    if candidate[i] not in candidates_list:
        candidates_list.append(candidate[i])

candidate_total = []
for i in candidates_list:
    vote_count = candidate.count(i)
    candidate_total.append(vote_count)

candidates_percentages = []
for i in range(len(candidates_list)):
    vote_percent = round(100*candidate_total[i]/total_votes, 2)
    candidates_percentages.append(vote_percent)

most_votes = max(candidate_total)
winner = candidates_list[candidate_total.index(most_votes)]

print("The candidates were: \n")
for i in range(len(candidates_list)):
    print(candidates_list[i] + ", with " + str(candidate_total[i]) + " votes (" + str(candidates_percentages[i]) + "%" +  " of the popular vote)")
print("\nThe winner of the election is: " + str(winner))

with open("Election Results.txt", "w+") as e:
    e.write("The candidates were: \n\n")
    for i in range(len(candidates_list)):
        e.write(candidates_list[i] + ", with " + str(candidate_total[i]) + " votes (" + str(candidates_percentages[i]) + "%" +  " of the popular vote)\n")
    e.write("\n\nThe winner of the election is: " + str(winner))
