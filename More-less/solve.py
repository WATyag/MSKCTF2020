from pwn import *

r = remote('more-less.tasks.2020.ctf.cs.msu.ru', 20001)

data = r.recv().decode()
for _ in range(3):
	left = 0
	right = 1023
	
	while left + 1 < right:
		mid = (left + right) // 2
		
		r.sendline(str(mid).encode())
		data = r.recv().decode()

		if 'smaller' in data:
			right = mid
		elif 'bigger' in data:
			left = mid
		elif 'right' in data:
			print('Guessed')
			break

print(data)