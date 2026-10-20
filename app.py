import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="رسالة اعتذار لقلبك", page_icon="💌", layout="centered")

# تصميم الواجهة والتأثيرات البصرية والخط العربي
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f3f4f6;
        font-family: 'Cairo', sans-serif;
    }
    
    .poem-text {
        font-family: 'Amiri', serif;
        font-size: 24px;
        line-height: 2.2;
        color: #f8fafc;
        text-align: center;
        direction: rtl;
        background: rgba(30, 41, 59, 0.7);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(244, 114, 182, 0.3);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    .envelope-box {
        background: #fbcfe8;
        padding: 50px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(244, 114, 182, 0.3);
        max-width: 500px;
        margin: 50px auto;
        border: 3px dashed #db2777;
    }
    
    h2 {
        color: #f472b6 !important;
        font-family: 'Amiri', serif;
    }
</style>
""", unsafe_allow_html=True)

# إدارة حالات التفاعل (Session State)
if "opened" not in st.session_state:
    st.session_state.opened = False

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; font-family: 'Amiri', serif; margin-top: 20px;'>إلى من يمتلكه القلب... 🤍</h1>", unsafe_allow_html=True)

# الخطوة الأولى: Envelope (الجواب البينك والختم)
if not st.session_state.opened:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="envelope-box">
            <span style="font-size: 70px;">💌</span>
            <h2 style="color: #831843 !important; margin-top: 10px;">رسالة خاصة جداً</h2>
            <p style="color: #9d174d; font-size: 14px;">اضغط على الختم لفتح الجواب وتكسير الحواجز...</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔴 اضغط هنا لكسر الختم وفتح الجواب", use_container_width=True):
            st.session_state.opened = True
            st.rerun()

# الخطوة الثانية: بعد فتح الجواب (الصورة ثم الشعر والموسيقى)
else:
    # تأثير تكسير الختم وقلوب متطايرة وهمية
    st.markdown("<p style='text-align: center; color: #f472b6; font-size: 18px;'>✨ تم تكسير الختم وتطايرت القلوب لعينيك... ✨</p>", unsafe_allow_html=True)
    
    # مكان عرض صورة الأسد الـ AI بالبوكيه ورد لمدة مؤقتة
    image_placeholder = st.empty()
    
    # رابط صورة أسد لطيف وماسك بوكيه ورد (يمكنك استبدالها برابط صورتك المفضلة المرفوعة على جيثب أو سوبابيس)
    ai_lion_image_url = "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?q=80&w=1000&auto=format&fit=crop" # مثال مؤقت لصورة فخمة، أو صورة أسد كرتوني/واقعي بالورد
    
    # عرض الصورة أولاً لمدة 5 ثوانٍ
    with image_placeholder.container():
        col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
        with col_img2:
            st.image("https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?q=80&w=800&auto=format&fit=crop", caption="هدية خاصة لعيونك 🦁🌹", use_container_width=True)
    
    # الانتظار لمدة 5 ثوانٍ
    time.sleep(5)
    image_placeholder.empty() # مسح الصورة بعد 5 ثوانٍ
    
    # تشغيل الموسيقى الهادئة للحب (رابط صوتي هادئ ورومانسي)
    music_url = "https://www.bensound.com/bensound-music/bensound-tenderness.mp3"
    st.audio(music_url, format='audio/mp3', autoplay=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # عرض الشعر بخط عربي فخم (Amiri)
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
    if st.button("🔄 إعادة التجربة من جديد", use_container_width=True):
        st.session_state.opened = False
        st.rerun()
