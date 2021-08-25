import os
import csv

csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader =csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)
    

    num_votes = 0
    candidate_count = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []

    for row in csvreader:
        #counting rows to find total votes
        num_votes += 1
        candidate_count.append(row[2])
    # if name exists, storage name in a new list(candidate_count), count the candidate's votes
    # use math to calculate vote percentage    
    for candidate in candidate_count:
        if candidate == "Khan":
           Khan.append(candidate_count)
           Kvote = len(Khan)
           Kvote_percent = "{:.3f}".format((Kvote/num_votes)*100)
        elif candidate == "Correy":
           Correy.append(candidate_count)
           Cvote = len(Correy)
           Cvote_percent = "{:.3f}".format((Cvote/num_votes)*100)
        elif candidate == "Li":
           Li.append(candidate_count)
           Lvote = len(Li)
           Lvote_percent = "{:.3f}".format((Lvote/num_votes)*100)
        else:
           candidate == "OTooley"
           OTooley.append(candidate_count)
           Ovote = len(OTooley)
           Ovote_percent = "{:.3f}".format((Ovote/num_votes)*100)

#create a dictonary to store candidate name and corresponding votes          
list = {"Khan":Kvote,"Correy":Cvote,"Li":Lvote, "O'Tooley":Ovote}
#use python distionary's max function to find the winner
biggest_vote = max(list,key=list.get)

print("Election Results")
print("---------------------------------")
print(f"Total Votes:{num_votes}") 
print(f"Khan: {Kvote_percent}% ({Kvote})")
print(f"Correy: {Cvote_percent}% ({Cvote})")
print(f"Li: {Lvote_percent}% ({Lvote})")
print(f"O'Tooley: {Ovote_percent}% ({Ovote})")
print("---------------------------------")
print(f"Winner:{biggest_vote}")
print("---------------------------------")

output_result = os.path.join("PyPoll","analysis","PyPoll.txt")

with open(output_result,"w") as txt_file:
    txt_file.write("Election Results"+"\n")
    txt_file.write("----------------"+"\n")
    txt_file.write("Total Votes:"+ str(num_votes) + "\n")
    txt_file.write("Khan:" + str(Kvote_percent) + "%" + str(Kvote) + "\n")
    txt_file.write("Correy:" + str(Cvote_percent) + "%" + str(Cvote) + "\n")
    txt_file.write("Li:" + str(Lvote_percent) + "%" + str(Lvote) + "\n")
    txt_file.write("O'Tooley:" + str(Ovote_percent) + "%" + str(Ovote) + "\n")
    txt_file.write("----------------"+"\n")
    txt_file.write("Winner:"+ str(biggest_vote) + "\n")
    txt_file.write("----------------"+"\n")