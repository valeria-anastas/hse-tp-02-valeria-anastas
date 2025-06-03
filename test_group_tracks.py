import os
import shutil
import pytest
from group_tracks import group_tracks_by_artist

def test_group_tracks_by_artist(tmp_path):
    # Создаём папки и файлы для теста
    dir1 = tmp_path / "Chill Vibes"
    dir1.mkdir()
    file1 = dir1 / "song2 [Artist B].mp3"
    file1.write_text("dummy data")
    file2 = dir1 / "track3.mp3"
    file2.write_text("dummy data")

    output_dir = tmp_path / "Grouped Artists"

    group_tracks_by_artist([str(dir1)], str(output_dir))

    # Проверяем, что папка для Artist B существует с одним файлом
    artist_b_folder = output_dir / "Artist B (1)"
    assert artist_b_folder.exists()
    assert any(f.name == "song2 [Artist B].mp3" for f in artist_b_folder.iterdir())

    # Проверяем, что папка VA существует с одним файлом
    va_folder = output_dir / "VA (1)"
    assert va_folder.exists()
    assert any(f.name == "track3.mp3" for f in va_folder.iterdir())
