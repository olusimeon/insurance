from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import mlflow.pyfunc

app = Flask(__name__)

# using Mlflow pyfunc to load model from s3.
#model = mlflow.pyfunc.load_model('path to s3 file uri where model is stored /model')

# Path to the local model file
model_file_path = "part to your mlartifacts model.pkl"

# Load the model using joblib
model = joblib.load(model_file_path)

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('temp.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    
    file = request.files['file']
    
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return jsonify({"error": f"Failed to read the CSV file: {str(e)}"}), 400
    
    # Define the expected columns
    expected_columns = [
        "subscription_length", "vehicle_age", "customer_age", "region_density", "airbags",
        "is_esc", "is_adjustable_steering", "is_tpms", "is_parking_sensors", "is_parking_camera",
        "rear_brakes_type", "displacement", "cylinder", "turning_radius", "length", "width",
        "gross_weight", "is_front_fog_lights", "is_rear_window_wiper", "is_rear_window_washer",
        "is_rear_window_defogger", "is_brake_assist", "is_power_door_locks", "is_central_locking",
        "is_power_steering", "is_driver_seat_height_adjustable", "is_day_night_rear_view_mirror",
        "is_ecw", "is_speed_alert", "ncap_rating", "segment_A", "segment_B1", "segment_B2", 
        "segment_C1", "segment_C2", "segment_Utility", "model_M1", "model_M10", "model_M11", 
        "model_M2", "model_M3", "model_M4", "model_M5", "model_M6", "model_M7", "model_M8", 
        "model_M9", "fuel_type_CNG", "fuel_type_Diesel", "fuel_type_Petrol", 
        "max_torque_113Nm@4400rpm", "max_torque_170Nm@4000rpm", "max_torque_200Nm@1750rpm", 
        "max_torque_200Nm@3000rpm", "max_torque_250Nm@2750rpm", "max_torque_60Nm@3500rpm", 
        "max_torque_82.1Nm@3400rpm", "max_torque_85Nm@3000rpm", "max_torque_91Nm@4250rpm", 
        "max_power_113.45bhp@4000rpm", "max_power_118.36bhp@5500rpm", 
        "max_power_40.36bhp@6000rpm", "max_power_55.92bhp@5300rpm", 
        "max_power_61.68bhp@6000rpm", "max_power_67.06bhp@5500rpm", 
        "max_power_88.50bhp@6000rpm", "max_power_88.77bhp@4000rpm", 
        "max_power_97.89bhp@3600rpm", "engine_type_1.0 SCe", 
        "engine_type_1.2 L K Series Engine", "engine_type_1.2 L K12N Dualjet", 
        "engine_type_1.5 L U2 CRDi", "engine_type_1.5 Turbocharged Revotorq", 
        "engine_type_1.5 Turbocharged Revotron", "engine_type_F8D Petrol Engine", 
        "engine_type_G12B", "engine_type_K Series Dual jet", "engine_type_K10C", 
        "engine_type_i-DTEC", "transmission_type_Automatic", "transmission_type_Manual", 
        "steering_type_Electric", "steering_type_Manual", "steering_type_Power"
    ]
    
    # Ensure the DataFrame has all expected columns
    df = df.reindex(fill_value=0)

    try:
        # Convert DataFrame to NumPy array to match the training format
        data_for_prediction = df.to_numpy()
        # Predict using the loaded model
        predictions = model.predict(df)
        # Return the predictions as JSON
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)

    #to run on ec2 instance change host to accept requests from any  IP address and edit security inbound rules to allow traffic from port 5050 
    #app.run(host='0.0.0.0', port=5050, debug=True)
