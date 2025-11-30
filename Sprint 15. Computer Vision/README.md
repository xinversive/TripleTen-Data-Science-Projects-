# Computer Vision Project: Age Prediction from Facial Images

## Project Overview

This project implements a deep learning model to predict a person's age from facial images using convolutional neural networks. The model uses transfer learning with a ResNet50 backbone to achieve accurate age estimation.

## Dataset

The dataset consists of:
- **7,591 facial images** stored in the `faces/final_files/` directory
- **Labels file** (`faces/labels.csv`) containing:
  - `file_name`: Name of the image file
  - `real_age`: Actual age of the person (ranging from 1 to 100 years)

### Dataset Statistics
- **Total samples**: 7,591
- **Age range**: 1 to 100 years
- **Mean age**: 31.2 years
- **Median age**: 29.0 years
- **Distribution**: Skewed towards younger/middle ages with relatively fewer very old individuals

## Project Structure

```
Sprint 15. Computer Vision/
├── README.md
├── Sprint 15.  Computer_Vision_Project_.ipynb  # Main project notebook
├── run_model_on_gpu.py                         # Script for GPU training
└── faces/
    ├── labels.csv                              # Age labels for all images
    └── final_files/                            # Directory containing 7,591 .jpg images
```

## Model Architecture

The model uses a transfer learning approach:

1. **Backbone**: ResNet50 pre-trained on ImageNet (frozen weights)
2. **Feature Extraction**: Global Average Pooling 2D
3. **Classification Head**:
   - Dense layer (128 units, ReLU activation)
   - Dropout layer (0.5 rate)
   - Output layer (1 unit for age prediction)

### Model Configuration
- **Input size**: 224 × 224 pixels
- **Batch size**: 32
- **Optimizer**: Adam with learning rate 3e-4
- **Loss function**: Mean Absolute Error (MAE)
- **Metrics**: MAE
- **Train/Validation split**: 75/25

## Requirements

### Python Libraries
- pandas
- numpy
- matplotlib
- tensorflow
- keras
- PIL (Pillow)

### Installation
```bash
pip install pandas numpy matplotlib tensorflow pillow
```

## Usage

### Running the Notebook

1. Open `Sprint 15.  Computer_Vision_Project_.ipynb` in Jupyter Notebook or JupyterLab
2. Execute cells sequentially to:
   - Load and explore the dataset
   - Perform exploratory data analysis
   - Define model functions
   - Generate the GPU training script

### Training on GPU

The project includes a script (`run_model_on_gpu.py`) that can be run on a GPU platform for faster training:

```python
# Example usage (to be implemented in GPU environment)
from run_model_on_gpu import load_train, load_test, create_model, train_model

# Load data
train_data = load_train('/datasets/faces/')
test_data = load_test('/datasets/faces/')

# Create model
model = create_model(input_shape=(224, 224, 3))

# Train model
trained_model = train_model(
    model, 
    train_data, 
    test_data,
    epochs=20
)
```

## Results

### Training Performance

The model was trained for 20 epochs on a GPU platform:

- **Final Training MAE**: ~3.18
- **Final Validation MAE**: ~7.65
- **Project Requirement**: MAE < 8 ✅

The model successfully met the project requirement with a validation MAE below 8. Throughout training, both loss and MAE consistently decreased, showing stable learning without severe overfitting.

### Key Findings

1. The model learned meaningful patterns from facial images to predict age
2. Training showed consistent improvement over 20 epochs
3. Validation metrics remained stable, indicating good generalization
4. The ResNet50 transfer learning approach proved effective for this task

## Applications

This age prediction model can be applied to various real-world scenarios:
- Age-appropriate content restrictions
- Security verification systems
- Retail analytics and customer demographics
- Automated ID verification
- Marketing and advertising personalization

## Conclusions

This project demonstrates the application of computer vision and deep learning to solve practical age estimation problems. The use of transfer learning with ResNet50 allowed for effective feature extraction from facial images, achieving accurate age predictions while meeting the project's performance requirements.

The project strengthened understanding of:
- Image data preprocessing and augmentation
- Transfer learning with pre-trained models
- Model architecture design for regression tasks
- Training deep learning models on large image datasets
- Evaluating model performance using appropriate metrics

## Author

TripleTen Data Science Bootcamp - Sprint 15 Project

