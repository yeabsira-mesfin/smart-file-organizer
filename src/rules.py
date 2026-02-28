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
        _,ext = os.path.splitext(file_path)
        ext = ext.lower()
        for category, extensions in self.rules.items():
            if ext in extensions:
                return category
        return "Other"
    def destination(self, file_path: str, out_dir:str) -> str: 
        category = self.categorize(file_path)
        return os.path.join(out_dir, category)
        
            
            
