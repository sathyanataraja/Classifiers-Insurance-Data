import pandas as pd
import numpy as np
import uuid 
np.random.seed(0)

df = pd.DataFrame({'TenureDays':  np.random.randint(low=30, high=1800, size=15000),
        'AverageHandleTime ':np.random.randint(low=0, high=200, size=15000),
        'NumberOfClaims': np.random.randint(low=1, high=1800, size=15000),
        'BilledAmountPerPolicy': np.random.randint(low=10, high=200, size=15000),
        'TotalLapses': np.random.randint(low=30, high=1800, size=15000)})
        
df['NumberOfMonthsBillPaid'] = round(df['TenureDays']/30)
df['ClaimsPaid'] = np.random.randint(low=0, high=df['NumberOfClaims'])
df['ClaimsDenied'] = df['NumberOfClaims'] - df['ClaimsPaid']
df['DaysSinceLastClaim'] = np.random.randint(low=29, high=df['TenureDays'])
df['ReceivedAmountPerPolicy'] = np.random.randint(low=0, high=df['BilledAmountPerPolicy'])
df['DaysSinceAgentChange'] = np.random.randint(low=0, high=df['TenureDays'])

items  = ["Active","Lapsed"]
probs = [0.55,0.45]
trials =15000
df['StatusText'] = np.random.choice(items, trials, p=probs)

ary = list(range(15000,37000))
df['AccountId'] = np.random.choice(ary, size=15000, replace=False)

df = df[['AccountId','TenureDays', 'AverageHandleTime ', 'NumberOfClaims',
         'ClaimsPaid', 'ClaimsDenied','DaysSinceLastClaim',
         'BilledAmountPerPolicy','ReceivedAmountPerPolicy',
         'TotalLapses', 'NumberOfMonthsBillPaid',
         'DaysSinceAgentChange', 'StatusText' ]]

df['Status'] = 0
df.loc[df['StatusText'] == 'Lapsed','Status'] = 1
del df['StatusText']
