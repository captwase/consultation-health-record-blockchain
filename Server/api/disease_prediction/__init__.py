import os.path
import pickle
import numpy as np
import pandas as pd
from ehr.settings import BASE_DIR

symptoms_csv = pd.read_csv(os.path.join(BASE_DIR, 'static/Symptom-severity.csv'))

with open(os.path.join(BASE_DIR, 'static/model.pkl'), 'rb') as f:
    model = pickle.load(f)


def svm(_symptoms=None):
    symptoms = _symptoms

    a = np.array(symptoms_csv["Symptom"])
    b = np.array(symptoms_csv["weight"])

    for j in range(len(symptoms)):
        for k in range(len(a)):
            if symptoms[j] == a[k]:
                symptoms[j] = b[k]

    remaining = 17 - len(symptoms)
    nulls = [0] * remaining
    prediction_symptoms = [symptoms + nulls]

    prediction = model.predict(prediction_symptoms)

    return prediction[0]
