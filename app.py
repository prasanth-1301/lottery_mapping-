
import streamlit as st
import random
from itertools import product


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Number Possibility Generator",
    page_icon="🔢",
    layout="centered"
)


# ============================================================
# DIGIT MAPPING
# ============================================================

DIGIT_MAP = {
    "0": ["2", "9", "4", "8"],
    "1": ["6", "8", "9", "7"],
    "2": ["9", "7", "6", "5"],
    "3": ["6", "8", "2", "6"],
    "4": ["7", "8", "5", "3"],
    "5": ["7", "0", "1", "8"],
    "6": ["1", "9", "3", "7"],
    "7": ["5", "6", "8", "9"],
    "8": ["3", "1", "0", "5"],
    "9": ["4", "2", "6", "1"]
}


# ============================================================
# SESSION STATE
# ============================================================

if "results" not in st.session_state:
    st.session_state.results = []

if "last_number" not in st.session_state:
    st.session_state.last_number = ""

if "display_number" not in st.session_state:
    st.session_state.display_number = ""

if "error" not in st.session_state:
    st.session_state.error = ""


# ============================================================
# CUSTOM CSS - GREEN & WHITE UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #f5faf6;
}

.block-container {
    max-width: 600px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* HEADER */

.main-title {
    text-align: center;
    color: #14532d;
    font-size: 38px;
    font-weight: 850;
    letter-spacing: -1px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 15px;
    margin-bottom: 35px;
}

/* INPUT LABEL */

.input-label {
    color: #166534;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* INPUT FIELD */

.stTextInput input {
    background: #ffffff !important;
    color: #14532d !important;
    border: 1.5px solid #bbf7d0 !important;
    border-radius: 13px !important;
    height: 58px;
    font-size: 22px !important;
    text-align: center;
    font-weight: 600;
}

.stTextInput input:focus {
    border-color: #16a34a !important;
    box-shadow: 0 0 0 1px #16a34a !important;
}

/* GENERATE BUTTON */

.stButton button {
    height: 55px;
    border-radius: 13px;
    background: linear-gradient(90deg, #16a34a, #15803d);
    color: white;
    border: none;
    font-size: 16px;
    font-weight: 750;
    transition: 0.2s;
}

.stButton button:hover {
    background: #166534;
    color: white;
    border: none;
}

/* RESULT HEADING */

.result-heading {
    text-align: center;
    color: #14532d;
    font-size: 24px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 20px;
}

/* RESULT CARDS */

.result-card {
    background: linear-gradient(135deg, #ffffff, #f0fdf4);
    border: 1px solid #bbf7d0;
    border-left: 5px solid #16a34a;
    border-radius: 15px;
    padding: 19px 22px;
    margin: 13px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 14px rgba(22, 101, 52, 0.07);
}

.result-label {
    color: #15803d;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.result-number {
    color: #14532d;
    font-size: 32px;
    font-weight: 850;
    letter-spacing: 5px;
}

.result-index {
    background: #dcfce7;
    color: #166534;
    padding: 9px 13px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 800;
}

/* ORIGINAL NUMBER */

.original-number {
    text-align: center;
    color: #64748b;
    font-size: 14px;
    margin-bottom: 20px;
}

.original-number span {
    color: #15803d;
    font-size: 18px;
    font-weight: 800;
}

/* EMPTY STATE */

.empty-card {
    text-align: center;
    padding: 35px 15px;
    background: #ffffff;
    border: 1px solid #bbf7d0;
    border-radius: 16px;
    margin-top: 25px;
    box-shadow: 0 4px 15px rgba(22, 163, 74, 0.05);
}

.footer {
    color: #64748b;
    text-align: center;
    font-size: 12px;
    margin-top: 30px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

header[data-testid="stHeader"] {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# GENERATE ALL UNIQUE ASSIGNED COMBINATIONS
# ============================================================

def generate_all_possibilities(number):

    digit_options = [
        list(dict.fromkeys(DIGIT_MAP[digit]))
        for digit in number
    ]

    possibilities = []

    # Replace EVERY digit using its assigned mapping
    for combination in product(*digit_options):

        new_number = "".join(combination)

        if new_number not in possibilities:
            possibilities.append(new_number)

    return possibilities


# ============================================================
# GENERATE 3 POSSIBILITIES
# ============================================================

def generate_results(number):

    all_possibilities = generate_all_possibilities(number)

    if len(all_possibilities) < 3:
        return False

    # --------------------------------------------------------
    # NEW INPUT: GENERATE 3 UNIQUE POSSIBILITIES
    # --------------------------------------------------------

    if st.session_state.last_number != number:

        st.session_state.results = random.sample(
            all_possibilities,
            3
        )

        st.session_state.last_number = number
        st.session_state.display_number = number

        return True

    # --------------------------------------------------------
    # SAME INPUT: KEEP FIRST 2 FIXED
    # CHANGE ONLY THIRD POSSIBILITY
    # --------------------------------------------------------

    current_results = st.session_state.results

    fixed_two = current_results[:2]

    current_third = current_results[2]

    unused = [
        possibility
        for possibility in all_possibilities
        if possibility not in fixed_two
        and possibility != current_third
    ]

    if unused:

        current_results[2] = random.choice(unused)

    st.session_state.results = current_results

    st.session_state.display_number = number

    return True


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🔢 Number Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generate 3 assigned number possibilities</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="input-label">ENTER YOUR NUMBER</div>',
    unsafe_allow_html=True
)

number = st.text_input(
    "Enter Number",
    placeholder="Enter 2 to 6 digits",
    max_chars=6,
    label_visibility="collapsed"
)

st.caption("Supports 2, 3, 4, 5 and 6 digit numbers.")

st.write("")


# ============================================================
# GENERATE BUTTON
# ============================================================

if st.button(
    "✨ Generate 3 Possibilities",
    type="primary",
    use_container_width=True
):

    number = number.strip()

    if not number:

        st.session_state.error = "Please enter a number."

    elif not number.isdigit():

        st.session_state.error = "Please enter numbers only."

    elif len(number) not in [2, 3, 4, 5, 6]:

        st.session_state.error = (
            "Please enter exactly 2, 3, 4, 5 or 6 digits."
        )

    else:

        success = generate_results(number)

        if success:
            st.session_state.error = ""
        else:
            st.session_state.error = (
                "Not enough unique combinations."
            )


# ============================================================
# ERROR DISPLAY
# ============================================================

if st.session_state.error:
    st.error(st.session_state.error)


# ============================================================
# RESULTS DISPLAY
# ============================================================

if (
    len(st.session_state.results) == 3
    and st.session_state.display_number
):

    st.markdown(
        '<div class="result-heading">🎯 Your 3 Possibilities</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="original-number">
            Original Number:
            <span>{st.session_state.display_number}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    for index, possibility in enumerate(
        st.session_state.results,
        start=1
    ):

        st.markdown(
            f"""
            <div class="result-card">
                <div>
                    <div class="result-label">
                        POSSIBILITY {index}
                    </div>
                    <div class="result-number">
                        {possibility}
                    </div>
                </div>
                <div class="result-index">
                    0{index}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="footer">
            First 2 possibilities stay fixed.
            Only the 3rd possibility changes on every click.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="empty-card">
            <div style="font-size:38px;">🎯</div>
            <div style="
                color:#14532d;
                font-size:18px;
                font-weight:800;
                margin-top:12px;
            ">
                Ready to Generate?
            </div>
            <div style="
                color:#64748b;
                font-size:13px;
                margin-top:8px;
            ">
                Enter your number above to get 3 possibilities.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
