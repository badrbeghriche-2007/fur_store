# -*- coding: utf-8 -*-
"""
متجر دار الأناقة لبيع الأثاث والمرايا (Streamlit Native App)
مخصص للعمل مباشرة وبشكل متكامل 100% على منصة Streamlit Cloud دون الحاجة إلى Flask.
"""

import streamlit as st
import urllib.parse

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="دار الأناقة | الأثاث والمرايا",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# رقم الواتساب المستلم
WHATSAPP_NUMBER = "213784803429"

# أنماط مخصصة (Custom CSS) للثيم الأبيض والبيج والأزرار الناعمة
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .stApp {
        background-color: #FCFBF9;
        color: #3D3124;
    }
    
    .top-bar {
        background-color: #665035;
        color: #FCFBF9;
        padding: 10px 16px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        margin-bottom: 25px;
    }
    
    .product-box {
        background: #FFFFFF;
        border: 1px solid #ECE4D5;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(100, 80, 50, 0.05);
        margin-bottom: 15px;
    }
    
    .price-tag {
        font-size: 26px;
        font-weight: 800;
        color: #665035;
    }
    
    .stButton>button {
        background-color: #665035 !important;
        color: white !important;
        border-radius: 14px !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #53412C !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# الشريط العلوي
st.markdown("""
<div class="top-bar">
    ✨ مرحباً بكم في دار الأناقة | خدمة الزبائن وتأكيد الطلبات عبر واتساب: <span dir="ltr"><b>0784803429</b></span>
</div>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 style='text-align:center; color:#53412C; font-weight:800; margin-bottom:10px;'>أثاث عصري ومرايا ديكور راقية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#7D623F; font-size:16px; margin-bottom:40px;'>اختر المنتج لإدخال معلومات التوصيل وإرسال طلبك فوراً باسمك عبر الواتساب</p>", unsafe_allow_html=True)

# إدارة حالة المنتج المختار
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="product-box">
        <span style="background:#F6F2EB; color:#7D623F; padding:4px 12px; border-radius:8px; font-size:12px; font-weight:700;">الأثاث المنزلي</span>
        <h2 style="color:#53412C; font-weight:800; margin-top:10px;">أثاث صالون عصري فاخر</h2>
        <div class="price-tag">65,000 دج</div>
        <p style="color:#7D623F; font-size:14px; line-height:1.7; margin-top:10px;">
            طقم صالون عصري متكامل بتصميم ناعم ومريح باللونين الأبيض والبيج، مصنوع بجودة عالية لراحة وأناقة منزلك.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("طلب الأثاث الآن (65000 دج)", key="btn_furn"):
        st.session_state.selected_product = {"name": "أثاث صالون عصري فاخر", "price": "65000 دج"}

with col2:
    st.markdown("""
    <div class="product-box">
        <span style="background:#F6F2EB; color:#7D623F; padding:4px 12px; border-radius:8px; font-size:12px; font-weight:700;">المرايا والديكور</span>
        <h2 style="color:#53412C; font-weight:800; margin-top:10px;">مرآة ديكور مقوسة فاخرة</h2>
        <div class="price-tag">3,000 دج</div>
        <p style="color:#7D623F; font-size:14px; line-height:1.7; margin-top:10px;">
            مرآة مقوسة عصرية فائقة النقاء بإطار ناعم بلون البيج الذهبي، تمنح الغرفة إضاءة ومظهراً جمالياً واسعاً.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("طلب المرآة الآن (3000 دج)", key="btn_mirror"):
        st.session_state.selected_product = {"name": "مرآة ديكور مقوسة فاخرة", "price": "3000 دج"}

# نافذة تعبئة البيانات عند اختيار منتج
if st.session_state.selected_product:
    prod = st.session_state.selected_product
    st.markdown("---")
    st.markdown(f"<h3 style='color:#53412C;'>تعبئة معلومات الطلب: <span style='color:#665035;'>{prod['name']}</span> ({prod['price']})</h3>", unsafe_allow_html=True)
    
    with st.form(key="order_form"):
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            first_name = st.text_input("الاسم *", placeholder="مثال: محمد")
        with f_col2:
            last_name = st.text_input("اللقب *", placeholder="مثال: بن علي")
            
        phone = st.text_input("رقم الهاتف *", placeholder="07 / 06 / 05 XX XX XX XX")
        email = st.text_input("البريد الإلكتروني *", placeholder="example@mail.com")
        address = st.text_input("مكان السكن (الولاية والعنوان الكامل) *", placeholder="الولاية، الدائرة أو البلدية، الحي...")
        
        submitted = st.form_submit_button("إرسال الطلب عبر واتساب (0784803429)")
        
        if submitted:
            if not first_name or not last_name or not phone or not email or not address:
                st.error("يرجى ملء جميع الحقول المطلوبة لإتمام الطلب.")
            else:
                full_name = f"{first_name} {last_name}".strip()
                message = (
                    f"🛒 *طلب جديد باسم: {full_name}*\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"📦 *المنتج المطلوب:* {prod['name']}\n"
                    f"💰 *السعر:* {prod['price']}\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"👤 *الاسم:* {first_name}\n"
                    f"👤 *اللقب:* {last_name}\n"
                    f"📞 *رقم الهاتف:* {phone}\n"
                    f"📧 *البريد الإلكتروني:* {email}\n"
                    f"📍 *مكان السكن:* {address}\n"
                    f"━━━━━━━━━━━━━━━\n"
                    f"مرسل من طرف الزبون: *{full_name}*"
                )
                encoded_msg = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_msg}"
                
                st.success(f"تم تسجيل طلبك باسم {full_name}! اضغط على الزر أدناه لتأكيد الإرسال عبر واتساب:")
                st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                    <div style="background-color:#10B981; color:white; text-align:center; padding:14px; border-radius:14px; font-weight:800; font-size:16px;">
                        📲 فتح تطبيق واتساب وإرسال الطلب الآن
                    </div>
                </a>
                """, unsafe_allow_html=True)