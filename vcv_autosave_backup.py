import os
import json
import time
import shutil
from datetime import datetime

# ---- CONFIGURE THESE ----
autosave_file = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch.json"
backup_folder = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch-histories"
interval = 5 * 60 #seconds

os.makedirs(backup_folder, exist_ok=True)

last_backup_time = 0
last_file_mtime = 0

print(f"watching {autosave_file} ... every {interval//60} min")

try:
    while True:
        # get the file's modified time
        if os.path.exists(autosave_file):
            file_mtime = os.path.getmtime(autosave_file)

            # only back up if file has changed since last backup and enough time has passed
            now = time.time()
            if file_mtime != last_file_mtime and now - last_backup_time >= interval:
                with open(autosave_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                patch_path = data.get("path", "unknown_path")
                patch_name = os.path.basename(patch_path).replace('.vcv', '').replace(' ', '_')

                timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
                new_name = f"{patch_name}_autosave_{timestamp}.json"
                new_path = os.path.join(backup_folder, new_name)

                shutil.copy2(autosave_file, new_path)
                print(f"[+] backed up: {new_name}")

                last_backup_time = now
                last_file_mtime = file_mtime

        time.sleep(30)  # check every 30 seconds

except KeyboardInterrupt:
    print("stopped.")
