# %%
import pandas as pd

# %%
# load data
data = pd.read_csv("input/input_1.csv", header=None)
data.columns = ['raw']


# %%
data['num'] = data['raw'].str.replace('[^0-9]', '', regex=True).astype(int)
print('Random sample of 10 entries', data.sample(10), '\n')


# %%
# SOLUTION
sum_num = data['num'].sum()

print(f"The solution is {sum_num}!")