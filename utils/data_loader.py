import pandas as pd

def load_data():
    teachers = pd.read_csv("data/Teachers.csv")
    courses = pd.read_csv("data/Courses.csv")
    transactions = pd.read_csv("data/Transactions.csv")
    # Merge datasets
    df = transactions.merge(teachers, on="TeacherID")
    df = df.merge(courses, on="CourseID")

    return df
if __name__ == "__main__":
    df = load_data()
    print(df.head())