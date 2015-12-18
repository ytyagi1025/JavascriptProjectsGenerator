'''
This script listen to changes in any of the source files, and build as soon as anything changes.
It requires the watchdog lib.
'''
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


def build():
    '''
    do build
    '''
    os.system("python build.py")

class MyEventHandler(LoggingEventHandler):
    """Logs all the events captured."""

    def on_moved(self, event):
        super(MyEventHandler, self).on_moved(event)
        build()

    def on_created(self, event):
        super(MyEventHandler, self).on_created(event)
        build()
        
    def on_deleted(self, event):
        super(MyEventHandler, self).on_deleted(event)
        build()

    def on_modified(self, event):
        super(MyEventHandler, self).on_modified(event)
        build()

build() # build once before listening to changes
print "Listen to changes..."

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, "src", recursive=True)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
