import numpy as np
from numpy.random import default_rng
rng = default_rng()
print('Welcome to the dice roller!')
print('###########################')
with open('ascii-art_d20.txt') as art:
    d20ascii = art.read()
print(d20ascii)
print('Enter a number of dice followed by the dice type to roll. \n For example, type 4d4 to roll 4 d4s or d20 to roll a d20')
from time import sleep
def overprint(text,repl, t=1, char=" "):
    print(text, end="\r")
    sleep(t) 
    print('\r{0:{1}<{2}}'.format(repl, char, len(text)))

def overprint_mult(repls, t=1, char=''):
    for i, repl in enumerate(repls):
        sleep(t)
        if i !=0:
            print('\r{0:{1}<{2}}'.format(repl, char, len(repls[i-1])), end='\r')
        elif i ==0:
            print(repl, end="\r")
        elif repl == repls[-1]:
            print(repl, end="\n")
            
def parse_command(command):

    cmds = command.split('d')
    if len(cmds) == 1:
        print('This is a dice roller!')
        return
    numdice = cmds[0]
    if numdice == '':
        numdice = '1'
    if numdice == 'a':
        numdice = 'Advantage'
    dicetype = cmds[1]
    return numdice, dicetype
def roll_dice(dicetype):
    global rng
    arrs = {'100':np.arange(1,101, 1), '20':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],'12':[1,2,3,4,5,6,7,8,9,10,11,12],'10':np.arange(1,11,1),
    '8':np.arange(1,9,1), '6':np.arange(1,7,1), '4':np.arange(1,5,1)}
    poss_vales = arrs[dicetype]
    roll = rng.choice(poss_vales)
    return roll
def bigger(x,y):
    if x > y:
        return x
    else: 
        return y


while True:
    try:
        command = input('>>> ' )
    except KeyboardInterrupt:
        break
    print(command)
    # overprint_mult(['[#    ]', '[##   ]', '[###  ]', '[#### ]', '[#####]', 'Loaded'])
    print('')
    numdice, dicetype = parse_command(command)
    if numdice == 'Advantage':
        result = roll_dice(dicetype)
        result2 = roll_dice(dicetype)
        print('Rolling d{} with advantage'.format(dicetype))
        # print(result)
        # print(result2)
        overprint_mult([str(result), str(result2), str(bigger(result, result2))])
        print('Result is {}'.format(bigger(result, result2)))
        continue
    print('Rolling d{}'.format(dicetype))
    running_total = 0
    for i in range(0, int(numdice)):
        result = roll_dice(dicetype)
        if result == 20 and dicetype == '20':
            print(d20ascii)
        running_total += result
        print(result)
    print('Total: {}'.format(running_total))
    # print(parse_command(command))

