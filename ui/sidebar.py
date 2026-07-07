import streamlit as st
from streamlit_option_menu import option_menu


def sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/fluency/96/artificial-intelligence.png",
            width=70
        )

        st.markdown("## ResearchPilot AI")

        selected = option_menu(

            menu_title=None,

            options=[

                "Dashboard",

                "Research",

                "Papers",

                "Analysis",

                "Research Gap",

                "Literature Review",

                "Export",

                "History"

            ],

            icons=[

                "house",

                "search",

                "file-earmark-text",

                "robot",

                "lightbulb",

                "journal-text",

                "download",

                "clock-history"

            ],

            default_index=0,
             key="main_sidebar_menu"

        )

        st.divider()

        st.caption("Powered by Gemini")
        st.caption("Multi-Agent AI")

    return selected