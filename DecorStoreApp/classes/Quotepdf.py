from django.http import HttpResponse
from django.views.generic import View

from DecorStoreApp.utils import render_to_pdf
import datetime
from num2words import num2words
from django.utils.safestring import mark_safe
from django.conf import settings
import PyPDF2
from django.template.loader import get_template
from django.template import Context
# import xhtml2pdf as pisa
# import cStringIO as StringIO
from io import StringIO
import cgi

import os
from PyPDF2 import PdfFileMerger

# pdf


def GenerateQuotePdf(request, quote_list):
    allData = []
    totalSum = 0
    
    # for quote in (quote_list):
    if (quote_list['glass']):
        glasstotal = float(quote_list['glass'][-1]['totalamount'])
        glass = quote_list["glass"]
    else: 
        glasstotal = 0
        glass = ''
    if (quote_list['fittings']):
        fittingtotal = float(quote_list['fittings'][-1]['totalamount'])
        fittings = quote_list["fittings"]
    else: 
        fittingtotal = 0
        fittings = ''
    if (quote_list['misc']):
        misctotal = float(quote_list['misc'][-1]['totalamount'])
        misc = quote_list["misc"]
    else: 
        misctotal = 0
        misc = ""
    grandtotal = grandtotal = round(glasstotal + fittingtotal + misctotal,2)

    igst = 0
    cgst = 0
    sgst = 0
    if quote_list['igst'] == 1:
        igst = round(((glasstotal + fittingtotal + misctotal) * 0.18), 2)

        if quote_list['discount']:
            discount = float(quote_list['discount'])
            if quote_list['discount_type'] == "percentage":
                discount = round((grandtotal * discount / 100), 2)  # Calculate % discount

            discountgrand_total = round((grandtotal - discount + igst), 2)
        else:
            discount = 0
            discountgrand_total = round((grandtotal - discount + igst), 2)

    elif quote_list['cgst'] == 1:
        cgst = round(((glasstotal + fittingtotal + misctotal) * 0.09), 2)
        sgst = round(((glasstotal + fittingtotal + misctotal) * 0.09), 2)

        if quote_list['discount']:
            discount = float(quote_list['discount'])
            if quote_list['discount_type'] == "percentage":
                discount = round((grandtotal * discount / 100), 2)  # Calculate % discount

            discountgrand_total = round((grandtotal - discount + cgst + sgst), 2)
        else:
            discount = 0
            discountgrand_total = round((grandtotal - discount + cgst + sgst), 2)

    else:
        if quote_list['discount']:
            discount = float(quote_list['discount'])
            if quote_list['discount_type'] == "percentage":
                discount = round((grandtotal * discount / 100), 2)  # Calculate % discount

            discountgrand_total = round((grandtotal - discount), 2)
        else:
            discount = 0
            discountgrand_total = grandtotal - discount


    data = {
        'client': quote_list['client'],
        'clientPhoneNo': quote_list['clientPhoneNo'],
        'clientaddress': quote_list['clientaddress'],
        'Pino': quote_list['piNo'],
        'pi_date': quote_list['pi_date'],
        'quoteItemmaster': glass,
        'misc': misc,
        'fittings': fittings,
        'totalsqft': quote_list['glasstotal'],
        'total' : round(grandtotal,0),
        'discounttotal': round(discountgrand_total,0),
        'unit' : quote_list['unit'],
        'interior_name': quote_list['interior_name'],
        'staffname': quote_list['staffname'],
        'staffnumber': quote_list['staffnumber'],
        'discount': discount,
        'number_in_words': num2words(round(discountgrand_total,0), lang='en_IN'),
        'quoteid': quote_list['quoteid'],
        'cgst': cgst,
        'igst': igst,
        'sgst': sgst,
        'igstvalue': quote_list['igst'],
        'cgstvalue': quote_list['cgst'],
        'terms': quote_list['terms'],
        'header': quote_list['header'],
        'preparedby': quote_list['preparedby']
    }
    # print("GENERATE QUOTELIST: ", quote_list)
    # print("GENERATE : ", quote_list['glass'][-1]['totalamount'])
    allData.append(data)
    # print("all", allData)
    grouped= {}
    for key in allData[0]['quoteItemmaster']:
        # print("chck", allData[0]['quoteItemmaster'])
        group = grouped.setdefault(key['glassItem'], [])
        group.append(key)
    allData[0]['grouped'] = grouped
    
    fittinggroup= {}
    for key in allData[0]['fittings']:
        # print("chck", allData[0]['fittings'])
        group = fittinggroup.setdefault(key['fittingItem'], [])
        group.append(key)
    allData[0]['fittinggroup'] = fittinggroup

    miscgroup= {}
    for key in allData[0]['misc']:
        # print("chck", allData[0]['misc'])
        group = miscgroup.setdefault(key['miscItem'], [])
        group.append(key)
    allData[0]['miscgroup'] = miscgroup

    # print("QUOTE RECEIVED ", allData)
    pdf = render_to_pdf('custom-templates/pdf/quotepdf.html', allData)
      
    # if pdf:
    source_dir = './pdf_dir/' 
    merger = PdfFileMerger()

    invoice_file = './pdf_dir/' + str(quote_list['quoteid'])+'.pdf'
    print('invoice', invoice_file)
    if quote_list['diagramfile'] and quote_list['diagram_file'] == 1:
        diagram_file =  './media/' + str(quote_list['diagramfile'])
        print('diagram_file', diagram_file)
    else:
        diagram_file = ''
    if invoice_file != '' and diagram_file != '': 
        to_merge = [invoice_file, diagram_file]

        merger = PdfFileMerger()
        for item in to_merge:
            merger.append(item)
        print('merge',to_merge)
            
        # Here check if you have already created the file 
        merger.write(source_dir + 'Output/'+str(quote_list['quoteid'])+'.pdf')       
        merger.close()
        
        diagramdata = source_dir + 'Output/'+str(quote_list['quoteid'])+'.pdf' 
        with open(diagramdata, 'rb') as f:
           file_data = f.read()
        pdf = PyPDF2.PdfFileReader(diagramdata,"rb")
        p = pdf.getPage(1)
        w_in_user_space_units = p.mediaBox.getWidth()
        h_in_user_space_units = p.mediaBox.getHeight()
        print('height',h_in_user_space_units,'width',w_in_user_space_units)
        w = float(p.mediaBox.getWidth()) * 0.352
        h = float(p.mediaBox.getHeight()) * 0.352
        print('new height',h,'new width',w)

        response = HttpResponse(file_data, content_type='application/pdf')
        print('pdf doc', diagramdata)
        filename = "QuotePDf.pdf"
        content = "inline; filename=%s" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content

        return response
    if invoice_file != '' and diagram_file == '':
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "PI-"+str(quote_list['piNo'])+"_"+allData[0]['client']+".pdf"
        content = "inline; filename=%s" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content

        return response
    return HttpResponse("Not found")
