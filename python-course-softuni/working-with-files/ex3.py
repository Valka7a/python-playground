import csv

def average_price(kind, price = 0, count = 0):
    with open('files/catalog_full.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x in reader:
            if x[5] == kind:
                price += float(x[6])
                count += 1

        avg_price = price / count
        print('Average price of all {} products: {:.2f}'.format(kind, avg_price))

average_price('Infant')
average_price('Kid')
average_price('Men')
average_price('Unisex')
average_price('Woman')
