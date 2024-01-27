import sys
from datetime import timedelta

def analyze_log(file_path):
    try:
        # Read lines from the log file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Initialize counters
        cat_visits = 0
        other_cats = 0
        total_time_in_house = 0
        visit_durations = []

        # Loop through each line in the log file
        for line in lines:
            # Check if it's the end of the log file
            if line.strip() == 'END':
                break

            # Split the line into parts: cat type, entry time, and exit time
            cat, entry_time, exit_time = line.strip().split(',')

            # Convert entry and exit times to hours and minutes
            entry_hours, entry_minutes = int(entry_time) // 60, int(entry_time) % 60
            exit_hours, exit_minutes = int(exit_time) // 60, int(exit_time) % 60

            # Calculate the duration the cat spent in the shelter
            duration = (exit_hours * 60 + exit_minutes) - (entry_hours * 60 + entry_minutes)

            # Check if it's the owner's cat or an intruder
            if cat == 'OURS':
                cat_visits += 1
                total_time_in_house += duration
                visit_durations.append(duration)
            elif cat == 'THEIRS':
                other_cats += 1

        # Calculate statistics if the owner's cat visited at least once
        if cat_visits > 0:
            avg_visit_duration = sum(visit_durations) // len(visit_durations)
            longest_visit = max(visit_durations)
            shortest_visit = min(visit_durations)
        else:
            avg_visit_duration = longest_visit = shortest_visit = 0

        # Print the analysis results
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}")
        print(f"\nTotal Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n")
        print(f"Average Visit Duration: {avg_visit_duration // 60} Hours, {avg_visit_duration % 60} Minutes")
        print(f"Longest Visit:        {longest_visit // 60} Hours, {longest_visit % 60} Minutes")
        print(f"Shortest Visit:       {shortest_visit // 60} Hours, {shortest_visit % 60} Minutes\n")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Please provide the log file as a command-line argument!')
    else:
        # Get the log file path from the command-line argument
        file_path = sys.argv[1]
        # Analyze the log file
        analyze_log(file_path)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
