
votes=[]
r=0
d=0
c=0
candidates=["Raymon Anthony Doane", "Diana DeGette", "Charles Casper Stockham"] 

with open("PyPoll/Resources/election_data.csv") as f:
    line=f.readline()
    while line:
        line=f.readline()
        if len(line):
            line=line.replace("\n", "")
            line=line.split(",")
            if line[2]=="Raymon Anthony Doane":
                r+=1
            if line[2]=="Diana DeGette":
                d+=1
            if line[2]=="Charles Casper Stockham":
                c+=1
            votes.append(line)
winner=max([r,d,c])
winner=candidates[[r,d,c].index(winner)]

output="Election Results\n-------------------------"
output+=f"\nTotal Votes: {len(votes)}\n-------------------------"
output+=f"\nCharles Casper Stockham: {round(c/len(votes)*100, 3)}% ({c})"
output+=f"\nDiana DeGette: {round(d/len(votes)*100, 3)}% ({d})"
output+=f"\nRaymon Anthony Doane: {round(r/len(votes)*100, 3)}% ({r})"
output+=f"\n-------------------------\nWinner: {winner}"

with open("C:/Users/Scherz/Desktop/School/Homework/Python-challenge/PyPoll/Analysis/Election_Results.txt", "w") as f:
    f.write(output)
    f.close()
print(output)