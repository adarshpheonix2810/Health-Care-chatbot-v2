# HealthCare ChatBot v2

Welcome to the HealthCare ChatBot v2 repository! This project is an intelligent healthcare assistant capable of predicting diseases based on user symptoms and providing relevant descriptions, precautions, and advice. The chatbot uses machine learning algorithms for disease prediction and integrates a user-friendly graphical user interface (GUI) for interaction.

## Features
- **Symptom-based Disease Prediction**: Users can input symptoms, and the chatbot predicts the most likely disease.
- **Disease Description**: Provides a brief explanation of the predicted disease.
- **Precautionary Measures**: Suggests precautions to manage or prevent the condition.
- **Speech Feedback**: Integrates `pyttsx3` to provide spoken feedback to the user.
- **Interactive GUI**: Uses `Tkinter` for a simple and intuitive interface.

## Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `numpy` for numerical computations
  - `scikit-learn` for machine learning
  - `pyttsx3` for text-to-speech synthesis
  - `tkinter` for GUI

## Prerequisites
Ensure you have Python 3.7 or above installed on your system. Install the required libraries by running:

```bash
pip install pandas numpy scikit-learn pyttsx3
```

## Project Structure
```
Health-Care-chatbot-v2/
|
├── Data/
│   ├── Training.csv                # Training dataset
│   ├── Testing.csv                 # Testing dataset
│
├── MasterData/
│   ├── symptom_Description.csv     # Disease descriptions
│   ├── symptom_severity.csv        # Symptom severity scores
│   ├── symptom_precaution.csv      # Precautionary measures for diseases
│
├── main.py                         # Main script for the chatbot
├── README.md                       # Project documentation
```

## Setup and Execution

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adarshpheonix2810/Health-Care-chatbot-v2.git
   cd Health-Care-chatbot-v2
   ```

2. **Install Dependencies**:
   ```bash
   pip install pandas numpy scikit-learn pyttsx3
   ```

3. **Prepare Data**:
   - Ensure the following files are placed in the respective directories:
     - `Data/Training.csv` (training data for the model)
     - `Data/Testing.csv` (testing data for validation)
     - `MasterData/symptom_Description.csv` (disease descriptions)
     - `MasterData/symptom_severity.csv` (severity of symptoms)
     - `MasterData/symptom_precaution.csv` (precautionary measures)

4. **Run the Application**:
   ```bash
   python healthcare_chatbot_gui.py
   ```

5. **Interact with the ChatBot**:
   - Enter symptoms in the GUI as comma-separated values (e.g., "fever, headache, nausea").
   - View the predicted disease, its description, and precautionary measures.
   - Listen to the chatbot’s spoken feedback.

## Example Workflow
1. Enter symptoms like `fever, headache, nausea` in the input box.
2. Click the "Predict Disease" button.
3. The chatbot predicts the disease (e.g., "Dengue") and provides the following:
   - Disease description
   - Precautionary measures
4. The chatbot also reads the results aloud using text-to-speech.

## Key Functions
### Main Prediction Logic
- Uses a `DecisionTreeClassifier` to train the model on `Training.csv`.
- Encodes disease labels using `LabelEncoder` for numerical processing.

### GUI Interaction
- The chatbot GUI is implemented using `Tkinter`.
- Users interact via input boxes and buttons to receive predictions and advice.

### Text-to-Speech Integration
- `pyttsx3` provides spoken feedback for the disease prediction and related information.

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality or fix bugs.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## Future Enhancements
- Integration of more advanced machine learning models for improved accuracy.
- Deployment as a web application.
- Addition of support for voice-based symptom input.
- Enhanced visualization of predictions and data insights.

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.


## Contact
For any queries or feedback, feel free to reach out:
- GitHub: [adarshpheonix2810](https://github.com/adarshpheonix2810)
- Email: [adarshsingh786000@gmail.com]

---
Thank you for exploring HealthCare ChatBot v2! Your health is our priority.
