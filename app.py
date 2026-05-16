from drug_info import get_drug_info
from data import DRUGS
import streamlit as st
from streamlit_searchbox import st_searchbox
from interactions import check_interaction
from dose_calculator import calculate_drug_dose, estimate_weight_from_age
st.set_page_config(
    page_title="Pharmacy AI",
    page_icon="℞",
    layout="wide"
)
st.markdown("""
<style>
/* إخفاء زر Fork ورابط GitHub */
button[kind="header"],
a[href*="github.com"],

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
    font-weight: 800;
}
            
h2 {
    font-size: 2.2rem;
    font-weight: 800;
}
            
h3 {
    font-weight: 700;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3rem;
    font-size: 18px;
    font-weight: 600;
}

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

[data-testid="stSidebar"] {
    border-right: 1px solid rgba(255,255,255,0.1);
}

div[data-testid="stVerticalBlock"]:has(.result-card) {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.30);
    margin-top: 20px;
            
}

.result-card {
    display: none;
}


.footer {
    text-align: center;
    margin-top: 80px;
    padding: 20px 0;
    color: rgba(255, 255, 255, 0.55);
    font-size: 13px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    line-height: 1.8;
}

.footer strong {
    color: rgba(255, 255, 255, 0.85);
    font-weight: 600;
} 

</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1> Pharmacy AI</h1>
<h3 style='text-align:center; color:gray;'>Clinical Decision Support System</h3>
<hr>
""", unsafe_allow_html=True)

module = st.sidebar.selectbox(
    "Choose a Module",
    [
        "Home",
        "Drug Interaction Checker",
        "Drug Information",
        "Dose Calculator",
        "Prescription OCR",
        "Lab Interpretation"
    ]
)
st.sidebar.markdown("---")
st.sidebar.info("Developed by Dr. Mahmoud Helmy")

if module == "Home":
    st.header("Welcome to Pharmacy AI")
    st.write("Select a module from the sidebar.")

elif module == "Drug Interaction Checker":
    st.header("🔍 Drug Interaction Checker")
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    drug1 = st.text_input("Enter first drug")
    drug2 = st.text_input("Enter second drug")

    if st.button("Check Interaction"):
        result = check_interaction(drug1, drug2)

        if result:
            st.success("Interaction Found!")
            st.write("Severity:", result["severity"])
            st.write("Mechanism:", result["mechanism"])
            st.write("Recommendation:", result["recommendation"])
        else:
            st.warning("No known interaction found.")
    st.markdown('</div>', unsafe_allow_html=True)
elif module == "Drug Information":
    st.header("💊 Drug Information")
 # بداية الكارد
    st.markdown('<div class="result-card"></div>', unsafe_allow_html=True)
    all_names = []

    for drug in DRUGS.values():
        all_names.append(drug["generic_name"])
        all_names.extend(drug["brand_names"])
        all_names.extend(drug["arabic_names"])

    # إزالة التكرارات وترتيب الأسماء
        all_names = sorted(list(set(all_names)))

    # مربع كتابة للبحث
    def search_drugs(search_term):
        if not search_term:
            return []

        return [
            name for name in all_names
            if name.lower().startswith(search_term.lower())]

    drug_name = st_searchbox(
        search_drugs,
        
        placeholder="Type drug name..."
    )
    if drug_name and st.button("Search Drug"):
        info = get_drug_info(drug_name)

        if info:
            st.success("Drug Found!")

            tab1, tab2, tab3, tab4 = st.tabs([
                "📋 General Info",
                "💊 Doses",
                "🇪🇬 Trade Names",
                "⚠️ Side Effects"
            ])

            with tab1:
                st.write("**Active Ingredient:**", info["generic_name"])
                st.write("**Class:**", info["class"])

                if "moa" in info:
                    st.write("**Mechanism of Action (MOA):**", info["moa"])

                st.write("**Indications:**", info["indications"])

            with tab2:
                st.subheader("Available Strengths")
                for strength in info["strengths"]:
                    st.write(f"✓ {strength}")

            with tab3:
                st.subheader("Other Trade Names in Egypt")
                st.info(" | ".join(info["brand_names"]))

            with tab4:
                st.write("**Common Side Effects:**", info["side_effects"])


        else:
            st.warning("Drug not found.")
    # نهاية الكارد
    
