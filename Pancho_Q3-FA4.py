names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

print("Step Counts Dataset:")
for i, person in enumerate(steps):
    print(f"{names[i]}: {person}")

print("Summary per Person:")
totals = []
for i, person in enumerate(steps):
    total = sum(person)
    totals.append(total)
    print(f"{names[i]} - Total Steps={total}, Average={total/len(person):.2f}")


highest_total = max(totals)
highest_person = names[totals.index(highest_total)]


print("\nOverall Results:")
print(f"Highest Total Steps: {highest_person} with {highest_total}")
