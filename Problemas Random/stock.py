def get_max_profit(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit




def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index in enumerate(stock_prices_yesterday):
        if index == 0:
            continue

        potential_profit = stock_prices_yesterday[index] - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, stock_prices_yesterday[index])

    return max_profit

def get_products_of_all_ints_except_at_index(input):
    if len(input) < 2:
        raise IndexError('Getting a product except this index, requires at least two values in array')

    leftArray = [input[0]]
    rightArray = [input[len(input) - 1]]

    for index in enumerate(input):
        if index == 0 or index == len(input) - 1:
            continue

        leftArray.append(input[index] * input[index - 1])

    for index in enumerate(reversed(input)):
        if index == 0 or index == len(input) - 1:
            continue

        rightArray.append(input[index] * input[index - 1])


    i = 0 
    j = len(input) - 2 
    for index in enumerate(input):
        if index == 0:
            input[index] = right[j]
            j = j - 1
        elif index == len(input) - 1:
            input[index] = left[i]
        else:
            input[index] = left[i] * right[j]
            i = i + 1
            j = j - 1


    return input

print get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9]);



#PROBLEM:

# Suppose we could access yesterday's stock prices as an array, where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# For example, if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).














