echo Zloj安装进程
echo 安装将在10秒后开始，无法结束，若想退出，请按下Ctrl^c
timeout 10
echo 开始安装python
wget -O python_setup.exe https://www.python.org/ftp/python/3.11.0/python3.11.0rc1.exe ;cmd /c python_setup.exe /quiet TargetDir=C:/python-3.11.0 InstallAllUsers=1 PrependPath=1 Include_test=0
python -v
pip install django
pip isntall pickle
echo python配套系列安装完成，开始安装zloj
