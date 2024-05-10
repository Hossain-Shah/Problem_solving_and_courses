#importing libraries
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


#data inputting
DATA = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
data_input = pd.read_csv(DATA, index_col="page_id")

#dataset describing
data_input

#lineplot visualization
plt.figure(figsize = (16,6))
plt.title("Yearly appearance of Comic characters")
sns.lineplot(data = data_input['APPEARANCES'], label = "APPEARANCES")
sns.lineplot(data = data_input['YEAR'], label = "YEAR")
plt.xlabel("page_id")

#barplot visualization 
input_data = pd.read_csv(DATA, index_col="YEAR")
plt.figure(figsize=(10,8))
plt.title("Yearly appearance of Comic characters")
sns.barplot(x = data_input['YEAR'], y = data_input['APPEARANCES'])
plt.xlabel("YEAR")
plt.ylabel("APPEARANCES")

#scatterplot visualization
sns.scatterplot(x = data_input['YEAR'], y = data_input['APPEARANCES'])

#regplot visualization
sns.regplot(x = data_input['YEAR'], y = data_input['APPEARANCES'])

#histplot visualization
sns.histplot(data_input['YEAR'])

#kdeplot visualization
sns.kdeplot(data = data_input['YEAR'], shade=True)

#jointplot visualization
sns.jointplot(x = data_input['YEAR'], y = data_input['APPEARANCES'], kind="kde")