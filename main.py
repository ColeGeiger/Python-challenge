
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


print(bankdata)   
print("Total months: ", len(bankdata))
print("Total: $"+ str(net))
print("Average Change: $"+ str(round(sum(change)/len(change), 2)))
print("Greatest Increase in Profits: "+max_date+" ($"+str(max_change)+")")
print("Greatest Decrease in Profits: "+min_date+" ($"+str(min_change)+")")