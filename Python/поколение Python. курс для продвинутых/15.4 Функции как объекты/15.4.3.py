def sum_tpl(tpl):
    return min(tpl) + max(tpl)


numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67),
           (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50),
           (34, 78, 65), (-5, 90, -1)]
numbers.sort(key=sum_tpl)
print(numbers)
