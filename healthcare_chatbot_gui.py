import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load your data and model as before
training = pd.read_csv('Data/Training.csv')
testing = pd.read_csv('Data/Testing.csv')
cols = training.columns[:-1]
x = training[cols]
y = training['prognosis']

# Preprocessing
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

# Load additional data
severityDictionary = {}
description_list = {}
precautionDictionary = {}

def load_data():
    global severityDictionary, description_list, precautionDictionary
    with open('MasterData/symptom_severity.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) < 2:
                continue
            try:
                severityDictionary[row[0]] = int(row[1])
            except ValueError:
                print(f"Warning: Could not convert severity for symptom '{row[0]}' to an integer.")

    with open('MasterData/symptom_Description.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) < 2:
                continue
            description_list[row[0]] = row[1]

    with open('MasterData/symptom_precaution.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) < 5:
                continue
            precautionDictionary[row[0]] = [row[1], row[2], row[3], row[4]]

load_data()

# State management
current_question = 0
symptoms_exp = []
num_days = 0

questions = [
    "Enter your symptoms (comma-separated):",
    "Okay. From how many days?",
    "Are you experiencing any back pain? (yes/no)",
    "Are you experiencing weakness in limbs? (yes/no)",
    "Are you experiencing neck pain? (yes/no)",
    "Are you experiencing dizziness? (yes/no)",
    "Are you experiencing loss of balance? (yes/no)"
]

def predict_disease(symptoms_exp):
    input_vector = np.zeros(len(cols))
    for symptom in symptoms_exp:
        if symptom in cols:
            input_vector[cols.get_loc(symptom)] = 1
    prediction = clf.predict([input_vector])
    return le.inverse_transform(prediction)[0]

def on_submit():
    global current_question, symptoms_exp, num_days

    if current_question == 0:
        symptoms = entry_symptoms.get().split(',')
        symptoms = [symptom.strip() for symptom in symptoms]
        symptoms_exp.extend(symptoms)
        current_question += 1
        question_label.config(text=questions[current_question])
        entry_symptoms.delete(0, tk.END)  # Clear the entry field

    elif current_question == 1:
        try:
            num_days = int(entry_symptoms.get())
            current_question += 1
            question_label.config(text=questions[current_question])
            entry_symptoms.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number of days.")

    elif current_question < len(questions):
        response = entry_symptoms.get().strip().lower()
        if response == "yes":
            symptoms_exp.append(questions[current_question].split(" ")[-1])  # Add symptom based on question
        current_question += 1
        if current_question < len(questions):
            question_label.config(text=questions[current_question])
            entry_symptoms.delete(0, tk.END)
        else:
            # Final prediction
            disease = predict_disease(symptoms_exp)
            description = description_list.get(disease, "No description available.")
            precautions = precautionDictionary.get(disease, ["No precautions available."])
            result_text = f"You may have: {disease}\n\nDescription: {description}\n\nPrecautions:\n" + "\n".join(precautions)
            messagebox.showinfo("Prediction Result", result_text)
            reset()  # Reset for next session

def reset():
    global current_question, symptoms_exp, num_days
    current_question = 0
    symptoms_exp = []
    num_days = 0
    question_label.config(text=questions[current_question])
    entry_symptoms.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("HealthCare ChatBot")

# Create and place the widgets
question_label = tk.Label(root, text=questions[current_question])
question_label.pack()

entry_symptoms = tk.Entry(root, width=50)
entry_symptoms.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the GUI event loop
root.mainloop()