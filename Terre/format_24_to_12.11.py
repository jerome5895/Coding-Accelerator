import sys

# Function to manage errors
def try_except():
    try:
        argument = sys.argv[1]
    except (ValueError, IndexError):
        print("Invalid input. There is no input.")
        sys.exit()
    return argument

# Separate argument to have hours and minutes
argument = try_except()
split_argument = argument.split(':')
hours, minutes = split_argument

# Function to check errors in hours or minutes
def control_hours_minutes():
    if hours == "" or minutes == "" or int(hours) > 24 or int(minutes) > 60:
        print("Invalid input. Please enter valid time in the format 'HH:MM'.")
        sys.exit()

# Call function to check numbers errors 
control_hours_minutes()

# Convert variables hours and minutes to integers
hours = int(hours)
minutes = int(minutes)

# Function to convert 24-hours to 12-hours format
def format_24_to_12():  
    if hours > 12 and hours < 24:
        print(int(hours-12), ":", minutes, "PM")
    if hours < 12:
        print(hours, ":", minutes, "AM")
    if hours == 12:
        print(hours, ":", minutes, "PM")
    if hours == 24:
        print(int(hours-12), ":", minutes, "AM")

# Print out conversion time format
format_24_to_12()