import streamlit as st


def gap_page():

    st.header("💡 Research Gap")

    gap = st.session_state.get("gap", "")

    if not gap:

        st.info(
            "No research gap generated yet.\n\n"
            "Go to the Research page and click **Find Research Gap**."
        )

        return

    st.success("Research Gap Generated Successfully")

    st.divider()

    st.markdown(gap)

    st.download_button(
        "📥 Download Research Gap",
        data=gap,
        file_name="Research_Gap.md",
        mime="text/markdown"
    )