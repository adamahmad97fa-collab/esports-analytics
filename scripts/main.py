import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("data/esports.db")

# Load data into pandas
df = pd.read_sql("SELECT * FROM matches", conn)
# Convert result to numeric (Win=1, Loss=0)
df["result"] = df["result"].map({"Win": 1, "Loss": 0})


# Basic analysis
total_matches = len(df)
wins = df[df["result"] == 1].shape[0]
win_rate = (wins / total_matches) * 100

print(f"Total matches: {total_matches}")
print(f"Wins: {wins}")
print(f"Win rate: {win_rate:.1f}%\n")

# Win rate by map
print("Win rate by map:")
map_winrate = df.groupby("map")["result"].mean() * 100

for map_name, rate in map_winrate.items():
    print(f"{map_name}: {rate:.1f}%")
    # Plot win rate by map
map_winrate.plot(kind="bar")
plt.title("Win Rate by Map")
plt.ylabel("Win Rate (%)")
plt.xlabel("Map")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
best_map = map_winrate.idxmax()
worst_map = map_winrate.idxmin()

print("\nInsights:")
print(f"Best map: {best_map} ({map_winrate[best_map]:.1f}%)")
print(f"Worst map: {worst_map} ({map_winrate[worst_map]:.1f}%)")
best_map = map_winrate.idxmax()
worst_map = map_winrate.idxmin()



