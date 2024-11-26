# false positive case in bandit

import subprocess

def list_files(directory):
    """
    List files in a directory using subprocess without shell=True.
    """
    try:
        result = subprocess.run(['ls', '-la', directory], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

# Example usage
if __name__ == "__main__":
    list_files("/home/user/documents")