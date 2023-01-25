import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext(r'E: \Document_Classification\Images\ITR.png')

print(results)

text = ''
for result in results:
    text += result[1] + ' '

print(text)
