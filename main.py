import os
import pikepdf

def decrypt_pdf(file_name):
    input_path = os.path.join(os.getcwd(), file_name)
    output_path = os.path.join(os.getcwd(), "decrypted_"+file_name)
    input_pdf = pikepdf.Pdf.open(input_path)
    pdf = pikepdf.Pdf.new()

    for _, page in enumerate(input_pdf.pages):
        pdf.pages.append(page)
        
    pdf.save(output_path)
    input_pdf.close()
    print("saved at : {}".format(output_path))

if __name__ == "__main__":
    if len(os.sys.argv)>1:
        decrypt_pdf(os.sys.argv[1])
    else:
        print("re-run with file name")