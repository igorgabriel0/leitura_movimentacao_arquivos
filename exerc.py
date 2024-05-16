import re
from tkinter.filedialog import askdirectory
import TEXTOPDF as topdf
import os

def pdfGet(dir):
  list = []
  for file in os.listdir(dir):
    # Check whether file is in text format or not
    if file.endswith(".PDF") or file.endswith(".pdf") :
        file_path = f"{file}"
        list.append(str(file_path))
  return (list)

def getExerc(string):
  global ano
  pattern = 'EXERCÍCIO'
  lines_number = []
  for m in re.finditer(pattern, string):
    start = m.start()
    lineno = string.count('\n', 0, start)
    lines_number.append(lineno)
    break
  for l in lines_number: 
    print ("Ano Fabricação encontrado......:"+string.split('\n')[l+1])
    ano = string.split('\n')[l+1]
    return (string.split('\n')[l+1])


diretorio = askdirectory() 
Lista_pdfs = pdfGet(diretorio)
for i in (Lista_pdfs):
  try:
    text = topdf.convert_pdf_to_string("".join([str(diretorio),'/',str(i)]))
    getExerc(text)
    print(f"ARQUIVO: {i}")
    if ano >= "2023":
        pasta = "VIGENTE"
    else:
        pasta = "NAO VIGENTE"
    dir_final = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\CRLV_eu\PDFS"+f"/{pasta}"
    print(dir_final)
    
    if not os.path.exists(f'{dir_final}'):
        os.makedirs(f'{dir_final}')
        print(f"PASTA: {pasta} criada")
    else:
        print(f"\nJá existe a pasta {pasta}\n")

    print(f"\nLENDO {i}...\n")
    os.replace(f"{diretorio}/{i}", f"{dir_final}/{i}")
    print(f"MOVIDO") 

  except Exception as e:
    print(f"ERRO: {e}")