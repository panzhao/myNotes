#在linux下的一些常见问题
###上网经常掉线
    把/etc/ppp/options中的lcp-echo-failure的值改大点
###linux查看系统以及内核版本
    用df -h查看硬盘状况
    查看内核版本:uname -a
    查看系统版本:lsb_release -a
                :cat /proc/version
                :cat /etc/issue
###linux开机显示频率超出限制
   修改/boot/grub/grub.cfg中set gfxmode=auto改为set gfxmode=‘自己设置分辨率’ 

###用户组
    查看用户所在组:    groups [用户名]
      查看用户信息:        id [用户名]

###Linux安装Flash插件
    1. 下载flash插件 http://get.adobe.com/flashplayer/completion/?installer=Flash_Player_11.2_for_other_Linux_(.tar.gz)_32-bit
    2. 安装：sudo cp libflashplayer.so /usr/lib/mozilla/plugins/
