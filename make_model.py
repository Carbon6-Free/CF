import autokeras as ak
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
# from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib
matplotlib.use('Agg')

model_summary = []

class CustomLSTMBlock(ak.Block):
    def build(self, hp, inputs):
        model = Sequential()
        model.add(LSTM(units=hp.Int('units', min_value=32, max_value=128, step=32),
                       activation='relu',
                       return_sequences=True,
                       input_shape=(inputs.shape[1], inputs.shape[2])))
        model.add(LSTM(units=hp.Int('units', min_value=32, max_value=128, step=32),
                       activation='relu'))
        model.add(Dense(1, activation='linear'))
        return model
    
class TimeSeriesRegressor(ak.StructuredDataBlock):
    def build(self, hp, inputs):
        lstm_block = CustomLSTMBlock()(inputs)
        output_node = ak.RegressionHead()(lstm_block)
        return output_node

def Training_Model(data_path, max_trials=50, epochs=20):
    data_with_volatility = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')

    X = data_with_volatility.iloc[:-1].values
    y = data_with_volatility['Consumption'].shift(-1).dropna().values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    reg = ak.StructuredDataRegressor(overwrite=True,
                                     directory=".",
                                     seed=42,
                                     objective="val_mean_squared_error",
                                     max_trials=max_trials
                                    #  categorical_columns=[],
                                     )

    history = reg.fit(X_scaled[:-60], y[:-60], epochs=epochs, validation_split=0.2)

    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history.get('val_loss', []), label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Mean Squared Error')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.savefig(data_path[:-4] + "_loss.png")

    best_model = reg.export_model()
    # best_model.summary(print_fn=lambda x: model_summary.append(x))
    # model_summary = "\n".join(model_summary)
    # print(model_summary)
    best_model.save(data_path[:-4])
    plot_model(best_model, to_file=data_path[:-4] + "_model_structure.png", show_shapes=True)
    # best_model = load_model(data_path[:-4])

    X_test_scaled = scaler.transform(X[-60:])
    predictions_test = best_model.predict(X_test_scaled)

    plt.figure(figsize=(12, 6))
    plt.plot(data_with_volatility.index, data_with_volatility['Consumption'], label='Actual Consumption', color='blue')
    plt.plot(data_with_volatility.index[-60:], predictions_test, label='Predicted Consumption (Test)', color='red', linestyle='dashed')
    plt.title('Power Consumption Prediction Results (Test)')
    plt.xlabel('Date')
    plt.ylabel('Power Consumption (Kwh)')
    plt.legend()
    plt.grid(True)
    plt.savefig(data_path[:-4] + "_prediction_results.png")

    # return model_summary

# Training_Model("bio.csv", 50, 20)