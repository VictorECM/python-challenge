import os
import csv

csvpath = os.path.join("..","Resources","election_data.csv")

#adding my lists to store my data
count = 0
candidates = []
winner_candidate = []
vcount = []
vpercent = []

# always check what reader is reading, instead of csvfile I had csvpath
with open(csvpath, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

   
#   * A complete list of candidates who received votes
    for row in reader:
        count = count + 1

        candidates.append(row[2])


    for x in set(candidates):
        winner_candidate.append(x)
#   * The total number of votes each candidate won
        y = candidates.count(x)

        vcount.append(y)
#   * The percentage of votes each candidate won
        p = (y/count)*100
# tried to format the print, found it better to format value P when passing it to the list
        vpercent.append("{:.2f}".format(p))

       #   * The winner of the election based on popular vote 
        winn_count = max(vcount)
        winner = winner_candidate[vcount.index(winn_count)]

    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(count))    
    print("-------------------------")
for i in range(len(winner_candidate)):
            print(winner_candidate[i] + ": " + str(vpercent[i]) +"% (" + str(vcount[i])+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
# had to move indentation otherwise winner appeared after every candidate

output_path = os.path.join("..", "Analysis", "electoral_analysis.txt")
with open(output_path, 'w') as text:
      text.write("Election Results" + "\n")
      text.write("------------------------------"+ "\n")
      text.write("Total Votes :" + str(count)+ "\n")
      text.write("------------------------------"+ "\n")
      for i in range(len(winner_candidate)):
        text.write(winner_candidate[i] + ": " + str(vpercent[i]) +"% (" + str(vcount[i])+ ")"+ "\n")
      text.write("------------------------------"+ "\n")
      text.write("Winner: " + winner + "\n")
      text.write("------------------------------"+ "\n")
# had to move indentation otherwise winner appeared after every candidate




