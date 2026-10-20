import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="إلى عزة... رسالة اعتذار من القلب", page_icon="💌", layout="centered")

# تصميم الواجهة والتأثيرات الخرافية والخط العربي
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0f19 1e1b4b 100%, #1e1b4b 100%);
        color: #f3f4f6;
        font-family: 'Cairo', sans-serif;
    }
    
    .poem-text {
        font-family: 'Amiri', serif;
        font-size: 23px;
        line-height: 2.3;
        color: #f8fafc;
        text-align: center;
        direction: rtl;
        background: rgba(30, 41, 59, 0.85);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(244, 114, 182, 0.4);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
    }
    
    .real-envelope {
        background: linear-gradient(135deg, #fbcfe8 0%, #f472b6 100%);
        padding: 50px 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(244, 114, 182, 0.4);
        max-width: 480px;
        margin: 60px auto;
        border: 2px solid #db2777;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .real-envelope:hover {
        transform: scale(1.03);
        box-shadow: 0 25px 50px rgba(244, 114, 182, 0.6);
    }
    
    h2 {
        color: #831843 !important;
        font-family: 'Amiri', serif;
    }
</style>
""", unsafe_allow_html=True)

# إدارة حالات التفاعل
if "state" not in st.session_state:
    st.session_state.state = "closed" # closed, loading, opened

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; font-family: 'Amiri', serif; margin-top: 20px; color: #f472b6;'>إلى من يمتلكه القلب... عزة 🤍</h1>", unsafe_allow_html=True)

# المرحلة الأولى: الجواب المغلق الواقعي
if st.session_state.state == "closed":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.6, 1])
    with col2:
        # استخدام زر شفاف يغطي شكل الجواب لتنفيذ اللمس
        with st.form("envelope_form"):
            st.markdown("""
            <div style="text-align: center;">
                <span style="font-size: 75px;">💌</span>
                <h2 style="color: #831843 !important; margin-top: 10px;">رسالة خاصة جداً</h2>
                <p style="color: #831843; font-size: 15px; font-weight: bold;">إلى حبيبتي عزة 🤍</p>
                <p style="color: #9d174d; font-size: 13px; margin-top: 10px;">(اضغط في أي مكان على الجواب لفتحه وتكسير الختم)</p>
            </div>
            """, unsafe_allow_html=True)
            
            clicked = st.form_submit_button("✨ افتح الجواب الآن ✨", use_container_width=True)
            if clicked:
                st.session_state.state = "loading"
                st.rerun()

# المرحلة الثانية: تأثير التحميل لمدة 5 ثوانٍ (قلوب تتحول لفراشات)
elif st.session_state.state == "loading":
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        load_text = st.empty()
        load_text.markdown("<h3 style='text-align: center; color: #f472b6;'>💖 جارِ كسر الختم وتطير القلوب لعيون عزة...</h3>", unsafe_allow_html=True)
        
        # محاكاة التايمر لمدة 5 ثوانٍ مع رسوم تعبيرية متحركة للقلوب والفراشات
        time.sleep(1.5)
        load_text.markdown("<h3 style='text-align: center; color: #f472b6;'>🦋 القلوب تتحول إلى فراشات تملأ الكون شوقاً...</h3>", unsafe_allow_html=True)
        time.sleep(2.0)
        load_text.markdown("<h3 style='text-align: center; color: #f472b6;'>✨ افتح قلبك الآن... الرسالة تنتظرك ✨</h3>", unsafe_allow_html=True)
        time.sleep(1.5)
        
        st.session_state.state = "opened"
        st.rerun()

# المرحلة الثالثة: عرض صورة البنت والقصيدة بعد الفتح
elif st.session_state.state == "opened":
    st.markdown("<br>", unsafe_allow_html=True)
    
    # عرض صورة البنت (يمكنك رفع صورتك المرفوعة على GitHub أو استخدام رابطها المباشر)
    # ملاحظة: استبدل الرابط أدناه برابط صورتك الحقيقية لو رفعتها على المستودع
    girl_image_url = "https://raw.githubusercontent.com/username/repository/main/your_image_filename.jpg" # أو رابط مباشر
    
    col_img1, col_img2, col_img3 = st.columns([1, 1.5, 1])
    with col_img2:
        # عرض صورة البنت بجودة عالية
        st.image("azza.png", caption="إلى أطهر وأغلى الناس.. عزة 🤍", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # القصيدة بخط عربي فخم (Amiri)
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
    
    st.markdown(f'<div class="poem-text">{poem_content}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
    with col_b2:
        if st.button("💌 إغلاق الرسالة وإعادة التجربة", use_container_width=True):
            st.session_state.state = "closed"
            st.rerun()
