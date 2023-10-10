"""
Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""


def blackjack(a, b, c):
    result = ""
    total = sum((a, b, c))

    if total <= 21:
        result = total
    else:
        if 11 in (a, b, c):
            total -= 10
            if total > 21:
                result = "Bust"
            else:
                result = total
        else:
            if total > 21:
                result = "Bust"

    return result


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
