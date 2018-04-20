# PyMicroChat

## 声明：本项目仅用于通信方面知识的学习交流，请勿用于非法用途.  

## 安装python3.5
wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tar.xz
xz -d Python-3.5.3.tar.xz
tar xvf Python-3.5.3.tar

cd Python-3.5.3
./configure --prefix=/usr/local/python3.5 --enable-shared
make && make install
ln -s /usr/local/python3.5/bin/python3.5 /usr/bin/python3

1. /etc/ld.so.conf下面加一行/usr/local/python3.5/lib/

2. 保存后执行 ldconfig  生效

python3 -V

## Python3.3以上的版本通过venv模块原生支持虚拟环境，可以代替Python之前的virtualenv.低版本请用pip安装。

> git 下载
>>    git clone https://github.com/InfiniteTsukuyomi/PyMicroChat.git  
>>    or git clone git@github.com:InfiniteTsukuyomi/PyMicroChat.git  

Windows环境
> 创建Python3的venv虚拟环境
>> D:\VSCODE\PyMicroChat>python3 -m venv .

> windows 进入虚拟环境
>> D:\VSCODE\PyMicroChat>.\Scripts\activate

> CentOS 进入虚拟环境
>> source bin/activate

> 首次执行，配置依赖包，以后根据更新依赖环境运行
>> (PyMicroChat) D:\VSCODE\PyMicroChat>pip3 install -r requirements.txt

> 修改run.py相应的usrname & passwd，执行
>> (PyMicroChat) D:\VSCODE\PyMicroChat>python run.py

> 退出
>> (PyMicroChat) D:\VSCODE\PyMicroChat>deactivate

### 工程中的dll文件源码地址：https://github.com/InfiniteTsukuyomi/MicroChat/tree/master/test/ecdh

##### QQ交流群：306804262
