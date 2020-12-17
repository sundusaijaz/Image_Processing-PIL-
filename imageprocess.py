from PIL import Image

###Open imgae

file = 'one.jpg'

img = Image.open(file)

img.show()

###create new image

new_img = Image.new("RGB",(400,400),(0,125,255))

new_img.show()

###rotate image

rotate_img = img.rotate(angle=90,expand=True,fillcolor='pink')

rotate_img.show()

###rotate image

resize_img = img.resize((int(img.width/2),int(img.height/2)),resample=Image.LANCZOS,box=(20,20,100,100))

resize_img.show()

###blending two images

file2 = 'two.jpg'

img2 = Image.open(file2)

blended_img = Image.blend(img,img2,alpha=0.5)

blended_img.show()

###crop image

crop_img = img.crop(box=(20,20,200,200))

crop_img.show()