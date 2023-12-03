# %% [markdown]
# # Advent of Code 2023 - Day 1

# %% [markdown]
# ## Part 1

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
# SOLUTION 1
sum_num = data['res'].astype(int).sum()

print(f"The solution of puzzle 1 is {sum_num}!")

# %% [markdown]
# ## Part 2

# %%
data_2 = data[['raw']].copy()

# %%
number_mapping = {
    'oneight': '18',
    'twone': '21',
    'threeight': '38',
    'nineight': '98',
    'fiveight': '58',
    'sevenine': '79',
    'eighthree': '83',
    'eightwo': '82',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# %%
data_2[data_2.raw.str.contains('eightwo')]

# %%
# for key, values in number_mapping.items():
#     col_name_temp = key + '_repl'
#     print(col_name_temp)

#     # 
#     data_2[col_name_temp] = data_2['raw'].replace({key:values}, regex=True)

# data_2.head()

# %%
# replace name of numbers with digit
data_2['words_repl'] = data_2['raw'].replace(number_mapping, regex=True)

# get column with numbers only
data_2['num'] = data_2['words_repl'].str.replace('[^0-9]', '', regex=True)

# save first and last digit (when only one digit, it gets save twice)
data_2['res'] = data_2['num'].str[0] + data_2['num'].str[-1]

data_2.sample(10)

# %%
data_2['words_repl'].sample(10)

# %%
# SOLUTION 2
sum_num_2 = data_2['res'].astype(int).sum()

print(f"The solution of puzzle 2 is {sum_num_2}!")


