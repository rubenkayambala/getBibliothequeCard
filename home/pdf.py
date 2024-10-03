from io import BytesIO
from unittest import result
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def makepdf(template_source, context_dict={}):
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
    if not pdf:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None

# def makepdf(template_source, context_dict={}):
#     template = get_template(template_source)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
#     if not pdf:
#         return HttpResponse(result.getvalue(), content_type="application/pdf")
#     return None