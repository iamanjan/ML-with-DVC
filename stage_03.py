#read file
with open('artifact.txt','r') as f:
    text=f.read()

with open('artifact.txt','w') as f:
    f.write(text+'i hav added one line')

print(text) 
print('its an end of stage 3')   