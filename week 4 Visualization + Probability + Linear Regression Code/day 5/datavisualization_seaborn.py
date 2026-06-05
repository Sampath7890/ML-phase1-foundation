import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



tips = sns.load_dataset("tips")
print(tips.to_string())

#kde plot
sns.kdeplot(tips["total_bill"])
plt.show()

#histgram
sns.histplot(tips["total_bill"])
plt.show()

#count plot
sns.countplot(x="day", data=tips)
plt.show()

#boxplot
sns.boxplot(y="total_bill", data=tips)
plt.show()

"""
5. violinplot()
Purpose : Combines boxplot + distribution shape.
"""

sns.violinplot(y="total_bill", data=tips)
plt.show()

"""
6. scatterplot()
Purpose : Shows relationship between two variables.
"""

sns.scatterplot(
    x="total_bill",
    y="tip",
    data=tips
)
plt.show()

"""7. lineplot()
Purpose : Shows trends over time or sequence."""

sns.lineplot(
    x=[1,2,3,4,5],
    y=[10,15,20,18,25]
)
plt.show()

"""10. heatmap()
Purpose : Shows values using colors."""
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()


"""9. pairplot()
Purpose : Shows relationships between ALL numerical columns."""
iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()

"""8. regplot()
Purpose : Scatterplot + best fit line."""
sns.regplot(
    x="total_bill",
    y="tip",
    data=tips
)
plt.show()