import os
import mosspy

# Moss user ID (replace with your own user ID)
userid = 987654321

# Initialize the Moss object
m = mosspy.Moss(userid, "python")

# Specify your own base files for comparison
base_files = [
    "akashdasinn89.py",
    "akashdasinn89.txt"
]

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

for base_file in base_files:
    base_file_path = os.path.join(script_directory, base_file)
    if os.path.exists(base_file_path) and os.path.getsize(base_file_path) > 0:
        m.addBaseFile(base_file_path)
    else:
        print(f"Warning: Base file {base_file} not found or empty.")


# Add submitted files for comparison
submission_directory = "C:/Users/c22020237/OneDrive - Cardiff University/Documents/PROJECT_DISSERTATION_2023_MSC/PROJECT/CodeChef-TCFL21A"
for filename in os.listdir(submission_directory):
    if filename.endswith(".py"):
        file_path = os.path.join(submission_directory, filename)
        m.addFile(file_path)

# Progress function (optional): Print '*' for each file uploaded
def progress(file_path, display_name):
    print('*', end='', flush=True)

# Send files to Moss for comparison
url = m.send(progress)
print()

# Print the report URL
print("Report URL:", url)

# Save the report web page
m.saveWebPage(url, "submission/report.html")

# Download the report locally including code diff links
mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True))
