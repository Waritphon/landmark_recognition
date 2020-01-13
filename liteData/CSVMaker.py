#this file will reduce the data size of CSV to around 10%
import pandas as pd
def run():
    train = pd.read_csv("../data/train.csv")
    df = pd.DataFrame(columns=['url', 'label'])

    for i in range(len(train)):
        if i%9 == 0:
            df = df.append(train[i:i+1][['url', 'label']], ignore_index=True, sort=False)

    df.to_csv('ltrain.csv')

if __name__ == '__main__':
    run()