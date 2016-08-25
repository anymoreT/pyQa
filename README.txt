该包是成都团队使用的一个公用基础测试包．
主要功能：
１．支持web测试
２．支持接口测试


查看包文件：
python setup.py check
打包命令：
python setup.py sdist
安装包：
sudo pip install DianRongQa-1.0.0.tar.gz


cx_Oracle安装：
该报需要支持oracel的操作
１．　安装dpk
apt-get isntall  oracle-instantclient12.1-basic_12.1.0.2.0-1_amd64.deb
apt-get isntall  oracle-instantclient12.1-devel_12.1.0.2.0-1_amd64.deb
apt-get isntall oracle-instantclient12.1-sqlplus_12.1.0.2.0-1_amd64.deb

２．安装python3-dev
apt-get isntall  python3-dev

3. 拷贝libaio.so.1　libaio.so.1.0.1到
/lib/x86_64-linux-gnu/
/lib/x86_64-linux-gnu

４．/etc/profile　添加环境变量
export ORACLE_HOME=/usr/lib/oracle/12.1/client64

export ORACLE_BASE=/usr/lib/oracle/12.1

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH

export NLS_LANG=AMERICAN_AMERICA.AL32UTF8

５．安装ox-Oracle
pip install cx-Oracle

