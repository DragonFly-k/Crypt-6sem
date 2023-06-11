import stegospacings

stegospacings.encode('katy', 'container.docx', 'encoded.docx')
print(stegospacings.decode('encoded.docx'))
