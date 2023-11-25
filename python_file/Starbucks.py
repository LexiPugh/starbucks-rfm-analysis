import pandas as pd
import numpy as np
import plotly.express as px
raw_df = pd.read_csv('datasets/starbucks_purchases.csv')
print(raw_df.shape)
raw_df.head()
agg_dict = {
    'order_id':'count',
    'sales_amount':'sum',
    'purchase_date':'max'
}
fm_df = raw_df.groupby('customer_id').agg(agg_dict)
print(fm_df.shape)
fm_df
fm_df = fm_df.reset_index()
fm_df
fm_df.rename(columns={'order_id':'frequency', 'sales_amount':'monetary', 'purchase_date':'last_purchase_date'}, inplace=True)
fm_df
recency = pd.read_csv('datasets/recency.csv')
recency
rfm_df = pd.merge(fm_df, recency, left_on='last_purchase_date', right_on='date', how='inner')
rfm_df
rfm_df = rfm_df.drop(columns=['date', 'last_purchase_date'])
rfm_df.head()
fig = px.histogram(rfm_df, x='frequency', title='Starbucks Customer Purchase Frequency')
fig.update_layout(yaxis_title="Number of Customers", xaxis_title="Number of Purchases")
def frequency_grade(frequency): 
    '''
    Given a frequency value, function compares the value to 
    the frequency grading scale and returns the appropriate
    grade. 
    '''
    if frequency <= 5:
        return 'D'
        
    elif frequency <= 7:
        return 'C'
        
    elif frequency <= 11:
        return 'B'
        
    else:  
        return 'A'
rfm_df['frequency_grade'] = rfm_df['frequency'].apply(frequency_grade)
rfm_df.head()
fig = px.histogram(rfm_df, x='frequency_grade', category_orders = {'frequency_grade': ['A', 'B', 'C', 'D']}, 
                   title="Starbucks Customer Frequency Grade Distribution")
fig.update_layout(yaxis_title="Number of Customers", xaxis_title="Frequency Grades")