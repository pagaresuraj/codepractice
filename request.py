import requests
import pandas as pd
r =requests.post('https://jsonplaceholder.typicode.com/posts/1')
data = r.json()
print(data)
df = pd.DataFrame(data, index=[0])
print(df)

# . /Users/consultadd/PycharmProjects/surajtest