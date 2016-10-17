from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()

#int inCount =  len([name for name in os.listdir('invoices') if os.path.isfile(name)])
#int pCount= len([name for name in os.listdir('pslips') if os.path.isfile(name)])

#if inCount != pCount:
#    raise Exception("Invoices and Packaging Slips do not coincide")

os.makedirs("./merged/")
invoices = os.listdir('invoices')
pslips = os.listdir('pslips')
cwd = os.path.dirname(os.path.abspath(__file__))

if len(invoices) != len(pslips):
	raise Exception ("Invoices and pslips not equal")

for invoice, pslip in zip(invoices, pslips):
	inOne = open(cwd + '/invoices/' + invoice, "rb")
	inTwo = open(cwd + '/pslips/' + pslip, "rb")
	merger.append(inOne)
	merger.append(inTwo)

	filename = os.path.split(invoice)[1]
	output = open("./merged/" + filename, "wb")
	merger.write(output)

