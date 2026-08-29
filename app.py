import streamlit as st
import random


# ============================================================
# NUMBER MAPPING
# ============================================================

DIGIT_MAP = {
    "0": ["5", "3"],
    "1": ["9", "8"],
    "2": ["3", "5"],
    "3": ["8", "4"],
    "4": ["7", "6"],
    "5": ["0", "7"],
    "6": ["1", "2"],
    "7": ["4", "1"],
    "8": ["6", "9"],
    "9": ["2", "0"]
}


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Number Possibility Generator",
    page_icon="🔢",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("🔢 Number Possibility Generator")

st.write("Enter a 3, 5, or 6 digit number.")

st.divider()


# ============================================================
# INPUT
# ============================================================

number = st.text_input(
    "Enter Number",
    placeholder="Example: 156",
    max_chars=6
)


# ============================================================
# GENERATE ALL POSSIBILITIES
# ============================================================

def generate_all_possibilities(number):

    possibilities = []

    # Change exactly ONE digit at a time
    for position in range(len(number)):

        original_digit = number[position]

        replacements = DIGIT_MAP[original_digit]

        for replacement in replacements:

            new_number = (
                number[:position]
                + replacement
                + number[position + 1:]
            )

            if new_number not in possibilities:
                possibilities.append(new_number)

    return possibilities


# ============================================================
# UPDATE RESULTS
# ============================================================

def update_results(number):

    all_possibilities = generate_all_possibilities(number)

    # --------------------------------------------------------
    # FIRST TIME
    # --------------------------------------------------------

    if "results" not in st.session_state:

        st.session_state.results = random.sample(
            all_possibilities,
            min(5, len(all_possibilities))
        )

        st.session_state.last_number = number

        return


    # --------------------------------------------------------
    # NEW NUMBER ENTERED
    # --------------------------------------------------------

    if st.session_state.last_number != number:

        st.session_state.results = random.sample(
            all_possibilities,
            min(5, len(all_possibilities))
        )

        st.session_state.last_number = number

        return


    # --------------------------------------------------------
    # SAME NUMBER
    #
    # KEEP 1st, 2nd, 3rd and 4th POSSIBILITY
    #
    # CHANGE ONLY 5th POSSIBILITY
    # --------------------------------------------------------

    current_results = st.session_state.results

    if len(current_results) >= 5:

        # Find possibilities that are not already displayed
        unused = [
            possibility
            for possibility in all_possibilities
            if possibility not in current_results
        ]

        # Change ONLY the 5th position
        if unused:

            new_possibility = random.choice(unused)

            current_results[4] = new_possibility

    st.session_state.results = current_results


# ============================================================
# GENERATE BUTTON
# ============================================================

if st.button(
    "Generate 5 Possibilities",
    type="primary",
    use_container_width=True
):

    number = number.strip()

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if number == "":

        st.warning("Please enter a number.")

    elif not number.isdigit():

        st.error("Please enter numbers only.")

    elif len(number) not in [3, 5, 6]:

        st.error("Please enter exactly 3, 5, or 6 digits.")

    else:

        # Generate / update results
        update_results(number)

        # ----------------------------------------------------
        # ORIGINAL NUMBER
        # ----------------------------------------------------

        st.subheader("Original Number")

        st.markdown(
            f"## `{number}`"
        )

        st.divider()

        # ----------------------------------------------------
        # SHOW 5 POSSIBILITIES
        # ----------------------------------------------------

        st.subheader("🎯 5 Possibilities")

        for index, possibility in enumerate(
            st.session_state.results,
            start=1
        ):

            st.markdown(
                f"### {index}. `{possibility}`"
            )

        st.divider()

        # ----------------------------------------------------
        # SHOW MAPPING
        # ----------------------------------------------------

        st.subheader("Digit Mapping")

        for position, digit in enumerate(
            number,
            start=1
        ):

            st.write(
                f"Position {position}: "
                f"{digit} → "
                f"{DIGIT_MAP[digit][0]}, "
                f"{DIGIT_MAP[digit][1]}"
            )


# ============================================================
# COMPLETE NUMBER MAPPING
# ============================================================

st.divider()

with st.expander("View Complete Number Mapping"):

    for digit, values in DIGIT_MAP.items():

        st.write(
            f"{digit} → "
            f"{values[0]}, "
            f"{values[1]}"
        )