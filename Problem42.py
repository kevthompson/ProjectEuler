def alphasum(string):
    score = 0
    for char in string.lower().strip('"'):
        score += ord(char) - ord('a') + 1
    if score > 190:
        print(score)
    return score

triNums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
with open("./p042_words.txt") as f:
    words = f.read().split(",")
    print(len(words))
    filtered = list(filter(lambda x: alphasum(x) in triNums, words))
    print(filtered)
    print(len(filtered))
