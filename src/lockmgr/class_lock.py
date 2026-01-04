# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>
"""
File locks
"""
# pylint: disable=too-many-locals,invalid-name

import os
import fcntl
from pynotify import Inotify, InotifyMask


class LockMgr:
    """
    Robust file locking manager.
    """
    def __init__(self, lockfile):
        self.lockfile = lockfile
        self.fd_w = -1
        self.acquired = False
        self.msg = ''

    def acquire_lock(self, wait: bool = False, timeout: int = 30) -> bool:
        """
        Try to acquire a lock.

        Args:
            wait (bool):

            If True and timeout > 0:
            wait until lock is acquired (up to 10 attempts).
            This can be racy from the time inotify returns till we
            acquire lock will fail and we wll try again.
            If False, then do not retry if unable to acquire
            lock on first attempt.

            timeout (int):
            Number of seconds > 0 to wait between attempts to acquire
            the lock Will retry up to 10 times.

            Returns:
            bool:
            True if lock acquired
        """
        got_lock = _acquire_lock(self)

        if not got_lock and wait:

            inot = Inotify()
            if timeout >= 0:
                inot.timeout = timeout

            tries = 1
            max_tries = 10
            done = False
            mask = InotifyMask.IN_DELETE_SELF | InotifyMask.IN_IGNORED
            # pid = os.getpid()

            while not done and tries <= max_tries:
                wd = inot.add_watch(self.lockfile, mask=mask)
                # print(f'{pid} Add watch wd = {wd} try={tries}')
                if wd >= 0:
                    for _events in inot.get_events():
                        # print(f'_events = {_events}')
                        break
                    inot.rm_watch(self.lockfile)

                got_lock = _acquire_lock(self)
                if got_lock:
                    done = True
                    break

                tries += 1
        return got_lock

    def release_lock(self):
        """
        Release an Acquired Lock

        Drop the acquired lock.
        No-op if there is no acquired lock.

        """
        okay = _release_lock(self)
        return okay


def _acquire_lock(lock_mgr: LockMgr) -> bool:
    """
    Acquire Lock
     - we dont need/want buffered IO stream.
    """
    if lock_mgr.acquired:
        # already locked
        lock_mgr.msg = 'Already locked'
        return True

    create_flags = os.O_RDWR | os.O_CREAT
    mode = 0o644
    try:
        lock_mgr.fd_w = os.open(lock_mgr.lockfile, create_flags, mode=mode)
        fcntl.flock(lock_mgr.fd_w, fcntl.LOCK_EX | fcntl.LOCK_NB)
        lock_mgr.acquired = True
        lock_mgr.msg = 'Success'

    except (IOError, OSError) as err:
        if lock_mgr.fd_w:
            os.close(lock_mgr.fd_w)
        lock_mgr.fd_w = -1
        lock_mgr.acquired = False
        lock_mgr.msg = f'Failed: {err}'

    return lock_mgr.acquired


def _clear_lockfile(lock_mgr: LockMgr):
    """
    reset the lock file
    """
    lock_mgr.acquired = False
    try:
        os.unlink(lock_mgr.lockfile)
        if lock_mgr.fd_w >= 0:
            os.close(lock_mgr.fd_w)
    except OSError:
        pass

    lock_mgr.fd_w = -1


def _release_lock(lock_mgr: LockMgr) -> bool:
    """
    Release acquired lock
    """
    if not lock_mgr.acquired:
        lock_mgr.msg = 'No lock to release'
        return False

    if lock_mgr.fd_w < 0:
        _clear_lockfile(lock_mgr)
        lock_mgr.msg = 'error: Lock acquired but bad lockfile fd'
        return False

    try:
        fcntl.flock(lock_mgr.fd_w, fcntl.LOCK_UN)
        lock_mgr.msg = 'success: lock released'
        okay = True

    except OSError as err:
        # Shouldn't happen: failed somehow - still mark unlocked?
        lock_mgr.msg = f'Error: failed releasing lock: {err}'
        okay = False

    _clear_lockfile(lock_mgr)
    lock_mgr.acquired = False

    return okay
