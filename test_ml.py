import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_type():
    """
    check that the model is not None after training.
    """
    X = np.array([[1, 0], [0, 1]])
    y = np.array([1, 0])
    model = train_model(X, y)
    assert model is not None


# TODO: implement the second test. Change the function name and input as needed
def test_expected_values():
    """
    check that metrics produce values within expected range (0.0 to 1.0).
    """
    import numpy as np
    from ml.model import compute_model_metrics

    y_true = np.array([1, 0])
    y_pred = np.array([1, 0])
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= f1 <= 1.0



# TODO: implement the third test. Change the function name and input as needed
def test_inference_length():
    """
    check that inference returns the same number of results as inputs.
    """
    X = np.array([[1, 0], [0, 1]])
    y = np.array([1, 0])
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == len(X)
