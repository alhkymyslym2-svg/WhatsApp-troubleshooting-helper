[app]
title = مساعد فك حظر واتساب
package.name = whatsapp_helper_pro
package.domain = com.jalal.apps
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3, kivy==2.2.1, kivymd==1.1.1, pillow, requests, urllib3, certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
[buildozer]
log_level = 2
warn_on_root = 1
