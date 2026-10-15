import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="MORA STORE", page_icon="🛍️", layout="centered")

# --- إدارة حالة تسجيل الدخول واسم المستخدم ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

# --- تصميم الألوان المبتكر والخلاب (CSS) ---
st.markdown("""
    <style>
        /* خلفية متدرجة فخمة بألوان عصرية مريحة للعين */
        .stApp {
            background: linear-gradient(135deg, #1f4068 0%, #162447 50%, #1b1b2f 100%);
            color: #ffffff;
        }
        
        /* تنسيق العناوين بألوان ناصعة وظلال مميزة */
        h1, h2, h3 {
            color: #e4e4e4;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
        }

        /* تنسيق الزراير بألوان جذابة مع تأثيرات انسيابية */
        div.stButton > button {
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            border-radius: 25px;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover {
            background: linear-gradient(45deg, #ff4b2b, #ff416c);
            box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
            transform: translateY(-2px);
        }
        
        /* تنسيق صناديق الإدخال */
        div.stTextInput > div > div > input {
            border-radius: 12px;
            border: 2px solid #00adb5;
            background-color: #0f172a;
            color: white;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- صفحة تسجيل الدخول ---
def show_login_page():
    st.markdown("<h1>🛍️ MORA STORE</h1>", unsafe_allow_html=True)
    st.markdown("<h3>مرحباً بك، يرجى تسجيل الدخول للبدء</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("---")
        username = st.text_input("اسم المستخدم", placeholder="ادخل اسمك هنا...")
        password = st.text_input("كلمة المرور", type="password", placeholder="••••••••")
        
        login_button = st.button("تسجيل الدخول")
        
        if login_button:
            if username.strip() != "" and password == "12345":
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = username.strip()
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            elif username == "" or password == "":
                 st.warning("الرجاء إدخال اسم المستخدم وكلمة المرور.")
            else:
                st.error("كلمة المرور غير صحيحة (كلمة السر هي: 12345).")

# --- صفحة المنتجات والترحيب بالاسم ---
def show_products_page():
    # ترحيب بالاسم الذي أدخله المستخدم
    user = st.session_state['user_name']
    st.markdown(f"<h1>Hello, {user}! 👋 أهلاً بك في متجرك</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00adb5; font-size: 18px;'>استمتع بأحدث تشكيلة من تصاميم MORA الفخمة</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("هودي MORA الأسود")
        st.image("tshirt.jpg", use_column_width=True)
        st.markdown("**السعر:** 450 جنيه")
        st.button("إضافة للعربة", key="tshirt_btn")

    with col2:
        st.subheader("شروال MORA الرياضي")
        st.image("pants.jpg", use_column_width=True)
        st.markdown("**السعر:** 350 جنيه")
        st.button("إضافة للعربة", key="pants_btn")

    st.write("---")
    
    st.subheader("🔥 الطقم الكامل (هودي + شروال)")
    col_c1, col_c2, col_c3 = st.columns([1,2,1])
    with col_c2:
        st.image("full_suit.jpg", use_column_width=True)
        st.markdown("**السعر:** 750 جنيه")
        st.button("إضافة الطقم للعربة", key="suit_btn")

    st.write("---")
    col_out1, col_out2, col_out3 = st.columns([1,1,1])
    with col_out2:
        if st.button("تسجيل الخروج"):
            st.session_state['logged_in'] = False
            st.session_state['user_name'] = ""
            st.rerun()

# --- التشغيل ---
if st.session_state['logged_in']:
    show_products_page()
else:
    show_login_page()