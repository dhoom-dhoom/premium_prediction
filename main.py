# codebasics ML course: codebasics.io, all rights reserved
import streamlit as st
from prediction_helper import predict

# Configure page
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86C1;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .sub-header {
        text-align: center;
        color: #5D6D7E;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #2874A6;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #AED6F1;
        padding-bottom: 0.5rem;
    }
    .prediction-box {
        background: linear-gradient(90deg, #E8F8F5, #D5F4E6);
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #27AE60;
        margin: 2rem 0;
    }
    .info-box {
        background-color: #EBF5FB;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #3498DB;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background: linear-gradient(90deg, #2E86C1, #3498DB);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">🏥 Health Insurance Cost Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Get accurate predictions for your health insurance premiums based on your personal profile</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("### 📊 About This Tool")
    st.markdown("""
    This AI-powered tool helps you estimate your health insurance costs based on various personal and health factors.
    
    **Key Features:**
    - Instant cost predictions
    - Comprehensive factor analysis
    - User-friendly interface
    - Accurate ML algorithms
    """)
    
    st.markdown("### 💡 Tips for Accurate Results")
    st.markdown("""
    - Provide accurate personal information
    - Select the most appropriate categories
    - Consider your current health status
    - Review all inputs before prediction
    """)

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    # Personal Information Section
    st.markdown('<h3 class="section-header">👤 Personal Information</h3>', unsafe_allow_html=True)
    
    personal_row1 = st.columns(3)
    with personal_row1[0]:
        age = st.number_input('Age', min_value=18, max_value=100, value=30, help="Your current age in years")
    with personal_row1[1]:
        gender = st.selectbox('Gender', ['Male', 'Female'], help="Select your gender")
    with personal_row1[2]:
        marital_status = st.selectbox('Marital Status', ['Unmarried', 'Married'], help="Your current marital status")
    
    personal_row2 = st.columns(3)
    with personal_row2[0]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=20, value=0, 
                                             help="Number of family members covered under your policy")
    with personal_row2[1]:
        income_lakhs = st.number_input('Annual Income (₹ Lakhs)', min_value=0, max_value=200, value=5,
                                     help="Your annual income in Indian Rupees (Lakhs)")
    with personal_row2[2]:
        employment_status = st.selectbox('Employment Status', 
                                       ['Salaried', 'Self-Employed', 'Freelancer', 'Unemployed'],
                                       help="Your current employment situation")

    # Health Information Section
    st.markdown('<h3 class="section-header">🏃‍♂️ Health Profile</h3>', unsafe_allow_html=True)
    
    health_row1 = st.columns(3)
    with health_row1[0]:
        bmi_category = st.selectbox('BMI Category', 
                                  ['Normal', 'Underweight', 'Overweight', 'Obesity'],
                                  help="Your Body Mass Index category")
    with health_row1[1]:
        smoking_status = st.selectbox('Smoking Status', 
                                    ['No Smoking', 'Occasional', 'Regular'],
                                    help="Your smoking habits")
    with health_row1[2]:
        genetical_risk = st.slider('Genetic Risk Score', min_value=0, max_value=5, value=2,
                                 help="Family history of diseases (0=No risk, 5=High risk)")

    # Medical & Insurance Details
    st.markdown('<h3 class="section-header">🏥 Medical & Insurance Details</h3>', unsafe_allow_html=True)
    
    medical_row = st.columns(3)
    with medical_row[0]:
        medical_history = st.selectbox('Medical History', [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ], help="Select your current medical conditions")
    with medical_row[1]:
        insurance_plan = st.selectbox('Insurance Plan Type', 
                                    ['Bronze', 'Silver', 'Gold'],
                                    help="Choose your preferred insurance plan tier")
    with medical_row[2]:
        region = st.selectbox('Region', 
                            ['Northwest', 'Northeast', 'Southeast', 'Southwest'],
                            help="Your geographical region")

with col2:
    st.markdown("### 📋 Input Summary")
    st.markdown(f"""
    **Personal Details:**
    - Age: {age if 'age' in locals() else 'Not set'}
    - Gender: {gender if 'gender' in locals() else 'Not set'}
    - Dependants: {number_of_dependants if 'number_of_dependants' in locals() else 'Not set'}
    
    **Financial:**
    - Income: ₹{income_lakhs if 'income_lakhs' in locals() else 'Not set'} Lakhs
    
    **Health:**
    - BMI: {bmi_category if 'bmi_category' in locals() else 'Not set'}
    - Smoking: {smoking_status if 'smoking_status' in locals() else 'Not set'}
    """)

# Prediction Section
st.markdown('<h3 class="section-header">🔮 Get Your Prediction</h3>', unsafe_allow_html=True)

# Create input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction button and results
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button('🔍 Predict Insurance Cost', use_container_width=True):
        with st.spinner('Analyzing your profile and calculating costs...'):
            try:
                prediction = predict(input_dict)
                
                # Display prediction with enhanced formatting
                st.markdown(f"""
                <div class="prediction-box">
                    <h2 style="color: #27AE60; text-align: center; margin-bottom: 1rem;">
                        💰 Predicted Annual Premium
                    </h2>
                    <h1 style="color: #2E86C1; text-align: center; font-size: 3rem; margin: 0;">
                        ₹{prediction:,.2f}
                    </h1>
                    <p style="text-align: center; color: #5D6D7E; margin-top: 1rem;">
                        This is your estimated annual health insurance premium
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Additional insights
                st.markdown("### 📈 Cost Factors Analysis")
                col_insight1, col_insight2 = st.columns(2)
                
                with col_insight1:
                    st.markdown("""
                    **Factors that may increase your premium:**
                    - Higher age groups
                    - Smoking habits
                    - Pre-existing medical conditions
                    - Higher BMI categories
                    - More dependants
                    """)
                
                with col_insight2:
                    st.markdown("""
                    **Ways to potentially reduce costs:**
                    - Maintain healthy lifestyle
                    - Choose appropriate plan tier
                    - Regular health check-ups
                    - Quit smoking
                    - Maintain optimal BMI
                    """)
                    
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")
                st.info("Please check your inputs and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #5D6D7E;">
    <p>💡 <strong>Disclaimer:</strong> This prediction is for informational purposes only. 
    Actual insurance costs may vary based on additional factors and insurer policies.</p>
    <p><em>Powered by Machine Learning | Built with Streamlit</em></p>
</div>
""", unsafe_allow_html=True)