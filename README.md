# restore-npp-session
Restores a lost notepad++ session as initially described here: https://superuser.com/a/1499453 (original author)

# How to
Reads all opened files from notepad++ backup folder and creates a new `session.xml` in the current working dir. This only works if session snapshots had already been enabled _before_ you lost your session. See `Settings` -> `Preferences` -> `Backup`

Copy the generated `restored_session.xml` and overwrite the existing `session.xml` in `%APPDATA%\Notepad++\`.