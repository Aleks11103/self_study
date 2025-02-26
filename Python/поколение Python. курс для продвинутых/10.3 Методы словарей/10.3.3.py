text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for el in text:
    result[el] = result.get(el, 0) + 1
print(result)
