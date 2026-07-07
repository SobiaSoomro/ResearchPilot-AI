import streamlit as st
from tools.pdf_export import export_pdf


def export_page():

    st.header("📥 Export Center")

    st.write("Generate and download your complete research report.")

    # ----------------------------------

    st.subheader("Available Content")

    st.checkbox(
        "Research Plan",
        value=bool(st.session_state.plan),
        disabled=True
    )

    st.checkbox(
        "Paper Analyses",
        value=bool(st.session_state.analyses),
        disabled=True
    )

    st.checkbox(
        "Research Gap",
        value=bool(st.session_state.gap),
        disabled=True
    )

    st.checkbox(
        "Literature Review",
        value=bool(st.session_state.review),
        disabled=True
    )

    st.divider()

    # ----------------------------------

    if not st.session_state.review:

        st.info(
            "Generate a Literature Review first to export the complete report."
        )

        return

    # ----------------------------------

    if st.button("📄 Generate PDF Report"):

        with st.spinner("Generating PDF..."):

            pdf_file = export_pdf(
                st.session_state.plan,
                st.session_state.analyses,
                st.session_state.gap,
                st.session_state.review
            )

            st.session_state.pdf_file = pdf_file

        st.success("PDF Generated Successfully!")

    # ----------------------------------

    if st.session_state.get("pdf_file"):

        with open(st.session_state.pdf_file, "rb") as file:

            st.download_button(
                "📥 Download PDF",
                file.read(),
                file_name="Research_Report.pdf",
                mime="application/pdf"
            )