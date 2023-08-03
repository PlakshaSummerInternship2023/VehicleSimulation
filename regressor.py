import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from typing import Callable

from constants import DATA_FILE, SHEET_NAME
from utils import testbanner


class Regressor(object):
    def __init__(
        self, filename: str, sheet_name: str, x_value: str, y_value: str, power: int = 6
    ):
        self.__dataframe__ = pd.read_excel(filename, sheet_name)
        self.__lr__ = LinearRegression()

        self.x_value = x_value
        self.y_value = y_value

        self.powers = range(power)

        self.__preprocess__()

    """
    preprocesses the dataframe to the required data spec 
    [x^2, x, 1]
    
    this is to train the linear regressor
    """

    def __preprocess__(self) -> None:
        x = self.__dataframe__.pop(self.x_value).to_numpy()
        self.plottable_features = x
        size = x.shape[0]
        self.feature_labels = np.array(
            [x**power for power in self.powers] + [np.ones(size)]
        )
        self.feature_labels = np.column_stack(self.feature_labels)
        # print(self.feature_labels[0])
        self.target_labels = np.abs(self.__dataframe__.pop(self.y_value).to_numpy())

    """
    trains the regressive model
    """

    def train(self, epochs=250) -> None:
        self.__lr__.fit(self.feature_labels, self.target_labels)
        print("\ntraining done")

    """
    predicts the value of the thrust based on the input 
    PWM

    x : the pwm value in np.float32
    """

    def __call__(self, x: np.float32) -> np.float32:
        size = x.shape[0]
        features = np.array([x**power for power in self.powers] + [np.ones(size)])
        features = np.column_stack(features)
        return self.__lr__.predict(features)


#########################################
# REGRESSOR
pwm_regressor = Regressor(DATA_FILE, SHEET_NAME, " PWM (µs)", " Force (Kg f)", power=6)
##########################################


def mean_squared_error(y, y_pred):
    return (y_pred - y) ** 2


class GradientDescent(object):
    def __init__(self, learning_rate=1e-2):
        self.learning_rate = learning_rate

    def __call__(self, w, x, y, y_pred):
        diff = -2 * (y - w * x) * x

        w -= self.learning_rate * diff
        return w


if __name__ == "__main__":
    testbanner()

    optimizer = GradientDescent(1e-3)
    regressor = Regressor(DATA_FILE, SHEET_NAME, " PWM (µs)", " Force (Kg f)")

    regressor.train(1)
    x = np.linspace(1100, 1900, 201)
    y = regressor(x)

    print(f"MSE : {np.sum((y-regressor.target_labels)**2)}")
    plt.plot(regressor.plottable_features, regressor.target_labels, "ro", label="data")
    plt.plot(x, y, "b", linewidth=4, label="regressor")
    plt.xlabel("PWM")
    plt.ylabel("thrust")
    plt.savefig("figure.png")
    plt.legend()
    plt.show()
