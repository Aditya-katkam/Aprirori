import numpy as np
import pandas as pd
from apyori import apriori
store_data = pd.read_csv('store_data.csv', header = None)

records = []
for i in range(0,7501):
    records.append([str(store_data.values[i,j])for j in range(0,20)])

association_rules = apriori(records, min_support=0.0045, min_confidence=0.5,min_lift = 3, min_length = 2)
association_rules = list(association_rules)
print("No of rules = ", len(association_rules))

for item in association_rules:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: "+ items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: "+str(item[2][0][2]))
    print("--------------------------------------------------------------------")
