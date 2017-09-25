from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    print 'context_dict ', context_dict
    template = get_template(template_src)
    html  = template.render(Context(context_dict))
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
