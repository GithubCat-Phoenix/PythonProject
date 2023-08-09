import pandas as pd
import numpy as np
order = pd.read_csv(r'C:\Users\Administrator\Desktop\chipotle.tsv', sep='\t')

print(order.shape)
print(order.columns)
order3 = order[["order_id", "item_name"]]
# print(order3.value_counts().head(3))
# print(order3.sort_values("item_name".count(), ascending=False).head(3))
print(order.item_name.count)