# Sentiment Analysis Jhonny Depp

This project aims to classify text into positive or negative sentiments using a machine learning model called Decision Tree Classifier. The resulting web app allows users to input text and get a prediction of whether the text has a positive or negative sentiment.

## Installation

To install and run the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip. You can do this by running the following command in your terminal:
`pip install -r requirements.txt`
3. Run the web app using the following command: `streamlit run app.py`
4. Access the web app by opening your web browser and navigating to `http://localhost:8501`.

## Usage

To use the web app, simply input the text you want to classify into the text box and click the "Predict" button. The web app will then use the pre-trained model to predict whether the text has a positive or negative sentiment.

## Example

Here's an example of how to use the web app:

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter the text "Shame on you amber!!!" into the text box.
3. Click the "Predict" button.
4. The web app should display the message "Text is classify as negative!".

## Issues

The outcome of this project is a highly accurate model that can classify text into either a negative or positive sentiment with an accuracy rate of 82%. However, model predictions may not always be correct when dealing with custom text due to the limited amount of data.

## Acknowledgements

This project was built using scikit-learn and Streamlit framework.
