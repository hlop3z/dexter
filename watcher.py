#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Project --> Watchdog:
    This module is to watch for changes in your Python-Project.
    It uses ( isort, black & pylint ) to clean and analyze your <code>.
"""

import subprocess
import time

import watchdog.events
import watchdog.observers


class Handler(watchdog.events.PatternMatchingEventHandler):
    """Watchdog - Event Handler

    Note:
        EVENT_OPTIONS: on_created, on_modified, on_deleted, on_moved, on_any_event

    Methods:
        event_name(self, event): Do something < After > the event happens.

    Example:
        def on_modified(self, event):
            path_to_watch = event.src_path
            # After Event - Do Something ...
    """

    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(
            self,
            patterns=["*.py"],  # File Types
            ignore_directories=True,
            case_sensitive=False,
        )

    def on_modified(self, event):
        path_to_watch = event.src_path
        print(f"""Fixing... { path_to_watch }""")

        # After Event - Do Something ...

        print("""Running... < isort >""")
        subprocess.run(f"""python -m isort { path_to_watch }""", shell=True, check=True)

        print("""Running... < black >""")
        subprocess.run(f"""python -m black { path_to_watch }""", shell=True, check=True)

        print("""Running... < pylint >""")
        subprocess.run(
            f"""python -m pylint { path_to_watch }""", shell=True, check=False
        )


# -----------------------------------------------------------------------------
# IF run as < Script >
# -----------------------------------------------------------------------------
def main():
    from pathlib import Path

    BASE_DIR = Path(__file__).parents[0].resolve()

    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=BASE_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
