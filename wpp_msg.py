from selenium import webdriver
import time

file = open("msg.txt","r")
names = []
msgs = []
for line in file:
	names.append(line)
	msgs.append(file.readline())
print(msgs)
print(names)


# Para los campos de entrada

### Nombre del chat en wpp
### Mensaje que se desea emviar 

# Estos dos campos deben estar en un línea cada uno 
# y finalizar con un salto de línea



driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code')

for i in range(len(names)):
	name = names[i][:-1]
	msg = msgs[i][:-1]

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_class_name('_2S1VP')

	for i in msg:
	    msg_box.send_keys(i)
	    time.sleep(0.2)

	button = driver.find_element_by_class_name('_2lkdt')
	button.click()
