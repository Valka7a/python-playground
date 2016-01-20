prices = []
while True:
    # User input
    user_input = input("Enter price or stop: ")
    # Show warning if there isn't enough prices
    if user_input == 'stop':
        if len(prices) < 4:
            print("You must enter 4 or more prices.")
            continue
        else:
            break

    try:
        price = float(user_input)

        if price <= 0:
            raise Exception('Price cannot be less then or equal to 0.')

        # Collect the price
        prices.append(price)

    except ValueError:
        print('Invalid input!')
        exit()

    except Exception as error:
        print(error)
        exit()

# Print minimum and maximum prices
min_price = min(prices)
max_price = max(prices)

# Check if all the prices are the same.
if min_price == max_price:
    print('All prices are the same: {0:.2f}'.format(min_price))
    exit()

# Print min and max prices
print('Min price: {0:.2f}'.format(min_price))
print('Max prices: {0:.2f}'.format(max_price))

# Filter the rest of the prices
prices = list(filter(lambda item: item not in [min_price, max_price], prices))

# Check if there is average price
if len(prices) < 1:
    print('Average price not found.')
    exit()

# Calculate and print the average price
avg_price = sum(i for i in prices) / len(prices)
print('Average: {0:.2f}'.format(avg_price))
