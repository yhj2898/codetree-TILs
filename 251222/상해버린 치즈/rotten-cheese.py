N, M, D, S = map(int, input().split())

eats = []
for _ in range(D):
    p, m, t = map(int, input().split())
    eats.append((p, m, t))

sicks = []
for _ in range(S):
    p, t = map(int, input().split())
    sicks.append((p, t))

answer = 0

# 치즈 하나씩 가정
for cheese in range(1, M + 1):
    possible = True

    # 모든 아픈 기록 검사
    for sick_p, sick_t in sicks:
        ok = False

        for p, m, t in eats:
            if p == sick_p and m == cheese and t + 1 <= sick_t:
                ok = True
                break

        if not ok:
            possible = False
            break

    if possible:
        people = set()
        for p, m, t in eats:
            if m == cheese:
                people.add(p)
        answer = max(answer, len(people))

print(answer)
