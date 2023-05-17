
import pyautogui

import keyboard as kb

def getPosition():

   procurar = 'sim'
   while(procurar == 'sim'):
    try:
      # pyautogui.keyUp(mouse.Button.left)
      if kb.is_pressed('e'): 
        x, y = pyautogui.position()
        print("Posicao atual do mouse:")
        print ("x = "+str(x)+" y = "+str(y))
        procurar = 'nao'
          

    except:
       print('Saiu do IF')
       procurar = 'nao'    
       


getPosition()

