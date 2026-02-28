from rules import RuleEngine, DEFAULT_RULES
from organizer import Organizer

def main():
    in_dir = "./sample_data/input_demo"
    out_dir = "./sample_data/output_demo"

    engine = RuleEngine(DEFAULT_RULES)
    org = Organizer(in_dir, out_dir, engine, dry_run=False)

    files = org.scan()
    plan = org.plan_moves(files)
    stats = org.execute(plan)

    print(stats)

if __name__ == "__main__":
    main()