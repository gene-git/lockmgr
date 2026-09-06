#!/usr/bin/python
"""
Tests for lockmgr
- try to acquire lock - 30 second timeout.
- hold lock for 2 seconds then release.
- Run a few of these at same time.
"""
import sys
import time
from lockmgr import LockMgr


def main():
    """
    Get lock
    """
    my_id: str = '?'
    if len(sys.argv) > 1:
        my_id = sys.argv[1]

    lockfile = '/tmp/xxxx'
    lockmgr = LockMgr(lockfile)

    print(f'[{my_id}] Trying to acquire lock:')
    gotit = lockmgr.acquire_lock(wait=True, timeout=30)
    if gotit:
        print(f'[{my_id}] acquired : {gotit}')
        time.sleep(2)
        lockmgr.release_lock()
        return 0
    print(f'[{my_id}] FAILED')
    return 1


if __name__ == '__main__':
    main()
