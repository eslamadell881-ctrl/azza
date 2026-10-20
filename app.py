import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="إلى عزة... رسالة من القلب", page_icon="💌", layout="centered")

# تصميم الأنيماشن الخرافي للقلوب والفراشات والجواب
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #1e1b4b 100%);
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
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* أنيماشن تطاير القلوب والفراشات */
    .animation-container {
        position: relative;
        height: 350px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    .floating-heart {
        position: absolute;
        font-size: 30px;
        animation: floatUpHearts 2.5s ease-in-out infinite;
    }

    @keyframes floatUpHearts {
        0% { transform: translateY(0px) scale(0.8); opacity: 1; }
        50% { transform: translateY(-120px) scale(1.3) rotate(15deg); opacity: 0.8; }
        100% { transform: translateY(-250px) scale(0.5); opacity: 0; }
    }

    .floating-butterfly {
        position: absolute;
        font-size: 35px;
        animation: floatButterflies 3s ease-in-out infinite;
        opacity: 0;
    }

    @keyframes floatButterflies {
        0% { transform: translateY(-50px) translateX(0px) scale(0.5); opacity: 0; }
        30% { opacity: 1; }
        100% { transform: translateY(-280px) translateX(80px) scale(1.2) rotate(-20deg); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# إدارة الحالات
if "state" not in st.session_state:
    st.session_state.state = "closed"

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; font-family: 'Amiri', serif; margin-top: 20px; color: #f472b6;'>إلى من يمتلكه القلب... عزة 🤍</h1>", unsafe_allow_html=True)

# المرحلة الأولى: الجواب المغلق
if st.session_state.state == "closed":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.6, 1])
    with col2:
        with st.form("envelope_form"):
            st.markdown("""
            <div style="text-align: center; background: linear-gradient(135deg, #fbcfe8 0%, #f472b6 100%); padding: 50px 30px; border-radius: 20px; border: 2px solid #db2777; box-shadow: 0 20px 40px rgba(244, 114, 182, 0.4);">
                <span style="font-size: 75px;">💌</span>
                <h2 style="color: #831843 !important; margin-top: 10px; font-family: 'Amiri', serif;">رسالة خاصة جداً</h2>
                <p style="color: #831843; font-size: 16px; font-weight: bold;">إلى حبيبتي عزة 🤍</p>
                <p style="color: #9d174d; font-size: 13px; margin-top: 10px;">(اضغط الزر أدناه لبدء السحر الأنيماشن)</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.form_submit_button("✨ افتح الجواب وشاهد السحر ✨", use_container_width=True):
                st.session_state.state = "animating"
                st.rerun()

# المرحلة الثانية: أنيماشن تفاعل القلوب والفراشات الحية (لمدة 5 ثوانٍ تلقائياً)
elif st.session_state.state == "animating":
    col_a1, col_a2, col_a3 = st.columns([1, 2, 1])
    with col_a2:
        st.markdown("""
        <div class="animation-container">
            <div class="floating-heart" style="left: 20%; animation-delay: 0s;">💖</div>
            <div class="floating-heart" style="left: 40%; animation-delay: 0.4s;">❤️</div>
            <div class="floating-heart" style="left: 60%; animation-delay: 0.2s;">💗</div>
            <div class="floating-heart" style="left: 80%; animation-delay: 0.6s;">💓</div>
            
            <div class="floating-butterfly" style="left: 30%; animation-delay: 1.5s;">🦋</div>
            <div class="floating-butterfly" style="left: 50%; animation-delay: 2.0s;">🦋</div>
            <div class="floating-butterfly" style="left: 70%; animation-delay: 1.8s;">🦋</div>
        </div>
        """, unsafe_allow_html=True)
    
    # الانتظار لمدة 5 ثوانٍ بالضبط ليعرض الأنيماشن البصري ثم يفتح المحتوى النهائي
    time.sleep(5.0)
    st.session_state.state = "opened"
    st.rerun()

# المرحلة الثالثة: عرض الصورة والقصيدة الفخمة
elif st.session_state.state == "opened":
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_img1, col_img2, col_img3 = st.columns([1, 1.5, 1])
    with col_img2:
        # تأكد أن اسم صورة رسمة عزة مرفوع في المستودع بهذا الاسم (أو عدله للاسم اللي رفعته)
        st.image("azza.png" if "azza.png" else "image_3.png", caption="إلى أطهر وأغلى الناس.. عزة 🤍", use_container_width=True)
    
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
    
    st.markdown(f'<div class="poem-text">{poem_content}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
    with col_b2:
        if st.button("💌 إغلاق الرسالة وإعادة التجربة", use_container_width=True):
            st.session_state.state = "closed"
            st.rerun()
