words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry',
         'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon',
         'currant', 'Almond']
print(*sorted({el.lower()[0] for el in words}))
