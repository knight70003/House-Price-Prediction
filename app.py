import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
from datetime import datetime
import folium
from streamlit_folium import st_folium
import base64

# ==========================================
# 2026 QUANTUM HYPER-TERMINAL GOD-MODE v13.0
# ==========================================
st.set_page_config(
    page_title="🌌 ORACLE COGNITIVE TERMINAL v13.0",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hardware Accelerated Asset Encoders
@st.cache_data
def get_base64_image(img_path):
    try:
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

@st.cache_data
def get_base64_video(video_path):
    try:
        with open(video_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

bin_str = get_base64_image("bac.jpg")
process_video_b64 = get_base64_video("process.mp4")

# Initialize Session States for Dynamic Layout Control
if 'predicted' not in st.session_state: st.session_state.predicted = False
if 'valuation' not in st.session_state: st.session_state.valuation = 0.0
if 'cluster_id' not in st.session_state: st.session_state.cluster_id = 0
if 'clicked_lat' not in st.session_state: st.session_state.clicked_lat = 47.6062  
if 'clicked_long' not in st.session_state: st.session_state.clicked_long = -122.3321

# ==========================================
# HYPER-ATTRACTION INTEGRATED VISUAL ENGINE
# ==========================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400;700&display=swap');

* {{ font-family: 'JetBrains Mono', monospace; }}

.stApp {{
    background-image: linear-gradient(rgba(0, 5, 10, 0.40), rgba(0, 8, 4, 0.45)), url("data:image/jpeg;base64,{bin_str}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.neural-glass {{
    background: rgba(1, 12, 18, 0.35);
    backdrop-filter: blur(25px) saturate(280%);
    -webkit-backdrop-filter: blur(25px);
    border: 2px solid rgba(0, 255, 136, 0.4);
    border-radius: 24px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.85);
    padding: 2.2rem;
    margin-bottom: 1.5rem;
}}

div[data-testid="stMarkdownContainer"] p, label {{
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.95);
}}

button[data-baseweb="tab"] {{
    background: rgba(1, 15, 25, 0.6) !important;
    border: 1px solid rgba(0, 255, 136, 0.3) !important;
    border-radius: 10px 10px 0 0 !important;
    color: #00d9ff !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 900 !important;
}}

button[aria-selected="true"] {{
    background: rgba(0, 255, 136, 0.2) !important;
    border-color: #00ff88 !important;
    color: #ffffff !important;
    box-shadow: 0 0 15px rgba(0, 255, 136, 0.3);
}}

.neural-title {{
    font-family: 'Orbitron', monospace !important;
    font-weight: 900 !important;
    text-transform: uppercase;
    background: linear-gradient(90deg, #00ff88 0%, #00d9ff 25%, #ff00ff 50%, #ffff00 75%, #00ff88 100%);
    background-size: 400% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: chromaShift 5s linear infinite;
    letter-spacing: 7px;
}}

@keyframes chromaShift {{
    0% {{ background-position: 0% center; }}
    100% {{ background-position: 400% center; }}
}}

.holo-metric {{
    background: radial-gradient(circle at center, rgba(255, 0, 255, 0.25) 0%, rgba(0,4,8,0.98) 100%);
    border: 3px solid #ff00ff;
    border-radius: 28px;
    padding: 3.5rem 2rem;
    text-align: center;
    backdrop-filter: blur(25px);
    animation: hyperGlow 1.5s infinite alternate ease-in-out;
    max-width: 750px;
    margin: 2rem auto;
}}

.price-display {{
    font-size: 5rem; 
    color: #00ff88; 
    font-weight: 900; 
    font-family: 'Orbitron', sans-serif; 
    letter-spacing: 2px; 
    text-shadow: 0 0 45px rgba(0,255,136,0.9);
    white-space: nowrap;
}}

@keyframes hyperGlow {{
    0% {{ box-shadow: 0 0 40px rgba(0, 255, 136, 0.4); border-color: #00ff88; }}
    100% {{ box-shadow: 0 0 90px rgba(255, 0, 255, 0.7); border-color: #ff00ff; }}
}}

.stButton>button {{
    background: linear-gradient(45deg, #ff00ff 0%, #00d9ff 50%, #00ff88 100%) !important;
    background-size: 300% auto !important;
    color: #ffffff !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 900 !important;
    letter-spacing: 5px !important;
    border: none !important;
    border-radius: 20px !important;
    padding: 1.5rem 3.5rem !important;
    box-shadow: 0 0 50px rgba(0, 255, 136, 0.5) !important;
}}

div[data-baseweb="input"], div[data-baseweb="select"] {{
    background-color: rgba(0, 6, 12, 0.75) !important;
    border: 1px solid rgba(0, 255, 136, 0.4) !important;
    border-radius: 14px !important;
}}

.folium-pulsing-marker {{
    border: 3px solid #00ff88;
    background: rgba(0, 255, 136, 0.4);
    border-radius: 50%;
    animation: mapPulse 1.2s infinite ease-out;
}}
@keyframes mapPulse {{
    0% {{ transform: scale(0.3); opacity: 1; }}
    100% {{ transform: scale(1.5); opacity: 0; }}
}}
</style>
""", unsafe_allow_html=True)

# Particle Background Engine
st.markdown("""
<canvas id="neuralParticles" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; pointer-events: none;"></canvas>
<script>
const canvas = document.getElementById('neuralParticles'); const ctx = canvas.getContext('2d'); let particles = [];
function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; } window.addEventListener('resize', resize); resize();
class Particle {
    constructor() { this.x = Math.random() * canvas.width; this.y = Math.random() * canvas.height; this.vx = (Math.random() - 0.5) * 0.8; this.vy = (Math.random() - 0.5) * 0.8; this.radius = Math.random() * 2 + 1; }
    update() { this.x += this.vx; this.y += this.vy; if(this.x < 0 || this.x > canvas.width) this.vx *= -1; if(this.y < 0 || this.y > canvas.height) this.vy *= -1; }
    draw() { ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2); ctx.fillStyle = 'rgba(0, 255, 136, 0.2)'; ctx.fill(); }
}
for(let i=0; i<60; i++) particles.push(new Particle());
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); particles.forEach(p => { p.update(); p.draw(); });
    for(let i=0; i<particles.length; i++) {
        for(let j=i+1; j<particles.length; j++) {
            let dx = particles[i].x - particles[j].x; let dy = particles[i].y - particles[j].y; let dist = Math.sqrt(dx*dx + dy*dy);
            if(dist < 120) { ctx.beginPath(); ctx.moveTo(particles[i].x, particles[i].y); ctx.lineTo(particles[j].x, particles[j].y); ctx.strokeStyle = `rgba(0, 217, 255, ${0.15 - dist/120})`; ctx.lineWidth = 0.5; ctx.stroke(); }
        }
    }
    requestAnimationFrame(animate);
}
animate();
</script>
""", unsafe_allow_html=True)

def render_smooth_overlay(b64_video_data, fixed_heading):
    return f'''
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0, 4, 8, 0.88); backdrop-filter: blur(20px); z-index: 999999; display: flex; justify-content: center; align-items: center;">
        <div style="background: rgba(1, 15, 24, 0.96); border: 3px solid #ff00ff; box-shadow: 0 0 90px rgba(255, 0, 255, 0.7); padding: 35px; border-radius: 32px; text-align: center; max-width: 600px; width: 90%;">
            <div style="color: #00d9ff; font-family: 'Orbitron', monospace; font-size: 1.4rem; font-weight: 900; letter-spacing: 4px; margin-bottom: 25px;">
                ⚡ {fixed_heading}
            </div>
            <video width="100%" autoplay loop muted playsinline style="border-radius: 20px; max-height: 300px; object-fit: cover; border: 2px solid rgba(0,217,255,0.4);">
                <source src="data:video/mp4;base64,{b64_video_data}" type="video/mp4">
            </video>
        </div>
    </div>
    '''

# =========================
# PRODUCTION FILE IMPORTS
# =========================
@st.cache_resource
def load_production_pipeline():
    with open("kc_house_model.pkl", "rb") as f:
        return pickle.load(f)

data_bundle = load_production_pipeline()
model = data_bundle["model"]
kmeans = data_bundle["kmeans"]
training_columns = data_bundle["training_columns"]

# Master Header Title
st.markdown("""
<div style='text-align: center; margin-top: 1rem; margin-bottom: 2rem;'>
    <h1 class='neural-title' style='font-size: 4.6rem; letter-spacing: 9px;'>ORACLE PREDICTION TERMINAL</h1>
Infinite Multiverse Quantum Core Array
</div>
""", unsafe_allow_html=True)

video_placeholder = st.empty()

# ==========================================
# CONDITION 1: IF PREDICTION IS NOT DONE (SHOW INPUT TERMINALS)
# ==========================================
if not st.session_state.predicted:

    main_col1, main_col2 = st.columns([1.1, 0.9])

    with main_col1:
        st.markdown("<div class='neural-glass' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00ff88; font-family:Orbitron; margin-top:0; letter-spacing:2px;'>📍 GEOSPATIAL VECTOR INTERCEPT</h3>", unsafe_allow_html=True)
        m = folium.Map(location=[st.session_state.clicked_lat, st.session_state.clicked_long], zoom_start=10, tiles="CartoDB dark_matter")

        # Click marker (pulsing)
        folium.Marker(
            [st.session_state.clicked_lat, st.session_state.clicked_long],
            icon=folium.DivIcon(html=f'<div class="folium-pulsing-marker" style="width:24px; height:24px;"></div>')
        ).add_to(m)

        # Pointer/crosshair overlay to make it feel like a real map pointer
        # (client-side only; works inside Folium iframe)
        m.get_root().html.add_child(
            folium.Element(
                """
                <style>
                  .bbai-crosshair {
                    position: absolute;
                    pointer-events: none;
                    z-index: 9999;
                    display: none;
                  }
                  .bbai-crosshair .dot {
                    width: 10px;
                    height: 10px;
                    border: 2px solid rgba(0,255,136,0.9);
                    border-radius: 50%;
                    background: rgba(0,255,136,0.25);
                    box-shadow: 0 0 18px rgba(0,255,136,0.5);
                    transform: translate(-50%, -50%);
                    position: absolute;
                    left: 0; top: 0;
                  }
                  .bbai-crosshair .hline, .bbai-crosshair .vline {
                    position: absolute;
                    background: rgba(0,217,255,0.75);
                    box-shadow: 0 0 16px rgba(0,217,255,0.45);
                  }
                  .bbai-crosshair .hline {
                    width: 18px;
                    height: 2px;
                    left: -9px;
                    top: -1px;
                  }
                  .bbai-crosshair .vline {
                    width: 2px;
                    height: 18px;
                    left: -1px;
                    top: -9px;
                  }
                  .bbai-pointer-label {
                    position: absolute;
                    transform: translate(-50%, calc(-100% - 10px));
                    pointer-events: none;
                    z-index: 99999;
                    display: none;
                    white-space: nowrap;
                    padding: 6px 10px;
                    border-radius: 12px;
                    background: rgba(0, 6, 12, 0.65);
                    border: 1px solid rgba(0, 255, 136, 0.35);
                    color: #00d9ff;
                    font-family: 'JetBrains Mono', monospace;
                    font-weight: 800;
                    letter-spacing: 0.5px;
                    font-size: 12px;
                    box-shadow: 0 0 40px rgba(0,255,136,0.12);
                  }
                </style>

                <div class="bbai-crosshair" id="bbaiCrosshair">
                  <div class="dot"></div>
                  <div class="hline"></div>
                  <div class="vline"></div>
                </div>
                <div class="bbai-pointer-label" id="bbaiPointerLabel"></div>

                <script>
                  (function(){
                    const mapRoot = document.currentScript && document.currentScript.parentElement ? document.currentScript.parentElement : null;
                    const iframe = window.frameElement;
                    // Folium creates a div.leaflet-map-pane inside its iframe; safest to use document.
                    const crosshair = document.getElementById('bbaiCrosshair');
                    const label = document.getElementById('bbaiPointerLabel');
                    if(!crosshair || !label) return;

                    // Find the leaflet container
                    const leafletContainer = document.querySelector('.leaflet-container');
                    const moveTarget = leafletContainer || document.body;
                    if(!moveTarget) return;

                    function setXY(clientX, clientY){
                      const rect = moveTarget.getBoundingClientRect();
                      crosshair.style.left = (clientX - rect.left) + 'px';
                      crosshair.style.top = (clientY - rect.top) + 'px';
                      label.style.left = (clientX - rect.left) + 'px';
                      label.style.top = (clientY - rect.top) + 'px';
                    }

                    moveTarget.addEventListener('mousemove', function(e){
                      crosshair.style.display = 'block';
                      label.style.display = 'block';
                      setXY(e.clientX, e.clientY);
                      // LatLng from leaflet if available
                      const ll = (typeof window.L !== 'undefined' && leafletContainer && leafletContainer._leaflet_map && leafletContainer._leaflet_map.mouseEventToLatLng)
                        ? leafletContainer._leaflet_map.mouseEventToLatLng(e)
                        : null;
                      if(ll && ll.lat != null && ll.lng != null){
                        label.textContent = 'LAT ' + ll.lat.toFixed(4) + ' , LNG ' + ll.lng.toFixed(4);
                      } else {
                        label.textContent = 'SELECT NODE';
                      }
                    });

                    moveTarget.addEventListener('mouseout', function(){
                      crosshair.style.display = 'none';
                      label.style.display = 'none';
                    });

                    // Hide label when clicking for cleaner feel
                    moveTarget.addEventListener('mousedown', function(){
                      // keep crosshair; label stays
                    });
                  })();
                </script>
                """
            )
        )


        map_data = st_folium(m, width="100%", height=370, key="infinite_god_map", returned_objects=["last_clicked"])


        # Robust coordinate extraction (folium/streamlit wrappers me key names vary ho sakte hain)
        if map_data and map_data.get("last_clicked"):
            clicked = map_data["last_clicked"]
            if isinstance(clicked, dict):
                new_lat = clicked.get("lat", clicked.get("latitude"))
                new_long = clicked.get("lng", clicked.get("longitude"))
            else:
                new_lat = None
                new_long = None

            if new_lat is not None and new_long is not None:
                # float conversion safety
                try:
                    new_lat = float(new_lat)
                    new_long = float(new_long)
                except Exception:
                    new_lat = None
                    new_long = None

            if new_lat is not None and new_long is not None:
                if abs(new_lat - st.session_state.clicked_lat) > 0.0001 or abs(new_long - st.session_state.clicked_long) > 0.0001:
                    st.session_state.clicked_lat = new_lat
                    st.session_state.clicked_long = new_long
                    st.rerun()

        c1, c2, c3 = st.columns(3)
        with c1: lat_input = st.number_input("GEOGRAPHIC LAT 🌐", value=st.session_state.clicked_lat, format="%.5f")
        with c2: long_input = st.number_input("GEOGRAPHIC LONG 🌐", value=st.session_state.clicked_long, format="%.5f")
        with c3: zipcode = st.text_input("📮 LOCATION ZIPCODE", "98103")
        
        if lat_input != st.session_state.clicked_lat or long_input != st.session_state.clicked_long:
            st.session_state.clicked_lat = lat_input
            st.session_state.clicked_long = long_input
            st.rerun()
            
        st.markdown("</div>", unsafe_allow_html=True)

    with main_col2:
        st.markdown("<div class='neural-glass'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00d9ff; font-family:Orbitron; margin-top:0; letter-spacing:2px;'>🏗️ STRUCTURAL ATTRIBUTE CORE</h3>", unsafe_allow_html=True)
        
        tab_core, tab_premium = st.tabs(["DIMENSION VECTORS", "PREMIUM SCALARS"])
        
        with tab_core:
            sqft_living = st.number_input("📐 Interior Space (Sqft Living)", value=2300, min_value=300)
            sqft_lot = st.number_input("🟩 Outer Plot Footprint (Sqft Lot)", value=7000, min_value=500)
            bedrooms = st.slider("🛏️ Structural Bedroom Matrix", 1, 8, 3)
            bathrooms = st.slider("🚿 Bathroom Capacity", 1.0, 6.0, 2.5, step=0.25)
            floors = st.slider("🏢 Floor Elevation Levels", 1.0, 3.5, 2.0, step=0.5)
            
        with tab_premium:
            grade = st.slider("🛠️ Materials & Architectural Grade", 1, 13, 8)
            condition = st.slider("🔧 Maintenance Reliability Index", 1, 5, 4)
            yr_built = st.number_input("⏳ Epoch Constructed (Year)", min_value=1900, max_value=2026, value=2000)
            yr_renovated = st.number_input("🔨 Modernization Loop Cycle", min_value=0, max_value=2026, value=0)
            view = st.slider("👁️ Panoramic Topography View", 0, 4, 0)
            waterfront = st.selectbox("🌊 Waterfront Riparian Proximity", [0, 1], format_func=lambda x: "ACTIVE PREMIUM NODE" if x==1 else "STANDARD MATRIX")
            
        st.markdown("</div>", unsafe_allow_html=True)

    # Trigger ML Compute Execution
    st.markdown("<div style='text-align: center; margin-top:1rem;'>", unsafe_allow_html=True)
    if st.button("⚡ EXECUTE NEURAL HOUSE PRICE INFERENCE", key="compute_btn", use_container_width=True):
        
        fixed_title = "EXECUTING REAL ESTATE VALUATION CORE..."
        for i in range(5):
            video_html = render_smooth_overlay(process_video_b64, fixed_title)
            video_placeholder.html(video_html)
            time.sleep(1.0)
            
        input_matrix = {
            'bedrooms': bedrooms, 'bathrooms': bathrooms, 'sqft_living': sqft_living, 'sqft_lot': max(sqft_lot, 1),
            'floors': floors, 'waterfront': waterfront, 'view': view, 'condition': condition, 'grade': grade,
            'sqft_above': sqft_living, 'sqft_basement': 0, 'sqft_living15': sqft_living, 'sqft_lot15': sqft_lot,
            'lat': st.session_state.clicked_lat, 'long': st.session_state.clicked_long,
            'house_age': 2026 - yr_built, 'is_renovated': 1 if yr_renovated > 0 else 0,
            'grade_squared': grade ** 2, 'living_per_lot': sqft_living / (sqft_lot + 1),
            'sqft_living_log': np.log1p(sqft_living), 'premium_view': waterfront * 3 + view
        }
        
        df_user = pd.DataFrame([input_matrix])
        st.session_state.cluster_id = kmeans.predict(df_user[['lat', 'long']])[0]
        df_user['location_cluster'] = str(st.session_state.cluster_id)
        df_user['zipcode'] = str(zipcode)
        
        df_user_encoded = pd.get_dummies(df_user)
        for col in training_columns:
            if col not in df_user_encoded.columns: df_user_encoded[col] = 0
        df_user_encoded = df_user_encoded[training_columns]
        
        predicted_log = model.predict(df_user_encoded)
        st.session_state.valuation = np.expm1(predicted_log)[0]
        
        # Change state & clean overlay
        st.session_state.predicted = True
        video_placeholder.empty()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================                       
# CONDITION 2: DIRECT PRICE INTERFACE DISPLAY (NO SCROLL!)
# ==========================================                 
else:
    st.markdown("<div class='neural-glass' style='max-width:900px; margin: 0 auto; text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h2 class='neural-title' style='font-size: 2.3rem;'>🛰️ PREDICTION RESOLVED SUCCESSFULLY</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='holo-metric'>
            <div class='price-display'>
                ${st.session_state.valuation:,.2f}
            </div>
            <div style='color: #00d9ff; font-size: 1.2rem; text-transform: uppercase; margin-top: 20px; font-family:Orbitron; letter-spacing:3px;'>Computed Property Valuation Core</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#00ff88; text-align:left; font-family:Orbitron; letter-spacing:1px; margin-top:2rem;'>📊 QUANTUM DATA ENGINE METRICS:</h4>", unsafe_allow_html=True)
    
    metrics_df = pd.DataFrame({
        "Mathematical Valuation Channel": ["Geospatial Cluster Node Path", "Environmental Coordinates Select"],
        "Vector Weights Evaluated": [f"Cluster Sector Location Code: -> [ {st.session_state.cluster_id} ]", f"Lat/Long: -> [ {st.session_state.clicked_lat:.4f}, {st.session_state.clicked_long:.4f} ]"]
    })
    st.table(metrics_df)
    
    st.write("")
    if st.button("🔄 RUN NEW VALUATION MODEL", use_container_width=True):
        st.session_state.predicted = False
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
