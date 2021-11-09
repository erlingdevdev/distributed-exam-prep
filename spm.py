
questions = {
        "chapter1":[],
        "chapter2":[],
        "chapter3":[],
        "chapter4":[],
        "chapter5":[],
        "chapter6":[],
        "chapter7":[],
        "chapter8":[],
        "chapter9":[],
        }
with open("oppgaver.txt") as f:
    for line in f:
        q = line.split(":")
        questions[q[0]].append(q[1].strip())


keys = [*questions]
print(keys)
import random

print(random.choice(keys))

try:
    x = input(f"What chapter? {keys}")
    chosen = random.choice(list(questions[x]))
except Exception:
    chosen = random.choice(list(questions.items()))


print(chosen)
