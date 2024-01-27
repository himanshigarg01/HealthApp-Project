#!/usr/bin/env python
# coding: utf-8

# # Project Name:- HealthApp
# ## By:- Himanshi Garg

# In[58]:


import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = r'C:\Users\Admin\Desktop\heathApp\healthapp_file.csv'

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)
df2 = pd.read_csv(file_path)

# Display the DataFrame
print(df)


# In[59]:


# Extract the ending 4-digit number using regex
df['Steps_Changed'] = df['Content'].str.extract(r'onStandStepChanged (\d{4})')

# Display the DataFrame
print(df)


# In[60]:


# Drop rows with NaN values in 'Steps_Changed' column
df = df.dropna(subset=['Steps_Changed'])

# Create a new DataFrame with 'Steps_Changed' and 'Time' columns
new_df = df[['Time', 'Steps_Changed']]

# Convert 'Steps_Changed' to numeric after replacing non-finite values with 0
new_df['Steps_Changed'] = pd.to_numeric(new_df['Steps_Changed'], errors='coerce').fillna(0).astype(int)

# Add a new column 'Steps' to calculate the difference between consecutive 'Steps_Changed'
new_df['Steps'] = new_df['Steps_Changed'].diff().fillna(0).astype(int)
print(new_df.head(50))


# In[61]:


# Convert 'Time' to datetime format
new_df['Time'] = pd.to_datetime(new_df['Time'], format='%Y%m%d-%H:%M:%S:%f')

# Group by minute and sum the 'Steps'
result_df = new_df.groupby(new_df['Time'].dt.to_period("T")).agg({'Steps': 'sum'}).reset_index()

print(result_df.head(50))


# In[62]:


print(result_df.dtypes)
result_df['Time'] = result_df['Time'].astype(str)

# Sort the DataFrame by 'Steps' in descending order
sorted_df = result_df.sort_values(by='Steps', ascending=False)

# Select the top 10 rows
top_10_df = sorted_df.head(10)

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_10_df['Time'], top_10_df['Steps'])

# Format the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Steps Changes')
plt.title('Top 10 Time Periods with Maximum Steps Changes')

# Show the plot
plt.show()


# In[63]:


# Above graph shows the top 10 time periods in which the person walked maximum steps.


# In[64]:


# Analysis on the basis of calories

# Extract the ending 4-digit number using regex
df2['Calories_Changed'] = df2['Content'].str.extract(r'calculateCaloriesWithCache totalCalories=(\d{6})')

# Display the DataFrame
print(df2)


# In[65]:


# Drop rows with NaN values in 'Calories_Changed' column
df2 = df2.dropna(subset=['Calories_Changed'])

# Create a new DataFrame with 'Steps_Changed' and 'Time' columns
new_df2 = df2[['Time', 'Calories_Changed']]

# Convert 'Steps_Changed' to numeric after replacing non-finite values with 0
new_df2['Calories_Changed'] = pd.to_numeric(new_df2['Calories_Changed'], errors='coerce').fillna(0).astype(int)

# Add a new column 'Steps' to calculate the difference between consecutive 'Steps_Changed'
new_df2['Calories_burnt'] = new_df2['Calories_Changed'].diff().fillna(0).astype(int)
print(new_df2.head(50))


# In[66]:


# Convert 'Time' to datetime format
new_df2['Time'] = pd.to_datetime(new_df2['Time'], format='%Y%m%d-%H:%M:%S:%f')

# Group by minute and sum the 'Steps'
result_df2 = new_df2.groupby(new_df2['Time'].dt.to_period("T")).agg({'Calories_burnt': 'sum'}).reset_index()

print(result_df2.head(50))


# In[67]:


print(result_df.dtypes)
result_df2['Time'] = result_df2['Time'].astype(str)

# Sort the DataFrame by 'Steps' in descending order
sorted_df2 = result_df2.sort_values(by='Calories_burnt', ascending=False)

# Select the top 10 rows
top_10_df2 = sorted_df2.head(10)

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_10_df2['Time'], top_10_df2['Calories_burnt'])

# Format the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Calories_burnt')
plt.title('Top 10 Time Periods with Maximum Calories Burnt')

# Show the plot
plt.show()


# In[68]:


# Above graph shows the top 10 time periods in which the person burnt maximum calories


# In[69]:


merged_df = pd.merge(top_10_df, top_10_df2, on='Time', how='inner')

# Plot the combined bar graph
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting the first bar plot for calories
color = 'tab:red'
ax1.set_xlabel('Time')
ax1.set_ylabel('Calories_burnt', color=color)
ax1.bar(merged_df['Time'], merged_df['Calories_burnt'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Creating a second y-axis for the steps
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Steps', color=color)
ax2.bar(merged_df['Time'], merged_df['Steps'], color=color, alpha=0.5)
ax2.tick_params(axis='y', labelcolor=color)

# Formatting x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Set title
plt.title('Combined Bar Plot for Calories and Steps over Time')

# Show the plot
plt.show()


# In[71]:


import numpy as np
merged_df = pd.merge(top_10_df, top_10_df2, on='Time', how='inner')

# Set up figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Bar width for each entry
bar_width = 0.4

# Plotting the first set of bars for calories
ax.bar(merged_df['Time'], merged_df['Calories_burnt'], width=bar_width, label='Calories')

# Offset the x-axis position for the second set of bars
ax.bar(np.arange(len(merged_df['Time'])) + bar_width, merged_df['Steps'], width=bar_width, label='Steps')

# Formatting x-axis labels for better readability
ax.set_xticks(np.arange(len(merged_df['Time'])) + bar_width / 2)
ax.set_xticklabels(merged_df['Time'], rotation=45, ha='right')

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Values')
plt.title('Bar Plot for Calories and Steps over Time')

# Display legend
plt.legend()

# Show the plot
plt.show()


# # Conclusion:-  Therefore, we can conclude that the person done the most workout at 22:17 on 23 December 2023
