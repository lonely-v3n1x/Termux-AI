import subprocess as sp

api='/data/data/com.termux/files/usr/libexec/termux-api'

def runcmd(tp):
    return sp.run([api,tp],stdout=sp.PIPE, stderr=sp.PIPE)

ru=runcmd('TelephonyDeviceInfo')

print(ru.stdout)
