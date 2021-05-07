import tabula
import pdftotext

csvfile = './tabula-csv-out/2020-12-26_0e147c0b0fb969662fdcaa21f5f519a6_SALARIOS_PN_MARZO_2019/test.csv'
filename = './pdf-parts/2020-12-26_0e147c0b0fb969662fdcaa21f5f519a6_SALARIOS_PN_MARZO_2019/sep-1.pdf'
df = tabula.io.read_pdf(filename, output_format='dataframe', pages='all', guess=False, stream=True, lattice=False)[0]
df.to_csv(csvfile)

txtfile = './pdftotext-out/2020-12-26_0e147c0b0fb969662fdcaa21f5f519a6_SALARIOS_PN_MARZO_2019/test.txt'

with open(filename, "rb") as f:
    pdf = pdftotext.PDF(f)
    
with open(txtfile, "w") as f:
    f.write(''.join(pdf))
