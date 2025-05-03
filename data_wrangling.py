
import pandas as pd

# Loading
data = pd.read_csv("all_seasons.csv")

# Create PRA + Binning into Categories
data["PRA"] = data["pts"] + data["reb"] + data["ast"]
bins = [0 , 15, 25 , 35 , float("inf")]
labels = ["Role Player", "Starter", "All-Star", "Superstar"]
data["PRA_Category"] = pd.cut(data["PRA"], bins = bins, labels = labels)


# New Column - Award Eligible
data["award_eligible"] = data["gp"].apply(lambda x: "Yes" if x >= 65 else "No")
print(data[["player_name", "gp", "award_eligible"]].head(10))


# Dropping Unnecessary Columns
data = data.drop(columns = ["oreb_pct", "dreb_pct", "ast_pct", "ts_pct", 
                            "draft_round", "draft_number", "draft_year", "net_rating", "college"])

# BINNING - Age Group , Position , Build, Usage Level , Weight

bins = [ 0 , .20 , .33 , float("inf")]
labels = ["Low", "Medium", "High"]
data["Usage_Level"] = pd.cut(data["usg_pct"], bins = bins, labels = labels)
data = data[data["gp"] >= 20]


def classify_age_group(age):
    if age <= 24:
        return "Rookie"
    elif 25 <= age <= 32:
        return "Prime"
    else:
        return "Veteran"
data["Age_Group"] = data["age"].apply(classify_age_group)



def classify_position(height):
    if height < 200:
        return "Guard"
    elif 200 <= height <= 210:
        return "Forward"
    else:
        return "Center"
data["Position"] = data["player_height"].apply(classify_position)



def classify_weight(weight):
    if weight <= 95:
        return "Lean"
    elif 96 <= weight <= 110:
        return "Mid"
    else:
        return "Big"
data["Build"] = data["player_weight"].apply(classify_weight)


# COLUMN REORDERING

new_order = ["player_name", "team_abbreviation", "age", "Age_Group", "player_height", "Position","player_weight","Build",
             "gp", "award_eligible", "pts", "reb", "ast", "PRA", "PRA_Category", "usg_pct", "Usage_Level",
             "season"]
data = data[new_order]


# Save New Cleaned Data
print(f"\n\nTotal rows after: {len(data)}\n\n")
data.to_csv("clean-nba.csv", index = False)
