# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[('./ffmpeg', '.')],
    datas=[('./lp_loop.mov', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    # runtime_hooks에 우리가 만든 resign_hook.py를 추가합니다.
    runtime_hooks=['resign_hook.py'],
    excludes=[],
    noarchive=False,
    optimize=1,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Yonhwa Video Editor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    # Developer ID를 지정합니다.
    codesign_identity="Developer ID Application: ",
    entitlements_file="./entitlements.plist",
    icon=['icons/icon.icns'],
)
app = BUNDLE(
    exe,
    name='Yonhwa Video Editor.app',
    icon='icons/icon.icns',
    bundle_identifier=None,
)
