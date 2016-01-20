prices = []

# Get user's input
while True:
    user_input = input('Enter price or stop: ')

    # Show warning if there isn't enough prices
    if user_input == 'stop':
        if len(prices) < 4:
            print('You must enter at least 4 prices.')
            continue
        else:
            break

    try:
        price = int(user_input)

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


unique_prices = list(set(prices))
prices_length = len(unique_prices)

# Check if all the prices are the same
if prices_length == 1:
    print('All the prices are the same:', unique_prices[0])
    exit()

# Sort the list if the prices list
# have more than one value
unique_prices.sort()

# Calculate middle price
if prices_length == 2:
    middle_price = 'Middle price not found.'
elif prices_length % 2 == 1:
    middle_price = 'Middle price:' + str(unique_prices[prices_length // 2])
else:
    middle_price = ' '.join([
        'Middle price is between:',
        str(unique_prices[prices_length // 2 - 1]),
        'and',
        str(unique_prices[prices_length // 2])])

# Print the results
print('Max price:', max(unique_prices))
print(middle_price)
print('Min price:', min(unique_prices))
