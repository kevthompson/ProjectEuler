with open("names.txt") as f:
    names = sorted(f.read().split(","))

s = 0
for i, name in enumerate(names):
    name_score = 0
    for c in name.strip("\""):
        name_score += ord(c) - ord('A') + 1
    s += name_score * (i + 1) 

print(s)