import pickle 
from flask import Flask, request, jsonify 
import numpy as np 

print("Loading Flask App")


try:
    # Load trained model and preprocessor
    with open("logistic_regression.pkl", "rb") as file:
        data = pickle.load(file)  # Unpickle (load) the saved dictionary

except Exception as e:
    print(f"Error Loading Model: {e}")
    exit()

model = data["model"]  # Retrieve the Logistic Regression model
preprocessor = data["preprocessor"]  # Retrieve the Preprocessing pipeline

# intialize Flask app before using @app.route

app = Flask(__name__)

def home():
    return "Flask is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        # Standardize new instance using saved preprocessor
        features_std = preprocessor.standardize_instance(features)

        # Make prediction
        predicted_label = model.predict(features_std)[0]
        predicted_prob = model.predict_proba(features_std)[0].tolist()

        # Return response
        return jsonify({"predicted_class": int(predicted_label), "predicted_probability": predicted_prob})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(debug=True)