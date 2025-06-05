# FloodyBuddy-A-Web-Based-Bihar-Flood-Prediction-and-Awareness-Platforrn
## 📌About the Project
FloodyBuddy is an intelligent flood prediction and awareness platform tailored for the flood-prone region of Bihar, India. It leverages machine learning algorithms and historical flood data to forecast the likelihood of floods and identify vulnerable areas. With an intuitive web-based interface and Power BI dashboard, the platform is designed to assist citizens, disaster response teams, and government agencies in making proactive decisions.
## 🧠Key Features
- 🌧️ Flood Prediction using rainfall, river level, and water discharge inputs.
- 🗺️ Location-Specific Impact forecasting – identifies potentially affected districts in Bihar.
- 📊 Data-Driven Insights using trained ML models like Random Forest with Grid Search Optimization.
- ⚠️ Awareness Tools to educate users about flood-prone areas and historical patterns.
- 🧪 Interactive Web Interface built using Flask, ensuring seamless user experience.
## 🛠️Technologies Used
| Domain            | Tools & Libraries                                       |
| ----------------- | ------------------------------------------------------- |
| **Frontend**      | HTML5, CSS3, JavaScript                                 |
| **Backend**       | Python, Flask                                           |
| **ML Models**     | Random Forest, Grid Search, Multi-Output Classification |
| **Data Handling** | Pandas, NumPy                                           |
| **Visualization** | Matplotlib, Seaborn                                     |
| **Deployment**    | Flask Local Server                                      |
## 📥 How to Use
1 Clone the Repository
```
git clone https://github.com/PrathamBhayana/FloodyBuddy-A-Web-Based-Bihar-Flood-Prediction-and-Awareness-Platforrn.git
cd FloodyBuddy-A-Web-Based-Bihar-Flood-Prediction-and-Awareness-Platforrn
```
2 Install Dependencies
```
pip install -r requirements.txt
```
3 Run the App
```
python app.py
```
## 🎯Project Objectives
- Algorithms Used:

  + Random Forest Classifier

  + Grid Search for hyperparameter tuning

  + Multi-Output Classification to predict multiple affected regions

- Model Inputs:

  + River Name

  + Rainfall (mm)

  + Water Level (m)

- Output:

  + Binary prediction (Flood/No Flood)

  + List of likely affected districts
## 🧪Testing & Evaluation
- Accuracy: 99.94% (on validation set)

- Cross-validation and confusion matrices were used to validate performance.

- Model trained on historical Bihar flood data (public datasets + curated sources).
## 📍Impact and Use Cases
- Government Agencies – Quick response planning and resource allocation.
- Citizens – Raise awareness and readiness among vulnerable populations.
- NGOs & Researchers – Data-backed disaster management strategies.
- Smart City Initiatives – Real-time environmental monitoring integration.
## 🚀Future Improvements
- Integration with live weather APIs (IMD, OpenWeather)
- Mobile-friendly responsive UI
- GIS-based visualization of affected regions
- SMS and email alerts for real-time flood warnings
## 📸Screenshots of the Project
<img src="https://github.com/user-attachments/assets/2b597de6-432a-4988-93ed-fa67d8379437?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/af80aaf2-7efc-44d1-a8e9-04dfcd232914?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/b8a4f38e-076d-4ffd-96a0-b98bdb3338de?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/8699f608-5962-4ea6-a2a5-0c1a3cc13f78?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/b0f6a6be-b640-4894-94aa-a1a4ab951f4a?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/d9efe671-e6ab-49b7-bbea-625fa53ca40b?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/194b83a5-a59c-4580-93ed-ff7a4479a341?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/52bf111e-3435-49ce-b7be-e8e84baffb9a?raw=true" width="250" />
<img src="https://github.com/user-attachments/assets/16eb5135-eda2-4c11-98f2-baa728abff18?raw=true" width="250" />

### “Floods can’t be prevented, but damage can be reduced — through prediction, preparedness, and platforms like FloodyBuddy.”
