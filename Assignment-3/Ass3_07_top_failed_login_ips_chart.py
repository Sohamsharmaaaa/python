"""write a python script using pandas, find the top 5 ip addresses having the most failed logins and plot
them as a bar chart. Save the chart as an image"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_records.csv")

# Keep only failed and count them per ip
failed = df[df["status"] == "failed"]
top5 = failed["ip"].value_counts().head(5)
print(top5)

# plot as a bar chart and save as an image
top5.plot(kind="bar", color="blue")
plt.title("Top 5 IPs with Most failed logins")
plt.xlabel("IP Address")
plt.ylabel("failed logins")
plt.tight_layout()
plt.savefig("top5_failed_ips.png")
plt.show()
