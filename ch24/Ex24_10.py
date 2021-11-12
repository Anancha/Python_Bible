import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = { "social_media" : ["Facebook","Instagram","Twitter",
                            "TikTok","Youtube","Line"],
          "%used" : [95,65,55,80,75,85]
        }
df = pd.DataFrame(my_df)
plt.figure(figsize=[8,5])
plt.barh(df["social_media"],df["%used"])
plt.xticks(np.arange(0,100,10))
plt.ylabel("social media platform")
plt.xlabel("used")
plt.title("Summary %used of social media platform")