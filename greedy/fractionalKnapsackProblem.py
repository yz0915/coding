# Given the weights and profits of N items, in the form of {profit, weight} put these items in a knapsack of capacity W to get the
# maximum total profit in the knapsack. In Fractional Knapsack, we only pick each item once, and can break items for
# maximizing the total value of the knapsack.
# Input: arr[] = {{100, 20}, {60, 10}, {120, 30}}, W = 50
# Output: 240
# Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg.
# Hence total price will be 60+100+(2/3)(120) = 240
# Input: arr[] = {{500, 30}}, W = 10
# Output: 166.667

def fractional_knapsack(items, capacity):
    # Sort by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_profit = 0
    knapsack = []
    for value, weight in items: 
        if capacity > weight:
            knapsack.append ( (value, weight))
            total_profit += value 
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((value * fraction, weight * fraction))
            total_profit += value * fraction
            break
    return total_profit, knapsack


items = [(100, 20), (60, 10), (120, 30)]
capacity = 50
total_profit, selected_items = fractional_knapsack(items, capacity)
print("Maximum total profit:", total_profit)
print("Selected items in knapsack:", selected_items)