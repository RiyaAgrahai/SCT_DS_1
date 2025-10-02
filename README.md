 📊 Task 01 – Data Visualization (Bar Chart & Histogram)

This repository contains solutions for **SkillCraft Technology – Task 01**.
The goal of this task is to **visualize the distribution of categorical or continuous variables** using Python.

---

✅ Task Description

* Create a **Bar Chart** or **Histogram** to visualize the distribution of a variable.
* Example variables:

  * Age distribution in a population (continuous data).
  * Gender distribution in a population (categorical data).

---

🛠 Tools & Libraries

* Python 🐍
* Matplotlib 📈

---

📂 Repository Structure

```
Task01-Data-Visualization/
│── histogram.py        # Code for age distribution histogram
│── bar_chart.py        # Code for gender distribution bar chart
│── age_distribution.png   # Output image (optional, screenshot of histogram)
│── README.md
```

---

📌 Code Examples

🔹 Histogram (Age Distribution)

```python
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
```

🔹 Bar Chart (Gender Distribution)

```python
import matplotlib.pyplot as plt

categories = ['Male', 'Female']
values = [55, 45]  # Example percentages

plt.bar(categories, values, color=['blue', 'pink'])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Percentage")
plt.show()
```

---

📊 Output Samples

* Histogram Example
  ![Histogram Output](age_distribution.png)

* Bar Chart Example
  [BarChart Output](gender_distribution.png)


---

🌟 Learning Outcome

* Understood how to use **Matplotlib** for visualizations.
* Learned difference between **histogram** (continuous data) and **bar chart** (categorical data).

---



Do you want me to also **create the bar_chart.py file** for you (so you’ll have both histogram and bar chart in the repo), or do you want to keep only the histogram for now?
