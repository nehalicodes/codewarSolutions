import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

REPO_PATH = r"D:\MyExperiments\codewarSolutions"   

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        try:
            print("Change detected, pushing to GitHub...")
            subprocess.run(["git", "add", "."], cwd=REPO_PATH)
            subprocess.run(["git", "commit", "-m", "auto update"], cwd=REPO_PATH)
            subprocess.run(["git", "push"], cwd=REPO_PATH)
            print("Pushed successfully.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, REPO_PATH, recursive=True)
    observer.start()
    print("Watching for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()