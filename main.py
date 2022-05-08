import subprocess
import sys
from subprocess import Popen, PIPE

pkg_file = 'packages.txt'
#write file for example
file_content = open(pkg_file, 'w')
#add to file list of all installed packages
pkg_list = subprocess.Popen(['dpkg-query', '-l'], stdout=subprocess.PIPE, text=True)
for line in pkg_list.stdout:
    sys.stdout.write(line)
    file_content.write(line)
pkg_list.wait()

#list of required packeges which want to find in pkg_file
required_pkg = ['git', 'python', 'apt', 'gzip', 'another']
#put result in array
query_list = [['grep', '-c', f'{pkg}', pkg_file] for pkg in required_pkg]
# print(query_list)
list_of_proc = [Popen(query, text=True, stdout=PIPE, stderr=PIPE) for query in query_list]
index = 0
for proc in list_of_proc:
    proc.wait()
    if proc.returncode == 1:
        print(f'The package {required_pkg[index]} not found!')
    index += 1