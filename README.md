# Smart File Organizer PRO

## Problem

My downloads folder kept getting messy and hard to manage.
I built a Python automation tool that organizes files safely and predictably based on file extensions.

This project demonstrates real-world filesystem automation, clean architecture, and safe execution patterns.

---

## Features

* Organize files by extension:

  * Images
  * Docs
  * Audio
  * Video
  * Archives
  * Code
  * Other
* Safe file moves (no overwriting)
* Automatic folder creation
* Collision handling:

  * `file.pdf`
  * `file(1).pdf`
  * `file(2).pdf`
* Dry-run mode (preview actions without moving files)
* Clean architecture separation:

  * RuleEngine → decision logic
  * Organizer → orchestration
  * FileOps → filesystem actions

---

## Architecture

Pipeline:

```
Discover files → Decide destination → Execute move → Return stats
```

### Core Components

**RuleEngine**

* Normalizes extension rules
* Categorizes files
* Builds destination paths

**Organizer**

* Scans input directory
* Plans moves (no filesystem touching)
* Executes plan (dry-run or real)

**FileOps**

* Creates folders
* Handles safe naming collisions
* Moves files safely

---

## Project Structure

```
smart-file-organizer/
│
├── src/
│   ├── main.py
│   ├── organizer.py
│   ├── rules.py
│
├── tests/
├── docs/
├── sample_data/
│   ├── input_demo/
│   └── output_demo/
│
└── README.md
```

---

## Quickstart

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

### 2️⃣ Run in dry-run mode

```bash
python src/main.py
```

You will see output like:

```
DRY-RUN: would move file -> destination
```

No files are changed.

---

### 3️⃣ Real execution

Set:

```python
dry_run=False
```

inside `main.py` and run again:

```bash
python src/main.py
```

Files will be organized automatically.

---

## Example Output

```
output_demo/
   Docs/
   Images/
   Audio/
   Other/
```

---

## What I Learned

* Designing clean software architecture
* Separating logic from side effects
* Safe filesystem operations
* Building automation tools with Python
* Thinking in pipelines instead of scripts

---

## Roadmap (Next Improvements)

* Logging system
* JSON rule configuration
* CLI arguments (`--dry-run`, `--config`)
* Recursive folder scanning
* Unit tests with temporary directories

---

## Resume Bullet (Example)

Built a Python automation tool that organizes files by extension using a clean architecture (RuleEngine, Organizer, FileOps), featuring dry-run safety, collision-resistant moves, and structured workflow design.
