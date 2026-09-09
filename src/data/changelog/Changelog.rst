Changelog
=========

Tags
====

.. code-block:: text

	1.3.0 (2024-03-29) -> 1.10.0 (2026-09-09)
	37 commits.

Commits
=======


* 2026-09-09  : **1.10.0**

.. code-block:: text

              - **1.10.0**
            
                * Bug in meson test runner with PYTHONPATH
                  One of those mornings ...

* 2026-09-09  : **1.9.8, origin/master**

.. code-block:: text

              - **1.9.8**
            
                * Bug in meson test runner with PYTHONPATH

* 2026-09-09  : **1.9.7**

.. code-block:: text

              - **1.9.7**
            
                * Test now runs several processs in parallel waiting to acquire lock

* 2026-09-09  : **1.9.6**

.. code-block:: text

              - **1.9.6**
            
                * typo

* 2026-09-09  : **1.9.5**

.. code-block:: text

              - **1.9.5**
            
                * meson now runs tests.
                * Clean html docs to avoid unneeded sphinx tmp files.
                * Fix bug with tests using relative path as reported by @piater on AUR

* 2026-09-06  : **1.9.4**

.. code-block:: text

              - **1.9.4**
            
                * Fix missing makedepends and ensure build/install scripts fail on error
                  Thanks to @TrialnError on Arch AUR.

* 2026-09-06  : **1.9.3**

.. code-block:: text

              - Add missing makedepends on meson (per @TrialnError from aur - thank you!)

* 2026-09-06  : **1.9.2**

.. code-block:: text

              - **1.9.2**
            
                * Typo in docs

* 2026-09-06  : **1.9.1**

.. code-block:: text

              - **1.9.1**
            
                * Use meson / meson-python for build and package management
                * Periodic review
                * Small code adjustments.
                * Add check to PKGBUILD
                * please delete any /usr/lib/python3.14/site-packages/lockmgr/__pycache__ before installing.
                  See important note below.
            
                ** IMPORTANT **
            
                Some older versions of this package did not include any byte compiled cache (__pycache__)
                and python auto creates them at runtime at a later date. If this exists, please delete
                the direcroty before installing this version since  it now includes the .pyc files.
                This will avoid pacman error that a .pyc file exists. So before upgrade please do::
            
                    /usr/bin/rm -rf /usr/lib/python3.14/site-packages/lockmgr/__pycache__
            
                My apologies.
 2026-01-06   ⋯

.. code-block:: text

              - update Docs/Changelog

* 2026-01-06  : **1.8.2**

.. code-block:: text

              - PKGBUILD small change
 2026-01-04   ⋯

.. code-block:: text

              - update Docs/Changelog

* 2026-01-04  : **1.8.1**

.. code-block:: text

              - fix license string in pyproject.toml
              - update Docs/Changelog

* 2026-01-04  : **1.8.0**

.. code-block:: text

              - **1.8.0**
            
                * Switch packaging from hatch to uv
                * Testing to confirm all working on python 3.14.2
                * License GPL-2.0-or-later
 2025-05-21   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2025-05-21  : **1.7.0**

.. code-block:: text

              - Small type hint change
 2025-05-02   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2025-05-02  : **1.6.1**

.. code-block:: text

              - Tidy ups: PEP-8, PEP-257, PEP-484 PEP-561
                improve reference API doc.
                Add py.typed so type checkers like mypy can be used with the module.
 2025-02-26   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2025-02-26  : **1.5.4**

.. code-block:: text

              - PKGBUILD: Add missing makedepends on python-installer (per aur comment by @piater)
 2024-12-31   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-12-31  : **1.5.3**

.. code-block:: text

              - Git tags are now signed.
                Update SPDX tags
                Add git signing key to Arch Package
 2024-12-22   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-12-22  : **1.5.2**

.. code-block:: text

              - Use autodoc style parameter descriptions for API docs
              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-12-22  : **1.5.1**

.. code-block:: text

              - Add API reference to documentation
 2024-10-19   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-10-19  : **1.5.0**

.. code-block:: text

              - remove unused requirements file
 2024-03-29   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-03-29  : **1.4.0**

.. code-block:: text

              - Change arch PKGBUILD dependency to python-pynotify
              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-03-29  : **1.3.2**

.. code-block:: text

              - Fix typo in PKGBUILD depends
              - update Docs/Changelog.rst Docs/lockmgr.pdf

* 2024-03-29  : **1.3.1**

.. code-block:: text

              - README fix rst title level

* 2024-03-29  : **1.3.0**

.. code-block:: text

              - Public release along with lockfile research and code
              - Initial commit


