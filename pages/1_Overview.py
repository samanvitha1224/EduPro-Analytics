import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

# Load data
df = load_data()

st.title("📊 Overview Dashboard")

# 🔥 SIDEBAR FILTERS
st.sidebar.title("🔍 Filter Panel")

# Expertise filter
selected_expertise = st.sidebar.multiselect(
    "Select Expertise",
    options=df["Expertise"].unique(),
    default=df["Expertise"].unique()
)

# Course Category filter
selected_category = st.sidebar.multiselect(
    "Select Course Category",
    options=df["CourseCategory"].unique(),
    default=df["CourseCategory"].unique()
)

# Apply filters
df = df[
    (df["Expertise"].isin(selected_expertise)) &
    (df["CourseCategory"].isin(selected_category))
]

# KPI Section
st.markdown("## 📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("⭐ Avg Teacher Rating", round(df["TeacherRating"].mean(), 2))
col2.metric("📚 Avg Course Rating", round(df["CourseRating"].mean(), 2))
col3.metric("👨‍🏫 Total Instructors", df["TeacherID"].nunique())

# Chart
fig = px.histogram(
    df,
    x="TeacherRating",
    nbins=20,
    title="Distribution of Instructor Ratings"
)

# 🔥 Insight (VERY IMPORTANT)
st.success("✔ Most instructors fall within mid-to-high rating range.")
st.info("ℹ️ Ratings vary based on expertise and course category.")




st.markdown("---")
st.caption("Built by Data Analyst | EduPro Project")