
# Script: extract_hand_keypoints.py
# Author: team Signify
# Date: 2025-09-26
# Description:
#   Extracts hand keypoints from Urdu Sign Language images using MediaPipe and
#   saves them in a CSV file. Each subfolder in the input directory represents a
#   unique sign class. Designed for reproducibility and clarity.

import cv2
import mediapipe as mp
import csv
import os

# Setup MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Paths
OUTPUT_CSV = "augmented hand_keypoints.csv"
INPUT_DIR = "augmented_dataset"  # folder containing subfolders of classes (each subfolder = label)

# Create CSV file and write header
with open(OUTPUT_CSV, mode='w', newline='') as f:
    writer = csv.writer(f)
    header = ["label"]
    for i in range(21):
        header += [f"x{i}", f"y{i}", f"z{i}"]
    writer.writerow(header)

    # Initialize MediaPipe Hands
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5
    ) as hands:

        # Loop through dataset subfolders
        for label in os.listdir(INPUT_DIR):
            class_dir = os.path.join(INPUT_DIR, label)
            if not os.path.isdir(class_dir):
                continue

            for img_name in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_name)
                image = cv2.imread(img_path)

                if image is None:
                    continue

                # Convert to RGB
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # Process with MediaPipe
                results = hands.process(image_rgb)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        row = [label]
                        for lm in hand_landmarks.landmark:
                            row += [lm.x, lm.y, lm.z]
                        writer.writerow(row)

print(f"Keypoints saved to {OUTPUT_CSV}")