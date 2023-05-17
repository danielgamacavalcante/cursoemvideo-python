
import pyautogui

import keyboard as kb

def getPosition():

   procurar = 'sim'
   pyautogui.alert('Posicione o mouse no local desejado e aperte a tecla "e" :')
   while(procurar == 'sim'):
    try:
      if kb.is_pressed('e'): 
        x, y = pyautogui.position()
        print("Posicao atual do mouse:")
        print ("x = "+str(x)+" y = "+str(y))
        pyautogui.alert('Aposição é X='+str(x)+' e Y='+str(y))
        procurar = 'nao'
          

    except:
       print('Saiu do IF')
       procurar = 'nao'    
       


getPosition()

