
========
Appendix
========

Installation
============

Available on
 * `Github <https://github.com/gene-git/lockmgr>`_
 * `Archlinux AUR <https://aur.archlinux.org/packages/lockmgr>`_

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
To build manually, clone the repo and ::

        ./scripts/do-build
        ./scripts/do-install <destination-dir>

Dependencies
============

* Run Time :

  * python          (3.14 or later)

* Building Package:

  * git
  * meson
  * meson-python
  * rsync

License
=======

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

 * SPDX-License-Identifier: GPL-2.0-or-later
 * SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>


.. [1] File private locks https://lwn.net/Articles/586904/
.. [2] Open File Description https://lwn.net/Articles/640404/
.. [3] Python fcntl docs: https://docs.python.org/3/library/fcntl.html
.. [4] Python struct module: https://docs.python.org/3/library/struct.html

