from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from DecorStoreApp.utils import render_to_pdf
import datetime
from num2words import num2words
from django.utils.safestring import mark_safe
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
# import xhtml2pdf as pisa
from DecorStoreApp.models import *
import json
import xlwt
import math

def ProjectReportFunc(request):
    print('hlw')
    queryString =  next(iter(request.POST))
    body = json.loads(queryString)
    glass = body['glass']
    from_date = body['fromdate']
    to_date =  body['todate']
    projects = Quote.objects.raw("""SELECT
            projects.client_id,
            projects.project_name,
            projects.type_of_work,
            MAX(quote.created_at) AS quote_created_at,
            projects.id as id,
            quote.id,
            SUM(
                (
                CASE
                    WHEN line_item_glass.Polish = 1 THEN 
                        ( ROUND((((
                            (CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2)) * line_item_glass.PolishRate
                    ELSE line_item_glass.Polishfeet
                END
            ) + (
                    CASE
                        WHEN line_item_glass.Beveling = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.BevelingRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Beveling2 = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling2Rate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Beveling3 = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling3Rate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Beveling4 = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling4Rate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Beveling5 = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling5Rate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Beveling6 = 1 THEN ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling6Rate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.frosting = 1 THEN line_item_glass.Total * line_item_glass.frostingRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.digital_printing = 1 THEN line_item_glass.Total * line_item_glass.printingRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.etching = 1 THEN line_item_glass.Total * line_item_glass.etchingRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.double_stroke = 1 THEN line_item_glass.Total * line_item_glass.strokeRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.crystal = 1 THEN line_item_glass.Total * line_item_glass.crystalRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.lacquered_black = 1 THEN line_item_glass.Total * line_item_glass.lacqueredblackRate
                        ELSE 0
                    END
                )+ (
                    CASE
                        WHEN line_item_glass.lacquered_white = 1 THEN line_item_glass.Total * line_item_glass.lacqueredwhiteRate
                        ELSE 0
                    END
                )
                + (
                    CASE
                        WHEN line_item_glass.hole = 1 THEN line_item_glass.holeQty * line_item_glass.holeRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.cutout = 1 THEN line_item_glass.cutoutQty * line_item_glass.cutoutRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.spacer_hole = 1 THEN line_item_glass.spacerholeQty * line_item_glass.spacerholeRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.screw_hole = 1 THEN line_item_glass.screwholeQty * line_item_glass.screwholeRate
                        ELSE 0
                    END
                ) + (
                    CASE
                        WHEN line_item_glass.Polish = 1 THEN IFNULL(line_item_glass.Polishfeet, ROUND(((((CASE
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
                    WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
                END) + ( CASE
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
                    WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2)
                    WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
                END)) * line_item_glass.Quantity) * 2), 2)) * line_item_glass.PolishRate
                        ELSE 0
                    END
                ) + (case WHEN quote.gst = 1 THEN round(((line_item_glass.Total) * round(((line_item_glass.Rate) / 1.18),2)),2) else line_item_glass.Total * line_item_glass.Rate END)
            ) AS grandtotal
        FROM
            DecorStoreApp_quote AS quote 
        JOIN
            DecorStoreApp_projects AS projects ON quote.ProjectId_id = projects.id
        JOIN
            DecorStoreApp_lineitemglass AS line_item_glass ON quote.id = line_item_glass.QuoteId_id 
        WHERE
            projects.type_of_work LIKE '%%{0}%%' 
            AND quote.created_at >= '{1}' 
            AND quote.created_at <= '{2}'
        GROUP BY
            projects.id;""".format(glass, from_date, to_date))
    
    sellingledger = []
    for project in projects:
        
        client = Client.objects.get(id = project.client_id)

        ledger = {
            'Date': str(project.quote_created_at),
            'Glass': str(project.type_of_work).replace("['", "").replace("']", ""),
            'quoteno': project.quote,
            'ProjectName': project.project_name if project.project_name else '' + "-" + client.firstname,
            'Amount': round(project.grandtotal,2) 
        }
        sellingledger.append(ledger)

    selling_ledger_list=["Date","Glass", "ProjectName", "Amount"]
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ProjectReport.xls"'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet("New Sheet")

    first_row=0
    for header in selling_ledger_list:
        col=selling_ledger_list.index(header)
        ws.write(first_row,col,header)
    row=1
    incrementor = 1
    for StockList in sellingledger:
        for _key,_value in StockList.items():
            col=selling_ledger_list.index(_key)
            if(_key == "SlNo") :
                ws.write(row,col,incrementor)
                incrementor +=1
            else:
                ws.write(row,col,_value)
            
        row+=1
    wb.save(response)
    return response

