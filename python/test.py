import platform
import subprocess
  
def checksystem():
    if 'Windows' in platform.system() :
        subprocess.call("cls", shell=True) # windows上执行cls命令
    if 'Linux' in platform.system() :    
        subprocess.call("clear") # linux上借助于call执行clear命令  

checksystem()    


 

