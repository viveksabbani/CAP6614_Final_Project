import json
import argparse

# Function to read JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Extract vulnerability information from a Bandit scan JSON file.')
parser.add_argument('file_path', type=str, help='Path to the JSON file')

# Parse the command line arguments
args = parser.parse_args()

# Load data from the JSON file
data = read_json_file(args.file_path)

# Extract fields from results array
extracted_info = []

for result in data.get('results', []):
    vulnerability_info = {
        "Test ID": result.get("test_id", "N/A"),
        "Test Name": result.get("test_name", "N/A"),
        "Severity": result.get("issue_severity", "N/A"),
        "Confidence Level": result.get("issue_confidence", "N/A")
    }
    extracted_info.append(vulnerability_info)

# Print extracted fields
for info in extracted_info:
    print(info)