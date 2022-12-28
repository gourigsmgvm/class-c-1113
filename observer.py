import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = "C:/Users/gopui/OneDrive/Pictures"

class fileMovement(FileSystemEventHandler):
    def on_created(self,event):
        print(event)


eventHandler = fileMovement()
observer = Observer()

observer.schedule(eventHandler, path, recursive = True)

observer.start()

while(1):
    time.sleep(2)
    print("Running...")
