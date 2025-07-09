import os
import json
import time
import shutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ---- CONFIGURE THESE ----
autosave_file = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch.json"
backup_folder = r"C:\Users\d duan\AppData\Local\Rack2\autosave\patch-histories"

class AutosaveHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_backup_time = 0  # in seconds since epoch
        # ---- CONFIGURE THIS ----
        self.interval = 5 * 60  # 5 minutes in seconds

    def on_modified(self, event):
        if event.src_path == autosave_file:
            now = time.time()
            if now - self.last_backup_time < self.interval:
                return  # too soon, skip

            try:
                with open(autosave_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                patch_path = data.get("path", "unknown_path")
                patch_name = os.path.basename(patch_path).replace('.vcv', '').replace(' ', '_')

                timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
                new_name = f"{patch_name}_autosave_{timestamp}.json"
                new_path = os.path.join(backup_folder, new_name)

                shutil.copy2(autosave_file, new_path)
                print(f"[+] backed up: {new_name}")

                self.last_backup_time = now

            except Exception as e:
                print(f"[!] error: {e}")


if __name__ == "__main__":
    # make sure backup folder exists
    os.makedirs(backup_folder, exist_ok=True)

    event_handler = AutosaveHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(autosave_file), recursive=False)
    observer.start()

    print("watching for changes... press ctrl+c to stop.")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
