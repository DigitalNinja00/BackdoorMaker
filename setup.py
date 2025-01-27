import os
import time
import subprocess
import colorama
import halo
import cmd
import random
import readline
from colorama import Fore

def ban_1():
	lista = [
	"        .-\"\"\"\".",
	"       /       \\",
	"   __ /   .-.  .\\",
	"  /  `\\  /   \\/  \"", 
	"  |  _ \\/   .==.==.",
	"  | (   \\  /____\\__\"",
	f"   \\ \\      {Fore.WHITE}(_{Fore.RED}(){Fore.WHITE}(_{Fore.RED}(){Fore.RESET}",
	"    \\ \\            '---._",
	f"     \\                   \\_          {Fore.YELLOW}##{Fore.RED}BACKDOOR MAKER{Fore.YELLOW}##{Fore.RESET}",
	"  /\\ |`       (__)________/",
	" /  \\|     /\\___/",
	f"|    \\     \\||{Fore.RED}VV{Fore.RESET}",
	f"|     \\     \\|{Fore.RED}\"\"\"\"{Fore.RESET},",
	"|      \\     ______)",
	"\\       \\  /`",
	"         \\("]
	for i in lista:
		print(i);

def ban_2():
	lista_2 = ["              __.......__",
	"            .-:::::::::::::-.", 
	"          .:::''':::::::''':::.",
	"        .:::'     `:::'     `:::.", 
	"   .'\\  ::'   ^^^  `:'  ^^^   '::  /`.",
	"  :   \\ ::   _.__       __._   :: /   ;",
	" :     \\`: .' ___\\     /___ `. :'/     ;", 
	f":       /\\   {Fore.RED}(_|_){Fore.RESET}\\   /{Fore.RED}(_|_){Fore.RESET}   /\\       ;",
	":      / .\\   __.' ) ( `.__   /. \\      ;", 
	":      \\ (        {   }        ) /      ;",
	" :      `-(     .  ^\"^  .     )-'      ;",
	"  `.       \\  .'<`-._.-'>'.  /       .'",
	"    `.      \\    \\;`.';/    /      .'", 
	f"      `._    `-._       _.-'    _.'        {Fore.RED}#{Fore.YELLOW}>{Fore.GREEN}BACKDOOR MAKER {Fore.YELLOW}<{Fore.RED}$",
	"       .'`-.__ .'`-._.-'`. __.-'`.",
	"     .'       `.         .'       `.",
	"   .'           `-.   .-'           `."]
	for y in lista_2:
		print(y);
def ban_3():
	lista_3 = ["        ,     .",
	f"        /(     )\\               {Fore.RED}A{Fore.RESET}",
	f"   .--.( `.___.' ).--.         {Fore.RED}/_\\{Fore.RESET}",
	f"   `._ `%_&%#%$_ ' _.'     {Fore.RED}/| {Fore.YELLOW}<{Fore.GREEN}___{Fore.YELLOW}>{Fore.RED} |\\{Fore.RESET}",
	f"      `|{Fore.YELLOW}({Fore.RED}@{Fore.YELLOW}\\{Fore.RESET}*%%{Fore.YELLOW}/{Fore.RED}@{Fore.YELLOW}){Fore.RESET}|'       {Fore.RED}/ {Fore.RED}(  |L|  ) \\{Fore.RESET}",
	f"       |  |%%#|  |       {Fore.RED}J d8bo|=|od8b L{Fore.RESET}",
	f"        \\ \\$#%/ /        {Fore.RED}| 8888|=|8888 |{Fore.RESET} {Fore.YELLOW}#{Fore.RED}BACKDOORMAKER{Fore.YELLOW}#{Fore.RESET}",
	f"        |\\|%%#|/|        {Fore.RED}J Y8P\"|=|\"Y8P F{Fore.RESET}",
	f"        | (.\".)%|         {Fore.RED}\\ (  |L|  ) /{Fore.RESET}", 
	f"    ___.'  `-'  `.___      {Fore.RED}\\|  |L|  |/{Fore.RESET}",
	"  .'#*#`-       -'$#*`.       / )|",
	" /#%^#%*_ *%^%_  #  %$%\\    .J (__)",
	" #&  . %%%#% ###%*.   *%\\.-'&# (__)",
	" %*  J %.%#_|_#$.\\J* \\ %'#%*^  (__)",
	" *#% J %$%%#|#$#$ J\\%   *   .--|(_)"]
	for z in lista_3:
		print(z)
class System:
	def chdir(ruta):
		try:
			os.chdir(ruta)
		except OSError as error:
			print(error)
	def lister():
		try:
			dir = os.listdir();
			for x in dir:
				print(x);
		except OSError as error:
			print(error);
	def listener(port):
		try:
			os.system(f"nc -lvp {port}")
		except OSError as error:
			print(error);
def sss(number):
	if(number == 1):
		ban_1()
	if(number== 2):
		ban_2();
	if(number==3):
		ban_3()
class Consola(cmd.Cmd):
	prompt = Fore.RED+">>> "+Fore.RESET
	def do_exit(self, arg):
		"""your RETURN 0;"""
		return True
	def do_cd(self, arg):
		"""Change Directory"""
		System.chdir(arg);
	def do_ls(self, arg):
		"""List directory"""
		System.lister();
	def do_listen(self, arg):
		"""
		listen in port
		command:
		listen <portnumber>
		"""
		System.listener(arg);
ran = random.choice([1, 2, 3]);
if __name__ == '__main__':
	sss(ran)
	mishell = Consola();
	mishell.cmdloop();