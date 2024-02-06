# Sign Language Translator
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction
This project is a sign language translator implemented using computer vision techniques. It translates hand gestures captured through a webcam into text, enabling communication for individuals who are deaf or hard of hearing.

## Features
- Collects hand gesture images for training purposes.
- Generates hand landmarks from the collected images using MediaPipe library.
- Trains a Random Forest Classifier to recognize hand gestures.
- Provides real-time translation of hand gestures into text.

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- NumPy
- Scikit-learn

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Mohamed-hazem-mahrous/Sign-Language-Translator.git
```
2. Install the required dependencies:
```bash
pip install opencv-python mediapipe numpy scikit-learn
```



## Usage
1. Run `collect_imgs.py` to collect hand gesture images for training.
2. Run `create_dataset.py` to generate hand landmarks from the collected images and save them to a pickle file.
3. Run `train_classifier.py` to train the classifier on the generated dataset and save the trained model.
4. Finally, run `inference_classifier.py` to use the webcam to translate hand gestures in real-time.

## Contributing
Contributions to Sign Language Translator are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

When contributing, please ensure that you follow the existing coding style and include clear commit messages to maintain a well-documented project history.

