from django.views import View
from DecorStoreApp.models import *
from django.shortcuts import render, redirect
from .Quotepdf import *
from DecorStoreApp.projectmodules import *
import math


class printPDFView(View):
    def get(self, request,id):
        print("request from AJAXXXX:",id)
        glasslist = []
        fittinglist = []
        misclist = []
        totalquantity = 0
        totalarea = 0
        totalamount = 0
        amount = 0
        grandtotal = 0
        grandtotalarea =0
        length = 0
        width = 0
        glasstotal = 0
        unit = ''
        glassareatotal = 0
        quotes = Quote.objects.get(id=id)
        quoteGlass = LineItemGlass.objects.filter(QuoteId__id=id).all()
        
        
        for glass in quoteGlass:
            if quotes.gst == 1:
                rate = round((float(glass.Rate) / 1.18),2)
                amount = round((float(glass.Total) * rate),2)
                
            else:
                rate = float(glass.Rate)
                amount = float(glass.Total) * rate
            totalquantity += float(glass.Quantity)
            
            if glass.billedlength != '':
                length = float(glass.billedlength)
                width = float(glass.billedwidth)
                if glass.UnitOfMeasurement == 'mm':
                    length = round((length / 304.8),2)
                    width = round((width / 304.8),2)
                elif glass.UnitOfMeasurement == 'inch':
                    length = round((length / 12),2)
                    width = round((width / 12),2)
                else:
                    length = length
                    width = width
                
            else:
                length = float(glass.Length)
                width = float(glass.Width)
                if glass.UnitOfMeasurement == 'mm':
                    length = math.ceil((length / 304.8) /0.5) * 0.5
                    
                    width = math.ceil((width / 304.8) /0.5) * 0.5
                    
                elif glass.UnitOfMeasurement == 'inch':
                    length = math.ceil((length / 12) /0.5) * 0.5
                    
                    width = math.ceil((width / 12) /0.5) * 0.5
                    
                else:
                    length = length
                    width = width
            
            if glass.Polish == 1:
                polishname = 'Polish'
                if glass.Polishfeet:
                    polisharea = float(glass.Polishfeet)
                else:
                    polisharea = round((((length+width) * float(glass.Quantity)) * 2),2)
                polishtotal = polisharea * float(glass.PolishRate)
                polishtotal = round(polishtotal,2)
            else:
                polishname = ''
                polisharea = 0
                print('areapolish', polisharea)
                polishtotal = 0
            if glass.Beveling1 == 1:    
                beveling1name = '0.25 in Bevel'
                beveling1area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling1total = round((beveling1area * float(glass.Beveling1Rate)),2)
            else: 
                beveling1name = ''
                beveling1area = 0
                beveling1total = 0
            if glass.Beveling2 == 1:
                beveling2name = '0.5 in Bevel'
                beveling2area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling2total = round((beveling2area * float(glass.Beveling2Rate)),2)
            else:
                beveling2name = ''
                beveling2area = 0
                beveling2total = 0  
            if  glass.Beveling3 == 1:
                beveling3name = '0.75 in Bevel'
                print(" float" , round((beveling1area * float(glass.Beveling3Rate)),2))
                beveling3area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling3total = round((beveling3area * float(glass.Beveling3Rate)),2)
            else:
                beveling3name = ''
                beveling3area = 0
                beveling3total = 0

            if glass.Beveling4 == 1:    
                beveling4name = '1 in Bevel'
                beveling4area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling4total = round((beveling4area * float(glass.Beveling4Rate)),2)
            else:
                beveling4name = ''
                beveling4area = 0
                beveling4total = 0

            if glass.Beveling5 == 1:    
                beveling5name = '1.25 in Bevel'
                beveling5area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling5total = round((beveling5area * float(glass.Beveling5Rate)),2)
            else:
                beveling5name = ''
                beveling5area = 0
                beveling5total = 0

            if glass.Beveling6 == 1:    
                beveling6name = '1.5 in Bevel'
                beveling6area = round((((length+width) * float(glass.Quantity)) *2),2)
                beveling6total = round((beveling6area * float(glass.Beveling6Rate)),2)
            else:
                beveling6name = ''
                beveling6area = 0
                beveling6total = 0
            if glass.frosting  == 1:
                frostingarea = round(float(glass.Total),2)
                frostingtotal = round((frostingarea * float(glass.frostingRate)),2)
                frostingname = 'Frosting'
            else: 
                frostingname = ''
                frostingarea = 0
                frostingtotal = 0
            if glass.digital_printing  == 1:
                printingarea = round(float(glass.Total),2)
                printingtotal = round((printingarea * float(glass.printingRate)),2)
                printingname = 'Digital Printing'
            else:
                printingarea = 0
                printingtotal = 0
                printingname = ''

            if glass.etching  == 1:
                etchingarea = round(float(glass.Total),2)
                etchingtotal = round((etchingarea * float(glass.etchingRate)),2)
                etchingname = 'Etching'
            else:
                etchingarea = 0
                etchingtotal = 0
                etchingname = ''

            if glass.double_stroke  == 1:
                strokearea = round(float(glass.Total),2)
                stroketotal = round((strokearea * float(glass.strokeRate)),2)
                strokename = 'Double Stroke'
            else:
                strokearea = 0
                stroketotal = 0
                strokename = ''

            if glass.crystal  == 1:
                crystalarea = round(float(glass.Total),2)
                crystaltotal = round((crystalarea * float(glass.crystalRate)))
                crystalname = 'Crystal'
            else:
                crystalarea = 0
                crystaltotal = 0
                crystalname = ''

            if glass.lacquered   == 1:
                lacqueredarea = round(float(glass.Total),2)
                lacqueredtotal = round((lacqueredarea * float(glass.lacqueredRate)),2)
                lacqueredname = 'Lacquered '
            else:
                lacqueredarea = 0
                lacqueredtotal = 0
                lacqueredname = ''

            if glass.hole  == 1:
                holeqty = round(float(glass.holeQty),2)
                holetotal = round((holeqty * float(glass.holeRate)))
                holename = 'Hole'
                print('inside if', holeqty)
            else:
                holeqty = 0
                holetotal = 0
                holename = ''
                print('inside else', holeqty)

            if glass.cutout  == 1:
                cutoutqty = round(float(glass.cutoutQty),2)
                cutouttotal = cutoutqty * float(glass.cutoutRate)
                cutoutname = 'Cutout'
            else:
                cutoutqty = 0
                cutouttotal = 0
                cutoutname = ''

            if glass.spacer_hole  == 1:
                spacerholeqty = round(float(glass.spacerholeQty),2)
                spacerholetotal = round((spacerholeqty * float(glass.spacerholeRate)),2)
                spacerholename = 'Spacer Hole'
            else:
                spacerholeqty = 0
                spacerholetotal = 0
                spacerholename = ''

            if glass.screw_hole  == 1:
                screwholeqty = round(float(glass.screwholeQty),2)
                screwholetotal = round((screwholeqty * float(glass.screwholeRate)),2)
                screwholename = 'Screw Hole'
            else:
                screwholeqty = 0
                screwholetotal = 0
                screwholename = ''
            
            grandtotal = float(polishtotal) + float(amount) + float(beveling1total) + float(beveling2total) + float(beveling3total) + float(beveling4total) + float(beveling5total) + float(beveling6total) + float(frostingtotal) + float(printingtotal) + float(etchingtotal) + float(stroketotal) + float(crystaltotal) + float(lacqueredtotal) + float(holetotal) + float(cutouttotal) + float(spacerholetotal) + float(screwholetotal)
            totalamount += grandtotal

            grandtotalarea = float(glass.Total) + polisharea + beveling1area + beveling2area + beveling3area + beveling4area + beveling5area + beveling6area
            totalarea += grandtotalarea + frostingarea + printingarea + etchingarea + strokearea + crystalarea + lacqueredarea

            glasstotal += float(glass.Total) 
            print('totalamount', totalamount)
            glass = {
                'glassid': glass.id,
                'glassItem': glass.ItemMasterId.Name,
                'length' : glass.Length,
                'width' : glass.Width,
                'qty': glass.Quantity,
                'rate': rate,
                'total': round(float(glass.Total),2),
                'unit': glass.UnitOfMeasurement,
                'totalqty': totalquantity,
                'totalarea': totalarea,
                'totalamount': round(totalamount,2),
                'amount': round(amount,2),
                'beveling1Rate': glass.Beveling1Rate,
                'beveling1Total': beveling1total,
                'beveling1name': beveling1name,
                'beveling1area': beveling1area,
                'beveling1': glass.Beveling1,
                'polish': glass.Polish,
                'polishRate': glass.PolishRate,
                'polishTotal': polishtotal,
                'polisharea': polisharea,
                'polishname': polishname,
                'glasstotal': round(glasstotal,2),
                'beveling2': glass.Beveling2,
                'beveling2Rate': glass.Beveling2Rate,
                'beveling2Total': beveling2total,
                'beveling2name': beveling2name,
                'beveling2area': beveling2area,

                'beveling3': glass.Beveling3,
                'beveling3Rate': glass.Beveling3Rate,
                'beveling3Total': beveling3total,
                'beveling3name': beveling3name,
                'beveling3area': beveling3area,

                'beveling4': glass.Beveling4,
                'beveling4Rate': glass.Beveling4Rate,
                'beveling4Total': beveling4total,
                'beveling4name': beveling4name,
                'beveling4area': beveling4area,

                'beveling5': glass.Beveling5,
                'beveling5Rate': glass.Beveling5Rate,
                'beveling5Total': beveling5total,
                'beveling5name': beveling5name,
                'beveling5area': beveling5area,

                'beveling6': glass.Beveling6,
                'beveling6Rate': glass.Beveling6Rate,
                'beveling6Total': beveling6total,
                'beveling6name': beveling6name,
                'beveling6area': beveling6area,
                
                'frosting': glass.frosting,
                'frostingRate': glass.frostingRate,
                'frostingtotal': frostingtotal,
                'frostingname': frostingname,
                'frostingarea': frostingarea,
                
                'printing': glass.digital_printing,
                'printingRate': glass.printingRate,
                'printingTotal': printingtotal,
                'printingname': printingname,
                'printingarea': printingarea,
                
                'etching': glass.etching,
                'etchingRate': glass.etchingRate,
                'etchingTotal': etchingtotal,
                'etchingname': etchingname,
                'etchingarea': etchingarea,
                
                'stroke': glass.double_stroke,
                'strokeRate': glass.strokeRate,
                'strokeTotal': stroketotal,
                'strokename': strokename,
                'strokearea': strokearea,
                
                'crystal': glass.crystal,
                'crystalRate': glass.crystalRate,
                'crystalTotal': crystaltotal,
                'crystalname': crystalname,
                'crystalarea': crystalarea,
                
                'lacquered': glass.lacquered,
                'lacqueredRate': glass.lacqueredRate,
                'lacqueredTotal': lacqueredtotal,
                'lacqueredname': lacqueredname,
                'lacqueredarea': lacqueredarea,
                
                'hole': glass.hole,
                'holeRate': glass.holeRate,
                'holeTotal': holetotal,
                'holename': holename,
                'holeqty': holeqty,

                'cutout': glass.cutout,
                'cutoutRate': glass.cutoutRate,
                'cutoutTotal': cutouttotal,
                'cutoutname': cutoutname,
                'cutoutqty': cutoutqty,

                'spacerhole': glass.spacer_hole,
                'spacerholeRate': glass.spacerholeRate,
                'spacerholeTotal': spacerholetotal,
                'spacerholename': spacerholename,
                'spacerholeqty': spacerholeqty,

                'screwhole': glass.screw_hole,
                'screwholeRate': glass.screwholeRate,
                'screwholeTotal': screwholetotal,
                'screwholename': screwholename,
                'screwholeqty': screwholeqty,
                'remarks': glass.remarks
            }
            glasslist.append(glass)
        quoteFittings = LineItemFittings.objects.filter(Quoteid__id=id).all()
        totalfittingsquantity = 0
        totalfittingarea = 0
        totalfittingamount = 0
        matecost = 0
        fittingamount = 0
        for fittings in quoteFittings:
            totalfittingsquantity += float(fittings.Quantity)
            if quotes.gst == 1:
                rate = round((float(fittings.Rate)/1.18),2)
                totalfittingarea += rate
                total = round((float(fittings.Total)/1.18),2)
                totalfittingamount += total
            else:
                rate = float(fittings.Rate)
                totalfittingarea += rate
                total = float(fittings.Total)
                totalfittingamount += total
            
            
            fittings = {
                'fittingid': fittings.id,
                'fittingItem': fittings.ItemMasterid.Name,
                'Quantity': fittings.Quantity,
                'Rate': rate,
                'total': total,
                'totalqty': totalfittingsquantity,
                'totalarea': totalfittingarea,
                'totalamount': totalfittingamount,
                # 'amount': fittingamount,
            }
            fittinglist.append(fittings)
        quoteMisc = LineItemMisc.objects.filter(Quote_id__id=id).all()
        totalmiscquantity = 0
        quantity = 0
        totalmiscamount = 0
        totalrate = 0
        total = 0
        for misc in quoteMisc:
            if quotes.gst == 1:
                rate = round((float(misc.Rate)/1.18),2)
            else:
                rate = float(misc.Rate)
            if misc.ItemMasterIdMisc:
                miscName = (misc.ItemMasterIdMisc.Name).lower()
                print(miscName)
                if miscName == 'installation':
                    if glasstotal:
                        quantity = glass['glasstotal']
                        if quotes.gst == 1:
                            total = float(quantity) * float(rate)
                            total = round((total),2)
                        else: 
                            total = float(quantity) * float(rate)
                    else:
                        quantity = 0
                        total = 0
                elif miscName != 'installation':
                    if misc.Quantity:
                        quantity = float(misc.Quantity)
                        if quotes.gst == 1:
                            total = quantity * float(rate)
                            total = round((total),2)
                        else:
                            total = quantity * float(rate)
                    else:
                        quantity = 0
                        total = 0

            if quantity:
                totalmiscquantity += float(quantity)
            else:
                totalmiscquantity = 0
            if rate:
                totalrate += float(rate)
            else:
                totalarea = 0
            
            totalmiscamount += float(total)
            remarks =str(misc.remarks).replace(',', '\n')
            
            misc = {
                'miscItem': misc.ItemMasterIdMisc,
                'qty': quantity,
                'rate': rate,
                'total': total,
                'totalqty': totalmiscquantity,
                'totalarea': totalrate,
                'totalamount': totalmiscamount,
                'remarks': remarks,
            }
            misclist.append(misc)

        if quotes.ProjectId.client.lastname:
            lastname = quotes.ProjectId.client.lastname
        else:
            lastname = ""

        
        if totalarea:
            glassareatotal = glasslist[-1]['totalarea']
        if unit:
            unit = glass['unit']
        else:
            unit = ''
        if glasstotal:
            glasstotal = glass['glasstotal']
        if quotes.ProjectId.measurement_staff:
            staff = quotes.ProjectId.measurement_staff
            phone = "("+str(quotes.ProjectId.measurement_staff.phone)+")"
        else:
            staff = ''
            phone = ''
        buildingAddress = str(quotes.ProjectId.client.building)
        streetAddress = ", " + str(quotes.ProjectId.client.street)  if str(quotes.ProjectId.client.street) and str(quotes.ProjectId.client.building) else str(quotes.ProjectId.client.street) if str(quotes.ProjectId.client.street) else ""
        cityAddress = ", " + str(quotes.ProjectId.client.city) if str(quotes.ProjectId.client.city)and (str(quotes.ProjectId.client.street) or str(quotes.ProjectId.client.building)) else str(quotes.ProjectId.client.city) if str(quotes.ProjectId.client.city) else  ""
        zipAddress = " - " + str(quotes.ProjectId.client.zip) if str(quotes.ProjectId.client.zip) and (str(quotes.ProjectId.client.street) or str(quotes.ProjectId.client.building) or str(quotes.ProjectId.client.city)) else str(quotes.ProjectId.client.zip) if str(quotes.ProjectId.client.zip) else  ""
        clientAddress = buildingAddress + streetAddress + cityAddress + zipAddress
        if quotes.terms:
            terms = quotes.terms
        else:
            terms = ''
            for terms in Settings.objects.filter(key='Terms'):
                terms = terms.value
        if quotes.choose_header == 1: 
            if quotes.header:
                header = quotes.header
            else:
                header = ''
                for header in Settings.objects.filter(key='Header'):
                    header = header.value

        else:
            header = ''
        quote={
            'project': quotes.ProjectId.type_of_work,
            'interior_name': quotes.interiorname if quotes.interiorname else "",
            'staffname': staff,
            'staffnumber': phone,
            'diagramfile': quotes.ProjectId.diagram_file,
            'piNo': quotes.pino,
            'pi_date': quotes.created_at,
            'discount': quotes.discount,
            'client': str(quotes.ProjectId.client.firstname)+ " "+str(lastname),
            'clientPhoneNo': quotes.ProjectId.client.phone_number,
            'clientaddress': clientAddress,
            'glass': glasslist,
            'fittings': fittinglist,
            'misc': misclist,
            'areatotal': glassareatotal,
            'unit': unit,
            'glasstotal': glasstotal,
            'quoteid': quotes.id,
            'gst': quotes.gst,
            'igst': quotes.igst,
            'cgst': quotes.cgst,
            'diagram_file': quotes.diagramfile,
            'terms': terms,
            'header': header,
            'discount_type': quotes.discount_type,
            'preparedby': quotes.preparedBy.Name if quotes.preparedBy else ""
        }
        # quote_list.append(quote)
        # print("chck quote: ",quote)
        printPDFView = GenerateQuotePdf(request,quote)
        return printPDFView 
        