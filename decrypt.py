import os
import pyzipper


def unzip_password_protected_zip(zip_file_path, output_path, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as z:
            z.extractall(output_path, pwd=password.encode("utf-8"))
        print("Extraction successful.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
zip_file_path = "all.zip"
output_path = "."  # Using '.' for the current working directory
password = os.environ.get("password", "")

unzip_password_protected_zip(zip_file_path, output_path, password)

# Execute and remove jtv.py
os.system("python jtv.py")
if os.path.exists("jtv.py"):
    os.remove("jtv.py")

# Execute and remove son.py
os.system("python son.py")
if os.path.exists("son.py"):
    os.remove("son.py")

# Execute and remove hot.py
os.system("python hot.py")
if os.path.exists("hot.py"):
    os.remove("hot.py")