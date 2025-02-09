from PIL import Image
#change colors
im=Image.open('CHina.jpg')
print(im,type(im))
r,g,b=im.split()
print(r,g,b)
om=Image.merge(mode="RGB",bands=(b,g,r))
om.save('newmap.jpg')