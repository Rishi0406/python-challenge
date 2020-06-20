#import libraries
import os
import csv

#csvpath to get data and output_path to publish result
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("analysis","Election Results.txt")

#define all variables
votes = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

total_votes = []
total_khan = []
total_correy = []
total_li = []
total_otooley = []

#read csv file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')

#ignore header in counting
    header = next(csvreader)

#loop to read through each row
    for row in csvreader: 

        votes = row[2]

        total_votes.append(votes) #count number of votes by adding

        if row[2] == "Khan":    #count and add Khan's votes and find his percentage from total votes

            total_khan.append(khan_votes) 
            khan_percent = (len(total_khan)/len(total_votes))*100

        elif row[2] == "Correy":    #count and add Correy's votes and find his percentage from total votes

            total_correy.append(correy_votes)
            correy_percent = (len(total_correy)/len(total_votes))*100

        elif row[2] == "Li":    #count and add Li's votes and find his percentage from total votes

            total_li.append(li_votes)
            li_percent = (len(total_li)/len(total_votes))*100

        elif row[2] == "O'Tooley":  #count and add O'Tooley's votes and find his percentage from total votes

            total_otooley.append(otooley_votes)
            otooley_percent = (len(total_otooley)/len(total_votes))*100

#find winner
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
vote_percent = [khan_percent, correy_percent, li_percent, otooley_percent]
vote_dict = (candidates, vote_percent)

winner_name = ""
winner_index = []
#import libraries
import os
import csv
#csvpath to get data and output_path to publish result
csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("analysis","Election Results.txt")
#define all variables
votes = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []
total_votes = []
total_khan = []
total_correy = []
total_li = []
total_otooley = []
#read csv file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=',')
#ignore header in counting
    header = next(csvreader)
#loop to read through each row
    for row in csvreader: 
        votes = row[2]
        total_votes.append(votes) #count number of votes by adding
        if row[2] == "Khan":    #count and add Khan's votes and find his percentage from total votes
            total_khan.append(khan_votes) 
            khan_percent = (len(total_khan)/len(total_votes))*100
        elif row[2] == "Correy":    #count and add Correy's votes and find his percentage from total votes
            total_correy.append(correy_votes)
            correy_percent = (len(total_correy)/len(total_votes))*100
        elif row[2] == "Li":    #count and add Li's votes and find his percentage from total votes
            total_li.append(li_votes)
            li_percent = (len(total_li)/len(total_votes))*100
        elif row[2] == "O'Tooley":  #count and add O'Tooley's votes and find his percentage from total votes
            total_otooley.append(otooley_votes)
            otooley_percent = (len(total_otooley)/len(total_votes))*100
            
#find winner
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
vote_percent = [khan_percent, correy_percent, li_percent, otooley_percent]
vote_dict = (candidates, vote_percent)
winner_name = ""

for i in range(len(candidates)):
    if i == vote_percent.index(max(vote_percent)):
        winner_name = candidates[i]

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(total_votes)}")
print("-------------------------")
print(f"Khan: {khan_percent:.3f}% ({len(total_khan)})")
print(f"Correy: {correy_percent:.3f}% ({len(total_correy)})")
print(f"Li: {li_percent:.3f}% ({len(total_li)})")
print(f"O'Tooley: {otooley_percent:.3f}% ({len(total_otooley)})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

#write output in text file
with open(output_path, 'w') as txtfile:

    txtfile.writelines("Election Results" + "\n")
    txtfile.writelines("-------------------------" + "\n")
    txtfile.writelines(f"Total Votes: {len(total_votes)}\n")
    txtfile.writelines("-------------------------" + "\n")
    txtfile.writelines(f"Khan: {khan_percent:.3f}% ({len(total_khan)})\n")
    txtfile.writelines(f"Correy: {correy_percent:.3f}% ({len(total_correy)})\n")
    txtfile.writelines(f"Li: {li_percent:.3f}% ({len(total_li)})\n")
    txtfile.writelines(f"O'Tooley: {otooley_percent:.3f}% ({len(total_otooley)})\n")
    txtfile.writelines("-------------------------" + "\n")
    txtfile.writelines(f"Winner: {winner_name}\n")
    txtfile.writelines("-------------------------" + "\n")