import numpy as np

names = ["Petteri", "Jaska", "Joni"]

ages = np.array([24, 25, 21], dtype=np.int64)

rnd = np.random.randint(30, size=3)

max_rnd = np.argmax(rnd)

names[max_rnd] = "Santeri"
ages[max_rnd] = 23

print(names)
print(ages)