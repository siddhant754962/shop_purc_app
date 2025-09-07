import streamlit as st
import pandas as pd
import joblib
import random

# ------------------------------ Load trained model ------------------------------
model = joblib.load("knn_shopper_model_smote_fixed.pkl")

# ------------------------------ CSS for 3D Neon Futuristic UI + Animated Background + Bomb Effect ------------------------------
st.markdown("""
<style>
/* Animated neon background */
body {
    background: radial-gradient(circle at 50% 50%, #1e3c72, #2a5298);
    overflow: hidden;
}
@keyframes neonMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
body::before {
    content: "";
    position: fixed;
    top:0; left:0;
    width: 100%; height: 100%;
    background: linear-gradient(45deg, #ff00ff, #00ffff, #ffdd59, #ff00ff);
    background-size: 400% 400%;
    opacity: 0.15;
    z-index: -1;
    animation: neonMove 20s linear infinite;
}

/* Floating 3D header card */
.header-card {
    background: rgba(0,0,0,0.6);
    border-radius: 25px;
    padding: 40px 30px;
    margin: 20px auto;
    max-width: 900px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 25px #ffdd59;
    backdrop-filter: blur(10px);
}
.header-card h1 {
    font-family: 'Arial Black', Gadget, sans-serif;
    font-size: 50px;
    background: linear-gradient(90deg, #ff6ec7, #ffd93d, #6effe0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 3px 3px 15px #000000;
}
.header-card p {
    font-family: 'Arial', sans-serif;
    font-size: 22px;
    color: #ffeaa7;
    margin-top: 15px;
    text-shadow: 1px 1px 5px #000000;
}

/* Buttons Styling */
.stButton>button {
    background: linear-gradient(to right, #fd6e6e, #ffdd59);
    color: #1e3c72;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #ffdd59;
}

/* Floating 3D input boxes */
.stNumberInput, .stSelectbox {
    background: rgba(0,0,0,0.6);
    border-radius: 20px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 20px #ffdd59;
    backdrop-filter: blur(5px);
    animation: floatWave 3s ease-in-out infinite;
}

/* Input labels */
label[data-baseweb="label"] {
    font-weight: bold;
    font-size: 18px;
    color: #ff6ec7 !important;
    text-shadow: 0 0 5px #ff6ec7, 0 0 10px #33ffff;
}

/* Inputs text */
input, select {
    border-radius: 10px;
    padding: 8px;
    border: 2px solid #ffeaa7;
    background-color: #2a5298;
    color: #fff;
}

/* Floating animation */
@keyframes floatWave {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* About Inputs & Output card */
.about-card {
    background: rgba(0,0,0,0.6);
    border-radius: 25px;
    padding: 25px 30px;
    margin: 20px auto;
    max-width: 900px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 25px #ff33cc;
    backdrop-filter: blur(10px);
    animation: floatWave 4s ease-in-out infinite;
}
.about-card h2 {
    text-align:center;
    font-size:28px;
    text-shadow: 0 0 10px #ff33cc, 0 0 20px #33ffff;
}
.about-card ul li {
    font-size:18px;
    line-height:1.8;
    padding:3px 0;
    transition: all 0.3s ease;
}
.about-card ul li:hover {
    color:#ff6ec7;
    text-shadow: 0 0 5px #ff6ec7, 0 0 15px #33ffff;
}

/* Cinematic Bomb Prediction Cards */
@keyframes cinematicBomb {
    0% { transform: scale(1) rotate(0deg); box-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99; }
    25% { transform: scale(1.1) rotate(-3deg); box-shadow: 0 0 50px #00ff99, 0 0 80px #00ff99; }
    50% { transform: scale(1.2) rotate(3deg); box-shadow: 0 0 80px #00ffff, 0 0 100px #33ffff; }
    75% { transform: scale(1.1) rotate(-2deg); box-shadow: 0 0 50px #ff33ff, 0 0 80px #ff33ff; }
    100% { transform: scale(1) rotate(0deg); box-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99; }
}
.success-card-bomb, .error-card-bomb {
    background: rgba(0,0,0,0.7);
    border-radius: 30px;
    padding: 30px;
    margin: 20px 0;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    animation: cinematicBomb 1.5s ease-in-out infinite;
}
.success-card-bomb { color: #00ff99; }
.error-card-bomb { color: #ff3300; }

/* Neon Footer - White Glowing */
.footer-neon {
    text-align: center;
    margin-top: 40px;
    font-size: 18px;
    font-weight: bold;
    color: #ffffff; /* White */
    text-shadow: 
        0 0 5px #ffffff, 
        0 0 10px #ffffff, 
        0 0 20px #ffffff, 
        0 0 30px #ffffff, 
        0 0 40px #ffffff;
    animation: neonPulse 2s ease-in-out infinite alternate;
}

@keyframes neonPulse {
    0% { text-shadow: 0 0 5px #ffffff, 0 0 10px #ffffff, 0 0 20px #ffffff, 0 0 30px #ffffff, 0 0 40px #ffffff; }
    50% { text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff, 0 0 30px #ffffff, 0 0 40px #ffffff, 0 0 50px #ffffff; }
    100% { text-shadow: 0 0 5px #ffffff, 0 0 10px #ffffff, 0 0 20px #ffffff, 0 0 30px #ffffff, 0 0 40px #ffffff; }
}
</style>

<div class="header-card">
    <h1>🛒 Shopper Purchase Prediction App (KNN)</h1>
    <p>Fill in the details below to predict if a shopper will make a purchase.</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------ Random Sample Function ------------------------------
def random_sample():
    return {
        'Administrative': random.randint(0, 10),
        'Administrative_Duration': round(random.uniform(0, 300), 1),
        'Informational': random.randint(0, 5),
        'Informational_Duration': round(random.uniform(0, 100), 1),
        'ProductRelated': random.randint(1, 20),
        'ProductRelated_Duration': round(random.uniform(10, 1000), 1),
        'BounceRates': round(random.uniform(0.0, 0.5), 3),
        'ExitRates': round(random.uniform(0.0, 0.5), 3),
        'PageValues': round(random.uniform(0.0, 200.0), 2),
        'SpecialDay': round(random.uniform(0.0, 1.0), 2),
        'Weekend': random.choice([0, 1]),
        'Browser': random.randint(1, 13),
        'Region': random.randint(1, 9),
        'TrafficType': random.randint(1, 20),
        'OperatingSystems': random.randint(1, 8),
        'Month': random.choice(['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec']),
        'VisitorType': random.choice(["Returning_Visitor","New_Visitor","Other"])
    }

# ------------------------------ Random Sample Button ------------------------------
if st.button("🎲 Generate Random Sample"):
    sample = random_sample()
    for key, value in sample.items():
        st.session_state[key] = value

# ------------------------------ User Inputs ------------------------------
Administrative = st.number_input("Administrative (Count of admin pages visited)", min_value=0, value=st.session_state.get('Administrative', 2), key='Administrative')
Administrative_Duration = st.number_input("Administrative Duration (Seconds)", min_value=0.0, value=st.session_state.get('Administrative_Duration', 30.0), key='Administrative_Duration')
Informational = st.number_input("Informational (Count of info pages visited)", min_value=0, value=st.session_state.get('Informational', 0), key='Informational')
Informational_Duration = st.number_input("Informational Duration (Seconds)", min_value=0.0, value=st.session_state.get('Informational_Duration', 0.0), key='Informational_Duration')
ProductRelated = st.number_input("Product Related (Count of product pages visited)", min_value=0, value=st.session_state.get('ProductRelated', 5), key='ProductRelated')
ProductRelated_Duration = st.number_input("Product Related Duration (Seconds)", min_value=0.0, value=st.session_state.get('ProductRelated_Duration', 200.0), key='ProductRelated_Duration')
BounceRates = st.number_input("Bounce Rates (0 to 1)", min_value=0.0, max_value=1.0, value=st.session_state.get('BounceRates', 0.02), key='BounceRates')
ExitRates = st.number_input("Exit Rates (0 to 1)", min_value=0.0, max_value=1.0, value=st.session_state.get('ExitRates', 0.05), key='ExitRates')
PageValues = st.number_input("Page Values (Estimated value in $)", min_value=0.0, value=st.session_state.get('PageValues', 20.0), key='PageValues')
SpecialDay = st.number_input("Special Day (0.0 to 1.0, closer to 1 if near a special event)", min_value=0.0, max_value=1.0, value=st.session_state.get('SpecialDay', 0.0), key='SpecialDay')
Weekend = st.selectbox("Weekend (0 = No, 1 = Yes)", [0, 1], index=st.session_state.get('Weekend',0), key='Weekend')
Browser = st.selectbox("Browser (Code 1–13)", list(range(1,14)), index=st.session_state.get('Browser',2)-1, key='Browser')
Region = st.selectbox("Region (1–9)", list(range(1,10)), index=st.session_state.get('Region',1)-1, key='Region')
TrafficType = st.selectbox("Traffic Type (1–20)", list(range(1,21)), index=st.session_state.get('TrafficType',1)-1, key='TrafficType')
OperatingSystems = st.selectbox("Operating Systems (1–8)", list(range(1,9)), index=st.session_state.get('OperatingSystems',2)-1, key='OperatingSystems')
Month = st.selectbox("Month", ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec'], index=['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec'].index(st.session_state.get('Month','Jan')), key='Month')
VisitorType = st.selectbox("Visitor Type", ["Returning_Visitor","New_Visitor","Other"], index=["Returning_Visitor","New_Visitor","Other"].index(st.session_state.get('VisitorType','Returning_Visitor')), key='VisitorType')

# ------------------------------ Prediction ------------------------------
input_dict = {k:[st.session_state[k]] for k in st.session_state.keys()}
input_data = pd.DataFrame(input_dict)

if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    probs = model.predict_proba(input_data)[0]
    prob = float(probs[int(prediction)])
    
    if prediction == 1:
        st.markdown(f"""
        <div class="success-card-bomb">
        ✅ Shopper is <strong>LIKELY</strong> to make a purchase.<br>
        Confidence: {prob:.2f}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="error-card-bomb">
        ❌ Shopper is <strong>NOT likely</strong> to make a purchase.<br>
        Confidence: {prob:.2f}
        </div>
        """, unsafe_allow_html=True)

        
        

# ------------------------------ About Inputs & Output ------------------------------
with st.expander("ℹ️ About Inputs & Output"):
    st.markdown("""
    <div class="about-card">
        <h2>✨ Input Fields ✨</h2>
        <ul>
            <li><strong>Administrative:</strong> Number of admin pages visited (integer).</li>
            <li><strong>Administrative Duration:</strong> Total time spent on admin pages (seconds).</li>
            <li><strong>Informational:</strong> Number of informational pages visited (integer).</li>
            <li><strong>Informational Duration:</strong> Time spent on informational pages (seconds).</li>
            <li><strong>Product Related:</strong> Number of product-related pages visited (integer).</li>
            <li><strong>Product Related Duration:</strong> Time spent on product-related pages (seconds).</li>
            <li><strong>Bounce Rates:</strong> Fraction of visits where shoppers leave immediately (0-1).</li>
            <li><strong>Exit Rates:</strong> Fraction of visits where shoppers exit a page (0-1).</li>
            <li><strong>Page Values:</strong> Estimated page value in dollars.</li>
            <li><strong>Special Day:</strong> Closeness to a special event (0 = not special, 1 = very special).</li>
            <li><strong>Weekend:</strong> 0 = weekday, 1 = weekend.</li>
            <li><strong>Browser:</strong> Browser code (1–13).</li>
            <li><strong>Region:</strong> Shopper's region code (1–9).</li>
            <li><strong>Traffic Type:</strong> Type of traffic source (1–20).</li>
            <li><strong>Operating Systems:</strong> Shopper's OS code (1–8).</li>
            <li><strong>Month:</strong> Month of visit.</li>
            <li><strong>Visitor Type:</strong> Returning_Visitor / New_Visitor / Other.</li>
        </ul>
        <h2>⚡ Output Explanation ⚡</h2>
        <ul>
            <li><strong>LIKELY to make a purchase:</strong> Shopper is predicted to buy something.</li>
            <li><strong>NOT likely to make a purchase:</strong> Shopper is predicted not to buy anything.</li>
            <li><strong>Confidence:</strong> Probability score of the prediction (0 to 1). Higher means more certain.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------ About Project & Algorithm ------------------------------
st.markdown("""
<div class="about-card">
    <h2>🚀 Project & Algorithm Details</h2>
    <ul>
        <li><strong>Project Goal:</strong> Predict whether a shopper will make a purchase on an e-commerce website using behavioral data.</li>
        <li><strong>Data Used:</strong> Number of pages visited, time spent on each page type, bounce rates, exit rates, special day indicator, traffic type, browser, OS, month, region, and visitor type.</li>
        <li><strong>Algorithm:</strong> <strong>K-Nearest Neighbors (KNN)</strong> is used. The model calculates distances between the input sample and existing data points, finds the <em>k</em> nearest neighbors, and predicts the class based on majority vote.</li>
        <li><strong>Why KNN:</strong> KNN is simple, intuitive, and works well with small-to-medium tabular datasets.</li>
        <li><strong>Prediction Output:</strong> 'LIKELY' or 'NOT likely' to purchase, along with confidence score.</li>
        <li><strong>App Feature:</strong> Interactive input fields, random sample generator, 3D floating UI, neon futuristic design, and detailed explanation cards.</li>
        <li><strong>Future Improvements:</strong> Include feature scaling, hyperparameter tuning, and more advanced models like Random Forest or XGBoost for higher accuracy.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ------------------------------ Footer ------------------------------
st.markdown("""
<div class="footer-neon">
Made with ❤️ by <strong>Siddhant patel </strong>
</div>
""", unsafe_allow_html=True)
