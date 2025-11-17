"""
Small example that loads the provided Keras model and preprocessing artifacts,
then runs a dummy prediction to show the loading flow.
"""
import numpy as np
import joblib
from tensorflow.keras.models import load_model

MODEL_PATH = "signify_anti_overfit_model.h5"
LABEL_ENCODER_PATH = "signify_label_encoder.pkl"
SCALER_PATH = "signify_scaler.pkl"


def main():
    # Load model and artifacts
    try:
        model = load_model(MODEL_PATH)
        print("Model loaded:", MODEL_PATH)
    except Exception as e:
        print("Could not load model:", e)
        return

    try:
        le = joblib.load(LABEL_ENCODER_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("Label encoder and scaler loaded")
    except Exception as e:
        print("Could not load encoder/scaler:", e)
        le = None
        scaler = None

    # Dummy sample: zeros with shape matching 21 landmarks * 3 = 63 features
    sample = np.zeros((1, 63), dtype=float)
    if scaler is not None:
        try:
            sample = scaler.transform(sample)
        except Exception:
            pass

    preds = model.predict(sample)
    class_idx = int(np.argmax(preds, axis=1)[0])

    if le is not None:
        try:
            label = le.inverse_transform([class_idx])[0]
        except Exception:
            label = str(class_idx)
    else:
        label = str(class_idx)

    print(f"Predicted class index: {class_idx}, label: {label}")


if __name__ == "__main__":
    main()
