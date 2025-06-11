n = int(input())
count_correct = 0
set_names = set()
for _ in range(n):
    name, res = input().split(": ")
    if res == "Correct":
        set_names.add(name)
        count_correct += 1
if len(set_names) > 0:
    print(f"Верно решили {len(set_names)} учащихся")
    print(f"Из всех попыток {round(count_correct / n * 100 + 0.002)}% верных")
else:
    print("Вы можете стать первым, кто решит эту задачу")
