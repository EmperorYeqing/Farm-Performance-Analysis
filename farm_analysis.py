# %% [markdown]
# ##Project 01: Farm Performance Analysis
# 
# 
# Aim: Understand Business problem, hired by a farm cooperative
# 
# Objectives: 
# 1. Which farmer performs best ?
# 2. which crop generates the most revenue?
# 3. is farm size related to productivity?
# 4. which farmer improved overtime?
# 5. which farmer uses land most efficiently?

# %% [markdown]
# ### STEP 01: Import

# %%
#STEP 01: Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ### STEP 02: Load the Dataset

# %%
#STEP 02: Load the Dataset
df = pd.read_csv(r"farm_data.csv")
df

# %% [markdown]
# ### STEP 03: Understand the dataset

# %%
#STEP 03: Understand the dataset
print(df.head())
df.info()
df.describe()

# %% [markdown]
# The dataset is Recorded Farm performance data for year 2023 and 2024 by different farmers, including parameters like Farm size per hectare, Yield per kg, Revenue generated, etc.
# 
# No missing, null or empty values, There's a total of 6 columns and 8 rows, two of the columns have string values and the other 4 columns have integer values.

# %%
pd.set_option('display.max_columns',1000)
pd.set_option('display.max_rows',1000)
print(pd.options.display.max_columns)
print(pd.options.display.max_rows)
df

# %% [markdown]
# ### STEP 04:  Creating first KPI

# %%
#STEP 04:  Creating first KPI
#Yield Per Hectare
'''Formula
Yield Per hectare = Yield_Kg / Farm_Size_Ha'''

df["Yield_per_Ha"] = df["Yield_Kg"]/df["Farm_Size_Ha"]
df.sort_values(by=["Year","Yield_per_Ha"], ascending=False)#highest yield per ha
df.sort_values(by=["Year","Revenue"],ascending=False)#highest revenue per 
print(df.groupby(['Farmer','Year'])['Yield_Kg'].sum())

# %% [markdown]
# I created my first KPI(key performance index), Yield per hectare to determine yield per hectare of land in each farm. I afterward answer the following questions with my analysis;
# 1. Who has the highest Yield_per_Ha in 2024?  
#         
#         Answer: "Farmer Amina has the highest Yield_per_Ha in the year 2024."
# 
# 2. Who has the highest Revenue in 2024?
#         
#         Answer: "Farmer John has the highest Revenue in the year 2024
# 
# 3.  Which farmer improved Yield_Kg from 2023 to 2024?
#         
#         Answer: "All farmers(Amina,John, Ngozi) except Musa has increase in Yield_kg from year 2023 - 2024"
# 

# %% [markdown]
# ### STEP 05: Another KPI created - Revenue Per Hectare / Generated Revenue

# %%
#Another KPI - Revenue Per Hectare
'''Formula
Revenue Per Hectare = Revenue / Farm_Size_Ha'''
df["Revenue_per_Ha"] = df["Revenue"]/df["Farm_Size_Ha"]
df.sort_values(by=["Year","Revenue_per_Ha",], ascending=False).round(2)#highest Revenue_per_Ha in 2024
df.sort_values(by=["Revenue","Revenue_per_Ha",], ascending=False).round(2)#highest Revenue_per_Ha in 2024
 

# %% [markdown]
# I create another KPI, Revenue Per Hectare to answer the following questions:
# 
# 1. Who has the highest Revenue_per_Ha in 2024?  
# 
#         Answer: "Farmer Amina has the highest Revenue_per_Ha in the year 2024."
# 
# 2. Does the farmer with the highest revenue also have the highest Revenue_per_Ha?
# 
#         Answer: "NO, the farmer with the highest revenue is farmer JOHN while the farmer with the highest Revenue_per_Ha is farmer Amina"
# 
# 3. What business insight can you draw from that?
# 
#         Answer: 1. Revenue itself does not equate to high productivity, Revenue_per_Ha reveal that.
#                 2. The difference in farm_Size_ha also reveal that farmer Amina revenue generation and land use efficiency is higher than farmer John based on the available data" 
#                 3. Yield_per_Ha also confirm the previous statement/ speculations

# %% [markdown]
# ### STEP 06: Crop Perfomance

# %%
#Crop Performance
df.groupby("Crop")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Crop Performance Analysis to determine:
# 1. Which crop generated the most revenue?
# 
#         Answer: "Maize generated the most revenue with a total revenue of 5350000"
# 2. Which crop generated the least revenue?
# 
#         Answer: "Soyabean generated the least total revenue of 4000000"

# %% [markdown]
# ### STEP 07: Farm productivity

# %%
df[["Farm_Size_Ha", "Yield_per_Ha"]].corr()

# %% [markdown]
# Correlation Analysis to determine relationship between Farm_Size_Ha and Yield_per_Ha:
# 
#         Answer: From the analysis result, it's clear that there is a weak or no relationship between Farm_Size_Ha and Yield_per_Ha

# %% [markdown]
# ### STEP 07: Farmer Revenue Ranking

# %%
#Farmer Revenue Ranking
df.groupby("Farmer")["Revenue"].sum().sort_values(ascending=False)

# %% [markdown]
# Farmer Revenue Ranking to determine:
# 1. Total Revenue Ranking of all Farmers
# 
# 2. Does the highest revenue farmer also have the highest Efficiency ?
# 
#         Answer: "No, the highest revenue farmer is farmer John while the farmer with highest land-use efficiency is farmer Amina (From previous analysis)"

# %% [markdown]
# ### STEP 08: Visualization

# %%
#Visualization - Revenue Ranking/ Land-use Efficiency  Ranking
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
df.groupby("Farmer")["Revenue"].sum().plot(kind="bar")
plt.title("Revenue Ranking")

plt.subplot(1,2,2)
df.groupby("Farmer")["Revenue_per_Ha"].mean().plot(kind="bar")
plt.title("Land-use Efficiency Ranking")
plt.show()
plt.savefig("revenue_&_efficiency.png")

# %% [markdown]
# ### Step 09: Recommendation

# %% [markdown]
# Farmer Amina will be my recommended farmer because of her high Land-use efficiency despite having less land than the highest revenue farmer(John).
# 
# Investigation should be done on farming pratices used by farmer Amina to determine factors contributing to her superior land-use efficiency and evaluate if those pratices can be replicated across other farms and crop types

# %% [markdown]
# ### Thanks to My buddy chatgpt for helping in confusing moment throughout the analysis


