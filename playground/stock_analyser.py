# from empyrial import empyrial,Engine
# portfolio = Engine(
#     start_date="2018-06-09",
#     portfolio=["MSFT","AAPL","IBM","TSLA","AMZN"],
#     weights=[0.2,0.2,0.2,0.2,0.2],
#     benchmark=["SPY"]
# )
# empyrial(portfolio)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from sklearn.preprocessing import MinMaxScaler

start = "2010-01-01"
end = "2019-12-31"
df = data.DataReader('AAPL','yahoo',start,end)
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot(df.Close)
fig.savefig('mplt.png')   # save the figure to file
plt.close(fig)

ma100 = df.Close.rolling(100).mean()
print(ma100)
ma100fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.plot(ma100, 'r')

ma200 = df.Close.rolling(200).mean()
plt.plot(ma200,'g')
ma100fig.savefig('ma100.png')
plt.close(ma100fig)
#splitting Data into training and Testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])
print(data_training.shape)
print(data_testing.shape)

scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)
print(data_training_array)

y_train = [] 
x_train = []

for i in range(100,data_training_array.shape[0]):
    x_train.append(data_training_array[i-100])
    y_train.append(data_training_array[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# ML Model
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential

model = Sequential()
model.add(LSTM(units = 50, activation='relu', return_sequences = True,
input_shape = (x_train.shape[1],1)))
model.add(Dropout(0.2))

model.add(LSTM(units = 60, activation='relu', return_sequences = True))
model.add(Dropout(0.3))

model.add(LSTM(units = 80, activation='relu', return_sequences = True))
model.add(Dropout(0.4))

model.add(LSTM(units = 120, activation='relu', return_sequences = True))
model.add(Dropout(0.5))

model.add(Dense(units=1))
print(model.summary())

model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(x_train,y_train,epochs=50)
