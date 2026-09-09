#
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
#

project('lockmgr', ['c'],
  version: files('src/version.txt'),
  meson_version: '>=1.10.0',
  default_options: [
    'c_std=c23',
    'warning_level=3',
    'b_pie=true',
    'prefix=/usr',
    'mandir=share/man',
    ],
)

d_etc = get_option('sysconfdir')
d_lib = get_option('libdir')
d_bin = get_option('bindir')
d_man = get_option('mandir')
d_share = get_option('datadir')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
proj_root = meson.project_source_root()
py_dep = py.dependency(embed: true)

inc_dir = []
lib_sources = []

#
# top-level files
#

#
# Python submodules
#
subdir('src/lockmgr')

#
# Deps
#

#
# Executables
#

#
# Install
#

s_license = 'src/data/license'
s_changelog = 'src/data/changelog'
s_docs = 'src/data/docs'
s_examples = 'src/data/examples'
s_scripts = 'src/scripts'
manual = 'lockmgr.pdf'

# 
# /usr/share/lockmgr/docs
# 
install_data(
  [
    s_docs / manual,
  ],
  install_dir: d_share / 'lockmgr/docs'
)

install_subdir(
  [
    s_docs / 'html',
  ],
  install_dir: d_share / 'lockmgr/docs',
  strip_directory: false
)

# 
# /usr/share/lockmgr 
# 
install_data(
  [
    'README.rst',
    s_changelog / 'Changelog.rst',
    'packaging/Changelog',
  ],
  install_dir: d_share / 'lockmgr'
)

install_data(
  [
    s_examples / 'test_lock.py',
    ],
  install_dir: d_share / 'lockmgr/examples',
)

install_data(
  [
    s_examples / 'research/Makefile',
    s_examples / 'research/c_lock_test.c',
    s_examples / 'research/flock_sizes.c',
    s_examples / 'research/lock_fcntl.py',
    s_examples / 'research/lock_flock.py',
    ],
  install_dir: d_share / 'lockmgr/examples/research',
)
# 
# /usr/share/licenses/lockmgr 
# 
install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'licenses/lockmgr'
)

#
# tests
# - these are run in parallel
# - each test run gets the counter 'i' as an argument, which uniquely identifies it.
#
srcdir = proj_root / 'src'
testdir = srcdir / 'tests'

num_tests = 5
test_exe = find_program(testdir / 'test_locks.py')

foreach i : range(num_tests)
  test('test_exe-@0@'.format(i), 
    test_exe,
    args : ['@0@'.format(i)],
    env: {'PYTHONPATH': srcdir},
    )
endforeach
