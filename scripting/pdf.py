import PyPDF2

# template = PyPDF2.PdfReader(open("super.pdf", "rb"))
# watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
# output = PyPDF2.PdfWriter()

with open("twopage.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    # page_edit = len(reader.pages)
    page_edit = reader.pages[0]
    page_edit.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page_edit)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)

#     with open("watermarked.pdf", "wb") as file:
#         output.write(file)
