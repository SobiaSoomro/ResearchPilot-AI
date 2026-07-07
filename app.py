import streamlit as st

from ui.export import export_page
from ui.styles import CSS
from ui.sidebar import sidebar
from ui.components import hero
from ui.dashboard import dashboard
from ui.research import research_section
from ui.papers import papers_page
from ui.analysis import analysis_page
from ui.gap import gap_page
from ui.review import review_page
from ui.history import history_page



# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# CSS
# ======================================

st.markdown(CSS, unsafe_allow_html=True)

# ======================================
# SESSION STATE
# ======================================

DEFAULT_STATE = {
    "papers": [],
    "plan": "",
    "analysis": "",
    "analyses": {},
    "comparison": "",
    "selected_papers": [],
    "gap": "",
    "review": "",
    "pdf_file": "",
    "topic": "",
    "history": []      
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ======================================
# SIDEBAR
# ======================================

selected = sidebar()

# ======================================
# HERO
# ======================================

hero()

# ======================================
# ROUTING
# ======================================

PAGES = {
    "Dashboard": dashboard,
    "Research": research_section,
    "Papers": papers_page,
    "Analysis": analysis_page,
    "Research Gap": gap_page,
    "Literature Review": review_page,
    "Export": export_page,
    "History": history_page
}

PAGES[selected]()

