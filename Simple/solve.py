from subprocess import check_output, PIPE, STDOUT, Popen
from string import ascii_letters, digits

alpha = ascii_letters + digits + '_{}'
encrypted_flag = open('output.txt', 'r').read().split()


def encrypt_char(payload):
	p = Popen(['./vm', 'task.raw'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
	grep_stdout = p.communicate(input=payload.encode())[0]
	return grep_stdout.decode().split()[4:]


flag = ''
for enc in encrypted_flag:
	for ch in alpha:
		payload = '%s\n' % (flag + ch)
		if encrypt_char(payload)[-1] == enc:
			break
	flag += ch

print(flag)