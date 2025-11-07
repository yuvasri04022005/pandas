#program1
# import pandas as pd

# df = pd.DataFrame({'Age': [22, 25, 24, 23, 120, 26, 27, 100]})

# Q1 = df['Age'].quantile(0.25)
# Q3 = df['Age'].quantile(0.75)
# IQR = Q3 - Q1

# lower_limit = Q1 - 1.5*IQR
# upper_limit = Q3 + 1.5*IQR

# outliers = df[(df['Age'] < lower_limit) | (df['Age'] > upper_limit)]
# print(outliers)

#program3
# import pandas as pd
# median = df['Age'].median()
# df['Age'] = np.where((df['Age'] < lower_limit) | (df['Age'] > upper_limit), median, df['Age'])
# print(df)

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'Age': [22, 25, 24, 23, 120, 26, 27, 100]})

# # IQR Calculation
# Q1 = df['Age'].quantile(0.25)
# Q3 = df['Age'].quantile(0.75)
# IQR = Q3 - Q1

# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR

# # Replace outliers with median
# median = df['Age'].median()
# df['Age'] = np.where((df['Age'] < lower_limit) | (df['Age'] > upper_limit), median, df['Age'])

# print(df)

#program2
# from scipy import stats
# import numpy as np

# data = np.array([10, 12, 11, 13, 150, 12, 11, 14])

# z = np.abs(stats.zscore(data))
# print("Z-scores:", z)

# outliers = data[z > 2.5]  # lowered threshold
# print("Outliers:", outliers)

#program4
# import pandas as pd

# data = {
#     'date': ['2025-01-01','2025-01-02','2025-01-03','2025-01-04'],
#     'sales': [100, 150, 200, 180]
# }
# df = pd.DataFrame(data)
# df['date'] = pd.to_datetime(df['date'])
# df.set_index('date', inplace=True)

# monthly = df.resample('M').sum()
# print(monthly)

#program5
import pandas as pd

# Sample time-series data
data = {
    'date': ['2025-01-01','2025-01-02','2025-01-03','2025-01-04','2025-01-05'],
    'sales': [100, 150, 200, 180, 220]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'])

# Set date column as index (important for time-series)
df.set_index('date', inplace=True)

# Create rolling average column (window size = 2)
df['rolling_avg_2'] = df['sales'].rolling(window=2).mean()

print(df)
