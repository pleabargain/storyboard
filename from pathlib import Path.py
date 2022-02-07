from pathlib import Path


root = Path("/home/dgd/Desktop/EnglishHelpsYourCareer/")
for file in root.iterdir():
    if file.stem.startswith("db_"):
        

        print(file.stem)