import pandas as pd

df = pd.DataFrame([
    [1,2,3],
    [4,5,6]
], columns=["a", "b", "c"], index = ["x", "y"])

# df.columns = ["a", "b", "c"]
# df.index = ["a", "b"]

df["d"] = df["a"] - df["b"]
df = df.append(df.sum(), ignore_index=True)

print(df)

df2 = pd.DataFrame([
    [1,2],
    [3,4]
], columns=list("ab"))

df3 = pd.DataFrame([
    [1,2],
    [3,4]
], columns=list("ab"))

df2 = df2.append(df3, ignore_index=True)

df2["a"]["0"] = 2

print(df2)
