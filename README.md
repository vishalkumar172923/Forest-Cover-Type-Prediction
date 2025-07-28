# Forest Cover Type Prediction 
A ML project that predicts the type of forest cover using a Random Forest Classifier. Built with Streamlit for an interactive UI.

##  Features
- Predicts one of 7 forest cover types
- Uses 54 input features from the dataset
- Displays relevant forest image for better visualisation

##  📁 Files
main.ipynb – model training
app.py – Streamlit app
rfc.pkl – trained Random Forest model
train.csv – dataset
*.jpg – images for each forest type

## Input Features
The model expects a comma-separated list of all 54 numerical features from the dataset. Example input:
2596,51,3,258,0,510,221,232,0,0,0,1,0,0,... (continues up to 54 values)


## 📷 Output Example
Predicts: Aspen
Shows: [Image of Aspen Forest]


##  How to Run Input Features
```bash
pip install -r requirements.txt
streamlit run app.py
