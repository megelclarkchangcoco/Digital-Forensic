import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define parameters
num_records = 1000
users = ['user1', 'user2', 'user3', 'admin', 'guest']
event_types = ['login_attempt', 'file_access', 'logout']
files = ['/confidential/report.docx', '/public/readme.txt', '/admin/settings.config', '/user/data.csv']
statuses = ['success', 'failure']

# Generate random timestamps within the past 30 days
end_date = datetime.now()
timestamps = [end_date - timedelta(minutes=random.randint(0, 43200)) for _ in range(num_records)]

# Generate synthetic data
data = {
    'timestamp': timestamps,
    'user': np.random.choice(users, num_records),
    'event_type': np.random.choice(event_types, num_records),
    'file_accessed': [random.choice(files) if event == 'file_access' else None for event in np.random.choice(event_types, num_records)],
    'status': [random.choice(statuses) if event == 'login_attempt' else 'success' for event in np.random.choice(event_types, num_records)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by timestamp for a realistic timeline
df = df.sort_values(by='timestamp').reset_index(drop=True)

# Save to CSV
df.to_csv('system_log_dataset.csv', index=False)

print(df.head())
