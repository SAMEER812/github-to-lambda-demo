import json
import requests
import pandas as pd

def custom_lambda(event, context):
    
    
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)
    return response.text

    d = {'col1':[1,2],'col2':[3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Demo Completed!!!!!!!')
    print('Demo Completed!!!!!!!')