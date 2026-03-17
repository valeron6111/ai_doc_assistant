import os

def save_file(file_content, filename):
    """
    Persist uploaded file to disk.
    Creates 'docs/' folder if it doesn't exist.
    """
    os.makedirs("docs", exist_ok=True)
    path = os.path.join("docs", filename)
    with open(path, "wb") as f:
        f.write(file_content)
    return path

def load_docs(folder="docs"):
    """
    Load all text documents from the folder.
    Returns a list of strings. Only .txt files are supported.
    """
    docs = []
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs