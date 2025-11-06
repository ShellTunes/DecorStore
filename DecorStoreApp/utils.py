from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

# from xhtml2pdf import pisa
from pathlib import Path

def render_to_pdf(template_src, context_dict=[]):
    template = get_template(template_src)
    html  = template.render({'data':context_dict})
    print('context', context_dict[0]['quoteid'])
    result = BytesIO()
    print("TODO add pdf")
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    # file = Path('./pdf_dir/'+str(context_dict[0]['quoteid'])+'.pdf')
    # if not file.is_file():
    #     with open('./pdf_dir/'+str(context_dict[0]['quoteid'])+'.pdf', 'wb+') as output:
    #         pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), output)
    #         print('pdf', pdf)
    # if not pdf.err:
    #     return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
