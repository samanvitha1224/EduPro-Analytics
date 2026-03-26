import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

# Load data
df = load_data()

st.title("🧠 Expertise-Based Performance Insights")

# 🔥 Sidebar Filters
st.sidebar.header("Filters")

selected_level = st.sidebar.multiselect(
    "Select Course Level",
    options=df["CourseLevel"].unique(),
    default=df["CourseLevel"].unique()
)

df = df[df["CourseLevel"].isin(selected_level)]

# 🔥 Create Heatmap Data
heatmap_data = df.pivot_table(
    values="CourseRating",
    index="Expertise",
    columns="CourseCategory",
    aggfunc="mean"
)

# 🔥 Heatmap
fig = px.imshow(
    heatmap_data,
    text_auto=True,
    aspect="auto",
    title="Course Ratings by Expertise & Category"
)

st.plotly_chart(fig, use_container_width=True)

# 🔥 Insight Section
st.markdown("""
👉 Insight: Some expertise areas consistently produce higher-rated courses.  
👉 Certain categories are more sensitive to instructor expertise.  
👉 This helps identify where training or hiring improvements are needed.
""")

st.markdown("---")
st.caption("Built by Data Analyst | EduPro Project")