from joblib import Parallel, delayed
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np


def machine_learning_function(parsed_message):
    parsed_message = [[parsed_message]]
    print(parsed_message)
    labelEncoder = LabelEncoder()
    # reshape data string to float something
    parsed_message = labelEncoder.fit_transform(parsed_message)
    print(parsed_message)
    parsed_message = np.reshape(parsed_message, (1, -1))
    print(parsed_message)
    # Load the model from the file
    ml_model = joblib.load('machine_learning\ml_model.pkl')
 
    # Use the loaded model to make predictions
    prediction = ml_model.predict(parsed_message)
#    print(prediction)
#    print(type(prediction))
    result = prediction[0]
#    print(type(test))
#    print(result)
    return result

machine_learning_function("https://google.com")