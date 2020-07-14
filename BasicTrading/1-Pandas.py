import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])

df["new"] = df["W"] + df["X"]

df[df < 0]
df[df["Z"] < 0]
df[(df["W"] < 0) & (df["X"] > 0)]

indexed_df = df.reset_index()

# Change index
newIndex = "sa ul ma ge tu".split()
df["states"] = newIndex
newIndexed_df = df.set_index("states")

# Multilevel data frame
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
df.index.names = ["Groups", "Num"]  # Insert names to index

df.loc["G2"].loc[2]["B"]

df.xs(1, level="Num")

# Missing Data
d = {"A": [1, 2, np.NaN], "B": [5, np.NaN, np.NaN], "C": [1, 2, 3]}

df_2 = pd.DataFrame(d)
df_2.dropna(axis=1)
df_2.dropna(thresh=2)
df_2.fillna(value="hello")
df_2["A"].fillna(value=df_2["A"].mean())

# Groupby
data = {
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
}

df_3 = pd.DataFrame(data)
companyMean = df_3.groupby("Company").mean()
companyStd = df_3.groupby("Company").std()
companyInfo = df_3.groupby("Company").describe().transpose()

# Merge, Join, Concatenate
df_31 = pd.DataFrame({"A": ["A0", "A1"], "B": ["B0", "B1"]}, index=[0, 1])

df_32 = pd.DataFrame({"A": ["A2", "A3"], "B": ["B2", "B3"]}, index=[2, 3])

df_33 = pd.DataFrame({"A": ["A4", "A5"], "B": ["B4", "B5"]}, index=[4, 5])

pd.concat([df_31, df_32, df_33])
pd.concat([df_31, df_32, df_33], axis=1)

df_left = pd.DataFrame({"key": ["k0", "k1", "k2", "k3"], "A": ["a0", "a1", "a2", "a3"]})
df_right = pd.DataFrame(
    {"B": ["b0", "b1", "b2", "b3"], "key": ["k0", "k1", "k2", "k3"]}
)

pd.merge(df_left, df_right, how="inner", on="key")

# Common Operators
df_4 = pd.DataFrame({"A": [2, 2, 3], "B": ["Tunc", "Utku", "Hello"]})
df_4["A"].unique()
df_4["A"].nunique()
df_4["A"].value_counts()


def times2(x):
    return x * 2


df_4["A"].apply(times2)
df_4["A"].apply(lambda x: x * 2)

df_4.sort_values(by="A")
df_4.isnull()

# Pivot Table
df_5 = pd.DataFrame(
    {
        "A": ["foo", "foo", "foo", "bar", "bar", "bar"],
        "B": ["one", "one", "two", "two", "one", "one"],
        "C": ["x", "y", "x", "y", "x", "y"],
        "D": [1, 3, 2, 5, 4, 1],
    }
)
df_5.pivot_table(values="D", index=["A", "B"], columns="C")

# Data Input and Output
df_6 = pd.read_csv("MyInput.csv")
df_6.to_csv("MyOutput.csv", index=False)

df_7 = pd.read_excel("MyInput2.xlsx", sheet_name="sampleData")
df_7.to_excel("MyOutput2.xlsx", sheet_name="sampleData")

df_8 = pd.read_html("https://www.fdic.gov/Bank/individual/failed/banklist.html")

