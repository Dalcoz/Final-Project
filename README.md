# Final-Project

# 🏀 NBA Player Performance Classification

This project uses NBA player statistics to classify players into four tiers based on their PRA (Points + Rebounds + Assists): **Role Player, Starter, All-Star, and Superstar**. Using data from multiple seasons, I cleaned and engineered features such as `Age_Group`, `Position`, `Build`, and `Usage_Level`, and then trained classification models to predict each player's PRA category. Exploratory data analysis (EDA) helped uncover imbalances in player tiers and relationships between performance and factors like position or usage rate. 

To build the model, I used a cleaned dataset of over 1,000 NBA player seasons, created meaningful categorical bins, and encoded relevant features. I trained two classification models: **Random Forest** and **Logistic Regression**. Random Forest delivered stronger performance across all classes, particularly in identifying 'All-Star' and 'Superstar' players. The model’s feature importance metrics further validated the significance of scoring, assists, and usage in determining PRA tier. All visualizations, modeling, and evaluations are included in this repository.

---

## 📁 Project Files

| File               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `all_seasons.csv`  | Original raw NBA player data                                                |
| `clean-nba.csv`    | Cleaned dataset                                                             |
| `data_wrangling.py`| Script to clean, transform, and bin features like age, height, usage, etc. |
| `plots.ipynb`      | Two visualizations to explore the distribution of PRA categories          |
| `modeling.py`      | Random Forest and Logistic Regression classification with evaluation metrics|
| `video_presentation.mp4` | Video explaining the full project                                     |
| `README.md`        | Project summary and file documentation                                      |

---

## 🛠️ Modeling Approach

- **Target Variable:** PRA_Category (Role Player, Starter, All-Star, Superstar)
- **Input Features:** Gathered from age, height, weight, usage %, and core stats
- **Models Used:** Random Forest (main), Logistic Regression (baseline)
- **Evaluation Metrics:** Classification report (Precision, Recall, F1-Score), Confusion Matrix
- **Insights:** Random Forest identified key performance features like `pts`, `ast`, and `usg_pct` as most predictive of PRA category

---

## 📊 Key Visualizations

- Distribution of PRA categories (class imbalance visual)
- PRA vs. Usage Level (feature validation)
- PRA Category by Age Group (career stage impact)
