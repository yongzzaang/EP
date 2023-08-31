import sys, pandas as pd, platform, distro
if platform.system() == 'Windows' :
    sys.path.append('C:/Users/seungyoung.jung/Desktop/var/yongzzaang')
elif platform.system() == 'Darwin' :
    sys.path.append('/Users/yongzzaang/Desktop/var/yongzzaang')
elif platform.system() == 'Linux' and distro.id() == 'ubuntu' :
    sys.path.append('/var/yongzzaang')
elif platform.system() == 'Linux' and distro.id() == 'rocky' :
    sys.path.append('/home/seungyoung.jung')
from wadiz.myClass import Func, Project
from wadiz.naverClass import NaverAPI, Report
from datetime import datetime
