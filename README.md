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

Windows环境
> 创建Python3的venv虚拟环境
>> python3 -m venv .

> windows 进入虚拟环境
>> .\Scripts\activate

> CentOS 进入虚拟环境
>> source bin/activate

> 首次执行，配置依赖包，以后根据更新依赖环境运行
>> (robot) [root@iz2ze2vve1jzbburujx43pz robot]>pip3 install -r requirements.txt

> 修改run.py相应的usrname & passwd，执行
>> (robot) [root@iz2ze2vve1jzbburujx43pz robot]>python run.py

> 退出
>> (robot) [root@iz2ze2vve1jzbburujx43pz robot]>deactivate