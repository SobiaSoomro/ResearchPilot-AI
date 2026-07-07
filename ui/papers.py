import streamlit as st
from ui.components import paper_card


def papers_page():

    st.header("📄 Research Papers")

    papers = st.session_state.get("papers", [])

    if not papers:
        st.info("No research papers available.\n\nStart a research first.")
        return

    # ======================================
    # SEARCH & SORT
    # ======================================

    col1, col2 = st.columns([3, 1])

    with col1:

        search = st.text_input(
            "🔍 Search Papers",
            placeholder="Search by title..."
        )

    with col2:

        sort = st.selectbox(
            "Sort By",
            [
                "Newest",
                "Oldest",
                "Title A-Z"
            ]
        )

    filtered = papers.copy()

    # ======================================
    # SEARCH
    # ======================================

    if search:

        filtered = [

            paper

            for paper in filtered

            if search.lower() in paper["title"].lower()

        ]

    # ======================================
    # SORT
    # ======================================

    if sort == "Title A-Z":

        filtered.sort(
            key=lambda x: x["title"]
        )

    elif sort == "Newest":

        filtered.sort(
            key=lambda x: x["published"],
            reverse=True
        )

    elif sort == "Oldest":

        filtered.sort(
            key=lambda x: x["published"]
        )

    # ======================================
    # RESULTS
    # ======================================

    st.write(f"### 📚 {len(filtered)} Papers Found")

    if not filtered:

        st.warning("No papers match your search.")

        return

    # ======================================
    # PAPER CARDS
    # ======================================

    for i, paper in enumerate(filtered, start=1):

        paper_card(
            paper,
            i
        )