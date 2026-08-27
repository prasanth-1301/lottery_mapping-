import streamlit as st
from itertools import product
import random


# ============================================================
# NUMBER MAPPING
# ============================================================

NUMBER_MAPPING = {
    "0": ["5", "7", "3"],
    "1": ["9", "5", "8"],
    "2": ["3", "0", "5"],
    "3": ["8", "6", "4"],
    "4": ["7", "9", "6"],
    "5": ["0", "2", "7"],
    "6": ["1", "4", "2"],
    "7": ["4", "9", "1"],
    "8": ["1", "3", "9"],
    "9": ["2", "4", "0"],
}


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Lottery Number Mapper",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    /* Main background and fonts */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --success-color: #10b981;
        --background: #0f172a;
        --surface: #1e293b;
        --text: #f1f5f9;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        padding: 40px 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3em;
        margin: 0;
        font-weight: 800;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1em;
        margin: 10px 0 0 0;
        font-weight: 500;
    }
    
    /* Input container */
    .input-container {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 30px;
        border-radius: 12px;
        border: 2px solid #334155;
        margin: 20px 0;
    }
    
    /* Input styling */
    input[type="text"] {
        font-size: 1.2em !important;
        padding: 15px !important;
        border-radius: 8px !important;
        border: 2px solid #334155 !important;
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
    }
    
    input[type="text"]:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 10px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        padding: 15px 30px;
        font-size: 1.1em;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
    }
    
    /* Results grid */
    .results-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 15px;
        margin: 30px 0;
    }
    
    .result-card {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.8em;
        font-weight: 700;
        color: white;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        transition: all 0.2s ease;
    }
    
    .result-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
    }
    
    /* Metric styling */
    .metric-card {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    .metric-card .metric-label {
        font-size: 0.9em;
        opacity: 0.9;
        margin-bottom: 8px;
    }
    
    .metric-card .metric-value {
        font-size: 2.5em;
        font-weight: 800;
    }
    
    /* Messages */
    .stSuccess {
        background-color: #065f46 !important;
        color: #d1fae5 !important;
        border: 2px solid #10b981 !important;
    }
    
    .stError {
        background-color: #7f1d1d !important;
        color: #fecaca !important;
        border: 2px solid #ef4444 !important;
    }
    
    .stInfo {
        background-color: #0c4a6e !important;
        color: #bae6fd !important;
        border: 2px solid #0ea5e9 !important;
    }
    
    /* Subheader */
    .stSubheader {
        color: #e2e8f0 !important;
        font-size: 1.5em !important;
        margin: 30px 0 20px 0 !important;
        font-weight: 700 !important;
    }
    
    /* Label text */
    label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 1em !important;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE SECTION
# ============================================================

st.markdown("""
<div class="main-header">
    <h1>🎰 Lottery Number Mapper</h1>
    <p>Transform your numbers into winning combinations</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #cbd5e1; margin-bottom: 30px; font-size: 1.05em;">
    Enter a <strong>3-digit</strong>, <strong>5-digit</strong>, or <strong>6-digit</strong> number to generate intelligent mapped combinations
</div>
""", unsafe_allow_html=True)


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown('<div class="input-container">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    number = st.text_input(
        "Enter your number",
        placeholder="Example: 156 or 12345 or 123456",
        label_visibility="collapsed"
    )

with col2:
    submit_button = st.button("Generate", type="primary", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# GENERATE LOGIC
# ============================================================

if submit_button:

    # Remove spaces
    number = number.strip()

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not number:
        st.error("⚠️ Please enter a number to continue.")

    elif not number.isdigit():
        st.error("⚠️ Please enter digits only (0-9).")

    elif len(number) not in [3, 5, 6]:
        st.error(
            "⚠️ Only 3-digit, 5-digit, or 6-digit numbers are accepted."
        )

    else:

        # ----------------------------------------------------
        # CHECK IF THIS IS A NEW INPUT
        # ----------------------------------------------------

        if st.session_state.get("current_number") != number:

            # Save the new number
            st.session_state.current_number = number

            # Generate mapped values
            mapped_digits = [
                NUMBER_MAPPING[digit]
                for digit in number
            ]

            # Generate ALL possible combinations
            combinations = list(product(*mapped_digits))

            # Convert tuples into strings
            results = [
                "".join(combination)
                for combination in combinations
            ]

            # Remove duplicates while preserving order
            unique_results = list(dict.fromkeys(results))

            # Shuffle the complete list once
            random.shuffle(unique_results)

            # Store all results
            st.session_state.all_results = unique_results

            # Start from the first batch
            st.session_state.result_index = 0

        # ----------------------------------------------------
        # GET STORED RESULTS
        # ----------------------------------------------------

        unique_results = st.session_state.all_results

        total_possibilities = len(unique_results)

        # ✅ SUCCESS MESSAGE
        st.success(f"✅ Successfully generated {total_possibilities} combinations from your input!")

        # ============================================================
        # METRICS DISPLAY
        # ============================================================

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:
            st.metric(
                "Total Combinations",
                f"{total_possibilities:,}",
                help="Total unique number combinations generated"
            )

        with metric_col2:
            st.metric(
                "Input Number",
                number,
                help=f"{len(number)}-digit number"
            )

        with metric_col3:
            st.metric(
                "Digit Count",
                f"{len(number)} digits",
                help="Length of your input number"
            )

        # ============================================================
        # DISPLAY RESULTS
        # ============================================================

        st.markdown("<hr style='border-color: #334155;'>", unsafe_allow_html=True)

        # Determine what to display
        if len(number) == 3:
            display_results = unique_results
            show_pagination = False
        else:
            start = st.session_state.result_index
            end = start + 8
            display_results = unique_results[start:end]
            show_pagination = True
            
            st.session_state.result_index = end
            if st.session_state.result_index >= total_possibilities:
                random.shuffle(unique_results)
                st.session_state.result_index = 0

        # Results heading
        st.markdown(f"### 🎯 Your Combinations")

        # Display results in a nice grid
        cols = st.columns(4)
        for index, result in enumerate(display_results):
            with cols[index % 4]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); 
                            padding: 25px; 
                            border-radius: 10px; 
                            text-align: center; 
                            font-size: 2em; 
                            font-weight: 700; 
                            color: white;
                            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
                            margin: 10px 0;
                            transition: transform 0.2s ease;">
                    {result}
                </div>
                """, unsafe_allow_html=True)

        # Pagination info for 5/6 digit numbers
        if show_pagination:
            st.markdown("<hr style='border-color: #334155;'>", unsafe_allow_html=True)
            
            info_text = f"📊 Showing {len(display_results)} combinations from {total_possibilities:,} total | Click 'Generate' again to see more"
            st.info(info_text)

        # Additional info
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)