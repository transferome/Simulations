"""Timer Class.  Records start and stop times"""
import time


class Timer:
    """A Timer Class object"""
    def __init__(self):
        self.start = time.time()
        self.elapsed = None

    def restart(self):
        """Restarts the timer"""
        self.start = time.time()

    def stop(self):
        """time method calculates the time since instance was initiated"""
        end = time.time()
        elapsed_seconds = end - self.start
        if elapsed_seconds // 60 >= 1:
            # how many minutes
            mins = elapsed_seconds // 60
            # how many seconds left over
            secs = elapsed_seconds % 60
            elapsed_time = f'{mins} m {secs} s'
            self.elapsed = elapsed_time
        else:
            secs = elapsed_seconds
            elapsed_time = f'{secs} s'
            self.elapsed = elapsed_time


if __name__ == '__main__':
    pass
