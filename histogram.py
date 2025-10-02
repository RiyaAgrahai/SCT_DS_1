import matplotlib.pyplot as plt

# Sample dataset: Age distribution
ages = [22, 25, 30, 45, 50, 34, 23, 40, 41, 36,
        28, 22, 24, 29, 33, 35, 52, 48, 27, 31]

plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
