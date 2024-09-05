# Insurance Claim Prediction app

## Overview
This application predicts whether a customer will make an insurance claim based on their profile and vehicle details. The app leverages machine learning models, logged and managed via MLflow, to ensure version control and easy deployment. The predictions are served through a Flask web application both on local machine and ec2 instance, which provides a simple user interface for file uploads and displays the prediction results. 

## Features
- **Predict Insurance Claims:** Upload customer and vehicle details in a CSV file to get predictions on insurance claims.
- **Model Versioning with MLflow:** Models are logged, tracked, and managed using MLflow.
- **Easy Deployment:** The app is designed to be deployed on local servers, with simple integration into cloud environments if needed.
- **Deployed on AWS EC2**: The application is hosted on an AWS EC2 instance, providing scalability and cloud-based access. File has been updated on our to deploy to EC2. AWS guide and notebook provided.

## Installation

### Prerequisites
- Python 3.11.7
- pip for package manaegement
- MLflow installed and configured
- Flask installed
- AWS Account: Required to store model artifacts,sagemaker notebook, deploy model and managing your application on AWS EC2.

### Setup Instructions

1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/insurance-claim.git
   cd insurance-claim-prediction
```
   
2. **Create a virtual environment:**

``` bash
python -m venv newvenv
source newvenv/bin/activate  # On Windows use `newvenv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up MLflow:**
   Ensure that MLflow is running on your machine you can specify the port you want mlflow to run on (optional)
```bash
mlflow ui # to start mlflow ui or
mlflow ui --port 8080 # to specify the port
```
   Configure the tracking URI in your Flask app or environment variables:
```bash
mlflow.set_tracking_uri("http://127.0.0.1:8080")
```

5. **Run the Flask app:**
```bash
python app.py
```
- The app will be accessible at http://127.0.0.1:5050 as specified in the app.py file.**

**Usage:**
   - Access the Web Interface:
   - Navigate to http://127.0.0.1:5000 in your web browser.
   - Upload a CSV File:
   - Prepare a CSV file with the required customer and vehicle details. Check mlartifacts/columns.txt for required details.
   - Upload the file via the provided form on the web interface.

6. **Deploy to AWS EC2**
   - Steps to follow on how to deploy to EC2 is already provided on aws flask app.txt
   - Ensure your EC2 instance is running and accessible 
   - Set up security group to allow traffic on the required ports i.e 5050 as specified in the app.py file.

7. **Accessing the Application**
   - Visit your application URL or public IP address on the EC2 instance to interact with it. 
   - For example, http://<your-ec2-public-ip>:5050.

## View Predictions:
After uploading the file, the app will return predictions indicating whether each customer is likely to make a claim.
 
**Model Details**

   - Model Management: Ensure that MLflow is properly configured to save model artifats on s3 and accessible from your EC2 instance for managing and tracking models.
   - Security: Implement appropriate security measures for your application, including using HTTPS for secure communication and securing access to your EC2 instance.
   - Model Training: The model was trained using historical insurance claim data, with features including customer demographics, vehicle specifications, and other relevant factors.
   - Model Logging with MLflow: During training, the model was logged using MLflow, capturing metrics, parameters, and artifacts.
   - Model Deployment: The model can be loaded directly from the MLflow tracking server, S3 bucket artifacts or from a local pickle file.

### Project Structure
```bash
insurance-claim-prediction-app/
│
├── app.py                      # Main Flask application
├── templates/
│   └── temp.html               # HTML template for file upload
├── mlartifacts/                # Directory for storing MLflow artifacts
│   └── 1909189155/            # Directory for a specific model run
│       ├── model.pkl           # Serialized model file (if using locally)
├── newvenv/                    # Virtual environment (optional)
├── requirements.txt            # Python dependencies
└── README.md                   # This README file
```

**Contributing**
I welcome contributions to enhance the functionality and performance of the app. Please follow these steps:

**Contact**
For questions, suggestions, or feedback, please open an issue or contact on olusimeon4@gmail.com.






