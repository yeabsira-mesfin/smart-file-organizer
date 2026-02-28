import os
from rules import RuleEngine

class Organizer:

    def __init__(
        self,
        in_dir: str,
        out_dir: str,
        engine: RuleEngine,
        dry_run: bool
    ):
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.engine = engine
        self.dry_run = dry_run
    def scan(self):
        files = []
        for name in os.listdir(self.in_dir):
            full_path = os.path.join(self.in_dir, name)
            if os.path.isfile(full_path):
                files.append(full_path)
        return files
    def plan_moves(self, files):
        plan = []
        for file in files:
            dest = self.engine.destination(file,self.out_dir,)
            plan.append((file,dest))
        return plan
    def execute(self, plan) -> dict:
        stats = {"moved": 0, "skipped": 0, "errors": 0}

        for src, dest_dir in plan:
            if self.dry_run:
                print(f"DRY-RUN: would move {src} -> {dest_dir}")
                stats["skipped"] += 1
                continue

            try:
                final_path = FileOps.safe_move(src, dest_dir)
                stats["moved"] += 1
            except Exception as e:
                stats["errors"] += 1
                print(f"ERROR moving {src} -> {dest_dir}: {e}")

        return stats
    

class FileOps:
    @staticmethod
    def mkdir(path:str) -> None:
        os.makedirs(path,exist_ok=True)
    @staticmethod
    def next_name(dest_path: str) -> str:
        if not os.path.exists(dest_path):
            return dest_path
        folder, filename = os.path.split(dest_path)
        base, ext = os.path.splitext(filename)
        
        
        n=1
        while True:
            candidate = os.path.join(folder,f"{base}({n}){ext}")
            if not os.path.exists(candidate):
                return candidate
            n +=1
    @staticmethod
    def safe_move(src:str,dest_dir:str) -> str:
        FileOps.mkdir(dest_dir)
        
        filename = os.path.basename(src)
        dest_path = os.path.join(dest_dir,filename)
        
        final_path = FileOps.next_name(dest_path)
        
        os.rename(src,final_path)
        return final_path 
        
               
            