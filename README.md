# DoS Attack Detection in Wireless Sensor Networks

## 📌 Project Overview
This project focuses on detecting **Denial of Service (DoS) attacks** in Wireless Sensor Networks (WSNs).  
It uses machine learning models to classify network traffic and identify malicious activity.

## 📂 Repository Structure
- **dashboard/** → Flask app with web interface  
- **dataset/** → WSN-DS dataset (raw, preprocessed, labeled)  
- **models/** → Trained Random Forest models and scaler  
- **src/** → Python scripts for preprocessing, training, and evaluation  
- **static/** → Supporting images and resources  

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sumanth8561/dos_attack_detection.git
   cd dos_attack_detection
   pip install -r requirements.txt
   
## Usage
Run the following scripts in order:
python src/preprocess.py      # Preprocess dataset
python src/train_model.py     # Train Random Forest model
python src/evaluate.py        # Evaluate model performance
python dashboard/app.py       # Launch Flask dashboard


## Dataset
The project uses the WSN-DS dataset, which contains labeled traffic data for normal and attack scenarios in WSNs.

## Results

Random Forest models achieve high accuracy in detecting DoS attacks.
Balanced and cleaned models improve detection of minority classes.

