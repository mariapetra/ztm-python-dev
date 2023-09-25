import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)

# with open("twopage.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     # page_edit = len(reader.pages)
#     page_edit = reader.pages[0]
#     page_edit.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page_edit)
#     with open("tilt.pdf", "wb") as new_file:
#         writer.write(new_file)
