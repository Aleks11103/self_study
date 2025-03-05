words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik',
         'beegeek']

result = {key: [ord(val) for val in key] for key in words}
print(result)
