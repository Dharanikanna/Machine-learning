import pandas as pd
import seaborn as sns
print("Libraries imported Sucessfully...!")


dataframes = pd.read_csv("middle_tn_schools.csv")
print(dataframes.head)

# sns.heatmap(dataframes.corr()) # visualisation
