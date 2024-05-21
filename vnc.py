import os

print("Code by DuonngwTek, DONOT COPY!")
print("Starting now...")
cmd = 'sudo apt-get update'
os.system(cmd)
cmd = 'wget -O cr.deb "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"'
os.system(cmd)
cmd = 'sudo apt-get install ./cr.deb'
os.system(cmd)
cmd = 'wget -O rm.deb "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"'
os.system(cmd)
cmd = 'sudo apt-get install ./rm.deb'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver'
os.system(cmd)
cmd = 'sudo apt install xfce4-terminal -y'
os.system(cmd)
cmd = 'sudo apt-get install geany -y'
os.system(cmd)
cmd = 'sudo apt-get install vim-gtk3 -y'
os.system(cmd)
cmd = 'sudo apt install iputils-ping -y'
os.system(cmd)
cmd = 'sudo apt install neofetch -y'
os.system(cmd)
print("Complete! Please go to remotedesktop.google.com/headless to continue")
