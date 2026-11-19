"""using Faker, generate a csv file of 50 fake login records (time, username, ip, status) and display the
first 10 rows using pandas"""

from faker import Faker
import pandas as pd
import random

fake = Faker()
records = []
for _ in range(50):
    records.append(
        {
            "time": fake.date_time_this_month(),
            "username": fake.user_name(),
            "ip": fake.ipv4(),
            "status": random.choice(["success", "failed"]),
        }
    )
df = pd.DataFrame(records)
df.to_csv("login_records.csv", index=False)
print(df.head(20))
