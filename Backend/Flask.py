import pickle 
from flask import Flask, request, jsonify 
import numpy as np 
from flask_cors import CORS


print("Loading Flask App")


app = Flask(__name__)
CORS(app)



try:
    
    with open("logistic_regression.pkl", "rb") as file:
        data = pickle.load(file)  # Unpickle (load) the saved dictionary

except Exception as e:
    print(f"Error Loading Model: {e}")
    exit()

model = data["model"] 
preprocessor = data["preprocessor"]  



@app.route('/')
def home():
    return "Flask is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        
        features_std = preprocessor.standardize_instance(features)

        # Make prediction
        predicted_label = model.predict(features_std)[0]
        predicted_prob = model.predict_proba(features_std)[0].tolist()

        
        return jsonify({"predicted_class": int(predicted_label), "predicted_probability": predicted_prob})
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == "__main__":
    app.run( debug=True)
