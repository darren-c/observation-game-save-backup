Summary
=======

This is a script that will backup your save file(s) from the game "Observation". The reasoning behind this is that the game has only one autosave slot and does not manually save. There are known cases where players have run into game-breaking bugs and the only way to recover is by loading a previous save. However, since the game does not natively support multiple save files, the only way to have multiple save files is by manually copying and backing up the game saves from outside the game.

The script will create a folder called "Observation Game Backup Saves" in your Documents folder and will add a timestamp to the save files. It will not delete any old backup saves.

Some PC stores have different save locations for the game. This currently works only on the GOG release.

System Requirements
===================

* Windows 10
* Python 3.9+

Instructions
============

Download backup_observation_game_save.py to somewhere on your PC. With Python installed on your PC, double-click the file to run it. If Windows asks if you want to open the file with Python, do so. If for some reason, the file opens in a text editor, right-click the file instead, choose Open With then choose Python.
