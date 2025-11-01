from DecorStoreApp.models import *
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count

class StockReportView(View):
    def get(self, request):
        stocks = ''
        if request.GET:
            item = request.GET['item']
            from_date = request.GET['fromdate']
            to_date =  request.GET['todate']
            if item and not from_date and not to_date:
                stocks  =  StockFittings.objects.filter(fittingsStock_id = item)
            elif from_date and to_date and not item:
                stocks  =  StockFittings.objects.filter(date__range=(from_date, to_date))
            elif item and from_date and to_date:
                stocks  =  StockFittings.objects.filter(fittingsStock_id = item).filter(date__range=(from_date, to_date))
            
            
        # print("QUERY SET RETURNED ", stocks)
        totalStockList = []
        totalOpeningStock = 0
        totalInventory = 0
        fittingStock_id = []
        for stock in stocks:
            if stock.fittingsStock.id:
                # print("FIT", type(stock.fittingsStock.id))
                # stocklist = {
                # 'id': stock.fittingsStock.id,
                # 'name': stock.fittingsStock.Name
                # }
                fittingStock_id.append({'id' : stock.fittingsStock.id,'value' : stock.fittingsStock.Name})

            # stockitemlist = ItemMaster.objects.filter(id = stock.fittingsStock.id)
            # for itemlist in stockitemlist:
            #     id =  itemlist.id,
            #     name = itemlist.Name
            if stock.stock_from == "Opening Stock":
                totalOpeningStock += float(stock.quantity)
            if stock.stock_from == "Inventory" or stock.stock_from == "Quote":
                totalInventory += float(stock.quantity)
            if stock.stock_to == 'Quote':
                stockto = str(stock.stock_to) + str(stock.quote.id)
            else: 
                stockto = str(stock.stock_to)
            try:
                stockList = {
                    'fittingsStockid': stock.fittingsStock.id,
                    'fittingsStock': stock.fittingsStock.Name,
                    'stock_from': stock.stock_from,
                    'stock_to': stockto,
                    'quantity': stock.quantity,
                    'isauto': stock.isauto,
                    'remarks': stock.remarks,
                    'date': stock.date,
                }
                totalStockList.append(stockList)
                # print('totalStockList', totalStockList)
            except:
                print('None')
        closingStock = totalOpeningStock - totalInventory
        totalStockList.append({'closing_stock' : closingStock})
        # print('totalstock', closingStock)
        itemlist = StockFittings.objects.values_list('fittingsStock', flat=True).annotate(Count('fittingsStock')).order_by()
        listfttng = []
        for items in itemlist:
            fittinglist = ItemMaster.objects.filter(id = items)
            for fitting in fittinglist:
                fitting = {
                    'id': fitting.id,
                    'name': fitting.Name
                }
            listfttng.append(fitting)
        print('IDSS ', totalStockList)
        return render(self.request, 'custom-templates/stock_report.html', {'totalStockList': totalStockList, 'listfttng': listfttng})