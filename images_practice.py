from PIL import Image
fig=Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg')
#fig.putalpha(128)
#fig.resize(200,200)
#fig.size
#fig.save("location")
pic=fig.crop((0,0,50,30))
fig.paste(im=pic,box=(0,0),mask=None)
fig.show()