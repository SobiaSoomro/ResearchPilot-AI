import streamlit as st


def history_page():

    st.header("🕘 Research History")

    history = st.session_state.get("history", [])

    if not history:
        st.info("No previous research found.")
        return

    for i, item in enumerate(history, start=1):

        with st.container(border=True):

            st.subheader(f"📚 Project {i}")

            st.write(f"**Topic:** {item['topic']}")

            st.write(f"**Papers Found:** {item['papers']}")