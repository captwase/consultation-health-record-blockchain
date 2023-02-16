import pickle
import numpy as np
import pandas as pd


# df = pd.read_csv('dataset.csv')
# print(df.head())
# # df.describe()

# print(df1.head())
#
# df.isna().sum()
# df.isnull().sum()
#
# cols = df.columns
# data = df[cols].values.flatten()
#
# s = pd.Series(data)
# s = s.str.strip()
# s = s.values.reshape(df.shape)
#
# df = pd.DataFrame(s, columns=df.columns)
#
# df = df.fillna(0)
# df.head()
#
# vals = df.values
# symptoms = df1['Symptom'].unique()
#
# for i in range(len(symptoms)):
#     vals[vals == symptoms[i]] = df1[df1['Symptom'] == symptoms[i]]['weight'].values[0]
#
# d = pd.DataFrame(vals, columns=cols)
#
# d = d.replace('dischromic _patches', 0)
# d = d.replace('spotting_ urination', 0)
# df = d.replace('foul_smell_of urine', 0)
# df.head()
#
# (df[cols] == 0).all()
#
# df['Disease'].value_counts()
#
# df['Disease'].unique()
#
# data = df.iloc[:, 1:].values
# labels = df['Disease'].values
#
# x_train, x_test, y_train, y_test = train_test_split(data, labels, shuffle=True, train_size=0.85)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#
# model = SVC()
# model.fit(x_train, y_train)
#
# preds = model.predict(x_test)
#
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)
#
# print(preds)
#
# conf_mat = confusion_matrix(y_test, preds)
# df_cm = pd.DataFrame(conf_mat, index=df['Disease'].unique(), columns=df['Disease'].unique())
# print('F1-score% =', f1_score(y_test, preds, average='macro') * 100, '|', 'Accuracy% =',
#       accuracy_score(y_test, preds) * 100)


def svm(_symptoms=None):
    symptoms = _symptoms

    symptoms_csv = pd.read_csv('Symptom-severity.csv')

    a = np.array(symptoms_csv["Symptom"])
    b = np.array(symptoms_csv["weight"])

    for j in range(len(symptoms)):
        for k in range(len(a)):
            if symptoms[j] == a[k]:
                symptoms[j] = b[k]

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    remaining = 17 - len(symptoms)
    nulls = [0] * remaining
    psy = [symptoms + nulls]

    prediction = model.predict(psy)
    print(prediction)


svm(['itching', 'fatigue', 'shivering', 'skin_rash', 'continuous_sneezing', 'muscle_wasting'])
