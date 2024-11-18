# objWatcher

**This NVDA add-on watches changes to attributes of navigation objects.**

* Authors: Cary-rowen (<manchen_0528@outlook.com>), hwf1324 (<1398969445@qq.com>)
* Compatibility: NVDA 2023.1 or later

## Possible Use Cases

1. **Subtitles and Lyrics Watching:**
   Watch subtitle or lyric objects of certain players, enabling automatic reporting when they refresh.
2. **Chat Activity Watching:**
   Watch items of interest within group chat lists in messaging apps such as Unigram or WeChat. Automatically report new messages, even when working in the background.
3. **Testing and Debugging:**
   Watch the status bar of applications like Notepad to automatically report changes in rows and columns during editing.

## Gestures

### Watcher Layer Commands

Press `NVDA+Alt+W` to activate the watcher layer, where you can perform watching actions:

- **Numeric Keys (0–9):** Add the current navigator object to a specific position or report the status of an object already being watched at that position.
- **Delete:** Press once to remove the last watched object; press twice to remove all watched objects.
- **T:** Toggle the watch status of the current foreground window.
- **P:** Pause or resume all watching activities.
- **Escape:** Exit the watcher layer.

When entering the watcher layer, the add-on announces the current status:

- *"No items are being watched. Please add items to watch."*
- *"Watching in progress. {n} items are being tracked."*
- *"Watching paused. {n} items in the watch list."*

### Other Gestures

The following actions are supported but have no default gestures assigned. Users can assign gestures to these actions via the Input Gestures dialog:

- **Add current navigator object to watchlist.**
  - **Note:** This action can only be assigned to gestures where the main key is a numeric key (0–9) with a modifier, such as `NVDA+Alt+0–9`.
- **Toggle the watch status of the current window.**
- **Toggle pause/resume watching.**
- **Press once to delete the last watched object; press twice to delete all watched objects.**

## Settings

Access the settings panel from NVDA’s Preferences menu to configure the following options:

- **Watcher Timer Interval:** Set the watching interval in milliseconds (default is 100ms)

## Contributors

- **Authors:**
  - Cary-rowen: Core developer
  - hwf1324: Code contributor
  - Ibrahim Hamadeh: Code contributor

- **Localization Contributors:**  
  - Ibrahim Hamadeh: Arabic Translation
  - VovaMobile: Ukrainian Translation

**Feel free to let me know the names of other localization contributors in any way you like.**

## Contribution

1. Submit Pull Requests (PRs) for new features or localized translations via [GitHub][GitHub].
2. Report bugs or provide feedback through the [GitHub Issues page][GitHubIssue].

## Release Notes
### Version 1.0.1
- Fixed duplicate objects being added
- Other improvements

### Version 1.0.0
- Added watcher layer commands (`NVDA+Alt+W`).
- Introduced watching feature for multiple objects.
- Introduced quick watching of the foreground window.
- Support pause/resume watching.

### Version 0.4.5
- Localization updates.

### Version 0.4.4
- Supported "speak on demand" mode for NVDA 2024.1.
- Localization updates.

### Version 0.4.0
- Introduced a configurable timer interval for watching objects.

[GitHub]: https://github.com/cary-rowen/objWatcher
[GitHubIssue]: https://github.com/cary-rowen/objWatcher/issues
