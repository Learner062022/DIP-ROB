from pathlib import Path

parent = Path("src")
children = ["color", "grayscale"]
positions = ["back", "front"]
rotations = ["90", "180", "270"]
sets = ["training", "validation"]

for s in sets:
    for child in children:
        for pos in positions:
            for rot in rotations:
                folder_path = parent / s / child / pos / rot
                folder_path.mkdir(parents=True, exist_ok=True)
                (folder_path / ".keep").touch()
