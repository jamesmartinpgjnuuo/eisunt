from agents import json_agent, pandas_agent

# Define the query data
query_data = {
    "key": "Top_Holdings",
    "query": "Your query here"
}

# Use the json_agent to fetch the data
json_data = json_agent.fetch_data(query_data)

# Convert the JSON data to a pandas dataframe
df = pandas_agent.json_to_dataframe(json_data)

# Perform any necessary data processing or analysis using the pandas dataframe

# Run the rest of your workflow using the processed data
