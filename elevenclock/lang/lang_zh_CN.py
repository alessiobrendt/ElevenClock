# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
    "Hide the clock when RDP Client or Citrix Workspace are running": "当使用远程桌面或运行Citrix Workspace时隐藏时钟区",
    "Clock Appearance:": "时钟区外观:",
    "Force the clock to have black text": "强制时钟区使用深色文本",
    " - It is required that the Dark Text checkbox is disabled": " - 当启用深色文本时不要使用",
    "Debbugging information:": "调试信息",
    "Open ElevenClock's log": "查看ElevenClock日志",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "在主显示器上显示时钟区(在屏幕左侧显示时钟区时推荐开启)",
    "Show weekday on the clock"  :"在时钟区显示星期",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock选项", # Also settings title
    "Reload Clocks"             :"重载时钟区",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"重启ElevenClock",
    "Hide ElevenClock"          :"隐藏ElevenClock",
    "Quit ElevenClock"          :"退出ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"通用设置:",
    "Automatically check for updates"                                                   :"自动检测更新",
    "Automatically install available updates"                                           :"自动安装可用更新",
    "Enable really silent updates"                                                      :"开启静默更新",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"跳过更新来源校验(不推荐，自行承担风险)",
    "Show ElevenClock on system tray"                                                   :"在系统托盘显示ElevenClock图标",
    "Alternative clock alignment (may not work)"                                        :"使用替代的时钟对齐方式(可能不起作用)",
    "Change startup behaviour"                                                          :"修改开机自启行为",
    "Change"                                                                            :"去修改",
    "<b>Update to the lastest version!</b>"                                             :"<b>更新到最新版!</b>",
    "Install update"                                                                    :"安装更新",
    
    #Clock settings
    "Clock Settings:"                                              :"时钟区设置:",
    "Hide the clock in fullscreen mode"                            :"在全屏模式下隐藏时钟区",
    "Hide the clock when RDP client is active"                     :"当使用远程桌面时隐藏时钟区",
    "Force the clock to be at the bottom of the screen"            :"强制时钟区在屏幕底部显示",
    "Show the clock when the taskbar is set to hide automatically" :"当启用任务栏自动隐藏时显示时钟区",
    "Fix the hyphen/dash showing over the month"                   :"修复连字符会挡住月份的问题",
    "Force the clock to have white text"                           :"强制时钟区使用白色文本",
    "Show the clock at the left of the screen"                     :"在屏幕左侧显示时钟区",
    
    #Date & time settings
    "Date & Time Settings:"                             :"时间与日期设置",
    "Show seconds on the clock"                         :"显示秒数",
    "Show date on the clock"                            :"显示日期",
    "Show time on the clock"                            :"显示时间",
    "Change date and time format (Regional settings)"   :"修改日期与时间格式(区域设置)",
    "Regional settings"                                 :"区域设置",
    
    #About the language pack
    "About the language pack:"                  :"关于语言包",
    "Translated to English by martinet101"      :"简体中文翻译由hlgsdx贡献", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"把ElevenClock翻译成您的语言",
    "Get started"                               :"开始",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"关于ElevenClock {0}版:",
    "View ElevenClock's homepage"               :"查看ElevenClock的主页",
    "Open"                                      :"打开",
    "Report an issue/request a feature"         :"报告问题/建议新功能",
    "Report"                                    :"报告",
    "Support the dev: Give me a coffee☕"       :"打赏开发者：给我买杯咖啡☕",
    "Open page"                                 :"打开页面",
    "Icons by Icons8"                           :"程序图标由Icons8设计", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"网站",
    "Close settings"                            :"关闭设置",
    "Close"                                     :"关闭",
}

lang = lang2_3