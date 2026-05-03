[app]
title = TG BlockFlow
package.name = tgblockflow
package.domain = org.tgblockflow
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1
orientation = portrait
fullscreen = 0

[android]
android.api = 35
android.minapi = 24
android.ndk = 25b
android.sdk = 35
android.accept_sdk_license = True
android.arch = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET
android.presplash_color = #0A0C17
android.splash_color = #0A0C17

[buildozer]
log_level = 2
warn_on_root = 1