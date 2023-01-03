from django.shortcuts import render
from docx import Document
from docx.shared import Pt
from datetime import date
from django.shortcuts import redirect
# Create your views here.


def index(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def kompleksen_doklad(request):
    if request.method == 'GET':
        # form = KompleksenDokladForm()

        template = 'pages/kompleksen.html'

        context = {
            # 'form': form
        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST
        document = Document()
        title = document.add_paragraph().add_run(form_data['docnum'])
        title.font.size = Pt(14)

        document.add_paragraph(form_data['vazlozhitel'])
        document.add_paragraph(form_data['build'])
        document.add_paragraph(form_data['location'])

        document.save('demo.docx')

        return redirect('/')


def okonchatelen_doklad(request):
    if request.method == 'GET':
        # form = OkonchatelenDokladForm()

        template = 'pages/okonchatelen.html'

        context = {
            # 'form': form
        }

        return render(request, template, context)