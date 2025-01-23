import pandas as pd

data = {
    "received_events_url": ["https://api.github.com/users/akien-mga/received_events"] * 5,
    "repos_url": ["https://api.github.com/users/akien-mga/repos"] * 5,
    "starred_url": ["https://api.github.com/users/akien-mga/starred{/owner}{/repo}"] * 5,
    "subscriptions_url": ["https://api.github.com/users/akien-mga/subscriptions"] * 5,
}

df = pd.DataFrame(data)
pd.set_option('display.max_colwidth', None)

df['username'] = df['received_events_url'].str.split('/').str[4]
print(df)