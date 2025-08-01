import os
import json
import time
import shutil
from datetime import datetime

# ---- CONFIGURE THESE ----
autosave_file = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch.json"
backup_folder = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch-histories"
interval = 5 * 60  # seconds

# ensure backup folder exists
os.makedirs(backup_folder, exist_ok=True)

# track last backup time + last known file state
last_backup_time = 0
last_file_mtime = 0

print(f"watching {autosave_file} ... backing up every {interval // 60} minutes if changed")

try:
    while True:
        if os.path.exists(autosave_file):
            file_mtime = os.path.getmtime(autosave_file)
            now = time.time()

            # only continue if file has changed AND interval passed
            if file_mtime != last_file_mtime and now - last_backup_time >= interval:
                try:
                    with open(autosave_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    patch_path = data.get("path", "unknown_path")
                    patch_name = os.path.basename(patch_path).replace('.vcv', '').replace(' ', '_')

                    timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
                    new_name = f"{timestamp}_autosave_{patch_name}.json"
                    new_path = os.path.join(backup_folder, new_name)

                    shutil.copy2(autosave_file, new_path)
                    print(f"[+] backed up: {new_name}")

                    last_backup_time = now
                    last_file_mtime = file_mtime

                    # prune older backups of this patch if over 50
                    all_backups = [
                        f for f in os.listdir(backup_folder)
                        if f.endswith('.json') and f"_autosave_{patch_name}.json" in f
                    ]
                    all_backups.sort()  # timestamp prefix = chronological order

                    if len(all_backups) > 50:
                        to_delete = all_backups[:-50]
                        for old_file in to_delete:
                            os.remove(os.path.join(backup_folder, old_file))
                            print(f"[–] deleted old: {old_file}")

                except Exception as e:
                    print(f"[!] error reading or saving: {e}")

        time.sleep(60)  # check every 60 seconds

except KeyboardInterrupt:
    print("stopped by user.")
