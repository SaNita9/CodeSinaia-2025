import statistics
#  import pandas as pd
# db = pd.read_csv("IntroToPy/mountains_db.tsv", sep='\t', encoding="utf-8-sig", header=None)
# print(db)
import ast
dict = {
      'names' : [],
      'altitudes': [],
      'countries': [],
      'codes': []

}
with open("IntroToPy/mountains_db.tsv", "r", encoding="utf-8-sig") as file:
    for line in file.readlines():
            line_parts = line.split("\t", -1)
            dict['names'].append(line_parts[0])
            alt = str(line_parts[1])
            if alt == "NULL":
                alt = 0
            # else:
            alt = float(alt)

            dict['altitudes'].append(alt)
            dict['countries'].append(line_parts[2])
            dict['codes'].append(line_parts[3])
            
# print(dict)  
distinct_countries = len(set(list(dict['countries'])))         
print(f"distinct countries = {distinct_countries}")
nullAlts = dict['altitudes'].count(0.0)
print(f"null altitudes = {nullAlts}")
notNullAlts = [item for item in dict['altitudes'] if item > 0.0]
print(len(notNullAlts))

sortedAlts = sorted(notNullAlts)
print(f"min value {sortedAlts[0]}")
print(f"max value {sortedAlts[-1]}")
print(f"mean {statistics.mean(notNullAlts)}")
print(f"median {statistics.median(notNullAlts)}")
print(f"STDev {statistics.stdev(notNullAlts)}")

