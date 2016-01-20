import csv
# Make empty list
catalog_file = []

def find_and_change_product(catalog_number, new_price):
    # Make new price to float
    new_price = float(new_price)

    # Open file in read mode
    with open('files/catalog_full.csv') as csvfile:
        # csv read file
        csv_file = csv.reader(csvfile, delimiter=',')
        for row in csv_file:
            # find product
            if row[0] == catalog_number:
                # Get current price
                old_price = float(row[6])
                # Change with new price
                row[6] = '{}'.format(new_price)
                # Save it in list
                catalog_file.append(row)
                # print the changed product
                print('{} product price change from: {:.2f} to: {:.2f}'.format(
                                        row[1], old_price, new_price))
            else:
                # Save other products in list
                catalog_file.append(row)

    # Open file in write mode to overwrite it
    with open('files/catalog_full.csv', 'w') as csvfile:
        csv_file = csv.writer(csvfile)
        # Replace products with changed product
        csv_file.writerows(catalog_file)

# User input
product = input('Enter catalog number: ')
price = input('Enter new price: ')

# Call the function with user input
find_and_change_product(product, price)
