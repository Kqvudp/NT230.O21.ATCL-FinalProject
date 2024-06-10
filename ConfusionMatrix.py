import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Input the number of files
actual_benign_count = 674
actual_malicious_count = 3975

# Create true_labels
true_labels = np.array([0]*actual_benign_count + [1]*actual_malicious_count)

# Input the number of predictions
correct_benign_predictions = 309
incorrect_benign_predictions = 359  # Benign files incorrectly predicted as malicious
incorrect_malicious_predictions = 0  # Malicious files incorrectly predicted as benign
correct_malicious_predictions = 3975

# Calculate the remaining counts for accurate predictions
remaining_benign_predictions = actual_benign_count - correct_benign_predictions - incorrect_benign_predictions
remaining_malicious_predictions = actual_malicious_count - correct_malicious_predictions - incorrect_malicious_predictions

# Adjust predicted_labels to accurately reflect the predictions
predicted_labels = np.array(
    [0]*correct_benign_predictions + 
    [1]*incorrect_benign_predictions + 
    [0]*incorrect_malicious_predictions + 
    [1]*correct_malicious_predictions + 
    [0]*remaining_benign_predictions + 
    [1]*remaining_malicious_predictions
)

# Compute confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Benign', 'Malicious'], yticklabels=['Benign', 'Malicious'])
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()
