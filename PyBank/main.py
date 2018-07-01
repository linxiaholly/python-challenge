import os
import csv
 #read csv file
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

#conver the file to 2 list and calculate the summary numbers
    totalmonth = 0
    totalamount = 0.0
    Month = []
    Revenue =[]
    changes = [ ]
    different = 0.0

    for row in csvreader:
        
        totalmonth += 1
        totalamount += float(row[1])
        changes.append (- different + float(row[1]))
        Month.append(row[0])
        Revenue.append(row[1])
        different = float(row[1])
#delet the first number in changes list 
    changes.pop(0)
    
    totalchange = 0.0
    numberofchange = 0
#get the average change
    for change in changes:
        totalchange += change
        numberofchange +=1
    avgchange = totalchange / numberofchange
#get the max and mix changes in profit and position in the list
    maxchange = max(changes)
    minchange = min(changes)
    maxmonth = Month[changes.index(maxchange)+1]
    minmonth = Month[changes.index(minchange)+1]
    maxrevenue = Revenue[changes.index(maxchange)+1]
    minrevenue = Revenue[changes.index(minchange)+1]

    print ("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: "+ str(totalmonth))
    print("Total: "+ "$"+str(int(totalamount)))
    print("Average Change: $"+str("{0:.2f}".format(avgchange)))
    print("Greatest Increase in Profits:"+ maxmonth + " ($"+ str(int(maxchange)) + ")")
    print("Greatest Decrease in Profits:"+ minmonth + " ($"+ str(int(minchange)) + ")")
    
    
        
        
    
