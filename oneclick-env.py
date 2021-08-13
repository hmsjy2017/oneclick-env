import os
import time
import base64
import argparse

def logo():
    print("""                             
  ___              ____ _ _      _         _____            
 / _ \ _ __   ___ / ___| (_) ___| | __    | ____|_ ____   __
| | | | '_ \ / _ \ |   | | |/ __| |/ /____|  _| | '_ \ \ / /
| |_| | | | |  __/ |___| | | (__|   <_____| |___| | | \ V / 
 \___/|_| |_|\___|\____|_|_|\___|_|\_\    |_____|_| |_|\_/  """)

    copyright_title = 'ICAgICDkuIDplK7phY3nva7njq/looM='
    copyright_url = 'aHR0cHM6Ly9naXRodWIuY29tL2htc2p5MjAxNy9vbmVjbGljay1lbnY='
    print('')
    print(base64.b64decode(copyright_title).decode('utf-8'))
    print(base64.b64decode(copyright_url).decode('utf-8'))
    print('')
    print(' 1. 更换 APT 源        2. 添加常用软件源')
    print(' 3. 安装 NodeJS        4. 卸载 NodeJS')
    print(' 5. 安装 Golang        6. 卸载 Golang')
    print(' 7. 安装 JDK           8. 卸载 JDK')
    print(' 9. 安装 Rust         10. 卸载 Rust')
    print('11. 安装 Ruby         12. 卸载 Ruby')
    print('13. 安装 Docker       14. 卸载 Docker')
    print('15. 安装 LNMP 环境    16. 退出脚本')
    print('')
    return copyright_title, copyright_url
logo()

bit = os.popen('getconf LONG_BIT').read()

# 1.更换 APT 源为国内源
def change_mirrors():
	print('\n正在备份原有 APT 源')
	os.system('sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak')
	os.system('sudo cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bak')
	print('\n备份完成 正在更换 APT 源为 SJTU 源')
	os.system('sudo sed -i "s|http://raspbian.raspberrypi.org/raspbian/|https://mirrors.sjtug.sjtu.edu.cn/raspbian/raspbian/|g" /etc/apt/sources.list')
	os.system('sudo sed -i "s|http://deb.debian.org/debian|https://mirrors.sjtug.sjtu.edu.cn/debian|g" /etc/apt/sources.list')
	os.system('sudo sed -i "s|http://archive.raspberrypi.org/debian/|https://mirrors.sjtug.sjtu.edu.cn/raspberrypi/debian/|g" /etc/apt/sources.list.d/raspi.list')
	os.system('sudo apt update')
	print('\n完成')

# 2.添加常用软件源
def add_common_apt_repositories():
	print('正在添加 Raspbian Addons 源')
	os.system('wget -qO- https://mirror.sjtu.edu.cn/raspbian-addons/KEY.gpg | sudo apt-key add -')
	os.system('echo "deb https://mirror.sjtu.edu.cn/raspbian-addons/debian/ buster main" | sudo tee /etc/apt/sources.list.d/raspbian-addons.list')
	os.system('sudo apt update')
	print('\nRaspbian Addons 源添加成功')
	print('正在添加 Deb Multimedia 源')
	os.system('echo "deb http://mirrors.ustc.edu.cn/deb-multimedia/ buster main non-free" >> /etc/apt/sources.list')
	os.system('echo "# deb-src http://mirrors.ustc.edu.cn/deb-multimedia/ buster main non-free" >> /etc/apt/sources.list')
	os.system('echo "deb http://mirrors.ustc.edu.cn/deb-multimedia/ buster-backports main" >> /etc/apt/sources.list')
	os.system('echo "# deb-src http://mirrors.ustc.edu.cn/deb-multimedia/ buster-backports main" >> /etc/apt/sources.list')
	print('\nDeb Multimedia 源添加成功')

# 3.安装 NodeJS	
def install_nodejs():
    print('\n正在下载 n')
    os.system('sudo curl -L https://cdn.jsdelivr.net/gh//hmsjy2017/n@master/bin/n -o /usr/bin/n')
    print('\n下载成功')
    print('\n正在安装 NodeJS 14 请耐心等待')
    os.system('sudo bash n stable')
    print('\n安装成功 正在更换 npm 源为淘宝源')
    os.system('npm config set registry https://registry.npm.taobao.org')
    os.system('node -v')
    os.system('npm -v')
    os.system('npm config get registry')
    print('\n   NodeJS 安装成功')
    print('\n    祝您使用愉快\n')

