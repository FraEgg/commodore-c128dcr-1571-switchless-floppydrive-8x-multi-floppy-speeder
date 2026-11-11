#!/usr/bin/env python3
"""Refresh this repository from the development folders of the Multi-Speeder project.

Run from anywhere:  python3 tools/update_release.py [--manuals DIR] [--manuals-en DIR] [--check]

Copies the DolphinDos26 ROMs for the C128DCR, the MS-Tools disk and the manuals
(German and English, as PDF) into this repository, writes CHECKSUMS.md5 and
CHECKSUMS.sha256 over everything published, and reports what is out of date:

- an English manual is missing or older than the German one;
- a manual does not state the MD5 of a ROM published here;
- a file in rom/ is not one of the allowed DolphinDos26 ROMs.

Only the DolphinDos26 ROMs and the EPROM template with Commodore DOS, DolphinDOS 3 and DolphinDos26 may be published. ROM images with original JiffyDOS code
(C64, C128, 1541, 1571) or complete EPROM images must never be added to this repository.

The hardware files (hardware/) are maintained here directly and are only checksummed.
The script exits with status 1 if anything is out of date. --check changes nothing.
"""
import argparse
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def find_root():
    """The project folder holding Builds/ – this repository sits in <root>/Git/<repo>."""
    for p in REPO.parents:
        if (p / 'Builds').is_dir():
            return p
    return REPO.parent.parent


ROOT = find_root()
ROMS = ['C1571_DOLPHINDOS26.bin', 'C128DolphinDos26-US.BIN', 'C128DolphinDos26-DE.BIN', 'C64IIDolphinDos26.bin']
# EPROM template from Builds: Commodore DOS 318047-01, DolphinDOS 3 in bank 3, DolphinDos26 in bank 4
TEMPLATES = ['C1571_C128DCR_29F040.BIN']
# Kernal switcher (U32) images from Builds (C128DD26 make builds, tools/u32_image.py): German and
# international/US version. Bank 4 holds the DolphinDos26 kernals (with JiffyDOS transfer routines,
# allowed); all other banks must be free of JiffyDOS. Not listed in the manual, so no MD5 check there.
KERNAL_IMAGES = ['C128DCR_KERNAL_29F040-DE.BIN', 'C128DCR_KERNAL_29F040-US.BIN']
MANUALS = {'MultiSpeederC128DCR-1571_Handbuch.pdf': 'MultiSpeederC128DCR-1571_Manual.pdf'}
CHECKSUMMED = ('rom', 'ms-tools', 'manuals', 'hardware', 'rom-builder')
# Browser tool from its development folder MS-ROM-Builder-C128DCR (contains no ROM data)
ROM_BUILDER = ('MS-ROM-Builder-C128DCR/index.html', 'rom-builder/MS-ROM-Builder-C128DCR.html')


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def copy(src, dst, check, problems):
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    if not src.exists():
        problems.append('missing source: %s' % src)
        return
    if check:
        if not dst.exists() or sha(src) != sha(dst):
            problems.append('out of date: %s' % dst.relative_to(REPO))
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=str(ROOT), help='project folder with Builds and MS-Tools')
    ap.add_argument('--manuals', help='folder with the German PDF (default: Builds)')
    ap.add_argument('--manuals-en', help='folder with the English PDF (default: dd25/doc/handbuch/build)')
    ap.add_argument('--check', action='store_true', help='report only, change nothing')
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    builds = root / 'Builds'
    man_de = pathlib.Path(a.manuals) if a.manuals else builds
    man_en = pathlib.Path(a.manuals_en) if a.manuals_en else root / 'dd25' / 'doc' / 'handbuch' / 'build'
    bad = []

    for r in ROMS + TEMPLATES + KERNAL_IMAGES:
        copy(builds / r, REPO / 'rom' / r, a.check, bad)
    for p in (REPO / 'rom').glob('*'):
        if p.name not in ROMS + TEMPLATES + KERNAL_IMAGES:
            bad.append('not allowed in rom/: %s (only the DolphinDos26 ROMs may be published)' % p.name)
    for t in TEMPLATES:
        p = REPO / 'rom' / t
        if p.exists() and b'JIFFY' in p.read_bytes().upper():
            bad.append('JiffyDOS found in %s' % t)
    for t in KERNAL_IMAGES:
        p = REPO / 'rom' / t
        if p.exists():
            b = p.read_bytes()
            if len(b) != 524288:
                bad.append('%s is not 512 KB' % t)
            for n in range(8):
                if n != 3 and b'JIFFY' in b[n * 65536:(n + 1) * 65536].upper():
                    bad.append('JiffyDOS found in bank %d of %s (only bank 4 may hold it)' % (n + 1, t))
    for p in REPO.rglob('*'):
        if '.git' not in p.parts and 'jiffy' in p.name.lower():
            bad.append('file name suggests JiffyDOS content, remove it: %s' % p.relative_to(REPO))

    for de, en in MANUALS.items():
        copy(man_de / de, REPO / 'manuals' / 'de' / de, a.check, bad)
        copy(man_en / en, REPO / 'manuals' / 'en' / en, a.check, bad)
        if (man_de / de).exists() and (man_en / en).exists() and \
                (man_en / en).stat().st_mtime < (man_de / de).stat().st_mtime:
            bad.append('English manual older than German one: %s' % en)

    copy(root / 'MS-Tools' / 'ms-tools.d64', REPO / 'ms-tools' / 'ms-tools.d64', a.check, bad)
    copy(root / ROM_BUILDER[0], REPO / ROM_BUILDER[1], a.check, bad)
    rb = REPO / ROM_BUILDER[1]
    if rb.exists() and rb.stat().st_size > 200000:
        bad.append('%s is larger than expected - it must not contain ROM data' % ROM_BUILDER[1])

    # every manual must state the MD5 of exactly the files published here
    for pdf in (REPO / 'manuals').rglob('*.pdf'):
        try:
            flat = re.sub(r'\s+', '', subprocess.check_output(['pdftotext', str(pdf), '-'], text=True))
        except (OSError, subprocess.CalledProcessError) as e:
            bad.append('cannot read %s: %s' % (pdf.name, e))
            continue
        for f in [REPO / 'rom' / r for r in ROMS + TEMPLATES] + [REPO / 'ms-tools' / 'ms-tools.d64']:
            if f.exists() and hashlib.md5(f.read_bytes()).hexdigest()[:16] not in flat:
                bad.append('%s does not state the MD5 of %s' % (pdf.name, f.name))

    if not a.check:
        files = sorted(p for d in CHECKSUMMED for p in (REPO / d).rglob('*') if p.is_file())
        for algo, out in (('md5', 'CHECKSUMS.md5'), ('sha256', 'CHECKSUMS.sha256')):
            lines = ['%s  %s' % (hashlib.new(algo, f.read_bytes()).hexdigest(), f.relative_to(REPO).as_posix())
                     for f in files]
            (REPO / out).write_text('\n'.join(lines) + '\n')

    for x in bad:
        print('PROBLEM:', x)
    print('%d problem(s)' % len(bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
