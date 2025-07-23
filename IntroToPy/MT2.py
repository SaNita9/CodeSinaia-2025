import pandas as pd
import matplotlib.pyplot as plt
mountains = pd.read_csv("IntroToPy/mountains_db.tsv", sep='\t', encoding="utf-8-sig", header=None)
names = mountains[0].tolist()
altitudes = mountains[1].replace("NULL", 0).astype(float).tolist()
countries = mountains[2].tolist()  
codes = mountains[3].tolist()

distinct_codes = pd.Series(codes).unique().tolist()
occurances = []
for dcode in distinct_codes:
    indexes = mountains.index[mountains[3] == dcode].tolist()
    occurances.append(len(indexes))

# plt.figure(figsize=(8, 4))
# plt.title("Bar chart of codes (x) and their counts (y)")
# plt.xlabel("value")
# plt.ylabel("code")

# x_ticks = range(0, len(distinct_codes), 20)
# plt.xticks(x_ticks)
# plt.bar(distinct_codes, occurances, color='blue')
# plt.show()



# distinct_codes = pd.Series(codes).unique().tolist()
# occurances = []
# for dcode in distinct_codes:
#     indexes = mountains.index[mountains[3] == dcode].tolist()
#     occurances.append(len(indexes))

# distinct_countries = pd.Series(countries).unique().tolist()
# max_altitudes_by_country = mountains.groupby(2)[1].apply(lambda x: x.max())
# print(max_altitudes_by_country)