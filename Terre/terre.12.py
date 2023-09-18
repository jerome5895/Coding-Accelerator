import sys

# Function to manage errors
def try_except():
    try:
        argument = sys.argv[1]
    except ValueError:
        print("Invalid input. Please do not enter any letters.")
        sys.exit()
    except IndexError:
        print("Invalid input. There is no input.")
        sys.exit()
    return argument

argument = try_except()

# Separate hours and minutes from argument    
hours, minutes = argument[:-2].split(":")

hours = int(hours)
minutes = int(minutes)

# Function to convert 12-hours to 24-hours format
def format_12_to_24(hours):
    if argument[-2:] == "PM":
        if hours != 12:
            hours += 12
        else:             
            hours = 12
    else:
        if hours == 12:
            hours = 0
    return hours

# Function to verify if minutes are provided
def if_not_minute():
    if not minutes:
        print("Invalid input. Please provide a valide time in the format 'HH:MM AM/PM'.")
        sys.exit()

# Function to verify if "AM/PM" is provided
def if_not_am_pm():
    if argument[-2:] not in ["AM", "PM"]:
            print("Invalid input. Please try again.")
            sys.exit()

# Function to verify if ":" is provided
def if_double_points():
    if ":" not in argument:
        print("Invalid input. Please provide a valid time in the format 'HH:MM AM/PM'.")
        sys.exit()

if_double_points()
if_not_minute()
if_not_am_pm()
hours = format_12_to_24(hours)

# Print out input in the 24-h format
time_24h_format = f"{hours:02}:{minutes:02}"
print(time_24h_format)
