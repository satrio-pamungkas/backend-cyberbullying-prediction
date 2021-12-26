from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
import pandas as pd
import joblib

def get_prediction(input_text):
    data = pd.read_csv("dataset/dataset-cyberbullying.csv")
    data['Komentar'] = data['Komentar'].str.replace(r"[\"\',]", '')
    
    x = data['Komentar']
    y = data['Kategori']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    
    cv = CountVectorizer()
    features = cv.fit_transform(x_train)
    
    model = joblib.load("model/NB_Cyberbullying_model.pkl")
    model.fit(features, y_train)
    inputan = cv.transform([input_text])
    result = model.predict(inputan)
    
    return result[0]
    
    

    