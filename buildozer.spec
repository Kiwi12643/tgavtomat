[app]
title = TG BlockFlow
package.name = tgblockflow
package.domain = org.tgblockflow
source.dir = .
source.include_exts = py
version = 0.1
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 0

[android]
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 31
android.accept_sdk_license = True
android.arch = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 1
warn_on_root = 1
