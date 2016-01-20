import csv

price = 0
items = 0

with open('files/catalog_full.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x in reader:
        price += float(x[6])
        items += 1

avg_price = price / items
print('Average price of all products: {0:.2f}'.format(avg_price))
