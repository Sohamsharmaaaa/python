"""write a python script using pandas, find the hour of the day in which th maximum number of failed login
occur and plot a line chart of failed logins per hour."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_records.csv")

# Keep only failed logins and count time per IP
failed = df[df["status"] == "failed"]
failed["time"] = pd.to_datetime(failed["time"])

hourly_counts = failed.groupby(failed["time"].dt.hour).size()
max_count = max(hourly_counts)
max_count_hours = hourly_counts[hourly_counts == max_count]
for h, count in max_count_hours.to_dict().items():
    print(f"{h} hour has {count} times failed attempts")

# plot as a line chart a save as an image
hourly_counts.plot(color="blue")
plt.title("Hour-wise no. of failed attempts")
plt.xlabel("hour")
plt.ylabel("failed logins")
plt.tight_layout()
plt.savefig("hourwise_failed_attempts.png")
plt.show()