class ProjectReportFuncShow(View):
    def get(self, request):
        projects = []
        sellingledger = []
        totalamount = 0.0
        if request.GET:
            glass = request.GET['glass']
            from_date = request.GET['fromdate']
            to_date =  request.GET['todate']
            
            projects = Quote.objects.raw("""SELECT projects.client_id, projects.project_name, quote.id as quote_id,
                projects.type_of_work, MAX(quote.created_at) AS quote_created_at, projects.id as id, SUM(
             (CASE WHEN line_item_glass.Polish = 1 THEN ( ROUND(((( (CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth END)) * line_item_glass.Quantity) * 2), 2)) * line_item_glass.PolishRate ELSE line_item_glass.Polishfeet END) + (CASE WHEN line_item_glass.Beveling = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.BevelingRate ELSE 0 END) + (CASE WHEN line_item_glass.Beveling2 = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
              WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
             END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling2Rate ELSE 0 END) + (
            CASE WHEN line_item_glass.Beveling3 = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE
             WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5
             WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
             END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling3Rate ELSE 0 END) + (
            CASE WHEN line_item_glass.Beveling4 = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling4Rate ELSE 0 END) + (CASE WHEN line_item_glass.Beveling5 = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
             END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
             END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling5Rate ELSE 0 END) + (
            CASE WHEN line_item_glass.Beveling6 = 1 THEN ROUND(((((CASE WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2)
             WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2)
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth END)) * line_item_glass.Quantity) * 2), 2) * line_item_glass.Beveling6Rate ELSE 0 END) + (CASE WHEN line_item_glass.frosting = 1 THEN line_item_glass.Total * line_item_glass.frostingRate ELSE 0 END) + (CASE WHEN line_item_glass.digital_printing = 1 THEN line_item_glass.Total * line_item_glass.printingRate ELSE 0 END) + (
             CASE WHEN line_item_glass.etching = 1 THEN line_item_glass.Total * line_item_glass.etchingRate
             ELSE 0 END) + (CASE WHEN line_item_glass.double_stroke = 1 THEN line_item_glass.Total * line_item_glass.strokeRate ELSE 0 END) + ( CASE WHEN line_item_glass.crystal = 1 THEN line_item_glass.Total * line_item_glass.crystalRate ELSE 0 END) + (CASE WHEN line_item_glass.lacquered_black = 1 THEN line_item_glass.Total * line_item_glass.lacqueredblackRate ELSE 0 END)+ (CASE WHEN line_item_glass.lacquered_white = 1 THEN line_item_glass.Total * line_item_glass.lacqueredwhiteRate ELSE 0
             END)+ (CASE WHEN line_item_glass.hole = 1 THEN line_item_glass.holeQty * line_item_glass.holeRate
             ELSE 0 END) + (CASE WHEN line_item_glass.cutout = 1 THEN line_item_glass.cutoutQty * line_item_glass.cutoutRate ELSE 0 END) + ( CASE WHEN line_item_glass.spacer_hole = 1 THEN line_item_glass.spacerholeQty * line_item_glass.spacerholeRate ELSE 0 END) + (CASE WHEN line_item_glass.screw_hole = 1 THEN line_item_glass.screwholeQty * line_item_glass.screwholeRate ELSE 0 END) + (CASE
             WHEN line_item_glass.Polish = 1 THEN IFNULL(line_item_glass.Polishfeet, ROUND(((((CASE
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Length / 12) / 0.5) * 0.5 WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Length / 304.8) / 0.5) * 0.5
             WHEN line_item_glass.Length != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Length WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actuallength / 12), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actuallength / 304.8), 2) WHEN line_item_glass.Length = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actuallength
             END) + ( CASE WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN CEIL((line_item_glass.Width / 12) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN CEIL((line_item_glass.Width / 304.8) / 0.5) * 0.5 WHEN line_item_glass.Width != '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.Width
             WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'inch' THEN ROUND((line_item_glass.actualwidth / 12), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'mm' THEN ROUND((line_item_glass.actualwidth / 304.8), 2) WHEN line_item_glass.Width = '' AND line_item_glass.UnitOfMeasurement = 'feet' THEN line_item_glass.actualwidth
             END)) * line_item_glass.Quantity) * 2), 2)) * line_item_glass.PolishRate ELSE 0 END) + (case WHEN quote.gst = 1 THEN round(((line_item_glass.Total) * round(((line_item_glass.Rate) / 1.18),2)),2) else line_item_glass.Total * line_item_glass.Rate END)) AS grandtotal FROM DecorStoreApp_quote AS quote 
             JOIN DecorStoreApp_projects AS projects ON quote.ProjectId_id = projects.id JOIN
             DecorStoreApp_lineitemglass AS line_item_glass ON quote.id = line_item_glass.QuoteId_id 
             WHERE projects.type_of_work LIKE '%%{0}%%' AND quote.created_at >= '{1}' AND quote.created_at <= '{2}' and projects.finalize = 1
             GROUP BY projects.id;""".format(glass, from_date, to_date))
            
            for project in projects:
                client = Client.objects.get(id = project.client_id)
                totalamount += float(project.grandtotal)
                ledger = {
                    'Date': str(project.quote_created_at),
                    'Glass': str(project.type_of_work).replace("['", "").replace("']", ""),
                    'quoteno': project.quote_id,
                    'ProjectName': project.project_name if project.project_name else '' + "-" + client.firstname,
                    'Amount': round(project.grandtotal,2) ,
                    'totalamount': round(totalamount,2)
                }
                sellingledger.append(ledger)
            print('amnt', sellingledger)
        return render(self.request, 'custom-templates/projectReport.html', {'projectreport': sellingledger})
    