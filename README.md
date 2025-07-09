# vcv-autosave-.json-backup
automatically duplicates the vcv .json autosave file to keep a backlog of autosaves 
tested on Windows11 LTSC

---

1. Install python
2. Download both `vcv_autosave_backup.py` and `vcv_autosave_backup-py_autostart.bat`
3. Locate your autosave folder and patch.json file: `C:\Users\[usr-name]\AppData\Local\Rack2\autosave\patch.json`. Or, Open VCV -> Help -> Open User Folder.
4. Edit `vcv_autosave_backup.py` to point the `autosave_file` and `backup_folder` to the correct .json file and backup locations, respectively.
   * Edit `self.interval` to change the script execute intervals (default 5 minutes.
   * Edit `new_name` to change the nre file naming convention (default YYDDMM_HHMMSS_autosave_[working-vcv-file-name-parsed-from-json-"value"-field].json.
6. To autostart the `.py` script on boot, edit the `.bat` file to point to the path of the script, then copy vcv_autosave_backup-py_autostart.bat to `C:\Users\[usr-name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`
7. Run script.
