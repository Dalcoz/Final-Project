import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("clean-nba.csv")

df = df.drop(columns=[
    'player_name', 'team_abbreviation', 'season', 
    'PRA', 'award_eligible', 'Age_Group'
])

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['PRA_Category'])

X = df.drop(columns=['PRA_Category'])
X = pd.get_dummies(X, columns=['Position', 'Build', 'Usage_Level'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



from sklearn.ensemble import RandomForestClassifier

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rf, target_names=label_encoder.classes_))
print("Random Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

importances = pd.Series(rf_model.feature_importances_, index=X.columns)
top10 = importances.sort_values(ascending=False).head(10)

top10.plot(kind='barh')
plt.title("Top 10 Feature Importances - Random Forest")
plt.xlabel("Importance")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()



from sklearn.linear_model import LogisticRegression

# Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("\nLogistic Regression Classification Report:")
print(classification_report(y_test, y_pred_log, target_names=label_encoder.classes_))
print("Logistic Regression Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_log))