elif module == "Dose Calculator":
    st.header("🧮 Dose Calculator")
    st.markdown('<div class="result-card"></div>', unsafe_allow_html=True)
    # جمع أسماء الأدوية
    all_names = []

    for drug in DRUGS.values():
        all_names.append(drug["generic_name"])
        all_names.extend(drug["brand_names"])
        all_names.extend(drug["arabic_names"])

    # إزالة التكرار وترتيب الأسماء
    all_names = sorted(list(set(all_names)))

    # دالة البحث
    def search_drugs(search_term: str):
        if not search_term:
            return []
        return [
            name for name in all_names
            if name.lower().startswith(search_term.lower())]

    # مربع بحث حقيقي مع اقتراحات تلقائية
    selected_drug = st_searchbox(
        search_drugs,
        placeholder="Type drug name...",
        key="dose_drug_search"
    )

    # بعد اختيار الدواء
    if selected_drug:
        st.markdown('<div class="result-card"></div>', unsafe_allow_html=True)
        st.success(f"Selected Drug: {selected_drug}")

            # اختيار طريقة الحساب
        calculation_method = st.radio(
            "Calculate dose by:",
            ["Weight (kg)", "Age"]
        )

        weight = None
        age = None

        # إدخال الوزن
        if calculation_method == "Weight (kg)":
            weight = st.number_input(
                "Enter weight (kg)",
                min_value=2.0,
                max_value=200.0,
                value=10.0,
                step=0.1
            )

        # إدخال العمر
        else:
            # اختيار وحدة العمر
            age_unit = st.selectbox(
                "Age Unit",
                ["Days", "Months", "Years"]
            )

            # العمر بالأيام
            if age_unit == "Days":
                age_value = st.number_input(
                    "Enter age (days)",
                    min_value=1,
                    max_value=365,
                    value=30,
                    step=1
                )
                age = age_value / 365.0

            # العمر بالشهور
            elif age_unit == "Months":
                age_value = st.number_input(
                    "Enter age (months)",
                    min_value=1,
                    max_value=120,
                    value=12,
                    step=1
                )
                age = age_value / 12.0

            # العمر بالسنوات
            else:
                age_value = st.number_input(
                    "Enter age (years)",
                    min_value=1,
                    max_value=120,
                    value=2,
                    step=1
                )
                age = age_value

        # زر الحساب
        if st.button("Calculate Dose"):

            # الحساب بالعمر
            if calculation_method == "Age":
                estimated_weight = estimate_weight_from_age(age)
                if age > 18:
                    st.warning(
            "For adults, using actual body weight is more accurate "
            "than estimating weight from age."
        )
                st.info(
                    f"Estimated weight based on age: "
                    f"{estimated_weight:.1f} kg"
                )

                dose = calculate_drug_dose(
                    selected_drug,
                    age=age
                )

            # الحساب بالوزن
            else:
                dose = calculate_drug_dose(
                    selected_drug,
                    weight=weight
                )

            # عرض النتائج
            if dose:
                st.success("Dose Calculated!")

                st.write(
                    f"Recommended dose: "
                    f"{dose['dose_mg']:.1f} mg per dose"
                )
                st.write(
                    f"Frequency: {dose['frequency']}"
                )
                dose_every_4h = int(dose["max_daily_dose_mg"] // dose["dose_mg"])
                dose_every_6h = min(4, dose_every_4h)

                st.write(f"If given every 4 hours: up to {dose_every_4h} doses/day")
                st.write(f"If given every 6 hours: up to {dose_every_6h} doses/day")
                st.write(
                    f"Maximum doses per day: "
                    f"{dose['max_doses_per_day']}"
                )
                st.write(
                    f"Maximum daily dose: "
                    f"{dose['max_daily_dose_mg']:.1f} mg/day"
                )
            else:
                st.warning("Dose calculation for this drug is coming soon.")
            # إذا توجد قاعدة جرعات
                st.markdown('</div>', unsafe_allow_html=True)
elif module == "Prescription OCR":
    st.header("🧾 Prescription OCR")
    st.markdown('<div class="result-card"></div>', unsafe_allow_html=True)
    st.info("Coming soon.")

elif module == "Lab Interpretation":
    st.header("🧪 Lab Interpretation")
    st.markdown('<div class="result-card"></div>', unsafe_allow_html=True)
    st.info("Coming soon.")





















    st.markdown("""
<div class="footer">
    © 2026 Pharmacy AI. All Rights Reserved.<br>
    Developed by <strong>Dr. Mahmoud Helmy</strong>
</div>
""", unsafe_allow_html=True)