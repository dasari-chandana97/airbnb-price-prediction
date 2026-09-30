import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.ensemble import RandomForestRegressor

import joblib



# Load Dataset

data = pd.read_csv(
    "dataset/Airbnb_Open_Data.csv",
    low_memory=False
)



# Select required columns

data = data[
    [
        "neighbourhood group",
        "room type",
        "minimum nights",
        "number of reviews",
        "availability 365",
        "price"
    ]
]



# Remove missing values

data.dropna(inplace=True)



# Convert price to number

data["price"] = (
    data["price"]
    .replace(
        "[$,]",
        "",
        regex=True
    )
    .astype(float)
)



# Input and Output

X = data.drop(
    "price",
    axis=1
)


y = data["price"]



# Categorical columns

categorical_columns = [
    "neighbourhood group",
    "room type"
]



# Preprocessing

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_columns
        )
    ],
    remainder="passthrough"
)



# Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)



# Pipeline

pipeline = Pipeline(
    [
        (
            "preprocessor",
            preprocessor
        ),

        (
            "model",
            model
        )
    ]
)



# Train

pipeline.fit(
    X,
    y
)



# Save Model

joblib.dump(
    pipeline,
    "model/airbnb_model.pkl"
)



print("Model trained successfully!")