import streamlit as st
import pandas as pd
import plotly.express as px
from ui.components import metric_card


def dashboard():

    st.markdown("## 📊 Dashboard")

    # ======================================
    # SESSION DATA
    # ======================================

    papers = len(st.session_state.get("papers", []))
    analyses = len(st.session_state.get("analyses", {}))
    selected = len(st.session_state.get("selected_papers", []))
    gap = bool(st.session_state.get("gap"))
    review = bool(st.session_state.get("review"))

    # ======================================
    # METRICS
    # ======================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Research Papers", papers)

    with col2:
        metric_card("Analyzed Papers", analyses)

    with col3:
        metric_card("Selected Papers", selected)

    with col4:
        metric_card("Research Gaps", 1 if gap else 0)

    st.divider()

    # ======================================
    # PROGRESS
    # ======================================

    st.subheader("📈 Research Progress")

    progress = 0

    if st.session_state.get("plan"):
        progress = 20

    if papers:
        progress = 40

    if analyses:
        progress = 60

    if gap:
        progress = 80

    if review:
        progress = 100

    st.progress(progress)

    st.caption(f"Overall Progress : {progress}%")

    st.divider()

    # ======================================
    # WORKFLOW CHART
    # ======================================

    st.subheader("📊 Research Workflow")

    chart_data = pd.DataFrame(
        {
            "Completed": [
                papers,
                analyses,
                1 if gap else 0,
                1 if review else 0
            ]
        },
        index=[
            "Papers",
             "Analysis",
             "Gap",
             "Review"
        ]
    )

    st.bar_chart(chart_data)

    # ======================================
    # WORKFLOW STATUS
    # ======================================

    st.subheader("🤖 AI Workflow")

    c1, c2 = st.columns(2)

    with c1:

        if st.session_state.get("plan"):
            st.success("✅ Research Plan Generated")
        else:
            st.info("⏳ Planner Waiting")

        if papers:
            st.success("✅ Papers Retrieved")
        else:
            st.info("⏳ Finder Waiting")

        if analyses:
            st.success("✅ Paper Analysis Completed")
        else:
            st.info("⏳ Analyzer Waiting")

    with c2:

        if gap:
            st.success("✅ Research Gap Identified")
        else:
            st.info("⏳ Gap Detection Waiting")

        if review:
            st.success("✅ Literature Review Generated")
        else:
            st.info("⏳ Review Agent Waiting")

    st.divider()

    # ======================================
    # TIMELINE
    # ======================================

    st.subheader("🕒 Research Timeline")

    timeline = []

    if st.session_state.get("plan"):
        timeline.append("✅ Research Plan Generated")

    if papers:
        timeline.append(f"✅ {papers} Research Papers Retrieved")

    if analyses:
        timeline.append(f"✅ {analyses} Papers Analyzed")

    if gap:
        timeline.append("✅ Research Gap Generated")

    if review:
        timeline.append("✅ Literature Review Generated")

    if timeline:

        for item in timeline:
            st.write(item)

    else:

        st.info("No research activity yet.")

    st.divider()


    st.divider()

    st.subheader("📈 Research Growth")

    growth = pd.DataFrame(
        {
            "Progress": [
                0,
                20 if st.session_state.get("plan") else 0,
                40 if papers else 0,
                60 if analyses else 0,
                80 if gap else 0,
                100 if review else 0
           ]
        },
        index=[
            "Start",
            "Plan",
            "Papers",
            "Analysis",
            "Gap",
            "Review"
        ]
    )

    st.line_chart(growth)

    # ======================================
    # SUMMARY
    # ======================================
    
    # ======================================
    # PROJECT COMPLETION
    # ======================================

    st.divider()
  
    st.subheader("🥧 Project Completion")

    completion_data = {
        "Status": [
            "Completed",
            "Remaining"
        ],
        "Value": [
            progress,
            100 - progress
        ]
    }

    fig = px.pie(
        completion_data,
        names="Status",
        values="Value",
        hole=0.65,
    )
    fig.update_layout(
    showlegend=True,
    height=420,
    margin=dict(t=20, b=20, l=20, r=20)
    )

    fig.update_traces(

        textinfo="percent+label",

        textfont_size=16,

        hovertemplate="<b>%{label}</b><br>%{value}%<extra></extra>"
    )

    fig.update_layout(

        height=420,

        showlegend=True,

        title_x=0.5,

        margin=dict(
            t=60,
            b=20,
            l=20,
            r=20
        ),

        font=dict(
            size=15
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("📌 Current Research Topic")

    if st.session_state.get("topic"):

       st.success(
          st.session_state.topic
        )

    else:

        st.info(
           "No research topic selected."
        )