# %%
import pandas as pd

# %%
# load data
data = pd.read_csv("input/input_1.csv", header=None)
data.columns = ['raw']


# %%
# get column with numbers only
data['num'] = data['raw'].str.replace('[^0-9]', '', regex=True)

# save first and last digit (when only one digit, it gets save twice)
data['res'] = data['num'].str[0] + data['num'].str[-1]

print(data.sample(10))


# %%
# SOLUTION
sum_num = data['res'].astype(int).sum()

print(f"The solution is {sum_num}!")


