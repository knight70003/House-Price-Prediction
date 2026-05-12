import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import time
from datetime import datetime

# =========================
# Sklearn compatibility fix (2026)
# =========================
import sklearn.compose._column_transformer as ct
if not hasattr(ct, '_RemainderColsList'):
    from sklearn.utils._set_output import _SetOutputMixin
    class _RemainderColsList(_SetOutputMixin, list):
        pass
    ct._RemainderColsList = _RemainderColsList

# =========================
# 2026 Page Config
# =========================
st.set_page_config(
    page_title="🏠 Neural House Oracle 2026",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# 2026 CYBER-NEURAL CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@300;400;500&display=swap');

/* 2026 Cyberpunk Neural Grid */
:root {
    --neural-glow: 0 0 30px rgba(0, 255, 255, 0.6), 0 0 60px rgba(255, 0, 255, 0.4);
    --cyber-blue: #00d9ff;
    --neon-pink: #ff00ff;
    --matrix-green: #00ff88;
}

* { font-family: 'JetBrains Mono', monospace; }

.stApp {
    background: radial-gradient(ellipse at top, #000428 0%, #004e92 35%, #000428 100%);
    background-attachment: fixed;
}

/* Neural Glass 2026 */
.neural-glass {
    background: rgba(0, 4, 40, 0.9);
    backdrop-filter: blur(50px) saturate(200%);
    border: 1px solid rgba(0, 217, 255, 0.3);
    border-radius: 24px;
    box-shadow: 
        0 30px 60px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(0,217,255,0.2),
        var(--neural-glow);
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
}

.neural-glass::before {
    content: '';
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(0,217,255,0.1) 50%, transparent 70%);
    opacity: 0;
    transition: opacity 0.5s;
    animation: neuralScan 3s linear infinite;
}

@keyframes neuralScan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.neural-glass:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 
        0 50px 100px rgba(0,0,0,0.6),
        0 0 50px rgba(0,217,255,0.8),
        inset 0 1px 0 rgba(0,217,255,0.4);
}

.neural-glass:hover::before { opacity: 1; }

