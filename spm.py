questions = {
    "chapter1": [],
    "chapter2": [],
    "chapter3": [],
    "chapter4": [],
    "chapter5": [],
    "chapter6": [],
    "chapter7": [],
    "chapter8": [],
    "chapter9": [],
}
with open("oppgaver.txt") as f:
    for line in f:
        q = line.split(":")
        questions[q[0]].append(q[1].strip())

keys = [*questions]
print(keys)
from os import tcgetpgrp
import random

print(random.choice(keys))
x = input(
    f"What chapter? {keys} add + at end of line to do all chapter up to chosen\n"
)

chosen_questions = []

if x[-1] == "+":
    x = x[:-1]
    desired = int(x[-1])
    temp = [f"chapter{i}" for i in range(1, desired + 1)]
    for key in temp:
        for item in questions[key]:
            chosen_questions.append(item)
else:
    x = f"chapter{x}"
    chosen_questions = questions[x]

while 1:
    input("go to next")
    chosen = random.choice(range(len(chosen_questions)))
    print(chosen_questions[chosen])
    chosen_questions.pop(chosen)
