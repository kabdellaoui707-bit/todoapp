[app]
# (str) Title of your application
title = MonApp

# (str) Package name
package.name = monapp

# (str) Package domain (must be unique)
package.domain = org.kheira

# (str) Source code where main.py is located
source.dir = .

# (str) The main entry point of the application
source.main = main.py

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash background color (for example #FFFFFF)
presplash_color = #FFFFFF

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (list) Application requirements
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, plyer

# (str) Custom source folders for requirements
# (useful if you need local version of a library)
# source.include_exts = py,png,jpg,kv,atlas

# (bool) Indicate if you want to include source code in the APK
copy_libs = 1

# (str) List of Java .jar files to add to the libs folder
android.add_jars =

# (list) Java .aar libraries to add
android.add_aars =

# (str) Entry point for the app
entrypoint = main.py

# (list) Patterns to exclude from the final APK
exclude_patterns = *.pyc, __pycache__

# (str) Android API level to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) The format used to package the app: apk or aab
android.packaging_format = apk

# (bool) Sign the APK
android.sign = True

# (str) Keystore file and credentials
# (optional if you just want debug builds)
# android.release_keystore = mykey.keystore
# android.release_keyalias = myalias
# android.release_keypass = mypassword
# android.release_storepass = mystorepassword

# (bool) Copy logcat output to stdout
log_level = 2

# (bool) Add Android logcat filters
android.logcat_filters = *:S python:D

# (str) Directory where buildozer will store files
build_dir = .buildozer

# (bool) Clean build on every run
clean = False
