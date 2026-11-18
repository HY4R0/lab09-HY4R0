# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # Restate: find two indices i and j whose values add to target.
    # Example: [3, 2, 4], target 6 -> [1, 2] because 2 + 4 = 6.
    # Approach: use a dictionary to remember each number seen and its index.
    # For each index i, calculate need = target - nums[i].
    # If need is already in the dictionary, return [old_index, i].
    # Otherwise, store nums[i] with i.
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def max_profit(prices):
    # Outline:
    # Restate: choose a buy day before a sell day and maximize sell - buy.
    # Example: [7, 1, 5, 3, 6, 4] -> buy at 1, sell at 6 for 5.
    # Approach: track the lowest price seen so far and the best profit.
    # For each price:
    # update the lowest price if this price is smaller.
    # calculate price - lowest_price and update the best profit if larger.
    # Return 0 if no positive profit was found.
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    if not prices:
        return 0

    lowest_price = prices[0]
    best_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        best_profit = max(best_profit, price - lowest_price)
    return best_profit


def max_subarray(nums):
    # Outline:
    # Restate: find the contiguous block with the largest sum.
    # Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6.
    # Approach: scan left to right while maintaining the best sum ending here.
    # For each number:
    # extend the current block or start a new block with this number,
    # whichever gives the larger sum.
    # Track the largest block sum found.
    # Initialize both values from the first number.
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # Restate: determine whether brackets close in a valid matching order.
    # Example: "{[]}" is valid; "([)]" is invalid.
    # Approach: use a list as a stack.
    # On an opening bracket, push it onto the stack.
    # On a closing bracket, check that the stack is not empty and that its
    # top opening bracket matches this closing bracket; if not, return False.
    # Pop the matching opening bracket from the stack.
    # Return True only if the stack is empty at the end.
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
