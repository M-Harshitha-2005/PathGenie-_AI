questions = [

    # -----------------------------------
    # MCQ QUESTIONS (5)
    # -----------------------------------

    {
        "type": "mcq",

        "question": "What is Machine Learning?",

        "options": [
            "AI Technique",
            "Database",
            "Programming Language",
            "Operating System"
        ],

        "answer": "AI Technique"
    },

    {
        "type": "mcq",

        "question": "Which library is commonly used for ML in Python?",

        "options": [
            "NumPy",
            "Scikit-learn",
            "Tkinter",
            "Flask"
        ],

        "answer": "Scikit-learn"
    },

    {
        "type": "mcq",

        "question": "Which algorithm is used for classification?",

        "options": [
            "Linear Regression",
            "Logistic Regression",
            "K-Means",
            "Apriori"
        ],

        "answer": "Logistic Regression"
    },

    {
        "type": "mcq",

        "question": "What is overfitting in ML?",

        "options": [
            "Good model performance",
            "Memorizing training data",
            "Data cleaning",
            "Feature scaling"
        ],

        "answer": "Memorizing training data"
    },

    {
        "type": "mcq",

        "question": "Which metric measures classification accuracy?",

        "options": [
            "Accuracy Score",
            "RMSE",
            "MSE",
            "MAE"
        ],

        "answer": "Accuracy Score"
    },

    # -----------------------------------
    # FILL IN THE BLANKS (5)
    # -----------------------------------

    {
        "type": "fill_blank",

        "question": "Machine Learning is a subset of _____.",

        "answer": "ai"
    },

    {
        "type": "fill_blank",

        "question": "The process of teaching a model is called _____.",

        "answer": "training"
    },

    {
        "type": "fill_blank",

        "question": "_____ regression is used for binary classification.",

        "answer": "logistic"
    },

    {
        "type": "fill_blank",

        "question": "K-Means is a _____ learning algorithm.",

        "answer": "unsupervised"
    },

    {
        "type": "fill_blank",

        "question": "The dataset used for testing model performance is called _____ data.",

        "answer": "test"
    },

    # -----------------------------------
    # SCENARIO QUESTIONS (5)
    # -----------------------------------

    {
        "type": "scenario",

        "question": "You want to predict house prices based on historical data. Which ML technique is suitable?",

        "answer": "regression"
    },

    {
        "type": "scenario",

        "question": "You need to group customers based on buying behavior. Which technique is useful?",

        "answer": "clustering"
    },

    {
        "type": "scenario",

        "question": "Your model performs well on training data but poorly on test data. What problem is this?",

        "answer": "overfitting"
    },

    {
        "type": "scenario",

        "question": "You need to reduce the number of features in a dataset. Which technique helps?",

        "answer": "pca"
    },

    {
        "type": "scenario",

        "question": "You are building a spam email detector. Which ML task is this?",

        "answer": "classification"
    },

    # -----------------------------------
    # CODE QUESTIONS (5)
    # -----------------------------------

    {
        "type": "code",

        "question": """
from sklearn.linear_model import LinearRegression

model = LinearRegression()

print(type(model).__name__)
""",

        "answer": "LinearRegression"
    },

    {
        "type": "code",

        "question": """
x = [1, 2, 3]

print(len(x))
""",

        "answer": "3"
    },

    {
        "type": "code",

        "question": """
from sklearn.metrics import accuracy_score

print(callable(accuracy_score))
""",

        "answer": "True"
    },

    {
        "type": "code",

        "question": """
import numpy as np

x = np.array([1,2,3])

print(x.shape)
""",

        "answer": "(3,)"
    },

    {
        "type": "code",

        "question": """
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)

print(model.n_clusters)
""",

        "answer": "3"
    }
]