scores = [
    [96, 90, 89, 89, 100],  
    [88, 90, 87, 90, 95],  
    [90, 85, 85, 98, 91], 
    [100, 89, 89, 90, 95],  
    [95, 89, 94, 99, 96],
    [100, 100, 99, 95, 96]
]

print("Scoresheet of 6 students in 5 subjects:")
for i, student in enumerate(scores, start=1):
    print(f"Student {i}: {student}")

print("\nTotal and Average per Student:")
for i, student in enumerate(scores, start=1):
    total = sum(student)
    avg = total / len(student)
    print(f"Student {i} → Total: {total}, Average: {avg:.2f}")

print("\nMaximum score of each student:")
for i, student in enumerate(scores, start=1):
    print(f"Student {i}: {max(student)}")

print("\nMinimum score of each student:")
for i, student in enumerate(scores, start=1):
    print(f"Student {i}: {min(student)}")

all_scores = [score for student in scores for score in student]
print("Overall Maximum Score in Dataset:", max(all_scores))
print("Overall Minimum Score in Dataset:", min(all_scores))

"As of using a 2D array, it made things easy to organize the scores by student and subject, so I could loop through each row systematically. 
"Summarizing totals and averages was straightforward because Python’s built-in functions like sum(), max(), and min() handle the calculations efficiently.
"The simplest part was computing averages because it only requires division of the total by the number of subjects. 
"The tricky part for me was searching the final maximum and minimum values, which required flattening the dataset into a single list.
