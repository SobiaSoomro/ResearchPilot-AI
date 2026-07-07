import streamlit as st


def review_page():

    st.header("📝 Literature Review")

    review = st.session_state.get("review", "")

    if not review:

        st.info(
            "No literature review generated yet.\n\n"
            "Go to the Research page and click **Generate Literature Review**."
        )

        return

    st.success("Literature Review Generated Successfully")

    st.divider()

    st.markdown(review)

    st.download_button(
        label="📥 Download Literature Review",
        data=review,
        file_name="Literature_Review.md",
        mime="text/markdown"
    )