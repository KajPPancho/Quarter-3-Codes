scores = [
    [96, 90, 89, 89, 100],  
    [88, 90, 87, 90, 95],  
    [90, 85, 85, 98, 91], 
    [100, 89, 89, 90, 95],  
    [95, 89, 94, 99, 96],
    [100, 100, 99, 95, 96]
]


print("Scoresheet of 7 students in 5 subjects:")
temp = enumerate(scores, start=1)
for i, student in temp:
    print(f"Student {i}: Math  2 ={student[0]} Math 3 ={student[1]} Chemistry ={student[2]} Biology ={student[3]} Adtech ={student[4]} ")

print()
print("Maximum score of each student:")
temp2 = enumerate(scores, start=1)
for x, student in temp2:
    l = x
    max_score = max(student)
    print(f"Student {l} : " ,max_score)
print()
print("Average Scores of each stuent:")
for i, student in enumerate(scores, start=1):
    avg = sum(student) / len(student)
    print(f"Student {i} Average:" ,avg)

print()
print("Minimum score of each student:")
temp3 = enumerate(scores, start=1)
for a, student in temp3:
    b = a
    min_score = min(student)
    print(f"Student {a} : " ,min_score)
