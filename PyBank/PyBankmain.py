import os
import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader =csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)

    num_rows = 0
    net_total_amount = 0
    current_row_profit = 0
    profit_dif = 0
    months = []
    profits_list = []
    month_change = []
    months = []

    for row in csvreader:
        num_rows += 1
        net_total_amount = net_total_amount + int(row[1])
        next_row_profit = int(row[1])
        months.append(row[0])
        profits_list.append(next_row_profit)
        
        if (num_rows == 1):
          current_row_profit = next_row_profit
          
        else:
           profit_dif = next_row_profit - int(current_row_profit)

    average_change = round(profit_dif/(num_rows - 1), 2)
    
    for i in range(0,len(profits_list)):
        month_change.append(profits_list[i]-profits_list[i-1])

    
    greatest_increase = max(month_change)
    greatest_decrease = min(month_change)
    month_for_increase = months[month_change.index(greatest_increase)]
    month_for_decrease = months[month_change.index(greatest_decrease)]

    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months:{num_rows}")
    print(f"Total:${net_total_amount}")
    print(f"Average Change:${average_change}")
    print(f"Greatest Increase in Profits:{month_for_increase} (${greatest_increase})")
    print(f"Greatest Decrease in Profits:{month_for_decrease} (${greatest_decrease})")
    
    output_result = os.path.join("PyBank","analysis","PyBank.txt")

with open(output_result,"w") as txt_file:
    txt_file.write("Financial Analysis"+"\n")
    txt_file.write("------------------"+"\n")
    txt_file.write("Total Months:"+ str(num_rows) + "\n")
    txt_file.write("Total:" + "$" + str(net_total_amount) +"\n")
    txt_file.write("Average Change:" +"$"+ str(average_change) + "\n")
    txt_file.write("Greatest Increase in Profits:" + str(month_for_increase) + "$" + str(greatest_increase) + "\n")
    txt_file.write("Greatest Decrease in Profits:" + str(month_for_decrease) + "$" + str(greatest_decrease) + "\n")