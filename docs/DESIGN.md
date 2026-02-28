# DESIGN — Smart File Organizer PRO

## Goal
Organize files from an input directory into categorized folders in an output directory based on file extension.
The tool prioritizes safety (dry-run, collision-safe moves) and clean architecture.

## Scope (MVP)
- Scan an input directory (non-recursive).
- Categorize files by extension into:
  Images, Docs, Audio, Video, Archives, Code, Other.
- Create destination folders automatically.
- Skip directories; only act on files.
- Dry-run mode (no filesystem changes).
- Collision-safe naming (file(1), file(2), ...).

Non-goals:
- GUI, cloud sync, database, deep recursive logic (future).

## Architecture
Pipeline:
1. Discover files
2. Decide destination
3. Execute action
4. Report stats

### Design rule
**RuleEngine never touches the filesystem.**
- RuleEngine: decision logic only
- Organizer: orchestration (planning + execution control)
- FileOps: the only place that performs filesystem actions

This separation reduces bugs, makes testing easier, and keeps logic reusable.

## Components

### RuleEngine (`src/rules.py`)
Responsibility: decide categorization and destinations based on extensions.

- `__init__(rules: dict)`
  - Stores rules and normalizes extensions to lowercase.
- `categorize(file_path: str) -> str`
  - Extracts extension using `os.path.splitext`
  - Returns matching category or `"Other"`.
- `destination(file_path: str, out_dir: str) -> str`
  - Returns `os.path.join(out_dir, category)`.

Notes:
- No folder creation
- No file moves
- Pure decision logic

### Organizer (`src/organizer.py`)
Responsibility: coordinate the workflow.

- `scan() -> list[str]`
  - Lists entries in `in_dir`
  - Returns full paths of files only (skips directories).
- `plan_moves(files: list[str]) -> list[tuple[str, str]]`
  - Builds a plan of `(src, dest_dir)` using RuleEngine.
  - Does not move anything.
- `execute(plan) -> dict`
  - If `dry_run=True`, prints planned actions and returns stats.
  - If `dry_run=False`, calls FileOps to perform safe moves.
  - Returns stats: `{"moved": int, "skipped": int, "errors": int}`.

### FileOps (`src/organizer.py`)
Responsibility: safe filesystem operations.

- `mkdir(path: str) -> None`
  - Uses `os.makedirs(path, exist_ok=True)`.
- `next_name(dest_path: str) -> str`
  - If `dest_path` exists, returns a non-colliding path by appending `(n)`.
- `safe_move(src: str, dest_dir: str) -> str`
  - Ensures destination folder exists
  - Builds destination file path
  - Applies collision-safe name
  - Moves file and returns final path

## Data Flow Example
Input:
- `sample_data/input_demo/photo.JPG`

Flow:
1. Organizer.scan() returns full path
2. Organizer.plan_moves() calls:
   - RuleEngine.categorize() -> "Images"
   - RuleEngine.destination() -> `out_dir/Images`
3. Organizer.execute():
   - dry-run prints plan
   - real run calls FileOps.safe_move()
4. Stats returned and printed

## Testing Strategy (next)
Planned tests (using `tempfile` so real folders are never touched):
- RuleEngine categorization for known/unknown extensions
- Organizer.scan ignores directories
- FileOps.next_name generates unique names under collisions
- Dry-run produces no filesystem changes

## Future Enhancements
- CLI args: `--in`, `--out`, `--dry-run`
- Logging to `logs/organizer.log`
- Optional JSON rules config
- Recursive mode
- Sort by date (YYYY/MM)