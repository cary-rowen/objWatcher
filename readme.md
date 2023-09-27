# obj Watcher

**This NVDA add-on watches changes to attributes of navigation objects.**

* Author: Cary-rowen <manchen_0528@outlook.com>, hwf1324 <1398969445@qq.com>
* Compatibility: NVDA-2023.1 or later

## Possible Use Cases

1. Watch subtitles or lyric objects of certain players and enable automatic reporting upon refreshing.
2. Watch items of interest within the group chat list in the Unigram or WeChat conversation list. New messages can be automatically reported, and background reporting is supported.
3. Solely for testing purposes, you can also watch the status bar of Notepad to automatically report rows and columns during content insertion/deletion.

## Gestures

``Control+NVDA+W``: Press once to start watching the current navigator object. If a navigator object is currently being watched, the watched attribute will be reported. Press twice to stop watching.

**You can change this gesture from the Input Gestures dialog.**

## Contributors

* Cary-rowen
* ibrahim hamadeh
* hwf1324

## Contribution Guidelines

1. The add-on welcomes Pull Requests (PRs) for new features and localized translations on [GitHub][GitHub].
2. For any feedback, please submit it through a [GitHub Issue][GitHubIssue].

## Release Notes
### Version 0.4.1
* Added Arabic translation by ibrahim hamadeh.

### Version 0.4.0
*The watcher timer interval can be set in the settings panel, the default value is 100.

### Version 0.3.4
* Enhanced documentation.
* The rapid double press gesture no longer consistently prioritizes the execution of the first press function.

[GitHub]: https://github.com/cary-rowen/objWatcher
[GitHubIssue]: https://github.com/cary-rowen/objWatcher/issues
