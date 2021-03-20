#(2822) 점수 계산

import sys

scores = []
for _ in range(8):
    scores.append(int(sys.stdin.readline()))
sorted_scores = sorted(scores, reverse=True)

question_index = []
for score in sorted(sorted_scores[:5]):
    question_index.append(scores.index(score)+1)
question_index.sort()
print(sum(sorted_scores[:5]))
print(*question_index)
