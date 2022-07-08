import pandas as pd
#https://www.youtube.com/watch?v=AmHZxULclLQ

def lambda_handler(event, context):
    d = {'col1':[w,2],'col2':[3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done first test!'
    )
    