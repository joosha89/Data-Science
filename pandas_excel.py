import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('management_test.xlsx', sheet_name='Sheet1')


df['근무시간'] = df['퇴근시간'] - df['출근시간']
df['시간당 생산'] = df['생산'] / df['근무시간']

df = df.sort_values(by=['시간당 생산','근무시간'], ascending=[False, False])
print(df)

df['생산'].plot(kind='bar')
plt.show(block=True)

df.to_excel('management_result.xlsx', sheet_name='Sheet1')