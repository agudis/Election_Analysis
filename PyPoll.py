
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote. 

#Add our dependencies. 

import csv
import os

#Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Add total vote counter. 
total_votes = 0 

#Declare candidates with a list. 
candidate_options = []

#Declare candidate votes with a dictionary. 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.  
with open(file_to_load) as election_data:

    #Read the file object with the read function. 
    file_reader = csv.reader(election_data)

    #Read the header row. 
    headers = next(file_reader)
    
    #Print each row in the CSV file. 
    for row in file_reader:

        #Add to the total vote count. 
        total_votes += 1

        #Print the candidate name from each row. 
        candidate_name = row[2]

        #If the candidate does not match any existing canddiate... 
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)

            #Track that candidates vote count. 
            candidate_votes[candidate_name] = 0

        #Add a vote to that canddiate's count. 
        candidate_votes[candidate_name] += 1
    
    #Determine the percentage of votes for each candidate by looping through the counts. 

    # 1. Iterate through the candidate list. 
    for candidate_name in candidate_votes:

        # 2. Get the vote count of each candidate. 
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes. 
        vote_percentage = float(votes)/float(total_votes) * 100 

        # 4. Print candidate name, vote count and percentage of vote. 
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        # Determine winning vote count and candidate. 

        # 1. Determine if the votes are greater than the winning count. 

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # 2. If true then set winning_count = votes and set winning_percentage = vote_percentage

            winning_count = votes
            winning_percentage = vote_percentage

            # 3. Set the winning_count = candidate name 

            winning_candidate = candidate_name

    # Print the winning Candidate.  

    winning_candidate_summary = ( 
        f'----------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winnig Percentage: {winning_percentage:.1f}%\n'
        f'----------------------------\n')

    print(winning_candidate_summary)
    

#Close the file. 
election_data.close 
