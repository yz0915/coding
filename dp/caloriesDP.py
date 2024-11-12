# Problem Statement:
# You're ordering food from DoorDash, and you're selecting items from a menu.
# You have a specific budget, and your goal is to get the maximum amount of calories that can be bought
# with this budget.
# Input:
# 1. A list of floating point values representing the dollar prices of items (example: 1.25 for $1.25)
# 2. A list of integers representing the calories value of each item in the same order as prices.
# 3. A floating point value representing your budget in dollar amount (example: 20.00 for $20)
# Output:
# An integer representing the maximum amount of calories that can be bought
# without going over the budget.

def max_calories(calories, prices, budget):
    budget_cent = convert_to_cents(budget)
    dp = [0] * (budget_cent + 1)

    for i in range(len(prices)):  # loop over items
        price_cent = convert_to_cents(prices[i])
        for j in range(price_cent, budget_cent + 1):  # calculate total calories
            dp[j] = max(dp[j], dp[j - price_cent] + calories[i])

    return dp[budget_cent]

def convert_to_cents(price):
    return int(price * 100)
