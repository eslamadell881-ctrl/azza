import streamlit as st
import time
import base64
import os

# إعدادات الصفحة والتجاوب
st.set_page_config(
    page_title="إلى من يمتلكه القلب... عزة 🤍",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# دالة لتشغيل الصوت في الخلفية بدون ظهور شريط التحكم وبشكل متكرر
def play_background_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64_audio = base64.b64encode(data).decode()
            audio_html = f"""
            <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)

# الأستايل والتصاميم البصرية الخرافية (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700&display=swap');

    /* خلفية فاخرة */
    .stApp {
        background: radial-gradient(circle at center, #1e112a 0%, #0a0512 100%);
        color: #f3f4f6;
        font-family: 'Cairo', sans-serif;
        overflow-x: hidden;
    }

    /* العنوان الرئيسي */
    .main-title {
        text-align: center;
        font-family: 'Amiri', serif;
        font-size: 2.8rem;
        color: #f472b6;
        text-shadow: 0 0 20px rgba(244, 114, 182, 0.6);
        margin-top: 10px;
        margin-bottom: 25px;
    }

    /* الجواب السحري */
    .envelope-card {
        background: linear-gradient(135deg, #f472b6 0%, #db2777 100%);
        padding: 45px 25px;
        border-radius: 24px;
        border: 2px solid #fbcfe8;
        box-shadow: 0 20px 50px rgba(219, 39, 119, 0.5);
        text-align: center;
        cursor: pointer;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    
    .envelope-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 60px rgba(244, 114, 182, 0.7);
    }

    /* أنيميشن تحول القلوب إلى فراشات */
    .magic-stage {
        position: relative;
        height: 380px;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* القلوب المتصاعدة */
    .heart-particle {
        position: absolute;
        font-size: 2.5rem;
        animation: floatHeart 3s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(244, 114, 182, 0.8));
    }

    @keyframes floatHeart {
        0% { transform: translateY(120px) scale(0.4) rotate(0deg); opacity: 0; }
        30% { opacity: 1; transform: translateY(0px) scale(1.2) rotate(10deg); }
        70% { opacity: 0.8; transform: translateY(-120px) scale(1) rotate(-10deg); }
        100% { transform: translateY(-220px) scale(0.2) rotate(15deg); opacity: 0; }
    }

    /* الفراشات المتحركة الساحرة */
    .butterfly-particle {
        position: absolute;
        font-size: 3rem;
        animation: flyButterfly 4s ease-in-out infinite;
        filter: drop-shadow(0 0 15px rgba(168, 85, 247, 0.9));
        opacity: 0;
    }

    @keyframes flyButterfly {
        0% { transform: translateY(80px) translateX(-40px) scale(0.3) rotate(-15deg); opacity: 0; }
        40% { opacity: 1; transform: translateY(-60px) translateX(30px) scale(1.1) rotate(15deg); }
        70% { opacity: 0.9; transform: translateY(-160px) translateX(-20px) scale(1) rotate(-10deg); }
        100% { transform: translateY(-280px) translateX(50px) scale(0.5) rotate(20deg); opacity: 0; }
    }

    /* نص القصيدة الاعتذارية */
    .poem-box {
        font-family: 'Amiri', serif;
        font-size: 1.5rem;
        line-height: 2.4;
        color: #fff;
        text-align: center;
        direction: rtl;
        background: rgba(23, 15, 38, 0.85);
        padding: 40px 25px;
        border-radius: 24px;
        border: 1px solid rgba(244, 114, 182, 0.4);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.8), inset 0 0 15px rgba(244, 114, 182, 0.15);
        backdrop-filter: blur(10px);
        animation: fadeIn 2s ease-in-out;
        margin-top: 25px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* تخصيص زِر الاستمرار والفتح */
    .stButton>button {
        background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 100%) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        padding: 14px 28px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(236, 72, 153, 0.4) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 15px 35px rgba(236, 72, 153, 0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# تهيئة حالة التطبيق
if "app_state" not in st.session_state:
    st.session_state.app_state = "closed"

# العنوان الرئيسي
st.markdown('<div class="main-title">إلى من يمتلكه القلب... عزة 🤍</div>', unsafe_allow_html=True)

# 1. المرحلة الأولى: الجواب المغلق
if st.session_state.app_state == "closed":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="envelope-card">
            <div style="font-size: 80px; margin-bottom: 10px;">💌</div>
            <h2 style="color: #ffffff; font-family: 'Amiri', serif; margin: 0; font-size: 2rem;">رسالة خاصة جداً</h2>
            <p style="color: #fbcfe8; font-size: 1.1rem; margin-top: 8px; font-weight: 600;">إلى حبيبتي عزة 🤍</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✨ افتحي الجواب لتبدأ الموسيقى والسحر ✨", use_container_width=True):
            st.session_state.app_state = "animating"
            st.rerun()

# 2. المرحلة الثانية: أنيميشن تحول القلوب إلى فراشات والموسيقى تعمل
elif st.session_state.app_state == "animating":
    # تشغيل ملف الموسيقى في الخلفية بدون إظهار أي لاعب صوتي وبدون توقف
    play_background_audio("music.mp3")

    # عرض أنيميشن طيران القلوب والفراشات
    st.markdown("""
    <div class="magic-stage">
        <!-- القلوب المتحركة -->
        <div class="heart-particle" style="left: 15%; animation-delay: 0s;">💖</div>
        <div class="heart-particle" style="left: 35%; animation-delay: 0.5s;">💗</div>
        <div class="heart-particle" style="left: 55%; animation-delay: 0.2s;">❤️</div>
        <div class="heart-particle" style="left: 75%; animation-delay: 0.7s;">💓</div>
        
        <!-- الفراشات الساحرة -->
        <div class="butterfly-particle" style="left: 20%; animation-delay: 1.2s;">🦋</div>
        <div class="butterfly-particle" style="left: 45%; animation-delay: 1.8s;">✨</div>
        <div class="butterfly-particle" style="left: 50%; animation-delay: 1.5s;">🦋</div>
        <div class="butterfly-particle" style="left: 70%; animation-delay: 2.1s;">🦋</div>
        <div class="butterfly-particle" style="left: 85%; animation-delay: 2.5s;">✨</div>
    </div>
    """, unsafe_allow_html=True)

    # وقت الانتظار لعرض السحر كاملاً (5 ثوانٍ)
    time.sleep(5.0)
    st.session_state.app_state = "opened"
    st.rerun()

# 3. المرحلة الثالثة: عرض صورة الرسمة والقصيدة الرومانسية
elif st.session_state.app_state == "opened":
    # استمرار الموسيقى في الخلفية دون انقطاع
    play_background_audio("music.mp3")

    col_img1, col_img2, col_img3 = st.columns([1, 2.2, 1])
    with col_img2:
        # عرض صورة الرسمة المرفوعة
        if os.path.exists("azza.png"):
            st.image("azza.png", caption="إلى أطهر وأغلى الناس.. عزة 🤍", use_container_width=True)
        elif os.path.exists("image_3.png"):
            st.image("image_3.png", caption="إلى أطهر وأغلى الناس.. عزة 🤍", use_container_width=True)
        else:
            st.warning("يرجى التأكد من رفع صورة الرسمة باسم azza.png في المستودع.")

    # أبيات الشعر المصممة بأسلوب فاخر
    poem_text = """
    وَفِي فَمِي مِنْ عَظِيمِ النَّدَمِ الْكَلَامُ<br>
    مَا كُنْتُ أَقْصِدُ أَنْ أُبْقِيَكَ فِي حَزَنٍ وَلَا أَرَدْتُ لِقَلْبِكَ لَحْظَةَ الْأَلَامِ<br><br>
    أَخْطَأْتُ، أَعْلَمُ أَنَّ الْعُذْرَ لَا يَمْحُو مَا قَدْ تَرَكْتُهُ فِي الرُّوحِ مِنْ سَقَمِ<br>
    لَكِنْ أَتَيْتُ، وَمَا فِي الْقَلْبِ مِنْ كِبَرٍ لِأَسْتَعِيدَ مِنَ الْأَيَّامِ مَا انْهَدَمَ<br><br>
    فَإِنْ عَفَوْتَ، فَذَاكَ الْعَفْوُ أَكْرَمَنِي<br>
    وَإِنْ أَبَيْتَ، سَأَحْتَرِمُ الَّذِي تَحْكُمُ<br><br>
    يَكْفِينِيَ الْيَوْمَ أَنِّي جِئْتُ مُعْتَذِرًا<br>
    فَالْحُبُّ أَصْدَقُ حِينَ يَصُونُهُ النَّدَمُ
    """
    
    st.markdown(f'<div class="poem-box">{poem_text}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
    with col_b2:
        if st.button("💌 إغلاق الرسالة وإعادة العرض", use_container_width=True):
            st.session_state.app_state = "closed"
            st.rerun()
