MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
min_score = min(scores)

class Spy:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

spies=[]
for i in range(5):
    spies.append(Spy(codenames[i], scores[i]))

for s in spies:
    if s.score == min_score:
        print(s.codename, s.score)
        break