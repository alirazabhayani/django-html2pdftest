# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template import Context
from django.template.loader import get_template
from django_html2pdf.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    print 'HELLO'
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
             "invoice_id": 123,
             "customer_name": "John Cooper",
             "amount": 1399.99,
             "today": "Today",
        }
        html = template.render(Context(context))
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class GeneratePdf2(View):
    def get(self, request, *args, **kwargs):
        data = {
          'today': datetime.date.today(),
          'amount': 39.99,
         'customer_name': 'Cooper Mann',
         'order_id': 1233434,
        }
        print 'Data is ', data
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
