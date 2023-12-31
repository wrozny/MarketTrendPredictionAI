import pandas
import os

def get_training_data(path):
    df = pandas.read_excel(path)
    for column in [12, 12, 12, 2, 2, 1]:
        df = df.drop(df.columns[column], axis=1)
    new_df = pandas.DataFrame({'Data': range(len(df.values))})
    df.update(new_df)
    return df

def create_training_data():
    data = []
    for name in os.listdir("Market"):
        new_data = get_training_data(f"Market/{name}")
        for row in new_data.values:
            data.append(row)
    df = pandas.DataFrame(data, columns=["Date", "Open", "Max", "Min", "Close", "Change", "Volume", "Transactions", "Rotation"])
    df.to_csv("training_data.csv")
