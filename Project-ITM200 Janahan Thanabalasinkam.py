import csv
import matplotlib.pyplot as plt

data = []

with open('data.csv', mode= 'r') as fileCSV:
    csv_reader = csv.reader(fileCSV)

    for line in csv_reader:
        data.append(line)
fileCSV.close()

#appending data list into its own individual lists
month = data[0]
year12 = data[1]
year13 = data[2]
year14 = data[3]
year15 = data[4]
year16 = data[5]
year17 = data[6]
year18 = data[7]
year19 = data[8]
year20 = data[9]
year21 = data[10]
year22 = data[11]

#coverting all strings into integers
year12 = [eval(i) for i in year12]
year13 = [eval(i) for i in year13]
year14 = [eval(i) for i in year14]
year15 = [eval(i) for i in year15]
year16 = [eval(i) for i in year16]
year17 = [eval(i) for i in year17]
year18 = [eval(i) for i in year18]
year19 = [eval(i) for i in year19]
year20 = [eval(i) for i in year20]
year21 = [eval(i) for i in year21]
year22 = [eval(i) for i in year22]

#Yearly Sums
year12Sum = sum(year12[1:])
year13Sum = sum(year13[1:])
year14Sum = sum(year14[1:])
year15Sum = sum(year15[1:])
year16Sum = sum(year16[1:])
year17Sum = sum(year17[1:])
year18Sum = sum(year18[1:])
year19Sum = sum(year19[1:])
year20Sum = sum(year20[1:])
year21Sum = sum(year21[1:])
year22Sum = sum(year22[1:])

#sales estimation
sales6M2021 = sum(year21[1:7])
sales6M2022 = sum(year22[1:7])

salesGrowthRate = ((sales6M2022 - sales6M2021)/sales6M2022)

year21.remove(2021)

estSale = []
for i in range (len(year21)):
    x = int(year21[i] + (year21[i]*salesGrowthRate))
    estSale.append(x)

dict = {'July':estSale[6], 'August':estSale[7], 'September':estSale[8], 'October':estSale[9], 'November': estSale[10], 'December':estSale[11]}

#printing car stats to txt file
carStats = open('carStats.txt', 'w')
carStats.write("2012: " + str(year12Sum) + '\n')
carStats.write("2013: " + str(year13Sum) + '\n')
carStats.write("2014: " + str(year14Sum) + '\n')
carStats.write("2015: " + str(year15Sum) + '\n')
carStats.write("2016: " + str(year16Sum) + '\n')
carStats.write("2017: " + str(year17Sum) + '\n')
carStats.write("2018: " + str(year18Sum) + '\n')
carStats.write("2019: " + str(year19Sum) + '\n')
carStats.write("2020: " + str(year20Sum) + '\n')
carStats.write("2021: " + str(year21Sum) + '\n')
carStats.write("2022: " + str(year22Sum) + '\n')
carStats.write("Sales Growth Rate: " + str(salesGrowthRate) + '\n')
carStats.write("Estimated Sales for last 6 months: " + str(dict))
carStats.close()


#Vertical Bar Graph
x = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
y = [year12Sum, year13Sum, year14Sum, year15Sum, year16Sum, year17Sum, year18Sum, year19Sum, year20Sum, year21Sum]
plt.figure(1)
plt.bar(x,y)

plt.title("Automotive Sales 2012-2021") # Writing plot title
plt.xlabel("Years")      # Writing x-axis label
plt.ylabel("Sales")  # Writing y-axis label

plt.show()

#Horizontal Bar Graph
x = ['July', 'August', 'September', 'October', 'November','December']
y = [estSale[6], estSale[7], estSale[8], estSale[9],estSale[10], estSale[11]]
plt.figure(2)
plt.barh(x,y)

plt.title("Estimated Sales for last 6 months of 2022") # Writing plot title
plt.xlabel("Sales")      # Writing x-axis label
plt.ylabel("Months")  # Writing y-axis label
plt.grid()

plt.show()

