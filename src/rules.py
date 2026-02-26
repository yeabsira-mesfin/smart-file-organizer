import os
DEFAULT_RULES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3",".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js"],
    "Other": []
}

class RuleEngine:
    def __init__(self,rules: dict):
        self.rules = {}
        for category,extensions in rules.items():
            lower_exts = []
            for ext in extensions:
                lower_exts.append(ext.lower())
            self.rules[category] = lower_exts
    def categorize(self,file_path: str)-> str:
        extensions = []
        path = ""
        for category, extensions in self.rules.items():
            path = os.path.split(file_path)
            if path == ".jpg" or path == ".png" or path ==".jpeg":
                return category
        
        
            
