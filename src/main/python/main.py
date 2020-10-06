# Copyright (c) 2020 Anastasiia Birillo

import pandas as pd

from src.main.python.api_handler import VkApiHandler

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    api_handler = VkApiHandler()
    current_user = api_handler.get_current_user()
    df = pd.DataFrame(columns=list(current_user.__dict__.keys()))
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
    df = df.append(current_user.__dict__, ignore_index=True)

    users = [api_handler.get_user_by_id(id) for id in range(1, 10)]
    real_users = [user for user in users if user is not None]
    for user in real_users:
        df = df.append(user.__dict__, ignore_index=True)
    print(df)