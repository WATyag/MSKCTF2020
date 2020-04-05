from pwn import *

tree = eval(open('tree', 'r').read())

r = remote('funny-farm.tasks.2020.ctf.cs.msu.ru', 20009)

r.recv().decode()
r.sendline('Y')

req = 'tree[1]'
guess = tree[0]
guess = "".join([str(el) for el in guess])
r.recv().decode()

while True:
	r.sendline(guess.encode())

	try:
		data = r.recv().decode()
	except:
		exit(0)

	if 'Great' in data:
		print(data)
		guess = tree[0]
		req = 'tree[1]'
		guess = "".join([str(el) for el in guess])
		continue
	elif 'MSKCTF' in data:
		print(data)
		exit(0)


	kek = "(%s)" % ", ".join(data.split())
	req = req + "['%s']" % kek

	guess = eval(req + '[0]')
	req += '[1]'
	guess = "".join([str(el) for el in guess])
