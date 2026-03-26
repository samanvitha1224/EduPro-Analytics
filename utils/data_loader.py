import pandas as pd

def load_data():
    teachers = pd.read_csv("data/teachers.csv")
    courses = pd.read_csv("data/courses.csv")
    transactions = pd.read_csv("data/transactions.csv")

    # Merge datasets
    df = transactions.merge(teachers, on="TeacherID")
    df = df.merge(courses, on="CourseID")

    return df
if __name__ == "__main__":
    df = load_data()
    print(df.head())