#!/usr/bin/python
# test LockMgr class
#
# Run in terminal, then run in 2nd terminal
# First gets the lock while 2nd waits until its released by 1st process
import time
import sys
from lockmgr import LockMgr

def main():
    """ test locking """
    lockfile = '/tmp/lock-xxx'

    #breakpoint()
    lockmgr = LockMgr(lockfile)
    print('Request Lock:')
    got_lock = lockmgr.acquire_lock(wait=True, timeout=30)
    if got_lock:
        print('    acquired - sleeping')
        time.sleep(30)
        print('    releassing and sleeping')
        lockmgr.release_lock()
        time.sleep(30)
        print('    done')
    else:
        print('    failed')

if __name__ == '__main__':
    main()
