s = input()

# print("a b c f") 3.4.R.py
print("A B C F")    # 3.4.S.py
for a in range(2):
    for b in range(2):
        for c in range(2):
            # f = int(eval(s)) 
            f = int(eval(s, {"A": a, "B": b, "C": c}))      # 3.4.S.py
            print(f"{a} {b} {c} {f}")
