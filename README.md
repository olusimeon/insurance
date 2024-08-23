Insurance Claim Prediction App

Overview
This application predicts whether a customer will make an insurance claim based on their profile and vehicle details. The app leverages machine learning models, logged and managed via MLflow, to ensure version control and easy deployment. The predictions are served through a Flask web application, which provides a simple user interface for file uploads and displays the prediction results.

Features
Predict Insurance Claims: Upload customer and vehicle details in a CSV file to get predictions on insurance claims.
Model Versioning with MLflow: Models are logged, tracked, and managed using MLflow.
Easy Deployment: The app is designed to be deployed on local servers, with simple integration into cloud environments if needed.
Installation
Prerequisites
Python 3.7 or later
pip for package management
MLflow installed and configured
Flask installed

Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/insurance-claim-prediction-app.git
cd insurance-claim-prediction-app

Create a virtual environment:

bash
Copy code
python -m venv newvenv


source newvenv/bin/activate  # On Windows use `newvenv\Scripts\activate`

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up MLflow:

Ensure that MLflow is running on your machine:
bash
Copy code
mlflow ui --p 8080
Configure the tracking URI in your Flask app or environment variables:
python
Copy code
mlflow.set_tracking_uri("http://127.0.0.1:8080")
Run the Flask app:

bash
Copy code
python app.py
The app will be accessible at http://127.0.0.1:5050.

Usage
Access the Web Interface:

Navigate to http://127.0.0.1:5000 in your web browser.
Upload a CSV File:

Prepare a CSV file with the required customer and vehicle details. Check mlartifacts columns.txt for required details

Upload the file via the provided form on the web interface.
View Predictions:

After uploading the file, the app will return predictions indicating whether each customer is likely to make a claim.

Model Details
Model Training: The model was trained using historical insurance claim data, with features including customer demographics, vehicle specifications, and other relevant factors.

Model Logging with MLflow: During training, the model was logged using MLflow, capturing metrics, parameters, and artifacts.

Model Deployment: The model can be loaded directly from the MLflow tracking server or from a local pickle file.
Project Structure
bash
Copy code
insurance-claim-prediction-app/
│
├── app.py                      # Main Flask application
├── templates/
│   └── temp.html               # HTML template for file upload
├── model/                      # Directory for storing model files
│   └── model.pkl               # Serialized model file (if using locally)
├── newvenv/                    # Virtual environment (optional)
├── requirements.txt            # Python dependencies
└── README.md                   # This README file
Contributing
We welcome contributions to enhance the functionality and performance of the app. Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature-name).
Create a new Pull Request.

Contact
For questions, suggestions, or feedback, please open an issue or contact the project maintainers at olusimeon4@gmail.com.