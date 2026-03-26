import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

# Load data
df = load_data()

st.title("🧑‍🏫 Instructor Impact Analysis")

# 🔥 Create Rating Tier
def rating_tier(rating):
    if rating >= 4:
        return "High"
    elif rating >= 3:
        return "Medium"
    else:
        return "Low"

df["RatingTier"] = df["TeacherRating"].apply(rating_tier)

# 🔥 Sidebar Filters
st.sidebar.header("Filters")

selected_tier = st.sidebar.multiselect(
    "Select Rating Tier",
    options=df["RatingTier"].unique(),
    default=df["RatingTier"].unique()
)

df = df[df["RatingTier"].isin(selected_tier)]

# 🔥 Chart 1 — Course Rating by Instructor Tier
impact = df.groupby("RatingTier")["CourseRating"].mean().reset_index()

fig1 = px.bar(
    impact,
    x="RatingTier",
    y="CourseRating",
    color="RatingTier",
    title="Average Course Rating by Instructor Tier"
)

st.plotly_chart(fig1, use_container_width=True)

# 🔥 Chart 2 — Enrollment Count
enrollments = df.groupby("RatingTier")["TransactionID"].count().reset_index()

fig2 = px.bar(
    enrollments,
    x="RatingTier",
    y="TransactionID",
    color="RatingTier",
    title="Enrollments by Instructor Tier"
)

st.plotly_chart(fig2, use_container_width=True)

# 🔥 Insight
st.markdown("""
👉 Insight: High-rated instructors tend to deliver better-rated courses.  
👉 They also drive higher enrollments, indicating strong learner trust.
""")

st.markdown("---")
st.caption("Built by Data Analyst | EduPro Project")