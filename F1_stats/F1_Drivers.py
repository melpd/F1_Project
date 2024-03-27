import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/mpdes/OneDrive/Desktop/Stat4188/F1_stats/F1DriversDataset.csv')
print(df.head())
active_drivers = df[df['Active']]
print(active_drivers)
print(active_drivers['Nationality'])
plt.scatter(df['Points_Per_Entry'], df['Win_Rate'])
plt.show()
#Danni Ric needs to be changed to active instead of Lawson unless RB decides to change things up again
