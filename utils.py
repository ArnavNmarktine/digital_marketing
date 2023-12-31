from datetime import datetime, timedelta
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np


start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 2, 1)



a={'organic_search':51,'Direct':16,'Referral':14,'Social':10,'Other':5,'paid_search':2,'Affiliates':1,'Display':1 }


percentages = a

def user_by_date(start_date, end_date, percentages):
    current_date = start_date
    df = pd.DataFrame(columns=['Date', 'Total_users'] + list(percentages.keys()))

    while current_date < end_date:
        df_temp = pd.DataFrame(columns=['Date', 'Total_users'] + list(percentages.keys()))
        df_temp['Date'] = [current_date]
        total_users = 2000 + (random.randint(-5, 5) * 50)
        df_temp['Total_users'] = [total_users]

        for key, value in percentages.items():
            df_temp[key] = [round(total_users * value / 100)]

        df = pd.concat([df, df_temp], axis=0)
        current_date += timedelta(days=1)

    return df

def plot(data):
    d=data.columns
    d = np.array(d)
    l=[]
    for i in d[2:]:
        l.append(data[i].sum())
    # m=[]
    # for i in data["Date"]:
    # # print(i)
    # # date_object = datetime.strptime(i, "%Y-%m-%d")
    # # Format the datetime object as "1 Jan 2023"
    #     m.append(i.strftime("%d %b %Y"))
    # data["Date"] = np.array(m)
    # print(l)
    plt.figure(figsize=(15, 6))
    plt.subplot(1,2,1)
    plt.pie(l,labels = d[2:])
    # st.pyplot(plt)
    plt.subplot(1,2,2)
    # plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data['Total_users'], marker='o', linestyle='-', color='b', label='Sales Data')
    plt.xlabel('Date')
    plt.ylabel('users')
    plt.title('Synthetic Sales Data with Seasonality and Upward Trend')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt