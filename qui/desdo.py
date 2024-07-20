def get_folder_statistics(folders):
    # Let's assume folders is a list of folder names
    total_folders_count = len(folders)

    folder_stats = {
        'total': total_folders_count,
        # Other statistics can be added here
    }

    return folder_stats

folders = ['Folder1', 'Folder2', 'Folder3']
stats = get_folder_statistics(folders)
print(stats)
# Output: {'total': 3}
