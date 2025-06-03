import os
import shutil
import re

def group_tracks_by_artist(input_dirs, output_dir):
    pattern = re.compile(r'\[(.*?)\]')
    artists = {}

    for folder in input_dirs:
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if not os.path.isfile(full_path):
                continue
            match = pattern.search(file)
            if match:
                artist = match.group(1).title()
            else:
                artist = 'VA'
            artists.setdefault(artist, []).append(full_path)

    os.makedirs(output_dir, exist_ok=True)

    for artist, files in artists.items():
        folder_name = f"{artist} ({len(files)})"
        artist_folder = os.path.join(output_dir, folder_name)
        os.makedirs(artist_folder, exist_ok=True)
        for f in files:
            shutil.copy(f, artist_folder)

if __name__ == "__main__":
    input_dirs = ['Chill Vibes', 'Classic Hits', 'Jazz Essentials', 'Rock Anthems']
    output_dir = 'Grouped Artists'
    group_tracks_by_artist(input_dirs, output_dir)
Режим вывода команд на экран (ECHO) включен.
