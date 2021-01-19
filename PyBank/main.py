import os
import csv

csvpath = os.path.join("..","Resources","budget_data.csv")


#read header and then the other lines of data into either dictionary or list


# not working in having only one list with row and column, have to split the data
#months = [row for row in reader]
# print(header)
# print(data)
pnl = []
changes = []
date = []


count = 0
total_pnl = 0
total_change = 0
initial_pnl = 0

#tried it in the beginning, changed this after variables

#file = open(csvpath, newline='') - opens csv file however its not saving the variables
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

#tried with nested fors, trying another approach
#total number of moths included in the dataset
#because all of the lines where not on the same level below the for it was returning wrong values  T_T
    for row in reader:
      count = count + 1

      date.append(row[0])

#net total amount of PnL over the period
      pnl.append(row[1])

      total_pnl = total_pnl + int(row[1])


#changes in PnL over the period , then find average of the changes
      final_pnl = int(row[1])
      motnhly_pnly = final_pnl - initial_pnl

#storing in the list
      changes.append(motnhly_pnly)

      total_change = total_change + motnhly_pnly
      initial_pnl = final_pnl

      average_pnl = (total_change/count)

    
#greatest increase in profits date and amount 
# not workingsaving when asking for monthly changes because I am not asking for the list bbut the item
#have to ask for changes
      max_pnl = max(changes)
      min_pnl = min(changes)

# greatest decrease in losses date and amount
      max_pnl_date = date[changes.index(max_pnl)]
      min_pnl_date = date[changes.index(min_pnl)]

      print("Financial Analysis")
      print("------------------------------")
      print("Total Months: " + str(count))
      print("Total " + "$" + str(total_pnl))
      print("Average Change:" + "$" + str(float(average_pnl)))
      print("Greatest Increase in Profits: " + str(max_pnl_date) + " $" + (str(max_pnl)))
      print("Greatest Decrease in Profits: " + str(min_pnl_date) + " $" +(str(min_pnl)))


output_path = os.path.join("..", "Analysis", "financial_analysis.txt")
with open(output_path, 'w') as text:
      text.write("Financial Analysis" + "\n")
      text.write("------------------------------"+ "\n")
      text.write("Total Months: " + str(count)+ "\n")
      text.write("Total " + "$" + str(total_pnl)+ "\n")
      text.write("Average Change:" + "$" + str(float(average_pnl))+ "\n")
      text.write("Greatest Increase in Profits: " + str(max_pnl_date) + " $" + (str(max_pnl))+ "\n")
      text.write("Greatest Decrease in Profits: " + str(min_pnl_date) + " $" +(str(min_pnl))+ "\n")    