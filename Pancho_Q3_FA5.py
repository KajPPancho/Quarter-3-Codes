names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

total_days = []

for day in range(len(days)):
    tot = 0
    for person in steps:
        tot += person[day]
    total_days.append(tot)
    print(f"{days[day]}: {tot} steps")


most_active_total = max(total_days)
most_active_day = days[total_days.index(most_active_total)]

print("Overall results:")
print(f"{most_active_day} with {most_active_total} steps")
