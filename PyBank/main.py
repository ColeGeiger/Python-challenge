
net=0
max_change=0
min_change=0
max_date=None
min_date=None
change=[]
bankdata=[]

with open("PyBank/Resources/budget_data.csv") as f:
    line=f.readline()
    previous=None
    while line:
        line=f.readline()
        if len(line):
            line=line.replace("\n", "")
            line=line.split(",")
            line[1]=int(line[1])
            num=line[1]
            net+=num
            bankdata.append(line)
            if previous: 
                chg=num-previous
                change.append(chg)
                if chg>max_change: 
                    max_change=chg
                    max_date=line[0]
                if chg<min_change:
                    min_change=chg
                    min_date=line[0]
            previous=num

output="Financial Analysis\n----------------------------"

output+="\nTotal months: " + str(len(bankdata))
output+="\nTotal: $"+ str(net)
output+="\nAverage Change: $"+ str(round(sum(change)/len(change), 2))
output+="\nGreatest Increase in Profits: "+max_date+" ($"+str(max_change)+")"
output+="\nGreatest Decrease in Profits: "+min_date+" ($"+str(min_change)+")"
with open("PyBank/Analysis/Financial_Analysis.txt", "w") as f:
    f.write(output)
    f.close()
print(output)
