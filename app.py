import pickle
import streamlit as st

from PIL import Image

pickled_vector = pickle.load(open('temp/load_file/vector/tfidf_lemma.pkl', 'rb'))
pickled_model = pickle.load(open('temp/load_file/model/DecisionTreeClassifier82.pkl', 'rb'))
image_icon = Image.open('temp/icon/icon.png')

st.set_page_config(
    page_title='Sentiment Analysis', 
    layout='wide', 
    initial_sidebar_state='auto', 
    page_icon=image_icon)


with st.sidebar:
    st.image(image_icon)
    st.title('Jhonny Depp Sentiment Analysis')
    st.sidebar.caption("Classify your text here!")
    choice = st.radio('Main Menu', ['Home', 'About'])
    st.info('This website application helps you classify text freely!')
    st.sidebar.markdown("---")
    # st.sidebar.markdown("Developed by [Bastian Armananta](https://www.linkedin.com/in/bastian-armananta/)")

if choice == 'Home':
    st.title("Let's classify your text!")
    st.markdown('This app clasify text using Machine Learning Decision Tree Classifier algorithm. You can find the code on [GitHub](https://github.com/bastianarmananta/sentiment-jhonny-amber).')
    st.caption('This web app trained using english dataset based on Jhonny Depp and Amber Heard case.')
    text_input = st.text_input(label="Insert text to predict", placeholder="Shame on you amber!")
    predict_button = st.button('Predict', type='primary')
    st.markdown("---")

    def predict_text(text):
        clf = pickled_vector
        sequence = [text]
        
        _ = clf.transform(sequence)
        
        predict = pickled_model.predict(_)
        if predict == 0:
            st.warning("Text is classify as negative!")
        else:
            st.success('Text is classify as positive!')
    
    if predict_button:
        predict_text(text_input)

if choice == 'About':
    st.title('About')
    st.markdown("---")
    st.header('Sentiment Analysis Jhonny Depp vs Amber Heard')
    st.caption('This project is based on Jhonny Depp and Amber Heard case, trained using Decision Tree Classifier algorithm using TfidfVectorizer to preprocess data.')
    st.caption('Result of this project is model can classify text into negative, and positive class with 82% model accuracy.')
    st.caption('Even the accuracy pretty high, model can be wrong when predicted custom text because lack of data.')
    st.caption("This project is developed by [Bastian Armananta](https://www.linkedin.com/in/bastian-armananta/) and [Fanisa Nimastiti](https://www.linkedin.com/in/fanisa-nimastiti-805404164/).")
