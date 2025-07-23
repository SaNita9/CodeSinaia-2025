import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Values': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Values'
grouped = df.groupby('Category').sum()

print(grouped)
