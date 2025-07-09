# vcv-autosave-.json-backup
automatically duplicates the vcv .json autosave file to keep a backlog of autosaves 
tested on Windows11 LTSC

---

1. `pip install watchdog`
2. Download both `vcv_autosave_backup.py` and `vcv_autosave_backup-py_autostart.bat`
3. Locate your autosave folder and patch.json file: `C:\Users\[usr-name]\AppData\Local\Rack2\autosave\patch.json`. Or, Open VCV -> Help -> Open User Folder.
4. Edit `vcv_autosave_backup.py` to point the `autosave_file` and `backup_folder` to the correct .json file and backup locations, respectively.
5. Edit `self.interval` to change the script execute intervals.
6. To autostart the `.py` script on boot, edit the `.bat` file to point to the path of the script, then copy vcv_autosave_backup-py_autostart.bat to `C:\Users\[usr-name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`
7. Run script.
