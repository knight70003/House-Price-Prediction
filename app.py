import streamlit as st
import pandas as pd
import joblib

# =========================
# Sklearn version compatibility fix
# =========================
import sklearn.compose._column_transformer as ct
if not hasattr(ct, '_RemainderColsList'):
    from sklearn.utils._set_output import _SetOutputMixin
    class _RemainderColsList(_SetOutputMixin, list):
        pass
    ct._RemainderColsList = _RemainderColsList

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="🏠 House Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Custom CSS - Attention Seeker Design
# =========================
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* Title Styling */
    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #00d9ff !important;
        text-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #00d9ff, 0 0 20px #00d9ff; }
        to { text-shadow: 0 0 20px #00d9ff, 0 0 30px #00d9ff, 0 0 40px #00d9ff; }
    }
    
    /* Card Styling */
    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Input Fields */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid #00d9ff !important;
        border-radius: 10px !important;
        color: #fff !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > div > div:focus {
        border-color: #ff00ff !important;
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.5) !important;
    }
    
    /* Labels */
    .stNumberInput label,
    .stSelectbox label {
        color: #00d9ff !important;
        font-weight: bold !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff00ff, #00d9ff) !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 15px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        color: white !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 25px rgba(255, 0, 255, 0.5) !important;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 35px rgba(255, 0, 255, 0.8) !important;
    }
    
    /* Success Message */
    .stSuccess {
        background: rgba(0, 255, 127, 0.2) !important;
        border: 2px solid #00ff7f !important;
        border-radius: 15px !important;
        padding: 20px !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Load Model & Columns
# =========================

pipeline = joblib.load('xgb_pipeline_new.pkl')
expected_columns = joblib.load('columns.pkl')


# =========================
# Sidebar - Feature Categories
# =========================
with st.sidebar:
    st.markdown("### 📊 Input Categories")
    st.markdown("---")
    
    # Create expandable sections
    with st.expander("🌍 Location", expanded=True):
        st.write("Geographic details")
    
    with st.expander("🏠 Property Details", expanded=True):
        st.write("Property characteristics")
    
    with st.expander("💰 Financial", expanded=True):
        st.write("Income & value")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("This AI model predicts house prices based on California housing dataset features.")

# =========================
# Main Content
# =========================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🏠 House Price Prediction")
    st.markdown("### Enter your property details below:")
    st.markdown("---")
    
    # Create input fields in a grid
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    
    # Location inputs
    with row1[0]:
        longitude = st.number_input("📍 Longitude", value=-122.23, format="%.4f",
                                   help="West is negative, East is positive")
    with row1[1]:
        latitude = st.number_input("📍 Latitude", value=37.88, format="%.4f",
                                  help="South is negative, North is positive")
    
    # Property age
    with row2[0]:
        housing_median_age = st.number_input("🏗️ Housing Median Age", value=41, min_value=1,
                                      help="Years since construction")
    with row2[1]:
        total_rooms = st.number_input("🚪 Total Rooms", value=880, min_value=1)
    
    # Room details
    with row3[0]:
        total_bedrooms = st.number_input("🛏️ Total Bedrooms", value=129, min_value=1)
    with row3[1]:
        population = st.number_input("👥 Population", value=322, min_value=1)
    
    # Household & income
    with row4[0]:
        households = st.number_input("🏠 Households", value=126, min_value=1)
    with row4[1]:
        median_income = st.number_input("💵 Median Income (×$10,000)", value=8.3252, min_value=0.0, 
                                     format="%.4f", help="In tens of thousands of dollars")
    
    # Ocean Proximity - Special input
    st.markdown("---")
    ocean_proximity = st.selectbox(
        "🌊 Ocean Proximity",
        ["<1H OCEAN", "INLAND", "ISLAND", "NEAR OCEAN", "NEAR BAY"],
        help="Proximity to the ocean"
    )
    
    st.markdown("---")
    
    # Predict Button
    if st.button("🔮 Predict House Price", use_container_width=True):
        # Create DataFrame with input data
        input_data = pd.DataFrame([[
            longitude, latitude, housing_median_age,
            total_rooms, total_bedrooms, population,
            households, median_income, ocean_proximity
        ]], columns=expected_columns[:9])
        
        # Feature engineering
        input_data["rooms_per_household"] = input_data["total_rooms"] / input_data["households"]
        input_data["bedrooms_per_room"] = input_data["total_bedrooms"] / input_data["total_rooms"]
        input_data["population_per_household"] = input_data["population"] / input_data["households"]
        
        # Make prediction
        prediction = pipeline.predict(input_data)[0]
        
        # Show result with animation
        st.markdown("---")
        st.markdown(f"""
        <div style="text-align: center; padding: 30px; background: rgba(0, 255, 127, 0.1); 
                    border-radius: 20px; border: 2px solid #00ff7f;">
            <h2 style="color: #00ff7f; margin-bottom: 10px;">🏡 Estimated House Price</h2>
            <h1 style="color: #00ff7f; font-size: 48px; text-shadow: 0 0 30px #00ff7f;">
                ${round(prediction, 2):,}
            </h1>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# Right Panel - Info Cards
# =========================
with col2:
    # Tips card
    st.markdown("""
    <div class="card">
        <h3 style="color: #00d9ff;">💡 Quick Tips</h3>
        <ul style="color: #fff;">
            <li>Higher income = Higher price</li>
            <li>Closer to ocean = Premium</li>
            <li>More rooms = Higher value</li>
            <li>Newer homes = Better price</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stats card
    st.markdown("""
    <div class="card">
        <h3 style="color: #ff00ff;">📈 Model Info</h3>
        <p style="color: #fff;">AI Model: XGBoost Pipeline</p>
        <p style="color: #fff;">Features: 12</p>
        <p style="color: #fff;">Dataset: California Housing</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.5);">
    <p>🏠 House Price Prediction App | Powered by XGBoost & Streamlit</p>
</div>
""", unsafe_allow_html=True)
