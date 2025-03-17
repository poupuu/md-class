import streamlit as st
import joblib

def load_model(filename):
  model = joblib.load(filename)
  return model

def predict_with_moel(model, user_input):
  prediction = mode.predict([user_input])
  return prediction[0]


def main():
  st.title('Dermatology Machine Learning')
  st.write('Halo!')
  
  #input data by user
  erythema = st.slider('erythema', min_value = 0, max_value=3, value=2)
  #min_value dan max_value = liat dari data, dan value itu nilai default pas dideploy

  
if __name__ == "__main__":
	main()

