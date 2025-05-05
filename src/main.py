import polars as pl

# df = sns.load_dataset("titanic")
# df.to_parquet("data/titanic.parquet")

df = pl.read_parquet("data/titanic.parquet")
print(df.head())
print(df.columns)