# 4.卸载 NodeJS
def uninstall_nodejs():
    print('\n正在卸载 NodeJS 请耐心等待')
    os.system('sudo npm uninstall npm -g')
    os.system('sudo rm -rf /usr/local/lib/node /usr/local/lib/node_modules /var/db/receipts/org.nodejs.*')
    os.system('sudo rm -rf /usr/local/include/node /Users/$USER/.npm')
    os.system('sudo rm /usr/local/bin/node')
    os.system('sudo rm /usr/local/share/man/man1/node.1')
    os.system('sudo rm /usr/local/lib/dtrace/node.d')
    os.system('sudo rm /usr/bin/n')
    print('\n卸载完成!')

# 5.安装 Golang
def install_golang():
    print("\n正在下载 Golang，请耐心等待")
    if bit == '64':
        os.system('wget https://dl.google.com/go/go1.16.7.linux-arm64.tar.gz')
        print('\n下载完成')
        print('\n正在解压 请耐心等待')
        os.system('sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.16.7.linux-arm64.tar.gz')
        os.system('export PATH=$PATH:/usr/local/go/bin')
        print('\n解压完成 正在删除已下载的压缩包')
        os.system('rm go1.16.7.linux-arm64.tar.gz')
    elif bit == '32':
        os.system('wget https://golang.google.cn/dl/go1.16.7.linux-armv6l.tar.gz')
        print('\n下载完成')
        print('\n正在解压 请耐心等待')
        os.system('sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.16.7.linux-armv6l.tar.gz')
        os.system('export PATH=$PATH:/usr/local/go/bin')
        print('\n解压完成 正在删除已下载的压缩包')
        os.system('rm go1.16.7.linux-armv6l.tar.gz')  
    os.system('go version')
    print('\n   Golang 安装成功!')
    else: 
        print('\n你使用的系统暂不支持')

# 6.卸载 Golang
def uninstall_golang():
    print('\n正在卸载 Golang 请耐心等待')
    os.system('sudo rm -rf /usr/local/go')
    print('\n卸载完成!')

# 7.安装 JDK
def install_jdk():
    print('正在添加 AdoptOpenJDK 源')
    os.system('wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -')
    os.system('echo "deb http://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/deb buster main" | sudo tee /etc/apt/sources.list.d/AdoptOpenJDK.list')
    os.system('sudo apt-get update')
    print('\n正在安装 AdoptOpenJDK 16，请耐心等待')
    os.system('sudo apt install -y adoptopenjdk-16-hotspot')
    os.system('java --version')
    print('\n   JDK 安装成功')

# 8.卸载 JDK
def uninstall_jdk():
    print('\n正在卸载 AdoptOpenJDK 16，请耐心等待')
    os.system('sudo apt purge -y adoptopenjdk-16-hotspot')
    print('\n卸载完成!')

# 9.安装 Rust
def install_rust():
    print('\n正在安装 Rust，请耐心等待')
    os.system('wget https://raw.fastgit.org/hmsjy2017/scripts/main/rustup-init.sh')
    #os.system('wget https://cdn.jsdelivr.net/gh/rust-lang-nursery/rustup.rs/rustup-init.sh')
    os.system('echo "export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup" >> ~/.bash_profile')
    os.system('chmod +x rustup-init.sh')
    os.system('./rustup-init.sh -y')
    os.system('source $HOME/.cargo/env')
    os.system('cargo --version')
    print('\n正在安装 Cargo 镜像')
    os.system('curl -sSf https://raw.fastgit.org/hmsjy2017/scripts/main/cargo.sh | sh')
    print('\n正在安装 Rustup 镜像')
    os.system('echo "export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup" >> ~/.bash_profile')
    os.system('rustup --version')
    print('\n   Rust 安装成功')

# 10.卸载 Rust
def uninstall_rust():
    print('\n正在卸载 Rust 请耐心等待')
    os.system('rustup self uninstall -y')
    print('\n卸载完成!')

