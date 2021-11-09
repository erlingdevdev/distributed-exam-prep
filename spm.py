
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
x = input(f"What chapter? {keys}")
while 1:
    input("go to next")
    chosen = random.choice(range(len(questions[x])))
    print(questions[x][chosen])
    questions[x].pop(chosen)
    
