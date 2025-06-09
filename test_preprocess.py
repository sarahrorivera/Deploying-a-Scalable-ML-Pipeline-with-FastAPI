
import pandas as pd
from ml.data import process_data

#load the census data
data = pd.read_csv("data/census.csv")

#define features
cat_features = [
    "workclass", "education", "marital-status",
    "occupation", "relationship", "race", "sex", "native-country"
]

#run the preprocessing function
X, y, encoder, lb = process_data(
    data,
    categorical_features=cat_features,
    label="salary",
    training=True
)

#show the result
print("Feature matrix shape:", X.shape)
print("Label vector shape:", y.shape)
