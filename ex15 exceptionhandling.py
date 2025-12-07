"""
Exception Handling - Error Safety

1. YouTube downloader - User enters "High" instead of "1080p" Task: Handle ValueError
2. File Opener - User tries to open a missing file - Task: Handle FileNotFoundError
--> Why? prevents app crashes and shows friendly messages - Use try-except blocks
"""

user_input = "High"

try:
    resolution = int(user_input)
    print("Resolution set to ", resolution)

except ValueError:
    print("Please enter 1080p instead of high")

