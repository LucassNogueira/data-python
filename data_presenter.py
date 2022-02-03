# import csv

# cupcake_invoice = 'CupcakeInvoices.csv'
# with open(cupcake_invoice, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
#         print(row)


file_name = open('CupcakeInvoices.csv')

# for line in file_name:
#     print(line)

# for line in file_name:
#     line = line.strip('\n').split(',')
#     print(line[2])

# for line in file_name:
#     line = line.split(',')
#     total = (float(line[3])*float(line[4]))
#     print(total)

total = 0

for line in file_name:
    line = line.split(',')
    total += float(line[3])*float(line[4])

print(round(total,2))

file_name.close()