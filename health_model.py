import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Separate encoders
emotion_encoder = LabelEncoder()
risk_encoder = LabelEncoder()

# Encode columns
data['emotion'] = emotion_encoder.fit_transform(data['emotion'])
data['risk'] = risk_encoder.fit_transform(data['risk'])

# Features and target
X = data[['emotion','sleep','exercise','junk_food']]
y = data['risk']

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# Prediction function
def predict_risk(emotion, sleep, exercise, junk):

    emotion_encoded = emotion_encoder.transform([emotion])[0]

    prediction = model.predict([[emotion_encoded, sleep, exercise, junk]])

    risk_level = risk_encoder.inverse_transform(prediction)

    return risk_level[0]