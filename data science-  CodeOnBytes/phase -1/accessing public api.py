import pandas as pd
import requests

# URL for JSONPlaceholder API to fetch dummy data (example: posts)
api_url = 'https://jsonplaceholder.typicode.com/posts'

# Make a GET request to the API
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    # Creating a Pandas DataFrame from the retrieved data
    df = pd.DataFrame(data)

    # Saving the DataFrame to a CSV file
    df.to_csv('data.csv', index=False)
    print("CSV file 'data.csv' has been created with the fetched data.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
