"""P5 Medium
Titanic analysis chart
Load titanic.csv using Pandas. Fill missing Age with median.
Create a 2×2 subplot figure:
Top-left: histogram of Age
Top-right: bar chart of survival rate by Sex
Bottom-left: bar chart of survival rate by Pclass
Bottom-right: scatter of Age vs Fare colored by Survived
Save as titanic_analysis.png"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tested.csv")


df["Age"] = df["Age"].fillna(df["Age"].median())
print(df.head().to_string())
fig , axes = plt.subplots(2,2 , figsize=(10,10))

#Top-left: histogram of Age
axes[0,0].hist(df["Age"] , bins=20 ,edgecolor="black")
axes[0,0].set_title("Histogram of Age")
axes[0,0].set_xlabel("Age")
axes[0,0].set_ylabel("Count")

#Top-right: bar chart of survival rate by Sex

survival_by_sex = df.groupby("Sex")["Survived"].mean()
axes[0,1].bar(survival_by_sex.index , survival_by_sex.values , edgecolor="black")
axes[0,1].set_title("Survival Rate")
axes[0,1].set_ylabel("Survival Rate")


#Bottom-left: bar chart of survival rate by Pclass

Pclass_survival = df.groupby("Pclass")["Survived"].mean()
axes[1,0].bar(Pclass_survival.index , Pclass_survival.values , edgecolor="black")
axes[1,0].set_title("Pclass Survival Rate")
axes[1,0].set_ylabel("Survival Rate")


#Bottom-right: scatter of Age vs Fare colored by Survived

scatter = axes[1,1].scatter(
    df["Age"],
    df["Fare"],
    c=df["Survived"],
    cmap="coolwarm",
    alpha=0.6,
    s=50,
    edgecolor="black"
)

axes[1,1].set_title("Age vs Fare by Survival")
axes[1,1].set_xlabel("Age")
axes[1,1].set_ylabel("Fare")

cbar = plt.colorbar(scatter, ax=axes[1,1])
cbar.set_label("Survived (0 = No, 1 = Yes)")


plt.show()