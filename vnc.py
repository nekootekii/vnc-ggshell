import os

cmd = 'sudo apt-get update'
os.system(cmd)
cmd = 'sudo apt-get install xfce4-terminal -y'
os.system(cmd)
cmd = 'sudo apt-get install geany -y'
os.system(cmd)
cmd = 'sudo apt-get install vim-gtk3 -y'
os.system(cmd)
cmd = 'wget -O cr.deb "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"'
os.system(cmd)
cmd = 'sudo apt-get install ./cr.deb'
os.system(cmd)
print("Complete!")
