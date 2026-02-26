scores = [
    [96, 90, 89, 89, 100],  
    [88, 90, 87, 90, 95],  
    [90, 85, 85, 98, 91], 
    [100, 89, 89, 90, 95],  
    [95, 89, 94, 99, 96],
    [100, 100, 99, 95, 96]
]


for i, row in enumerate(scores, start=1):
    print(f"\nScores of Student {i}: {row}")
    
    tot = sum(row)
    avrg = tot / len(row)
    
    print(f"  Total: {tot}")
    print(f"  Average: {avrg:.2f}")

max_value = max(max(row) for row in scores)
print("\nHighest score in dataset:", max_value)

"Using an array made it easier to organize the scores 
"because all the data was stored in a structural manner
"that allowed me to access each student’s results
"quickly. Through looping through the rows, I could
"easily calculate totals and averages without repeating
"code for each student. The easiest part which was
"using built-in functions such as sum() and max() in
"order to get the totals and highest score. The more
"challenging parts were remembering the correct
"indexing when opening specific values in the 2D array
"but once understood, it made analyzing the dataset
"much faster."