# 11.安装 Ruby
def install_ruby():
    print('\n正在安装 RVM，请耐心等待')
    os.system('gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB')
    os.system('\curl -sSL https://cdn.jsdelivr.net/gh/rvm/rvm@master/binscripts/rvm-installer | bash -s stable')
    os.system('source ~/.bashrc')
    os.system('source ~/.bash_profile')
    os.system('rvm -v')
    print('\nRVM 安装完成')
    print('\n正在安装 Ruby 请耐心等待')
    os.system('echo "ruby_url=https://cache.ruby-china.com/pub/ruby" > ~/.rvm/user/db')
    os.system('rvm install 3.0 --disable-binary')
    #可选 os.system('rvm docs generate-ri')
    os.system('ruby -v')
    print('\n正在安装 gems 镜像')
    os.system('gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/ --remove https://rubygems.org/')
    os.system('gem sources -l')
    print('\n   Ruby 安装成功')

# 12.卸载 Ruby
def uninstall_ruby():
    print('\n正在卸载 Ruby 请耐心等待')
    os.system('rvm remove 3.0')
    print('\n正在卸载 RVM 请耐心等待')
    os.system('rvm implode')
    print('\n卸载完成!')

# 13.安装 Docker
def install_docker():
    print('\n正在安装 Docker，请耐心等待')
    os.system('sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common')
    os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -')
    if bit == '64':
        os.system('echo "deb [arch=arm64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list')
    elif bit == '32':
        os.system('echo "deb [arch=armhf] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y docker-ce')
    os.system('docker -v')
    print('\n正在配置 Docker 镜像站（DaoCloud）')
    os.system('curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io')
    os.system('sudo service docker restart')
    print('\n   Docker 安装成功')

# 14.卸载 Docker
def uninstall_docker():
    print('\n正在安装 Docker，请耐心等待')
    os.system('sudo apt-get purge -y docker')

# 15.安装 LNMP 环境
def install_lnmp():
    print('\n正在安装 LNMP 环境，请耐心等待')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install nginx php7.3-fpm php7.3-cli php7.3-curl php7.3-gd php7.3-cgi')
    os.system('sudo service nginx start')
    os.system('sudo service php7.3-fpm restart')
    os.system('
    os.system('sudo apt-get install mariadb-server-10.3'）
    os.system('sudo mysql -uroot -hlocalhost -e "create user root@'127.0.0.1' identified by \"${mysql_password}\";"')
    os.system('sudo mysql -uroot -hlocalhost -e "grant all privileges on *.* to root@'127.0.0.1' with grant option;"')
    os.system('')
    os.system('')
    os.system('')
    os.system('')
    
#if __name__ == "__main__":
#    # 如果没有安装 screenfetch 就安装
#    result = os.popen('pkg list-installed|grep screenfetch')
#    if 'screenfetch' not in result.read():
#        print('正在安装相关依赖包: screenfetch')
#        os.system('pkg install screenfetch -y')

#    copyright = logo()
#    if copyright[0][10:13] != '11e' or copyright[1][10:13] != '93d':
#        print('校验失败 退出脚本')
#        os._exit(0)

    option = input('\n请选择要执行的操作: ')
    if int(option) == 1:
        change_mirrors()

    elif int(option) == 2:
        add_common_apt_repositories()

    elif int(option) == 3:
        install_nodejs()

    elif int(option) == 4:
        uninstall_nodejs()

    elif int(option) == 5:
        install_golang()

    elif int(option) == 6:
        uninstall_golang()

    elif int(option) == 7:
        install_jdk()

    elif int(option) == 8:
        uninstall_jdk()

    elif int(option) == 9:
        install_rust()

    elif int(option) == 10:
        uninstall_rust()

    elif int(option) == 11:
        install_ruby()

    elif int(option) == 12:
        uninstall_ruby()

    elif int(option) == 13:
        install_docker()

    elif int(option) == 14:
        uninstall_docker()

    elif int(option) == 15:
        install_lnmp()

    elif int(option) == 16:
        os._exit(0)
    else:
        print('不合法的输入选项 请重新输入')