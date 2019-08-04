def main():
    with open('poker.txt') as f:
        raw_text = f.read()
    lines = raw_text.splitlines()
    hands = list(map(lambda x: x.split(), lines))
    wins = 0
    for hand in hands:
        hand1 = hand[:5]
        hand2 = hand[5:]
     
        score1 = scoreHand(hand1)
        score2 = scoreHand(hand2)
        while score1 == score2 and len(hand1) > 0:
            if score1 > 20:
                print(hand1, hand2, score1, score2)
            score1 = highCard(hand1)
            score2 = highCard(hand2)
            hand1 = hand1[:-1]
            hand2 = hand2[:-1]
        if score1 > score2:
            wins += 1
        # break
    print(wins)

def isStraightFlush(hand):
    return isStraight(hand) and isFlush(hand)

def isFourOfKind(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    return (4 in counts)

def isFullHouse(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    return (2 in counts and 3 in counts)

def isFlush(hand):
    suits = list(map(lambda x: x[1], hand))
    counts = list(map(lambda x: suits.count(x), suits))
    return (5 in counts)

def isStraight(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    high_card = highCard(hand)
    low_card = lowCard(hand)
    return ((counts.count(1) == 5 and high_card == low_card + 4) or sorted(nums) == ['2', '3', '4', '5', 'A'])

def isThreeOfKind(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    return (3 in counts)

def isTwoPair(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    return (counts.count(2) == 4)

def isPair(hand):
    nums = list(map(lambda x: x[0], hand))
    counts = list(map(lambda x: nums.count(x), nums))
    return (2 in counts)

def highCard(hand):
    nums = sorted(list(map(lambda x: cardToInt(x[0]), hand)))
    return nums[-1]

def lowCard(hand):
    nums = sorted(list(map(lambda x: cardToInt(x[0]), hand)))
    return nums[0]

def cardToInt(card):
    if card == 'A':
        card = 14
    elif card == 'K':
        card = 13
    elif card == 'Q':
        card = 12
    elif card == 'J':
        card = 11
    elif card == 'T':
        card = 10
    else:
        card = int(card)
    return card


def scoreHand(hand):
    score = 0
    # if isRoyalFlush(hand):
    #     score += 180    
    if isStraightFlush(hand):
        score += 160
    elif isFourOfKind(hand):
        score += 140
    elif isFullHouse(hand):
        score += 120
    elif isFlush(hand):
        score += 100
    elif isStraight(hand):
        score += 80
    elif isThreeOfKind(hand):
        score += 60
    elif isTwoPair(hand):
        score += 40
    elif isPair(hand):
        nums = list(map(lambda x: cardToInt(x[0]), hand))
        counts = list(map(lambda x: nums.count(x), nums))
        score += int(nums[counts.index(2)])
        score += 20
    # else: 
    # if score > 0: 
    #     print(hand, score)
    return score

if __name__ == "__main__":
    main()