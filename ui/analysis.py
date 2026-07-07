import streamlit as st


def analysis_page():

    st.header("🧠 Paper Analysis")

    analyses = st.session_state.get("analyses", {})

    if not analyses:
        st.info("No paper has been analyzed yet.\n\nGo to the Research page and click 'Analyze' on a paper.")
        return

    st.success(f"{len(analyses)} Paper(s) Analyzed")

    st.divider()

    for title, analysis in analyses.items():

        with st.expander(f"📄 {title}", expanded=False):

            st.markdown(analysis)

            st.download_button(
                label="📥 Download Analysis",
                data=analysis,
                file_name=f"{title}.md",
                mime="text/markdown",
                key=f"download_{title}"
            )