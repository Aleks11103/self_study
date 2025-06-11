from decimal import Decimal


num = Decimal(input())
print(num.as_tuple())
if not -1 <= num <= 1:
    print(min(num.as_tuple()[1]) + max(num.as_tuple()[1]))
else:
    print(0 + max(num.as_tuple()[1]))
