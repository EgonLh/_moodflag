from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# loading the model and encoders
model = joblib.load("../model/xgb_model.pkl")
encoders = joblib.load("../model/label_encoders.joblib")
app = FastAPI()

for col, le in encoders.items():
    print(f"{col} → {le.classes_}")

class MoodSwingInput(BaseModel):
    Gender: str
    Country: str
    Occupation: str
    self_employed: str
    family_history: str
    treatment: str
    Days_Indoors: str
    Growing_Stress: str
    Changes_Habits: str
    Mental_Health_History: str
    Coping_Struggles: str
    Work_Interest: str
    Social_Weakness: str
    mental_health_interview: str
    care_options: str

@app.post("/predict")
def predict(data: MoodSwingInput):
    input_dict = data.dict()
    encoded_values = []
    for col in input_dict:
        val = input_dict[col]
        if col not in encoders:
            raise HTTPException(status_code=400, detail=f"Encoder for '{col}' not found.")
        try:
            encoded_val = encoders[col].transform([val])[0]
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid value '{val}' for column '{col}'.")
        encoded_values.append(encoded_val)
    input_array = np.array(encoded_values).reshape(1, -1)
    prediction = model.predict(input_array)
    return {"prediction": int(prediction[0])}
