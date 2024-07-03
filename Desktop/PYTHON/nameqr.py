import qrcode
img = qrcode.make('Nawaraj Panday')
type(img)#qrcode.image 
img.save("Nawaraj.png")
