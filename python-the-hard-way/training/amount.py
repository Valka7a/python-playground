orders = [
    {'amount': 250},
    {'amount': 400},
    {'amount': 100},
    {'amount': 325}
]


def get_total_amount(orders):
    total = 0

    for order in orders:
         total += order['amount']

    return total

def reduce_get_total_amount(orders):
    return reduce(lambda total, order: order['amount'] + total, orders, 0)

print get_total_amount(orders)

print reduce_get_total_amount(orders)
