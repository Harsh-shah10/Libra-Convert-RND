import subprocess # Import subprocess module
import os

def convert_file_to_pdf(file_path, output_dir):
    result = subprocess.run(
            f'libreoffice --headless --convert-to pdf "{file_path}" --outdir "{output_dir}"',
            shell=True,
            capture_output=True,
            text=True
        )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
        
    pdf_file_path = f'{output_dir}{file_path.rsplit("/", 1)[1].split(".")[0]}.pdf'
    
    if os.path.exists(pdf_file_path):
        return pdf_file_path
    else:
        return None
    
file_path = '/home/harry/Documents/Office Preview/docs/file.doc'
output_dir = '/home/harry/Documents/Office Preview/converted/'
file = convert_file_to_pdf(file_path, output_dir)
if file:
    print(f'File converted to {file}.')
else:
    print('Unable to convert the file.')