import random

# 1
print(random.randint(1, 100))

# 2
print(random.uniform(0, 1))

# 3
print(random.choice(['tosh', 'qaychi', 'qog'oz']))

# 4
print(random.randint(1, 25) * 2)

# 5
sonlar = [random.randint(0, 100) for _ in range(5)]
print(sorted(sonlar))

# 6
mevalar = ['olma', 'banan', 'apelsin', 'uzum', 'anor']
random.shuffle(mevalar)
print(mevalar)

# 7
print(random.sample(range(1, 11), 3))

# 8
if random.random() < 0.3:
    print("yutdingiz")
else:
    print("yutqazdingiz")

# 9
print(random.choice([x for x in range(100, 201) if x % 5 == 0]))

# 10
print(random.choice(["qizil", "yashil", "ko'k"]))
