# 对象监视器

**这是一个用于监视导航对象属性变化的插件。**

* 作者： Cary-rowen <manchen_0528@outlook.com>，hwf1324 <1398969445@qq.com>
* 兼容性： NVDA-2023.1 或更高版本

## 可能的用例

1. 监视某些播放器的字幕或歌词对象，内容刷新时可以自动读出。
2. 在 Unigram 或微信的会话列表中，监视感兴趣的会话。有新消息可自动读出，支持后台朗读。
3. 仅出于测试目的，可以监视记事本的状态栏，以在内容插入/删除过程中自动读出行/列。

## 按键与首饰

``Control+NVDA+W``：按一次开始监视当前导航对象。如果当前已开始监视，则会读出被监视的对象属性。连按两次停止监视。

**如果需要，可以从“按键与手势”对话框更改此快捷键。**

## 贡献者

* Cary-rowen
* ibrahim hamadeh
* hwf1324

## 贡献

1. 该插件在 [GitHub][GitHub] 上接受新功能和本地化翻译的 PR。
2. 有任何反馈，也可以通过 [GitHub Issue][GitHubIssue] 进行提交。

## 升级日志
### 版本0.4.2
* 由 VovaMobile 增加的乌克兰语翻译。

### 版本0.4.1
* 由 ibrahim hamadeh 增加的阿拉伯语翻译。

### 版本0.4.0
* 可以在设置面板中设置计时器间隔，默认值为100。

### 版本0.3.4
* 连按两次首饰不再始终优先执行第一次按下功能。
* 改进了文档

[GitHub]: https://github.com/cary-rowen/objWatcher
[GitHubIssue]: https://github.com/cary-rowen/objWatcher/issues
