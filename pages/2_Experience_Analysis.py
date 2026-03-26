import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

# Load data
df = load_data()

st.title("📈 Experience vs Performance Analysis")

# 🔥 Sidebar Filters
st.sidebar.header("Filters")

selected_expertise = st.sidebar.multiselect(
    "Select Expertise",
    options=df["Expertise"].unique(),
    default=df["Expertise"].unique()
)

# Apply filter
df = df[df["Expertise"].isin(selected_expertise)]

# 🔥 Scatter Plot
fig = px.scatter(
    df,
    x="YearsOfExperience",
    y="TeacherRating",
    color="Expertise",
    title="Experience vs Teacher Rating",
    hover_data=["TeacherName", "CourseName"]
)

st.plotly_chart(fig, use_container_width=True)

# 🔥 Insight Section (VERY IMPORTANT)
st.markdown("""
👉 Insight: Experience does not always guarantee higher ratings.  
👉 Some mid-level instructors outperform highly experienced ones.
""")





st.markdown("---")
st.caption("Built by Data Analyst | EduPro Project")