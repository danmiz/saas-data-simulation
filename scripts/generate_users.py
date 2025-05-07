import pandas as pd
import random
import yaml
from faker import Faker
from datetime import datetime, timedelta

# Load config
with open("config/config.yml", "r") as f:
    config = yaml.safe_load(f)

fake = Faker()

# Settings
user_count = config["simulation"]["user_count"]
start_date = datetime.strptime(config["simulation"]["start_date"], "%Y-%m-%d")
end_date = datetime.strptime(config["simulation"]["end_date"], "%Y-%m-%d")
personas = config["user_profiles"]["personas"]
signup_channels = ["organic", "paid", "referral", "social"]

# Generate users
def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

users = []
for i in range(1, user_count + 1):
    user = {
        "user_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "persona": random.choice(personas),
        "signup_channel": random.choice(signup_channels),
        "signup_date": random_date(start_date, end_date).date(),
        "churned": random.choice([True, False])
    }
    users.append(user)

df = pd.DataFrame(users)
df.to_csv("data/users.csv", index=False)
print("✅ users.csv generated.")
