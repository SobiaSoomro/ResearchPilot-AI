import streamlit as st

from agents.review import generate_literature_review
from tools.pdf_export import export_pdf
from agents.planner import research_planner
from agents.finder import paper_finder
from agents.compare import compare_papers
from agents.gap import generate_research_gap
from ui.components import paper_card


def research_section():

    st.markdown("## 🔍 Research")

    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Artificial Intelligence in Healthcare"
    )

    # ==========================================
    # START RESEARCH
    # ==========================================

    if st.button("🚀 Start Research"):

        if not topic:
            st.warning("Please enter a research topic.")
            st.stop()

        # Reset previous results
        st.session_state.plan = ""
        st.session_state.analysis = ""
        st.session_state.comparison = ""
        st.session_state.gap = ""
        st.session_state.review = ""
        st.session_state.selected_papers = []
        st.session_state.analyses = {}
        st.session_state.papers = []

        with st.spinner("🧠 Planner Agent Working..."):
            st.session_state.plan = research_planner(topic)

        with st.spinner("🔎 Finding Research Papers..."):
            st.session_state.papers = paper_finder(topic)
        
        history_item = {
            "topic": topic,
            "papers": len(st.session_state.papers)
        }

        if history_item not in st.session_state.history:
            st.session_state.history.append(history_item)

        st.success("✅ Research Completed Successfully!")
        st.rerun()

    # ==========================================
    # SHOW RESULTS
    # ==========================================
    if (
        st.session_state.plan
        and
        len(st.session_state.papers) == 0
    ):

        st.warning(
           "⚠️ No relevant research papers found.\n\nTry another research topic."
     )

        return
    if st.session_state.papers:

        left, right = st.columns([1.4, 1])

        # ======================================
        # LEFT PANEL
        # ======================================

        with left:

            st.subheader( f"📄 Research Papers ({len(st.session_state.papers)})")

            for i, paper in enumerate(st.session_state.papers, start=1):
                paper_card(paper, i)
        # ======================================
        # RIGHT PANEL
        # ======================================

        with right:
        

            st.subheader("🤖 AI Workspace")
            progress = 0

            if st.session_state.plan:
                progress = 40

            if st.session_state.analysis:
                progress = 60

            if st.session_state.gap:
                progress = 80

            if st.session_state.review:
                progress = 100

            st.progress(progress)
            st.caption(f"Research Progress: {progress}%")

            st.write("### 🤖 Agent Status")

            st.success("✅ Planner")
            st.success("✅ Finder")

            if st.session_state.analysis:
             st.success("✅ Analyzer")
            else:
             st.info("⏳ Analyzer")

            if st.session_state.gap:
             st.success("✅ Gap Agent")
            else:
             st.info("⏳ Gap Agent")

            if st.session_state.review:
                st.success("✅ Review Agent")
            else:
                st.info("⏳ Review Agent")


            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📋 Plan",
                "🧠 Analysis",
                "⚖ Compare",
                "💡 Gap",
                "📝 Review"
            ])
           

            # ==================================
            # PLAN
            # ==================================

            with tab1:

                if st.session_state.plan:
                    st.markdown(st.session_state.plan)
                else:
                    st.info("Research plan will appear here.")

            # ==================================
            # ANALYSIS
            # ==================================

            with tab2:

                if st.session_state.analysis:
                    st.markdown(st.session_state.analysis)
                else:
                    st.info("Click 'Analyze' on any paper.")

            # ==================================
            # COMPARE
            # ==================================

            with tab3:

                if st.button("⚖ Compare Selected Papers"):

                    if len(st.session_state.selected_papers) < 2:

                        st.warning("Please select at least 2 papers.")

                    else:

                        with st.spinner("Comparing Papers..."):

                            st.session_state.comparison = compare_papers(
                                st.session_state.selected_papers
                            )
                if st.session_state.get("comparison"):
                    st.markdown(st.session_state.comparison)

            # ==================================
            # RESEARCH GAP
            # ==================================

            with tab4:

                if st.button("💡 Find Research Gap"):

                    if len(st.session_state.analyses) == 0:

                        st.warning(
                            "Please analyze at least one paper first."
                        )

                    else:

                        with st.spinner("Finding Research Gaps..."):

                            st.session_state.gap = generate_research_gap(
                                st.session_state.analyses
                            )

                if st.session_state.gap:
                    st.markdown(st.session_state.gap)

                else:
                    st.info("Analyze papers first, then generate research gaps.")

            # ==================================
            # LITERATURE REVIEW
            # ==================================

            with tab5:

                if st.button("📝 Generate Literature Review"):

                    if not st.session_state.plan:

                        st.warning("Please define a research plan first.")

                    elif len(st.session_state.analyses) == 0:

                        st.warning("Please analyze at least one paper first.")

                    elif not st.session_state.gap:

                        st.warning("Please identify a research gap first.")

                    else:

                        with st.spinner("Generating Literature Review..."):

                            st.session_state.review = generate_literature_review(
                                st.session_state.plan,
                                st.session_state.analyses,
                                st.session_state.gap
                            )

                if st.session_state.review:
                    st.markdown(st.session_state.review)
                    st.divider()
                if st.session_state.review:
                    if st.button("📥 Export as PDF"):
                        pdf_file = export_pdf(
                            st.session_state.plan,
                            st.session_state.analyses,
                            st.session_state.gap,
                            st.session_state.review
                        )
                        st.session_state.pdf_file = pdf_file
                    if "pdf_file" in st.session_state:
                        with open(st.session_state.pdf_file, "rb") as file:
                            file_data = file.read()
                            st.download_button(
                                "📥 Download PDF Report",
                                file_data,
                                file_name="Research_Report.pdf",
                                mime="application/pdf"
                            )

                else:
                    st.info("Define a research plan, analyze papers, and identify a research gap to generate a literature review.")