# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['HeadsetControl_SystemTray.py'],
             binaries=[],
             datas=[('..\lib\headsetcontrol.exe','..\lib\libhidapi-0.dll','.')],
             hiddenimports=["infi.systray"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='HeadsetControl_SystemTray',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
