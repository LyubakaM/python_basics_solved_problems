people_to_play = int(input())
score_count = 0
mid_score_count = 0
failed_count = 0
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0

for single_student in range(1, people_to_play + 1):
    score = int(input())
    if 0 <= score <= 9:
        score_count += score * 0.2
        from_0_9 += 1
    elif 10 <= score <= 19:
        score_count += score * 0.3
        from_10_19 += 1
    elif 20 <= score <= 29:
        score_count += score * 0.4
        from_20_29 += 1
    elif 30 <= score <= 39:
        score_count += 50
        from_30_39 += 1
    elif 40 <= score <= 50:
        score_count += 100
        from_40_50 += 1
    else:
        failed_count += 1
        score_count = score_count / 2
from_0_9_fin = (from_0_9 / people_to_play) * 100
from_10_19_fin = from_10_19 / people_to_play * 100
from_20_29_fin = from_20_29 / people_to_play * 100
from_30_39_fin = from_30_39 / people_to_play * 100
from_40_50_fin = from_40_50 / people_to_play * 100
failed_count_fin = failed_count / people_to_play * 100
print(f"{score_count:.2f}")
print(f"From 0 to 9: {from_0_9_fin:.2f}%")
print(f"From 10 to 19: {from_10_19_fin:.2f}%")
print(f"From 20 to 29: {from_20_29_fin:.2f}%")
print(f"From 30 to 39: {from_30_39_fin:.2f}")
print(f"From 40 to 50: {from_40_50_fin:.2f}")
print(f"Invalid numbers: {failed_count_fin:.2f}")
