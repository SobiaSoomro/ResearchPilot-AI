import streamlit as st
from agents.analyzer import analyze_paper
from tools.citation import (
    generate_apa,
    generate_ieee,
    generate_mla,
    generate_bibtex
)


def hero():
    st.markdown("""
    <div class="hero">

    # 📚 ResearchPilot AI

    ### AI Multi-Agent Research Assistant

    Search • Analyze • Compare • Discover Research Gaps • Generate Literature Reviews

    </div>
    """, unsafe_allow_html=True)


def metric_card(title, value):
    st.markdown(f"""
    <div class="metric-card">

    <h2>{value}</h2>

    {title}

    </div>
    """, unsafe_allow_html=True)


def paper_card(paper, number):

    with st.container(border=True):

        # =====================================
        # PAPER NUMBER
        # =====================================

        st.caption(f"📄 Paper #{number}")

        # =====================================
        # RELEVANCE BADGE
        # =====================================

        summary = paper.get("summary", "").lower()

        score = 0

        for word in [
            "artificial",
            "intelligence",
            "ai",
            "learning",
            "education",
            "healthcare",
            "machine"
        ]:
            if word in summary:
                score += 1

        if score >= 4:
            st.success("🟢 Highly Relevant")
        elif score >= 2:
            st.warning("🟡 Relevant")
        else:
            st.info("🔵 Relevant")

        # =====================================
        # TITLE
        # =====================================

        st.markdown(f"### {paper.get('title','No Title')}")

        # =====================================
        # AUTHORS
        # =====================================

        authors = paper.get("authors", "Unknown")

        if len(authors) > 120:
            authors = authors[:120] + "..."

        st.caption(f"👨‍🔬 Authors: {authors}")

        # =====================================
        # PUBLISHED
        # =====================================

        st.caption(
            f"📅 Published: {paper.get('published','Unknown')}"
        )

        # =====================================
        # DOI
        # =====================================

        doi = paper.get("doi")

        if doi:
            st.caption(f"🔗 DOI: {doi}")

        # =====================================
        # KEYWORDS
        # =====================================

        keywords = []

        for word in summary.split():

            word = word.strip(".,()[]{}").lower()

            if len(word) > 7:
                keywords.append(word)

        keywords = list(dict.fromkeys(keywords))[:5]

        if keywords:
            st.caption("🏷 " + " • ".join(keywords))

        # =====================================
        # ABSTRACT
        # =====================================

        with st.expander("📖 Read Abstract"):
            st.write(paper.get("summary", ""))

        # =====================================
        # BUTTONS
        # =====================================

        col1, col2, col3 = st.columns(3)

        # PDF

        with col1:

            st.link_button(
                "📥 Open PDF",
                paper.get("pdf_url", "#")
            )

        # ANALYZE

        with col2:

            if st.button(
                "🧠 Analyze",
                key=f"analyze_{number}"
            ):

                try:

                    analysis = analyze_paper(
                        paper.get("title", ""),
                        paper.get("summary", "")
                    )

                    st.session_state.analysis = analysis

                    if "analyses" not in st.session_state:
                       st.session_state.analyses = {}

# Debug
                    st.write("Type of analyses:", type(st.session_state.analyses))

                    if isinstance(st.session_state.analyses, list):
                       st.error("❌ analyses is LIST")
                       st.stop()

                    st.session_state.analyses[
                        paper.get("title", f"paper_{number}")
                    ] = analysis

                    st.success("✅ Analysis Completed!")

                except Exception as e:

                    st.error(str(e))

        # CITATION

        with col3:

            with st.expander("📑 Citation"):

                st.code(generate_apa(paper))

                st.code(generate_ieee(paper))

                st.code(generate_mla(paper))

                st.code(
                    generate_bibtex(paper),
                    language="bibtex"
                )

        # =====================================
        # COMPARE
        # =====================================

        if "selected_papers" not in st.session_state:
            st.session_state.selected_papers = []

        selected = st.checkbox(
            "⚖ Select for Comparison",
            key=f"compare_{number}",
            value=paper in st.session_state.selected_papers
        )

        if selected:

            if paper not in st.session_state.selected_papers:
                st.session_state.selected_papers.append(paper)

        else:

            if paper in st.session_state.selected_papers:
                st.session_state.selected_papers.remove(paper)

        st.caption(
            f"📚 Selected Papers: {len(st.session_state.selected_papers)}"
        )