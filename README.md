# Insurance Claim Prediction App

## Overview
This application predicts whether a customer will make an insurance claim based on their profile and vehicle details. The app leverages machine learning models, logged and managed via MLflow, to ensure version control and easy deployment. The predictions are served through a Flask web application, which provides a simple user interface for file uploads and displays the prediction results.

## Features
- **Predict Insurance Claims:** Upload customer and vehicle details in a CSV file to get predictions on insurance claims.
- **Model Versioning with MLflow:** Models are logged, tracked, and managed using MLflow.
- **Easy Deployment:** The app is designed to be deployed on local servers, with simple integration into cloud environments if needed.

## Installation

### Prerequisites
- Python 3.7 or later
- pip for package management
- MLflow installed and configured
- Flask installed

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/insurance-claim-prediction-app.git
   cd insurance-claim-prediction-app

## Create a virtual environment:

bash
Copy code
python -m venv newvenv
source newvenv/bin/activate  # On Windows use `newvenv\Scripts\activate`
