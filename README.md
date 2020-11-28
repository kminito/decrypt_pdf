"# decrypt_pdf" 

PDF 파일의 '암호 해제'가 아닌, 암호가 없는 동일한 내용의 파일을 생성하는 코드. (읽기 권한 필수)



2020.11.28  
pikepdf 사용시 정상 작동

```python
import pikepdf

input_pdf = pikepdf.Pdf.open('test.pdf')
pdf = pikepdf.Pdf.new()

for n, page in enumerate(input_pdf.pages):
    pdf.pages.append(page)
    
pdf.save('test_decrypted.pdf')
```




2020.11.19
아래와 같이 PyPDF2를 사용할 경우
 - 대부분의 PDF 파일에서 정상 작동하나 일부에서 오류 발생
 -> Acrobat 이 아닌 다른 프로그램을 사용하여 PDF 파일 작성할 경우에 오류 발생하는 것이었음

pikepdf로 변경 예정

```python
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(file_name):

    input_path = os.path.join(os.getcwd(), file_name)
    output_path = os.path.join(os.getcwd(), "decrypted_"+file_name)

    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        reader = PdfFileReader(input_file)

        writer = PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))
        
        writer.write(output_file)

if __name__ == "__main__":
    decrypt_pdf(os.sys.argv[1])
```
