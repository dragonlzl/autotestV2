基于airtest + uniitest + ddt

已实现：

    利用多进程多设备同时运行多个包体，包括全设备都运行全部包体，不同设备运行不同包体
    能简单的自动根据所连设备数去判断执行策略
    生成报告和错误截图
    跳过用例



结构目录

根目录 xx:\xxx\xx\autotestV2

-autotestV2

    -apk    存放apk的目录
        -渠道1
            xxx1.apk
            xxx2.apk
        -渠道2
            xxx1.apk
        -渠道3
        ...
        -渠道N
    -bug_image  自动存放问题截图的目录
    -image  存放图片资源,一个文件夹为一个总页面，里面存放整个页面截图
        -xxxpage
            -button_image   存放从界面截图截取下来的按键截图
                button1.png
                button2.png
            xxxpage.png
            xxx2page.png
        -yyypage
            -button_image
                button1.png
                button2.png
            yyypage.png
            yyy2page.png
        ...
        -zzzpage
    -info_file  存放配置
        device_info.json
        info.py
        run_info.py
        runInfo_json_handle.py
    -report     存放报告
    -scripts    存放各种脚本
        -case   用例脚本
            all_case.py
            Test_normal.py
        -common     通用工具脚本
            devicesTool.py
            getApkinfo.py
            getImagePath.py
            HTMLTestRunner.py
            skip.py
            target_path.py
        -install    线程apk安装脚本
            usb_install.py
        -Runner     执行脚本
            caserunner.py
            MultiRun.py
    README.md
        