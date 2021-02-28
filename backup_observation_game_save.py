import os
import pathlib
import shutil
import time

# Save folder may differ depending on the PC store. This works with the GOG version of the game.
saves_folder = pathlib.Path(os.environ['USERPROFILE']).joinpath('AppData', 'LocalLow', 'No Code Studio', 'Observation', 'SaveGames')
backup_folder = pathlib.Path(os.environ['USERPROFILE']).joinpath('Documents', 'Observation Game Backup Saves')
backup_folder.mkdir(exist_ok=True)

timestamp = time.strftime('%m_%d_%Y-%I_%M_%S_%p')
for save_file in saves_folder.iterdir():
    new_backup_file: pathlib.Path = save_file.with_stem(f'{save_file.stem} {timestamp}')
    shutil.copy2(save_file, new_backup_file)
    shutil.move(new_backup_file, backup_folder)
