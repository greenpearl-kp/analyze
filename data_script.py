import pandas as pd
import json

# Create dummy analytics data
data = {
    'Category': ['Web', 'Mobile', 'Desktop', 'Cloud'],
    'Usage':,
    'Trend': ['Up', 'Stable', 'Down', 'Up']
}

df = pd.DataFrame(data)

# Save it so the HTML file can read it
df.to_json('data.json', orient='records')
print("Analytics updated!")
