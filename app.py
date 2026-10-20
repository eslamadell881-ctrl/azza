import streamlit as st
import time
import base64
import os

# ==========================================
# 1. إعدادات الصفحة والتصميم مع إخفاء شريط GitHub
# ==========================================
st.set_page_config(page_title="إلى عزة... رسالة من القلب", page_icon="💌", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700&display=swap');

    /* إخفاء القائمة العلوية وشعار GitHub بالكامل */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}
    button[title="View source"] {display: none !important;}
    .stAppHeader {display: none !important;}

    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #1e1b4b 100%);
        color: #f3f4f6;
        font-family: 'Cairo', sans-serif;
    }
    
    .poem-box {
        font-family: 'Amiri', serif;
        font-size: 24px;
        line-height: 2.3;
        color: #f8fafc;
        text-align: center;
        direction: rtl;
        background: rgba(30, 41, 59, 0.85);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(244, 114, 182, 0.4);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .anim-box {
        position: relative;
        height: 320px;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    .heart-particle {
        position: absolute;
        font-size: 38px;
        animation: flyHearts 2.8s ease-in-out infinite;
    }

    @keyframes flyHearts {
        0% { transform: translateY(100px) scale(0.6); opacity: 0; }
        30% { opacity: 1; transform: translateY(20px) scale(1.2); }
        70% { opacity: 0.9; transform: translateY(-100px) scale(1); }
        100% { transform: translateY(-220px) scale(0.4); opacity: 0; }
    }

    .butterfly-particle {
        position: absolute;
        font-size: 42px;
        animation: flyButterflies 3.2s ease-in-out infinite;
        opacity: 0;
    }

    @keyframes flyButterflies {
        0% { transform: translateY(80px) translateX(-20px) scale(0.4); opacity: 0; }
        40% { opacity: 1; transform: translateY(-30px) translateX(30px) scale(1.1) rotate(15deg); }
        80% { opacity: 0.8; transform: translateY(-140px) translateX(-20px) scale(0.9) rotate(-15deg); }
        100% { transform: translateY(-240px) translateX(40px) scale(0.3); opacity: 0; }
    }

    .stButton>button {
        background: linear-gradient(135deg, #f472b6 0%, #db2777 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(219, 39, 119, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 25px rgba(219, 39, 119, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. دالة تشغيل الصوت في الخلفية بدون شريط
# ==========================================
def play_background_audio():
    audio_file = "music.mp3"
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
            <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)

# ==========================================
# 3. إدارة حالة التطبيق
# ==========================================
if "state" not in st.session_state:
    st.session_state.state = "closed"

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; font-family: \"Amiri\", serif; margin-top: 15px; color: #f472b6;'>إلى من يمتلكه القلب... عزة 🤍</h1>", unsafe_allow_html=True)

# ==========================================
# المرحلة الأولى: الجواب المغلق
# ==========================================
if st.session_state.state == "closed":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        with st.form("envelope_form"):
            st.markdown("""
            <div style="text-align: center; background: linear-gradient(135deg, #fbcfe8 0%, #f472b6 100%); padding: 45px 25px; border-radius: 24px; border: 3px solid #db2777; box-shadow: 0 20px 40px rgba(244, 114, 182, 0.4);">
                <span style="font-size: 80px;">💌</span>
                <h2 style="color: #831843 !important; margin-top: 10px; font-family: 'Amiri', serif; font-size: 28px;">رسالة خاصة جداً</h2>
                <p style="color: #831843; font-size: 18px; font-weight: bold; margin-bottom: 5px;">إلى حبيبتي عزة 🤍</p>
                <p style="color: #9d174d; font-size: 13px;">(اضغط الزر أدناه لفتح الجواب)</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.form_submit_button("✨ افتح الجواب وشاهد السحر ✨", use_container_width=True):
                st.session_state.state = "animating"
                st.rerun()

# ==========================================
# المرحلة الثانية: أنيميشن القلوب والفراشات
# ==========================================
elif st.session_state.state == "animating":
    play_background_audio()
    
    col_a1, col_a2, col_a3 = st.columns([1, 2.5, 1])
    with col_a2:
        anim_html = '<div class="anim-box"><div class="heart-particle" style="left:15%; animation-delay:0s;">💖</div><div class="heart-particle" style="left:35%; animation-delay:0.3s;">❤️</div><div class="heart-particle" style="left:55%; animation-delay:0.1s;">💗</div><div class="heart-particle" style="left:75%; animation-delay:0.5s;">💓</div><div class="butterfly-particle" style="left:20%; animation-delay:1.2s;">🦋</div><div class="butterfly-particle" style="left:45%; animation-delay:1.8s;">✨</div><div class="butterfly-particle" style="left:50%; animation-delay:1.5s;">🦋</div><div class="butterfly-particle" style="left:70%; animation-delay:2.1s;">🦋</div><div class="butterfly-particle" style="left:85%; animation-delay:2.5s;">✨</div></div>'
        st.markdown(anim_html, unsafe_allow_html=True)
    
    time.sleep(5.0)
    st.session_state.state = "opened"
    st.rerun()

# ==========================================
# المرحلة الثالثة: العرض النهائي (الصورة + الشعر)
# ==========================================
elif st.session_state.state == "opened":
    play_background_audio()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_img1, col_img2, col_img3 = st.columns([1, 1.6, 1])
    with col_img2:
        image_name = "azza.png" if os.path.exists("azza.png") else "image_3.png"
        if os.path.exists(image_name):
            st.image(image_name, caption="إلى أطهر وأغلى الناس.. عزة 🤍", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    poem_content = """
    وَفِي فَمِي مِنْ عَظِيمِ النَّدَمِ الْكَلَامُ<br>
    مَا كُنْتُ أَقْصِدُ أَنْ أُبْقِيَكَ فِي حَزَنٍ وَلَا أَرَدْتُ لِقَلْبِكَ لَحْظَةَ الْأَلَامِ<br><br>
    أَخْطَأْتُ، أَعْلَمُ أَنَّ الْعُذْرَ لَا يَمْحُو مَا قَدْ تَرَكْتُهُ فِي الرُّوحِ مِنْ سَقَمِ<br>
    لَكِنْ أَتَيْتُ، وَمَا فِي الْقَلْبِ مِنْ كِبَرٍ لِأَسْتَعِيدَ مِنَ الْأَيَّامِ مَا انْهَدَمَ<br><br>
    فَإِنْ عَفَوْتَ، فَذَاكَ الْعَفْوُ أَكْرَمَنِي<br>
    وَإِنْ أَبَيْتَ، سَأَحْتَرِمُ الَّذِي تَحْكُمُ<br><br>
    يَكْفِينِيَ الْيَوْمَ أَنِّي جِئْتُ مُعْتَذِرًا<br>
    فَالْحُبُّ أَصْدَقُ حِينَ يَصُونُهُ النَّدَمُ
    """
    
    st.markdown(f'<div class="poem-box">{poem_content}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
    with col_b2:
        if st.button("💌 إعادة التجربة", use_container_width=True):
            st.session_state.state = "closed"
            st.rerun()
