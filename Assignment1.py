from PIL import Image
fig1=Image.open('word_matrix.png')
fig2=Image.open('mask.png')
wh=fig1.size
fig2=fig2.resize((wh))
fig2.putalpha(180)
fig1.paste(fig2,box=(0,0),mask=fig2)
fig1.show()