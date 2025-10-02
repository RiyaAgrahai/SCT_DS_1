# bar_chart.py
# A simple Python script to create a bar chart using matplotlib

import matplotlib.pyplot as plt

# Sample dataset: Gender distribution
categories = ['Male', 'Female']
values = [55, 45]  # Example percentages

# Create bar chart
plt.bar(categories, values, color=['blue', 'pink'])

# Add title and labels
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Percentage")

# Show the bar chart
plt.show()
