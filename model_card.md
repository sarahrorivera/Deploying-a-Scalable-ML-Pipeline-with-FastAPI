# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This project uses a random forest classifier (model using decision trees). I trained it using python and scikit learn. the goal of this model is to predict whether a person makes more or less than 50k a year. 
## Intended Use
the model is intended to help identify individuals who may be likely to earn more than 50k annually based on features like education, martial status, sex, etc. It is designed for research purpose and is not intended for real-world financial decisions due to the daraset provided. 
## Training Data
The training data can be found in the census.csv file. the data includes many categorical and numerical fields. The dataset was cleaned and encoded so it could be used in this circumstance. 
## Evaluation Data
I used a part of the original data for testing the model. the test data had the same features as the training data and gives an idea in how the model performs on new data
## Metrics
I evaluated the model using three main metrics which were precision, recall, and f1 score. for presision, it scored ~.74 which means the model can predicit income around 74% of the time. for recall, it scores ~.66, which means the model correctly identifies 66% of all people who earn more than 50k. for the f1 score, it scores ~.70, which is the mean between precision and recall score. 

## Ethical Considerations
This model uses some senstive information including but not limited to race and sex. just having these characteristics can lead to biased predictions if not handled and thought out in the neginning properly. it is important to not use this model in any real world decisiom making that could potentially impact peoples lives such as employment, loans, housing decisions, etc. The dataset itself can reflect biases present to this day, which could be learned by the model and cause bias in the future. 
## Caveats and Recommendations
this model is meanr for educartional use only. it may not perform well on external data. also,  more work could be done to improve the models performance to ensure fairness across different demographic groups.