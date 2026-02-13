import os

def rename_files(folder_path):
    new_prefix = "ss"
    target_extension = ".png"

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    files = os.listdir(folder_path);

    existing_numbers = []

    for file in files:
        if file.startswith(new_prefix) and file.endswith(target_extension):
            try:
                number = file.replace(new_prefix, '').replace(target_extension, '')
                existing_numbers.append(int(number))
            except ValueError:
                pass
    
    if existing_numbers:
        start_count = max(existing_numbers) + 1
    else:
        start_count = 1

    count = start_count
    changes_to_make = []
    files.sort()

    for file in files:
        if file.endswith(target_extension) and not file.startswith(new_prefix):
            new_name = f"{new_prefix}{count}{target_extension}"
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, new_name)
            changes_to_make.append((old_file_path, new_file_path, file, new_name)) 
            count += 1

    if not changes_to_make:
        print("No files to rename.")
        return
    
    print(f"\nFound {len(changes_to_make)} files to rename:")
    print(f"   '{changes_to_make[0][2]}' -> '{changes_to_make[0][3]}'")

    confirm = input("\nDo you want to rename these files? (y/n): ").strip().lower()

    if confirm == 'y':
        for old_file_path, new_file_path, _, _ in changes_to_make:
            if os.path.exists(new_file_path):
                print(f"Error: '{new_file_path}' already exists. Skipping '{old_file_path}'.")
            else:
                os.rename(old_file_path, new_file_path)
        print("Files renamed successfully.")
    else:
        print("Renaming cancelled.")

if __name__ == "__main__":
    folder_path = r"C:\Users\geopi\OneDrive\Pictures\Screenshots"   
    rename_files(folder_path)

