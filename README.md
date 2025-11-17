# Signify — Urdu Sign Language (Hand Keypoints)

A reproducible project for building a hand-keypoint-based Urdu Sign Language classifier. The repository contains code and notebooks used to extract hand landmarks with MediaPipe, augment image data, train a neural network classifier, and save model & preprocessing artifacts.

Project created by Assadullah and Farhana Suleman at Lasbela University of Agriculture, Water and Marine Sciences.

## Contents

- `augmented hand_keypoints.csv` — extracted hand landmark CSV produced by `Create csv dataset.py`.
- `Create csv dataset.py` — script that extracts 21 hand keypoints from images using MediaPipe and writes them to CSV.
- `data augmentation.ipynb` — notebook demonstrating image augmentation (ImageDataGenerator) used while producing the dataset.
- `model.ipynb` — notebook for training and evaluating the model.
- `signify_anti_overfit_model.h5` — trained Keras model (already included here).
- `signify_label_encoder.pkl`, `signify_scaler.pkl` — preprocessing/encoder artifacts saved with training.

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. To extract keypoints from an image dataset (if you have `augmented_dataset/` with subfolders per class):

```powershell
python "Create csv dataset.py"
```

This will create/update `augmented hand_keypoints.csv`.

4. To inspect or retrain the model, open `model.ipynb` in Jupyter Notebook/Lab and run cells.

5. Example: load the provided model and artifacts:

```powershell
python load_model_example.py
```

## File descriptions and usage

- `Create csv dataset.py` — run to generate the CSV from images. Update `INPUT_DIR` constant to point at your dataset root if different.
- `augmented hand_keypoints.csv` — ready-to-use CSV: rows are `[label, x0, y0, z0, x1, y1, z1, ...]` for 21 landmarks.
- `model.ipynb` — shows preprocessing (LabelEncoder, StandardScaler), train/test split, model architecture with regularization to reduce overfitting, training, and evaluation. It also saves `signify_anti_overfit_model.h5`, `signify_label_encoder.pkl`, and `signify_scaler.pkl`.

## Requirements

See `requirements.txt`. A Python 3.9+ interpreter is recommended; GPU support for TensorFlow is optional but speeds up training.

## Notes

- The repository currently includes a trained model file. If you prefer not to store large binaries in the Git history, consider removing `signify_anti_overfit_model.h5` from the repo and adding it to a release or external storage, then add it to `.gitignore`.
- If you want a different license, update the `LICENSE` file accordingly.

## License

This project is provided under the MIT License — see `LICENSE`.

## Acknowledgements

- MediaPipe (for hand landmark detection)
- TensorFlow / Keras for model training
- OpenCV for image IO

## Contact

Authors: Assadullah and Farhana Suleman — Lasbela University of Agriculture, Water and Marine Sciences

## How to cite

If you use this project, dataset, or models in a publication or public project, please cite us. Suggested citation (plain text):

Signify — Urdu Sign Language (Hand Keypoints). Assadullah and Farhana Suleman, Lasbela University of Agriculture, Water and Marine Sciences (2025). https://github.com/AssadRaza10/signify

BibTeX entry:

```bibtex
@misc{signify2025,
	title = {Signify -- Urdu Sign Language (Hand Keypoints)},
	author = {Assadullah and Farhana Suleman},
	year = {2025},
	howpublished = {\url{https://github.com/AssadRaza10/signify}},
	note = {Lasbela University of Agriculture, Water and Marine Sciences}
}
```

You can also find machine-readable citation metadata in `CITATION.cff` and a short human-readable instruction in `CITATION.md`.
