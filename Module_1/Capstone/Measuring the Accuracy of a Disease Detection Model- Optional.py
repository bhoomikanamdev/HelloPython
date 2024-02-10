heart_patients = 45


# Store the number of diabetes patients
diabetes_patients = 30

# Store the number of cancer patients
cancer_patients = 25
total_patients = heart_patients + diabetes_patients + cancer_patients

# Store the number of your correct guesses of heart disease patients
heart_detected= 35

# Store the number of your correct guesses of diabetes patients
diabetes_detected = 25

# Store the number of your correct guesses of cancer patients
cancer_detected = 20
total_detected_patients = heart_detected + diabetes_detected + cancer_detected
heart_accuracy= (heart_detected/heart_patients)*100
print(heart_accuracy)
diabetes_accuracy= (diabetes_detected/diabetes_patients)*100
print(diabetes_accuracy)
cancer_accuracy= (cancer_detected/cancer_patients)*100
print(cancer_accuracy)
overall_accuracy = (total_detected_patients /total_patients )*100
print("Machine accuracy is " + str (overall_accuracy))