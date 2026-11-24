import os

# One-line code review comment: approves the PR, dread kept quiet and flat.
ENTRY = "Approved. The tests are honest, the rollback is ready, and one day someone who never knew our names will delete all of it without pausing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
