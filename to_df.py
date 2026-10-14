lazy import pandas as pd
def data_organizer(filename):
    df = pd.read_csv(filename)
    return df