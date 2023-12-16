from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler 
import joblib
import numpy as np
from pathlib import Path

Base_dir=Path(__file__).resolve(strict=True).parent
with open(f"{Base_dir}/final_model.joblib","rb") as f:
    # Load the trained model
    model = joblib.load(f)

def sanitize(data:str):
    L=data.split(",")
    for i in range(6,11):
        L[i]=float(L[i])
    return L

def predict_loan(L:list):
    Labelencoder_x=LabelEncoder()
    ss=StandardScaler()
    # Performing necessary preprocessing
    L.append(np.log(L[8]))
    L.append(L[6] + L[7])
    L.append(np.log(L[13]))

    # Selecting only columns that we used for the model
    ranges_to_select = [(1,4),(9, 10), (13, 14)]
    selected_ranges = []
    for start, end in ranges_to_select:
        selected_ranges.extend(L[start:end + 1])
    # Label encoding for categorical columns
    selected_ranges[0:5] = Labelencoder_x.fit_transform(selected_ranges[0:5])
    # Convert to NumPy array
    result_array=np.array(selected_ranges)
    # Reshape the array as we are predicting for one instance
    result_re = result_array.reshape(1, -1)
    ss.fit_transform(result_re)
    prediction = model.predict(result_re)
    return int(prediction[0])

