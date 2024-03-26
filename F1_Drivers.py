import pandas as pd
df = pd.read_csv('C:/Users/mpdes/OneDrive/Desktop/Stat4188/F1_stats/F1DriversDataset.csv')
print(df.head())
active_drivers = df[df['Active']]
print(len(active_drivers))
