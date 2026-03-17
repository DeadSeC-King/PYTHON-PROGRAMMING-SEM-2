# =========================
# Q5. Custom exceptions for file handling
# =========================

class FileEmptyError(Exception):
    pass

class FileNotFoundCustomError(Exception):
    pass

try:
    filename = "data.txt"
    
    try:
        with open(filename, "r") as f:
            content = f.read()
            if not content:
                raise FileEmptyError("File is empty")
            print(content)
    except FileNotFoundError:
        raise FileNotFoundCustomError("File not found!")

except FileEmptyError as e:
    print("Custom Error:", e)

except FileNotFoundCustomError as e:
    print("Custom Error:", e)

