import fitz  # PyMuPDF

def pdf_to_text(pdf_path, txt_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize an empty string to store the text
    pdf_text = ""
    
    # Iterate through each page
    for page_num in range(pdf_document.page_count):
        # Get the page
        page = pdf_document.load_page(page_num)
        # Extract text from the page
        pdf_text += page.get_text()
    
    # Write the text to a .txt file
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_text)

    print(f"Text from {pdf_path} has been saved to {txt_path}")

# Example usage
pdf_to_text('breast_cancer.pdf', 'input/breast_cancer.txt')
