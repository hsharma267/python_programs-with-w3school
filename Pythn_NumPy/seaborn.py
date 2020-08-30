# Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
print("<-- Seaborn -->")

# import Matplotlib
print("-- import matplotlib --")

# import seaborn as sns
print("-- import seaborn as sns --")

# Plotting a distplot
print("-- plotting a distplot --")
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Distplot with the Histogram
print("-- Plotting a Distplot with the Histogram --")
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
