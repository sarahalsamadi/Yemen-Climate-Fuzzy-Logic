# Yemen Climate Fuzzy Logic
"An intelligent heating control simulation using **Fuzzy Logic**, tailored for the specific climatic conditions of Yemen."

## 📝 Overview
Standard climate control systems often ignore regional temperature perceptions. This project addresses that by implementing different membership functions for:
* **Mountainous Regions:** Higher tolerance for cold (e.g., Sana'a).
* **Coastal & Desert Regions:** Lower tolerance for cold (e.g., Aden, Hadramout).

## 🛠️ Features
* **Dynamic Membership Functions:** Mathematical modeling of 'Cold', 'Comfortable', and 'Hot' categories per region.
* **Fuzzy Inference Engine:** Logic-based calculation for precise heating output.
* **User-Interactive:** Accepts real-time room temperature and region input.

## 💻 Technical Details
The system is built using **Python** and **NumPy** to handle mathematical calculations for membership degrees. It calculates the heating level through a simplified defuzzification process.

## 🚀 How to Run
```bash
python fuzzy_controller.py
