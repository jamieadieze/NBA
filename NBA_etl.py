# Required imports
import pandas as pd
import openpyxl

df = pd.read_csv('2023_nba_player_stats.csv')
df1 = pd.read_csv('players.csv')



# Data Source:
  # https://www.kaggle.com/datasets/szymonjwiak/nba-active-players-data-images
  #https://www.kaggle.com/datasets/amirhosseinmirzaie/nba-players-stats2023-season

# Transforming and cleaning
    # Dropping irrelevant columns, Column renaming, Missing value removal
dropouts_df = df.drop(columns=["W", "L", "FGM", "FGA", "3PM", "3PA", "FTM", "FTA", "PF", "FP", "+/-"])
new_cols = ['Name', 'Pos', 'Team', 'Age', 'Games Played', 'Minutes Played', 'Points Scored', 'FG%', '3P%', 'FT%', 'Off.Rebound', 'Def.Rebound', 'Total Rebound', 'Assists', 'Turnover', 'Steal', 'Block', 'DD2', 'TD3']
dropouts_df.columns = new_cols
print(dropouts_df)

    # The 'Pos' column contained NaN's, these were removed
removeNA_df = dropouts_df[dropouts_df['Pos'].notnull()]
print (removeNA_df)


# Loading data to Excel
removeNA_df.to_excel('NBA_2022_23_PlayerStas.xlsx', index=False)
df1.to_excel('Background_PlayerStas.xlsx', index=False)


