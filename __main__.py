# Author Kiselev Nikolay 2017


import os, subprocess, time

print('''
   ___  _                          _                
  /___\| |__   _   _   ___  _ __  (_) _   _         
 //  //| '_ \ | | | | / _ \| '_ \ | || | | |        
/ \_// | | | || |_| ||  __/| | | || || |_| |        
\___/  |_| |_| \__,_| \___||_| |_||_| \__, |        
                                      |___/         
  _____              _           _  _               
  \_   \ _ __   ___ | |_   __ _ | || |  ___  _ __   
   / /\/| '_ \ / __|| __| / _` || || | / _ \| '__|  
/\/ /_  | | | |\__ \| |_ | (_| || || ||  __/| |     
\____/  |_| |_||___/ \__| \__,_||_||_| \___||_|     
                                                    
    ___        _                                    
   /   \ _ __ (_)__   __  ___  _ __   ___  __   __  
  / /\ /| '__|| |\ \ / / / _ \| '__| / _ \ \ \ / /  
 / /_// | |   | | \ V / |  __/| |   | (_) | \ V /   
/___,'  |_|   |_|  \_/   \___||_|    \___/   \_/    
                                                    
 ____    ___    ___    ___                 _  _____ 
|___ \  / _ \  / _ \  / _ \    _    _____ / ||___  |
  __) || | | || | | || | | | _| |_ |_____|| |   / / 
 / __/ | |_| || |_| || |_| ||_   _||_____|| |  / /  
|_____| \___/  \___/  \___/   |_|         |_| /_/   
                                                    
''')

COMMAND = "echo sas"
PROCCES = subprocess.Popen(COMMAND.split(), stdout=subprocess.PIPE)
OUTPUT, ERROR = PROCCES.communicate()

print(OUTPUT)

time.sleep(1)
print("\n\nВсе ок. Припупим.")

ANSWER = input("Не обходимо обновить пакеты, так как вот так вот. Ок? (y/отстань)")
print("Пытаемся понять ваш ответ: " + ANSWER)

time.sleep(1)
print("Прервать: ^C")

time.sleep(2)
print("Ну ок. Ставим.")

print("Будьте добры ввести пароль от корня. У вас всего 3 попы\nтки.\n\n\n")
COMMAND = "sudo apt update"
print("\nвыполняем apt update\n")
PROCCES = subprocess.call(COMMAND.split())

print("\n\nГАТОВА!)\n\n")
time.sleep(1)

print("МОЖЕТ БЫТЬ нужно будет ввести пароль от корня. У вас всего 3 попы\nтки.\n\n\n")
COMMAND = "sudo apt upgrade -y"
print("\nвыполняем apt upgrade\n")
PROCCES = subprocess.call(COMMAND.split())

ANSWER = input("Ты готов сменить пол компьютера?")

print("\n\n\n\n\nDu")
time.sleep(0.5)
print("Du hast")
time.sleep(0.4)
print("Du hast mich")
time.sleep(0.5)
print("Du hast mich")

time.sleep(1)
print("Du hast mich gefragt")
time.sleep(4)

DIR, FILE = os.path.split(os.path.abspath(__file__))
print("\n\n\n\n", DIR)

print("\nКАНФЕГУРАЦЕЯ\n")
ANSWER = input("Ты готов ввести пароль еси чо?")

FILE = "JEFI_DONT_MOVE_PLIS"

for i in range(3):
    COMMAND = "sudo dpkg -i {0}/{1}".format(DIR, FILE)
    print("\n", COMMAND, "\n")
    PROCCES = subprocess.call(COMMAND.split())

    COMMAND = "sudo apt -f install"
    print("\n", COMMAND, "\n")
    PROCCES = subprocess.call(COMMAND.split())


RECOMENDS = "\nЭТО ВСЕ, ЧТО НУЖНО, НО...\nвыполните: reboot\nпосле перезагрузки: xinput\nafter dat shit plug in your tablet.\nHAVE A NICE ВРЕМЯ."
print(RECOMENDS)

print("\nDu hast.")
