
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
