# https://imasters.com.br/back-end/automacao-de-gui-com-python-exemplo-de-uso-do-pyautogui-2
# https://www.hashtagtreinamentos.com/automacao-programa-sistema-python#:~:text=Clicar%20no%20arquivo%20e%20arrastar,-Ap%C3%B3s%20utilizar%20o&text=position%20para%20que%20voc%C3%AA%20consiga,se%20est%C3%A1%20na%20posi%C3%A7%C3%A3o%20correta.
# https://pt.stackoverflow.com/questions/523593/usar-if-no-pyautogui-em-pythonautoma%C3%A7%C3%A3o
import pyautogui 
import keyboard as kb
import time
import pygetwindow
import pytesseract
import cv2


windowExecute = str('PokeMMO')

#iniciando código
pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
password = input('Informe senha: ')
numberItem = input('Informe número do item a ser utilizado: ')
pyautogui.PAUSE = 0.5
#acessando aplicativo
pyautogui.press("winleft")

pyautogui.write(windowExecute)

pyautogui.press("enter")


#acessando janela

window = pygetwindow.getWindowsWithTitle("PokeMMO")
# window = window[0].maximize()
# window.activate()

if window != []:
    try:
        window[0].activate()
    except:
        window[0].minimize()
        window[0].maximize()

# window.resizeTo(1280,720)


#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
# x, y = pyautogui.position()
# print("Posicao atual do mouse:")
# print ("x = "+str(x)+" y = "+str(y))
#retorna True se x & y estiverem dentro da tela
# print ("\nEsta dentro da tela?")
# resp = pyautogui.onScreen(x, y)
# print(str(resp))
def getPosition():

   procurar = 'sim'
   while(procurar == 'sim'):
    try:
      pyautogui.alert('Posicione o mouse no local desejado e aperte a tecla "e" :')
      if kb.is_pressed('e'): 
        x, y = pyautogui.position()
        print("Posicao atual do mouse:")
        print ("x = "+str(x)+" y = "+str(y))
        procurar = 'nao'
          

    except:
       print('Saiu do IF')
       procurar = 'nao'    
       
pyautogui.moveTo(669,359,duration=0.5)
pyautogui.sleep(4.5)
pyautogui.write("zatiros",interval=0.2)
pyautogui.press('enter')
pyautogui.write(password)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.keyDown(numberItem)
pyautogui.keyUp(numberItem)
pyautogui.moveTo(356,37,duration=0.3)
pyautogui.sleep(3.5)

image = pyautogui.screenshot(region=(381,52,300,100))
image.save(r'c:/Users/user/Desktop/repositorio-de-outros/cursoemvideo-python/img/minha_imagem.png')

caminho = r"C:\Users\user\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho+r"\tesseract.exe"
image2 = cv2.imread(r'c:/Users/user/Desktop/repositorio-de-outros/cursoemvideo-python/img/minha_imagem.png')
text = pytesseract.image_to_string(image2)
open('texto.txt','w').write(text)
print(text)
if(text == open('texto.txt','r')):
   pyautogui.click()
   pyautogui.sleep(5.5)
   name_poke = pyautogui.screenshot()
   name_poke.save(r'c:/Users/user/Desktop/repositorio-de-outros/cursoemvideo-python/img/nome_poke.png')
   image2 = cv2.imread('nome_poke.png')
else:
   if(text =='Not even a nibble... '):
      pyautogui.click()
      pyautogui.sleep(0.5)
      pyautogui.click()
   else:
      print("Nada feito")
      
      3
      

# pyautogui.click()
# pyautogui.sleep(5.5)


# getPosition()
# x = 356 y = 37
#clicando em uma tecla e pressionando por 3s
# pyautogui.keyDown('s')
# time.sleep(3)
# pyautogui.keyUp('s')





