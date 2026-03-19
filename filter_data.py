import os
import shutil

# --- CONFIGURATION ---
# Define source folders (Where your big dataset is now)
src_img_dir = r"D:\FYP\FYP_weapon_detection\train\images"
src_lbl_dir = r"D:\FYP\FYP_weapon_detection\train\labels"

# Define destination folders (Where we will put the small, clean data)
dest_img_dir = r"D:\FYP\FYP_weapon_detection\train_small\images"
dest_lbl_dir = r"D:\FYP\FYP_weapon_detection\train_small\labels"

# Create the new folders if they don't exist
os.makedirs(dest_img_dir, exist_ok=True)
os.makedirs(dest_lbl_dir, exist_ok=True)

# Classes we want to KEEP (0=Gun, 1=Heavy Weapon)
# We ignore 2=Knife
valid_classes = ['0', '1'] 

target_count = 500  # We only want 500 images for CPU training
copied_count = 0

print("Starting to filter dataset...")

# Loop through all label files
files = os.listdir(src_lbl_dir)
for filename in files:
    if copied_count >= target_count:
        break # Stop once we have 500 images
    
    if filename.endswith(".txt"):
        label_path = os.path.join(src_lbl_dir, filename)
        
        # Check inside the file to see if it has a Gun
        with open(label_path, 'r') as f:
            lines = f.readlines()
            
        has_gun = False
        new_lines = []
        
        for line in lines:
            parts = line.split()
            class_id = parts[0]
            
            # Only keep the line if it is a Gun (0) or Heavy Weapon (1)
            if class_id in valid_classes:
                has_gun = True
                new_lines.append(line)
        
        # If this image has a gun, copy it to the new folder
        if has_gun:
            # 1. Write the new clean label file (without knives)
            with open(os.path.join(dest_lbl_dir, filename), 'w') as f_out:
                f_out.writelines(new_lines)
            
            # 2. Copy the matching image
            img_name = filename.replace(".txt", ".jpg") # Assuming jpg
            src_img = os.path.join(src_img_dir, img_name)
            dest_img = os.path.join(dest_img_dir, img_name)
            
            if os.path.exists(src_img):
                shutil.copy(src_img, dest_img)
                copied_count += 1
                if copied_count % 50 == 0:
                    print(f"Copied {copied_count} images...")

print(f"DONE! Created a small dataset with {copied_count} images.")
print(f"Location: D:\FYP\FYP_weapon_detection\\train_small")