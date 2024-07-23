import pandas as pd
import json

# Sample JSON data
json_data = {
    "id": 1,
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "email": ["john@example.com", "john1@example.com"]
}

# Normalize the JSON data into a dataframe
df = pd.json_normalize(json_data)

# Print the dataframe
print(df)
