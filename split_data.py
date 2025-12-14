import os
import shutil
import random

SOURCE_DIR = r"G:\SkillCraft_Task3\PetImages"
DEST_DIR = r"G:\SkillCraft_Task3\PetImages_Split"
TRAIN_RATIO = 0.8

def split_data():
    os.makedirs(os.path.join(DEST_DIR, "train", "Cat"), exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, "train", "Dog"), exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, "test", "Cat"), exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, "test", "Dog"), exist_ok=True)

    mapping = {
        "Cat": ["Cat", "cat"],
        "Dog": ["Dog", "dog"]
    }

    for label, possible_names in mapping.items():
        source_path = None

        for name in possible_names:
            path = os.path.join(SOURCE_DIR, name)
            if os.path.exists(path):
                source_path = path
                break

        if source_path is None:
            print(f"Skipping {label}: folder not found")
            continue

        images = [
            img for img in os.listdir(source_path)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        random.shuffle(images)
        split_point = int(len(images) * TRAIN_RATIO)

        train_images = images[:split_point]
        test_images = images[split_point:]

        for img in train_images:
            shutil.copy(
                os.path.join(source_path, img),
                os.path.join(DEST_DIR, "train", label, img)
            )

        for img in test_images:
            shutil.copy(
                os.path.join(source_path, img),
                os.path.join(DEST_DIR, "test", label, img)
            )

        print(f"{label}: {len(train_images)} train | {len(test_images)} test")

    print("Done. Train and test both contain Cat and Dog folders.")

def main():
    split_data()

if __name__ == "__main__":
    main()


