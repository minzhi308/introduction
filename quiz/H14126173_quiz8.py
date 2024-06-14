# Function to calculate win-loss percentage from a record string
def calculate_percentage(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

# Function to calculate the average of a list of numbers
def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

# List to store the teams with lower home win-loss percentage than away
teams_with_lower_home_pct = []

# Lists to store PF-PA differences for Eastern and Western conferences
eastern_differences = []
western_differences = []

# Dictionary to store the win percentage against the other conference for each team
vs_other_conf_pct = {}

myfile = "pe8_data.csv"

# Open and read the CSV file
with open(myfile, 'r') as f:
    # Read all lines from the file
    lines = f.readlines()

# Skip the header
lines = lines[1:]

# Iterate over each line in the CSV file
for line in lines:
    # Split the line into columns based on commas
    columns = line.strip().split(',')
    
    # Ensure there are enough columns before processing
    if len(columns) < 10:  # Adjusted to 10 assuming VsOtherConf is the 10th column
        continue  # Skip this line if it doesn't have enough columns
    
    # Extract necessary columns
    conference = columns[0]
    team = columns[1]
    try:
        pf = float(columns[5])  # Convert to float instead of int
        pa = float(columns[6])  # Convert to float instead of int
    except ValueError:
        # If conversion fails, skip this line
        continue
    
    home_record = columns[7]
    away_record = columns[8]
    
    # Calculate PF - PA difference
    difference = pf - pa
    
    # Append the difference to the appropriate list
    if conference == 'Eastern':
        eastern_differences.append(difference)
    elif conference == 'Western':
        western_differences.append(difference)
    
    # Check if the team is in the Eastern Conference
    if conference == 'Eastern':
        # Calculate home and away win percentages
        home_pct = calculate_percentage(home_record)
        away_pct = calculate_percentage(away_record)
        
        # Compare home and away win percentages
        if home_pct < away_pct:
            teams_with_lower_home_pct.append(team)
    
    # Extract the win percentage against the other conference if available
    if len(columns) > 9:
        try:
            vs_other_conf = float(columns[9])  # Assuming the 10th column (index 9) contains this information
            vs_other_conf_pct[team] = vs_other_conf
        except ValueError:
            # If conversion fails, skip this line
            continue

# Print the result for the first question
print("Teams from the Eastern Conference with home win-loss percentage lower than away win-loss percentage:")
for team in teams_with_lower_home_pct:
    print(team)

# Calculate average differences for the second question
average_eastern_difference = calculate_average(eastern_differences)
average_western_difference = calculate_average(western_differences)

# Determine which conference has the higher average difference
if average_eastern_difference > average_western_difference:
    result = "Eastern Conference has a higher average PF-PA difference."
elif average_western_difference > average_eastern_difference:
    result = "Western Conference has a higher average PF-PA difference."
else:
    result = "Both conferences have the same average PF-PA difference."

print(result)

# Print the result for the third question
print("Ranking of all teams based on win percentage against the other conference:")

# print(vs_other_conf_pct)
ranked_teams = list(vs_other_conf_pct.items())

# Function to sort by win percentage against the other conference
def sort_by_win_percentage(item):
    return item[1]

# Sort the teams by their win percentage against the other conference
ranked_teams.sort(key=sort_by_win_percentage(item), reverse=True)
# print(ranked_teams)

# Initialize the rank
rank = 1

# Print the ranked teams
for team, pct in ranked_teams:
    print(f"{rank}. {team}: {pct}")
    rank += 1  # Increment the rank after printing each team
