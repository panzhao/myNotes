#在linux下的一些常见问题
###上网经常掉线
    把/etc/ppp/options中的lcp-echo-failure的值改大点
###linux查看一些常用信息命令
    用df -h查看硬盘状况
    查看内核版本:uname -a
    查看系统版本:lsb_release -a
###linux开机显示频率超出限制
   修改/boot/grub/grub.cfg中set gfxmode=auto改为set gfxmode=‘自己设置分辨率’ 
    
