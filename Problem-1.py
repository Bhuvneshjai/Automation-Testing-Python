def coinChange(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if amount >= coin:
            count += amount // coin  # Add as many coins as possible
            amount %= coin  # Update the remaining amount
        if amount == 0:
            break
    return count if amount == 0 else -1