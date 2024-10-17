import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

%matplotlib inline

csv_file_path = '2025-VeloCityX-Expanded-Fan-Engagement-Data'
df = pd.read_csv(csv_file_path)

df.columns = df.columns.str.replace(' ', '_')

correlation, _ = pearsonr(df['Sponsorship_Interactions_(Ad_Clicks)'], df['Virtual_Merchandise_Purchases'])
print(f'Correlation between Sponsorship Interactions and Virtual Merchandise Purchases: {correlation:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(df['Sponsorship_Interactions_(Ad_Clicks)'], df['Virtual_Merchandise_Purchases'], color='green', label='Data Points')

m, b = np.polyfit(df['Sponsorship_Interactions_(Ad_Clicks)'], df['Virtual_Merchandise_Purchases'], 1)
plt.plot(df['Sponsorship_Interactions_(Ad_Clicks)'], m * df['Sponsorship_Interactions_(Ad_Clicks)'] + b, color='red', label='Regression Line')

plt.title('Correlation Between Sponsorship Interactions and Virtual Merchandise Purchases')
plt.xlabel('Sponsorship Interactions (Ad Clicks)')
plt.ylabel('Virtual Merchandise Purchases')
plt.legend()
plt.grid(True)

plt.show()


correlation, _ = pearsonr(df['Time_on_Live_360_(mins)'], df['Virtual_Merchandise_Purchases'])
print(f'Correlation between Time on Live and Virtual Merchandise Purchases: {correlation:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(df['Time_on_Live_360_(mins)'], df['Virtual_Merchandise_Purchases'], color='blue', label='Data Points')

m, b = np.polyfit(df['Time_on_Live_360_(mins)'], df['Virtual_Merchandise_Purchases'], 1)
plt.plot(df['Time_on_Live_360_(mins)'], m*df['Time_on_Live_360_(mins)'] + b, color='red', label='Regression Line')

plt.title('Correlation Between Time on Live and Virtual Merchandise Purchases')
plt.xlabel('Time on Live 360 (mins)')
plt.ylabel('Virtual Merchandise Purchases')
plt.legend()
plt.grid(True)

plt.show()