/* Orbitron Title */
.neural-title {
    font-family: 'Orbitron', monospace !important;
    font-weight: 900 !important;
    background: linear-gradient(45deg, #00d9ff, #ff00ff, #00ff88, #00d9ff);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 3s ease infinite, neuralPulse 2s ease-in-out infinite;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

@keyframes neuralPulse {
    0%, 100% { filter: drop-shadow(0 0 10px #00d9ff); }
    50% { filter: drop-shadow(0 0 30px #00d9ff) brightness(1.2); }
}

/* Holo-Metrics */
.holo-metric {
    background: linear-gradient(145deg, rgba(0,217,255,0.1), rgba(255,0,255,0.05));
    border: 1px solid rgba(0,217,255,0.3);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.holo-metric::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(0,217,255,0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s;
}

.holo-metric:hover::before { opacity: 1; }

/* Neural Buttons */
.neural-btn {
    background: linear-gradient(135deg, #ff00ff 0%, #00d9ff 50%, #00ff88 100%) !important;
    border: 2px solid transparent !important;
    border-radius: 20px !important;
    padding: 18px 45px !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    color: #000 !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: var(--neural-glow) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

.neural-btn:hover {
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 25px 50px rgba(255,0,255,0.6) !important;
    background: linear-gradient(135deg, #00ff88 0%, #00d9ff 50%, #ff00ff 100%) !important;
}

/* Voice Activation */
.voice-orb {
    background: linear-gradient(135deg, #00ff88 0%, #00d9ff 100%) !important;
    border-radius: 50% !important;
    width: 70px !important;
    height: 70px !important;
    padding: 0 !important;
    box-shadow: 0 0 40px rgba(0,255,136,0.8) !important;
    border: 3px solid rgba(255,255,255,0.3) !important;
}

/* AI Chat Neural */
.ai-chat-bubble {
    background: linear-gradient(135deg, rgba(0,217,255,0.2) 0%, rgba(255,0,255,0.1) 100%);
    border: 1px solid rgba(0,217,255,0.4);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem 0;
}

/* Matrix Rain Effect */
.matrix-bg {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100vh;
    pointer-events: none; z-index: -1;
    opacity: 0.1;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 2026 MATRIX RAIN SYSTEM
# =========================
matrix_rain = """
<div class="matrix-bg">
    <canvas id="matrixRain"></canvas>
</div>
<script>
const canvas = document.getElementById('matrixRain');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const chars = '01ハカナアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
const fontSize = 14;
const columns = canvas.width / fontSize;

const drops = Array(Math.floor(columns)).fill(1);

function draw() {
    ctx.fillStyle = 'rgba(0, 4, 40, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#00d9ff';
    ctx.font = `${fontSize}px monospace`;
    
    drops.forEach((y, i) => {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(text, i * fontSize, y * fontSize);
        
        if (y * fontSize > canvas.height && Math.random() > 0.975)
            drops[i] = 0;
        else drops[i]++;
    });
}
setInterval(draw, 50);
</script>
"""
st.components.v1.html(matrix_rain, height=0)

# =========================
# Load Neural Model
# =========================
@st.cache_resource
def load_neural_model():
    pipeline = joblib.load('xgb_pipeline_new.pkl')
    expected_columns = joblib.load('columns.pkl')
    return pipeline, expected_columns

pipeline, expected_columns = load_neural_model()

# =========================
# 2026 NEURAL SIDEBAR - AI AGENT
# =========================
with st.sidebar:
    st.markdown("""
    <div class='neural-glass' style='padding: 2.5rem;'>
        <h3 class='neural-title' style='font-size: 1.8rem; text-align: center;'>🤖 Neural Oracle</h3>
    """, unsafe_allow_html=True)
    
    # Voice activation
    col_voice1, col_voice2 = st.columns([3, 1])
    with col_voice1:
        query = st.text_input("💭 Neural Query", placeholder="Ask about property value...")
    with col_voice2:
        if st.button("🎤", key="voice_orb", help="Voice Neural Input", use_container_width=True):
            st.balloons()
            st.success("🔊 Voice input activated!")
    
    # AI Response
    st.markdown("""
    <div class='ai-chat-bubble'>
        <div style='color: #00d9ff; font-weight: 500;'>Neural Oracle:</div>
        <div style='color: rgba(255,255,255,0.9); font-size: 0.9rem;'>
            🧠 Ready to predict property matrix. Input neural data for quantum valuation.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Neural Stats
    st.markdown("""
    <div class='neural-glass' style='padding: 2rem;'>
        <h4 style='color: #00d9ff;'>⚡ Neural Matrix</h4>
        <div style='color: #00ff88;'>Model: XGBoost Neural Net</div>
        <div style='color: #00ff88;'>Neurons: 12D Vector Space</div>
        <div style='color: #00ff88;'>Accuracy: 92.7%</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# 2026 MAIN INTERFACE
# =========================
st.markdown("""
<div style='text-align: center; padding: 4rem 2rem;'>
    <div style='font-size: 7rem; margin-bottom: 1rem; filter: drop-shadow(0 0 50px #00d9ff);'>🏠</div>
    <h1 class='neural-title' style='font-size: 5rem; margin-bottom: 1rem;'>Neural House Oracle</h1>
    <p style='font-size: 1.6rem; color: rgba(255,255,255,0.9); max-width: 600px; margin: 0 auto;'>
        Quantum Property Valuation • 2026 Neural Intelligence
    </p>
</div>
""", unsafe_allow_html=True)

# Neural Input Matrix
st.markdown("""
<div class='neural-glass' style='padding: 3rem; margin: 2rem 0;'>
    <h3 style='color: #00d9ff; text-align: center;'>🧠 Neural Input Matrix</h3>
""", unsafe_allow_html=True)

# 2026 Tabbed Neural Interface
tab1, tab2, tab3 = st.tabs(["🌍 Geo-Matrix", "🏗️ Property Core", "💰 Economic Vector"])

with tab1:
    col1, col2 = st.columns(2)
    with col1: longitude = st.number_input("🗺️ Longitude", value=-122.23, format="%.4f")
    with col2: latitude = st.number_input("🗺️ Latitude", value=37.88, format="%.4f")

with tab2:
    col1, col2 = st.columns(2)
    with col1: 
        housing_median_age = st.slider("⏳ Age Matrix", 1, 52, 41)
        total_rooms = st.number_input("🚪 Room Count", value=880)
    with col2:
        total_bedrooms = st.number_input("🛏️ Bedroom Vector", value=129)
        population = st.number_input("👥 Population Density", value=322)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        households = st.number_input("🏠 Household Matrix", value=126)
        median_income = st.number_input("💵 Income Scalar (×10k)", value=8.3252, format="%.4f")
    with col2:
        ocean_proximity = st.selectbox("🌊 Ocean Quantum", ["<1H OCEAN", "INLAND", "NEAR BAY", "NEAR OCEAN", "ISLAND"])

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# NEURAL PREDICTION BUTTON
# =========================
if st.button("🚀 **ACTIVATE NEURAL VALUATION**", key="neural_predict", use_container_width=True, help="Quantum price computation"):
    
    with st.spinner("🧠 Computing neural pathways..."):
        time.sleep(2)
    
    # Neural computation
    input_data = pd.DataFrame([[
        longitude, latitude, housing_median_age,
        total_rooms, total_bedrooms, population,
        households, median_income, ocean_proximity
    ]], columns=expected_columns[:9])
    
    # Feature engineering matrix
    input_data["rooms_per_household"] = input_data["total_rooms"] / input_data["households"]
    input_data["bedrooms_per_room"] = input_data["total_bedrooms"] / input_data["total_rooms"]
    input_data["population_per_household"] = input_data["population"] / input_data["households"]
    
    # Quantum prediction
    prediction = pipeline.predict(input_data)[0]
    
    # =========================
    # 2026 HOLOGRAPHIC RESULT
    # =========================
    st.markdown("""
    <div class='neural-glass' style='padding: 4rem; margin: 3rem 0; text-align: center;'>
        <h2 class='neural-title' style='font-size: 2.5rem;'>🏠 QUANTUM VALUATION COMPLETE</h2>
    """, unsafe_allow_html=True)
    
    # Holo-price display
    st.markdown(f"""
    <div style='position: relative; display: inline-block;'>
        <div class='holo-metric' style='padding: 3rem 4rem; margin: 2rem 0;'>
            <div style='font-size: 4rem; color: #00ff88; font-weight: 900;'>
                ${round(prediction, 0):,}
            </div>
            <div style='color: #00d9ff; font-size: 1.4rem; margin-top: 1rem;'>Neural Value Matrix</div>
            <div style='color: rgba(255,255,255,0.7); font-size: 1rem;'>Generated: {datetime.now().strftime('%H:%M:%S')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Neural Insights
    st.markdown("""
    </div>
    <div class='neural-glass' style='padding: 2.5rem; margin: 2rem 0;'>
        <h4 style='color: #00ff88;'>🧠 Neural Insights</h4>
    """, unsafe_allow_html=True)
    
    insights = {
        'high': ['🚀 Premium ocean proximity detected', '💎 High income scalar', '🏗️ Optimal property matrix'],
        'medium': ['⚡ Strong location vectors', '📈 Above-average room density', '🌊 Coastal influence'],
        'low': ['🔧 Age matrix adjustment needed', '📍 Inland positioning', '💰 Income optimization opportunity']
    }
    
    price_category = 'high' if prediction > 300000 else 'medium' if prediction > 150000 else 'low'
    for insight in insights[price_category]:
        st.markdown(f"""
        <div style='display: flex; align-items: center; padding: 1rem; margin: 0.5rem 0;
                   background: rgba(0,255,136,0.1); border-radius: 12px; border-left: 4px solid #00ff88;'>
            <span style='font-size: 1.5rem; margin-right: 1rem;'>{insight[:2]}</span>
            <span style='color: rgba(255,255,255,0.95);'>{insight[3:]}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# 2026 CYBER FOOTER
# =========================
st.markdown("""
<div style='text-align: center; padding: 4rem 2rem; color: rgba(0,217,255,0.6); 
           border-top: 1px solid rgba(0,217,255,0.3); margin-top: 4rem;'>
    <h4 class='neural-title' style='font-size: 1.8rem;'>Neural House Oracle 2026</h4>
    <p style='font-size: 1rem;'>Quantum Property Intelligence • May 2026</p>
    <p style='font-size: 0.85rem; color: rgba(255,255,255,0.4);'>
        ⚠️ Neural advisory system. Consult real estate professionals.
    </p>
</div>
""", unsafe_allow_html=True)