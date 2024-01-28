import pandas
import os

def get_training_data(path):
    df = pandas.read_excel(path)
    for column in [12, 12, 12, 2, 2, 1]:
        df = df.drop(df.columns[column], axis=1)
    new_df = pandas.DataFrame({'Data': range(len(df.values))})
    df.update(new_df)
    return df

def create_training_data(workdir):
    market_data_path = os.path.join(workdir, "Market")
    training_output_path = os.path.join(workdir, "training_data.csv")
    data = []
    for name in os.listdir(market_data_path):
        input_file_path = os.path.join(market_data_path, name)
        new_data = get_training_data(input_file_path)
        for row in new_data.values:
            data.append(row)
    df = pandas.DataFrame(data, columns=["Date", "Open", "Max", "Min", "Close", "Change", "Volume", "Transactions", "Rotation"])
    df.to_csv(training_output_path)

def main():
    # get current path of this file
    workdir = os.path.dirname(os.path.realpath(__file__))
    create_training_data(workdir)

if __name__ == "__main__":
    main()
