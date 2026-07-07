from ui.theme import *

CSS = f"""
<style>

/* ==========================================
GLOBAL
========================================== */

.stApp {{
    background: {BACKGROUND};
}}

.block-container {{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:1500px;
}}

/* ==========================================
HERO
========================================== */

.hero {{

background:linear-gradient(
135deg,
{PRIMARY},
{SECONDARY}
);

padding:45px;

border-radius:22px;

color:white;

margin-bottom:25px;

box-shadow:{SHADOW};

}}

/* ==========================================
GLASS CARDS
========================================== */

.metric-card,
.paper-card {{

background:rgba(255,255,255,0.08);

backdrop-filter:blur(14px);

-webkit-backdrop-filter:blur(14px);

border:1px solid rgba(255,255,255,.15);

border-radius:22px;

padding:24px;

box-shadow:0 8px 30px rgba(0,0,0,.25);

transition:.35s ease;

margin-bottom:18px;

}}

.metric-card:hover,
.paper-card:hover {{

transform:translateY(-8px);

box-shadow:0 16px 40px rgba(0,0,0,.35);

border:1px solid rgba(255,255,255,.35);

}}

/* ==========================================
HEADINGS
========================================== */

h1,h2,h3,h4 {{

font-weight:700;

}}

h1 {{
    margin-bottom:.5rem;
}}

h2 {{
    margin-top:.3rem;
}}

h3 {{
    margin-top:1rem;
}}

/* ==========================================
TEXT INPUT
========================================== */

div[data-testid="stTextInput"] input {{

background:rgba(255,255,255,.05);

border:1px solid rgba(255,255,255,.15);

border-radius:18px;

padding:15px;

font-size:16px;

color:white;

}}

div[data-testid="stTextInput"] input:focus {{

border:1px solid {PRIMARY};

box-shadow:0 0 10px rgba(59,130,246,.35);

}}

/* ==========================================
SELECTBOX
========================================== */

div[data-baseweb="select"] {{

border-radius:16px;

}}

/* ==========================================
BUTTONS
========================================== */

.stButton>button {{

width:100%;

height:52px;

border:none;

border-radius:18px;

font-size:16px;

font-weight:600;

color:white;

background:linear-gradient(
90deg,
{PRIMARY},
{SECONDARY}
);

transition:.3s ease;

}}

.stButton>button:hover {{

transform:translateY(-3px);

box-shadow:0 10px 25px rgba(0,0,0,.35);

}}

/* ==========================================
DOWNLOAD BUTTON
========================================== */

.stDownloadButton>button {{

width:100%;

border-radius:18px;

height:52px;

font-weight:600;

}}

/* ==========================================
CHECKBOX
========================================== */

.stCheckbox {{

padding-top:8px;

padding-bottom:8px;

}}

/* ==========================================
EXPANDER
========================================== */

.streamlit-expanderHeader {{

font-size:16px;

font-weight:600;

}}

/* ==========================================
TABS
========================================== */

.stTabs [data-baseweb="tab-list"] {{

gap:10px;

}}

.stTabs [data-baseweb="tab"] {{

background:rgba(255,255,255,.06);

border-radius:14px;

padding:10px 18px;

}}

.stTabs [aria-selected="true"] {{

background:linear-gradient(
90deg,
{PRIMARY},
{SECONDARY}
);

color:white;

}}

/* ==========================================
SIDEBAR
========================================== */

section[data-testid="stSidebar"] {{

background:#111827;

border-right:1px solid rgba(255,255,255,.08);

}}

section[data-testid="stSidebar"] * {{

color:white;

}}

/* ==========================================
PROGRESS BAR
========================================== */

.stProgress > div > div > div > div {{

background:linear-gradient(
90deg,
{PRIMARY},
{SECONDARY}
);

}}

/* ==========================================
METRICS
========================================== */

[data-testid="metric-container"] {{

background:rgba(255,255,255,.06);

border-radius:18px;

padding:18px;

}}

/* ==========================================
LINK BUTTONS
========================================== */

a {{

text-decoration:none;

}}

a:hover {{

opacity:.85;

}}

/* ==========================================
SCROLLBAR
========================================== */

::-webkit-scrollbar {{

width:10px;

}}

::-webkit-scrollbar-thumb {{

background:{PRIMARY};

border-radius:12px;

}}

::-webkit-scrollbar-track {{

background:#111827;

}}

</style>
"""