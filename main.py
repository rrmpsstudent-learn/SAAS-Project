lazy import pandas as pd
lazy import matplotlib.pyplot as plt

def data_organizer(filename):
    df = pd.read_csv(filename)
    return df

df = data_organizer('data.csv')
# plt.bar(df.Name,df.Bid)
# plt.show()
print(df)