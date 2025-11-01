import enum
from django.db import models
from django.db.models import Max
from datetime import datetime
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db.models.functions import Cast
from django.db import transaction
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from optimized_image.fields import OptimizedImageField
from tinymce.models import HTMLField
from django.utils.html import format_html
from django.core.exceptions import NON_FIELD_ERRORS
import random
import re
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from datetime import date
from ckeditor.fields import RichTextField 
# Create your models here.



class Client(models.Model):
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254,  blank=True, default="", null= True)
    email = models.CharField(max_length=200, blank=True, default="")
    phone_number = models.CharField(max_length=12, unique=False)
    alternate_number = models.CharField(max_length=10, blank=True, default="")
    building = models.CharField(max_length=200, blank=True, default="")
    street = models.CharField(max_length=200, blank=True, default="")
    landmark = models.CharField(max_length=200, blank=True, default="")
    city = models.CharField(max_length=200, blank=True, default="")
    zip = models.CharField(max_length=200, blank=True, default="")
    

    class Meta:
        ordering = ('id',)
        verbose_name = 'Client'
        
    def __str__(self):
        return str(self.firstname).capitalize()+ " " +str(self.lastname).capitalize() if str(self.lastname) != 'None' else str(self.firstname).capitalize()
        


class Staff(models.Model):
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=12, unique=True)
    alternate_number = models.CharField(max_length=10, blank=True, default="")
   

    class Meta:
        ordering = ('id',)
        verbose_name = 'Staff'
        
    def __str__(self):
        return '{}' .format(self.name)
    

class Interior(models.Model):
    name = models.CharField(max_length=254,  blank=True, default="", null= True)
    number = models.CharField(max_length=10, blank=True, default="", verbose_name= 'Phone Number')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Interior'

    def __str__(self):
        return str(self.name)
    


class Statuses(object):

    CHOICES = (
        ('UPVC', 'UPVC'),
        ('ClearGlass', 'Clear Glass'),
        ('ToughenedGlass', 'Toughened Glass'),
        ('Purchase', 'Purchase'),
    )


class Projects(models.Model):
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELLED = 3
    _STATUS = [
        (IN_PROGRESS, "In progress"),
        (COMPLETED, "COMPLETED"),
        (CANCELLED, "CANCELLED"),
    ]
    type_of_work = models.CharField(max_length=100, default="",blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_id')
    interior_name = models.ForeignKey(Interior, on_delete=models.CASCADE, related_name='Interiorname', blank=True, null=True)
    reference_name = models.CharField(max_length=151, default="",blank=True, null=True, verbose_name="Reference Given By")
    project_name = models.CharField(max_length=151, default="",blank=True, null=True, verbose_name="Project Name")
    measurement_status = models.BooleanField(default=False)
    measurement_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_id', blank=True, null=True)
    diagram_status = models.BooleanField(verbose_name='Diagram(s)')
    diagram_file = models.FileField(blank=True, default="")
    diagram_file_1 = models.FileField(blank=True, default="")
    diagram_file_2 = models.FileField(blank=True, default="")
    quote_status = models.BooleanField(verbose_name='Quote(s)')
    quote_file = models.FileField(blank=True, default="", null=True, verbose_name = 'Quote File')
    finalize = models.BooleanField(verbose_name='Finalization(s)')
    onProduction = models.BooleanField(verbose_name='On Production', blank=True, null=True, default=False)
    dispatch_status = models.BooleanField(verbose_name='Delivered')
    installation_status = models.BooleanField()
    installation_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staffid', blank=True, null=True)
    # invoice_status = models.BooleanField()
    # invoice_file = models.FileField(blank=True, default="")
    totalsquareft = models.CharField(max_length=151, default="",blank=True, null=True, verbose_name="Total Square Feet")
    payment_status = models.BooleanField(default=False, verbose_name="Material Ready")
    notes = models.TextField(blank=True, default="")
    status = models.IntegerField(default=1, choices=_STATUS, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('id',)
        verbose_name = 'Project'
    
    def __str__(self):
        # Attempt to get the first quote associated with the project
        quote = Quote.objects.filter(ProjectId_id=self.id).first()
        if quote:
            # Return the pino from the quote, followed by the client name
            return f"{quote.pino}-{self.client}"
        else:
            # If no quote is found, fallback to displaying the client name
            return str(self.client)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.type_of_work:
            self.type_of_work= eval(self.type_of_work)

@receiver(post_save, sender= Projects)
def post_save_projects(sender, instance, **kwargs):
    try:
        project = Projects.objects.get(id=instance.id)
        project_finalised = project.finalize
        quotes =  Quote.objects.filter(ProjectId__id= project.id)
        
        for quote in quotes:
            quotedatecheck = datetime.strptime('03-10-2023', '%d-%m-%Y').date()
            quotedates =quote.created_at
            items = LineItemFittings.objects.filter(Quoteid__id=quote.id)
            for item  in items:
                print('repeat' , item.Quantity)
                if project_finalised:
                    if quotedatecheck < quotedates:
                        print('quote id',item.Quantity)
                        if StockFittings.objects.filter(quote_id = quote.id, fittingsStock__id = item.ItemMasterid.id).exists():
                            obj = StockFittings.objects.filter(quote_id = instance.id, fittingsStock__id = item.ItemMasterid.id)
                            print('obj', obj)
                            obj.stock_from = 'Inventory'
                            obj.stock_to = 'Quote'
                            obj.quantity = float(item.Quantity)
                            obj.isauto = 1
                            obj.fittingsStock_id = item.ItemMasterid.id
                            obj.save()
                        else:
                            StockFittings.objects.create(fittingsStock_id = item.ItemMasterid.id, stock_from = 'Inventory', stock_to = 'Quote', quantity = float(item.Quantity), isauto = 1, quote_id = quote.id, date = date.today()) 
                else:
                    stockdelete = StockFittings.objects.filter(quote_id=quote.id)
                    stockdelete.delete()
    except:
        print("An exception occurred")
post_save.connect(post_save_projects, sender=Projects)

previous = {}
@receiver(pre_save, sender= Projects)
def projectdelivered(sender, instance,update_fields=None, **kwargs):
    global previous
    if instance.id:
        previous = Projects.objects.get(id=instance.id)

@receiver(post_save, sender= Projects)
def post_save_projectdelivered(sender, instance, **kwargs):
    try:
        if previous:
            if not previous.dispatch_status == instance.dispatch_status:
                if instance.dispatch_status == True: 
                        # do something you want like
                        procurement_delivered = Procurement.objects.filter(project__id=instance.id)
                        for delivered in procurement_delivered:
                            print('procurement', delivered.delivered)
                            delivered.delivered=1
                            delivered.save()
    except:
        print("An exception occurred")

pre_save.connect(projectdelivered, sender=Projects)
post_save.connect(post_save_projectdelivered, sender=Projects)


class ProcurementStatuses(object):

    CHOICES = (
        ('Tuff', 'Tuff'),
        ('UPVC', 'UPVC'),
    )
OPTIONS = [
    ('Tuff', 'Tuff'),
    ('UPVC', 'UPVC'),
]

class Procurement(models.Model):
    date = models.DateField(auto_now=False, null=True, blank=True)
    pi_no = models.CharField(max_length=210, verbose_name='PI No', unique=True)
    amount = models.CharField(max_length=10, blank=True, default="")

    companyname = models.ForeignKey("Supplier", on_delete=models.CASCADE, blank=True,null=True, related_name='companyname', verbose_name='Supplier Name')

    # qty = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='quantity', blank=True, null=True,verbose_name='Quantity')

    uploadfile = models.FileField(blank=True, default="")
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project', blank=True, null=True)
    # company = models.CharField(max_length=100, blank=True, default="")
    material_ready = models.BooleanField(verbose_name='Glass Ready',default=False)
    received = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    materials = models.CharField(max_length=255, blank=True, choices=OPTIONS, verbose_name="Type of Work")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Procurement'
        
    def validate_unique(self,exclude=None):
        try:
            super(Procurement,self).validate_unique()
        except ValidationError as e:
            raise ValidationError(" This PI NO Already Exists.")

    def __str__(self):
        return str(self.pi_no)   
   
previous = {}
@receiver(pre_save, sender= Procurement)
def procurementdelivered(sender, instance,update_fields=None, **kwargs):
    global previous
    if instance.id:
        previous = Procurement.objects.get(id=instance.id)

@receiver(post_save, sender= Procurement)
def post_save_procurementdelivered(sender, instance, **kwargs):
    try:
        if previous:
            if not previous.delivered == instance.delivered:
                if instance.delivered == True: 
                        # do something you want like
                        projects = Projects.objects.get(id=instance.project.id)
                        print('project', projects.dispatch_status)
                        projects.dispatch_status=1
                        projects.save()
    except:
        print("An exception occurred")
pre_save.connect(procurementdelivered, sender=Procurement)
post_save.connect(post_save_procurementdelivered, sender=Procurement)

class Quantity(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True, verbose_name='Item')
    quantity = models.IntegerField(blank=True, null=True, verbose_name='Quantity')
    qty = models.ForeignKey(Procurement, on_delete=models.CASCADE, blank=True, default="", related_name='quantityItem')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Item'

    def __str__(self):
        return str(self.item)+ " "+ "x"+" " + str(self.quantity)

class Tasks(models.Model):
    
    task_status_list = (
        ('1', u'Pending'),
        ('2', u'Progress'),
        ('3', u'Completed'),
        ('4', u'Cancelled'),        
    )
    name        = models.CharField(max_length=201, blank=True, default="", verbose_name="Task Name")      
    asigned_to  = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff', blank=True, null=True, verbose_name="Assigned Staff")     
    project     = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projects', blank=True, null=True, verbose_name="Assigned Project")
    description = models.TextField(blank=True, default="", verbose_name="Task Details")    
    task_status = models.CharField(max_length=25, choices=task_status_list, null=True, blank=True)
    task_date   = models.DateTimeField(verbose_name="Task Date", blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Tasks'

    def __str__(self):
        return str(self.name)

class Supplier(models.Model):
    Name        = models.CharField(max_length=201, blank=True, default="", verbose_name="Name") 
    Address     = models.CharField(max_length=201, blank=True, default="", verbose_name="Address") 
    GST         = models.CharField(max_length=201, blank=True, default="", verbose_name="GST") 
    Email       = models.CharField(max_length=201, blank=True, default="", verbose_name="Email") 
    Phone       = models.CharField(max_length=201, blank=True, default="", verbose_name="Phone") 

    class Meta:
        ordering = ('id',)
        verbose_name = 'Supplier'

    def __str__(self):
        return str(self.Name)
    
class ItemMaster(models.Model):
    typeofitem = (
        ('Glass', 'Glass'),
        ('Fittings', 'Fittings'),
        ('Misc', 'Misc'),    
    )
    Name        = models.CharField(max_length=201, blank=True, default="", verbose_name="Name")   
    TypeOfItem  = models.CharField(max_length=201, choices=typeofitem, blank=True, default="", verbose_name="Type of item")   
    Rate        = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")   
    totalstock = models.CharField(max_length=201, blank=True, default="", verbose_name="Total Stock")   

    class Meta:
        ordering = ('id',)
        verbose_name = 'Item Master'

    def __str__(self):
        return '{}' .format(self.Name)

    def save(self, force_insert=False, force_update=False):
        self.Name = self.Name.upper()
        super(ItemMaster, self).save(force_insert, force_update)

class PreparedBy(models.Model):
    Name = models.CharField(max_length=201, blank=True, default="", verbose_name="Name")

    class Meta:
        ordering = ('id',)
        verbose_name = 'PreparedBy'

    def __str__(self):
        return str(self.Name)

DISCOUNT_CHOICES = [
    ('rupees', 'Rupees'),
    ('percentage', 'Percentage'),
]

class Quote(models.Model):
    ProjectId           = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ProjectId', blank=True, null=True, verbose_name="Project")
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_CHOICES, default='rupees', verbose_name="Discount Type")
    discount   = models.CharField(max_length=201, blank=True, default="", verbose_name="Discount Amount") 
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    pino       = models.CharField(max_length=201, blank=True, default="", verbose_name="Pi No")
    interiorname = models.ForeignKey(Interior, on_delete=models.CASCADE, related_name='Interior_name', blank=True, null=True)
    gst         = models.BooleanField(default=False, verbose_name="GST Breakup")
    igst         = models.BooleanField(default=False, verbose_name="IGST")
    cgst         = models.BooleanField(default=False, verbose_name="CGST/SGST")
    diagramfile  = models.BooleanField(default=False, verbose_name="Attach Diagram File")
    choose_terms = models.BooleanField(default=False, verbose_name="Choose Terms and Conditions")
    terms = RichTextField(default="", blank=True,  verbose_name="Terms and Conditions")
    choose_header = models.BooleanField(default=False, verbose_name="Choose Header")
    header = models.CharField(max_length=201, default="", blank=True)
    increamentPiNo = models.CharField(max_length=120, null = True, blank=True)
    preparedBy = models.ForeignKey(PreparedBy, on_delete=models.CASCADE, related_name='preparedBy', blank=True, null=True, verbose_name="Prepared By")
    class Meta:
        ordering = ('id',)
        verbose_name = 'Quote'

    def __str__(self):
        return str(self.pino)
    
@receiver(post_save, sender= Quote)
def post_save_piNo(sender, instance,created, **kwargs):
    if created and not instance.increamentPiNo:
        last_number = Quote.objects.aggregate(max_increment=Max(Cast('increamentPiNo', models.IntegerField())))
        print('last_number', last_number)
        if last_number['max_increment']:
            last_number = int(last_number['max_increment'])
            next_number = last_number + 1
            print('next', next_number)
        else:
            next_number = 1 

        formatted_next_number = "{:02d}".format(next_number)
        print('format', formatted_next_number)
        currentyear = datetime.now().strftime('%y')
        nextyear = int(currentyear) + 1

        instance.pino = str(currentyear) + "-" + str(nextyear) + "-" + "GD" + str(formatted_next_number)
        instance.increamentPiNo = formatted_next_number 
        instance.save(update_fields=['pino', 'increamentPiNo'])
       
post_save.connect(post_save_piNo, sender=Quote)

@receiver(post_save, sender= Quote)
def post_save_projectquote(sender, instance, **kwargs):
    if instance.ProjectId:
        quoteproject = Projects.objects.get(id = instance.ProjectId.id)
        if quoteproject.quote_status == 0:
            quoteproject.quote_status = 1
            quoteproject.save()
            print('status', 'true')
post_save.connect(post_save_projectquote, sender=Quote)

class LineItemGlass(models.Model):
    unitofmeasure = (
        ('mm', 'mm'),
        ('inch', 'inch'),
        ('feet', 'feet'),    
        # ('suta', 'suta'),  
    )
    # id                  = models.CharField(primary_key=True, editable=False, max_length=10)
    QuoteId             = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='QuoteId', blank=True, null=True, verbose_name="Quote")
    ItemMasterId        = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, related_name='ItemMasterId', blank=True, null=True, verbose_name="")
    UnitOfMeasurement   = models.CharField(max_length=201, choices=unitofmeasure, blank=True, default="", verbose_name="Unit")
    Length              = models.CharField(max_length=201, blank=True, default="", verbose_name="H")
    Width               = models.CharField(max_length=201, blank=True, default="", verbose_name="W")
    billedlength        = models.CharField(max_length=201, blank=True, default="", verbose_name="Billed H", db_column='actuallength')
    billedwidth         = models.CharField(max_length=201, blank=True, default="",verbose_name="Billed W", db_column='actualwidth')
    Quantity            = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    Rate                = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")
    Total               = models.CharField(max_length=201, blank=True, default="", verbose_name="Total Sqft")

    Polish              = models.BooleanField(default=False)
    PolishRate          = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")
    Polishfeet          = models.CharField(max_length=35, blank=True, default="", verbose_name="Feet")

    Beveling1           = models.BooleanField(default=False, verbose_name="0.25 inch Bevel", db_column='Beveling')
    Beveling1Rate        = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate", db_column='BevelingRate')

    Beveling2           = models.BooleanField(default=False, verbose_name="0.5 inch Bevel")
    Beveling2Rate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    Beveling3           = models.BooleanField(default=False, verbose_name="0.75 inch Bevel")
    Beveling3Rate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    Beveling4           = models.BooleanField(default=False, verbose_name="1 inch Bevel")
    Beveling4Rate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    Beveling5           = models.BooleanField(default=False, verbose_name="1.25 inch Bevel")
    Beveling5Rate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    Beveling6           = models.BooleanField(default=False, verbose_name="1.5 inch Bevel")
    Beveling6Rate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    frosting            = models.BooleanField(default=False, verbose_name="Frosting")
    frostingRate        = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    digital_printing    = models.BooleanField(default=False, verbose_name="Digital printing")
    printingRate        = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    etching             = models.BooleanField(default=False, verbose_name="Etching")
    etchingRate         = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    double_stroke       = models.BooleanField(default=False, verbose_name="Double Stroke")
    strokeRate          = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    crystal             = models.BooleanField(default=False, verbose_name="Crystal")
    crystalRate         = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    lacquered     = models.BooleanField(default=False, verbose_name="Lacquered",db_column='lacquered_white')
    lacqueredRate  = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate", db_column='lacqueredwhiteRate')

    lacquered_black     = models.BooleanField(default=False, verbose_name="Lacquered black")
    lacqueredblackRate  = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    hole                = models.BooleanField(default=False, verbose_name="Hole")
    holeQty             = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    holeRate            = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    cutout              = models.BooleanField(default=False, verbose_name="Cutout")
    cutoutQty             = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    cutoutRate          = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    spacer_hole         = models.BooleanField(default=False, verbose_name="Spacer Hole")
    spacerholeQty             = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    spacerholeRate      = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    screw_hole          = models.BooleanField(default=False, verbose_name="Screw Hole")
    screwholeQty             = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    screwholeRate       = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")

    remarks             = models.CharField(max_length=4000, blank=True, default="", verbose_name="Remarks")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Line Item'
        
    # def save(self, **kwargs):
    #     if not self.id:
    #         max = LineItemGlass.objects.raw('SELECT * FROM `DecorStoreApp_lineitemglass` order by length(id), id ASC')
    #         max  = list(max)
    #         print("self", max[-1])
    #         max = max[-1].id
    #         print('value dekha', (max))
    #         if max is not None:
                
    #             pattern = r'\d+'
    #             insert_id = re.findall(pattern, max)
    #             insert_id = insert_id[0]
    #             insert_id = int(insert_id) + 1
    #             self.id = "{}{}".format('G', str(insert_id))
    #         else:
    #             max = 1
    #             self.id = "{}{}".format('G', str(max))
           
    #     super().save(*kwargs)
    def __str__(self):
        return str(self.id)
    
class LineItemFittings(models.Model):
    # id                  = models.CharField(primary_key=True, editable=False, max_length=10)
    Quoteid             = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='Quoteid', blank=True, null=True, verbose_name="Quote")
    ItemMasterid        = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, related_name='ItemMasterid', blank=True, null=True, verbose_name="")
    # reference              = models.CharField(max_length=201, blank=True, default="", verbose_name="Reference")
    Quantity            = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    Rate                = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")
    Total               = models.CharField(max_length=201, blank=True, default="", verbose_name="Total Sqft")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Line Item'
        
    def __str__(self):
        return str(self.ItemMasterid)
    
@receiver(post_save, sender= LineItemFittings)
def post_save_function(sender, instance, **kwargs):
        
        # qty = LineItemFittings.objects.filter(Quoteid__id=instance.id).aggregate(Sum('Quantity'))['Quantity__sum']  
        print('qty', instance.Quantity)
        quote = Quote.objects.get(id = instance.Quoteid.id)
        project = Projects.objects.get(id=quote.ProjectId.id)
        project_finalised = project.finalize
        quotedatecheck = datetime.strptime('03-10-2023', '%d-%m-%Y').date()
        quotedates =quote.created_at
        # items = LineItemFittings.objects.filter(Quoteid__id=quote.id)
        # for item  in items:
        #     print('repeat' , instance.Quantity)
        if project_finalised:
            if quotedatecheck < quotedates:
                print('quote id',instance.Quantity)

                if StockFittings.objects.filter(quote_id = quote.id, fittingsStock__id = instance.ItemMasterid.id).exists():
                    obj = StockFittings.objects.get(quote_id = quote.id, fittingsStock__id = instance.ItemMasterid.id)
                    print('quote', obj)
                    obj.stock_from = 'Inventory'
                    obj.stock_to = 'Quote'
                    obj.quantity = float(instance.Quantity)
                    obj.isauto = 1
                    obj.fittingsStock_id = instance.ItemMasterid.id
                    obj.save()
                else:
                    StockFittings.objects.create(fittingsStock_id = instance.ItemMasterid.id, stock_from = 'Inventory', stock_to = 'Quote', quantity = float(instance.Quantity), isauto = 1, quote_id = quote.id, date = date.today()) 
            elif quotedatecheck > quotedates:
                print('date')
post_save.connect(post_save_function, sender=LineItemFittings)

class LineItemMisc(models.Model):
    ItemMasterIdMisc    = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, related_name='ItemMasterIdMisc', blank=True, null=True, verbose_name="")
    Quote_id            = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='Quote_id', blank=True, null=True, verbose_name="Quote")
    Quantity            = models.CharField(max_length=201, blank=True, default="", verbose_name="Qty")
    Rate                = models.CharField(max_length=201, blank=True, default="", verbose_name="Rate")
    Total               = models.CharField(max_length=201, blank=True, default="", verbose_name="Total Sqft")
    remarks             = models.CharField(max_length=3000, blank=True, default="", verbose_name="Remarks")
    class Meta:
        ordering = ('id',)
        verbose_name = 'Line Item'
        
    def __str__(self):
        return str(self.ItemMasterIdMisc)
    
class StockFittings(models.Model):
    stockTo = (
        ('Inventory', 'Inventory'),
        ('Quote', 'Quote'),  
        ('Misc', 'Misc'),  
    )
    stockFrom = (
        ('Opening Stock', 'Opening Stock'),
        ('Inventory', 'Inventory'),
        ('Quote', 'Quote'),  
    )
    fittingsStock  = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, related_name='fittingsStock', blank=True, null=True, verbose_name="Fitting Stock")
    stock_from     = models.CharField(max_length=201, choices=stockFrom, blank=True, default="", verbose_name="Stock From")
    stock_to     = models.CharField(max_length=201, choices=stockTo, blank=True, default="", verbose_name="Stock To")
    quantity     = models.CharField(max_length=201, blank=True, default="", verbose_name="Quantity")
    isauto         = models.BooleanField(default=False, verbose_name="Is Auto")
    quote             = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='quote', blank=True, null=True, verbose_name="Quote")
    date  = models.CharField(max_length=201, blank=True, default="", verbose_name="Date")
    remarks = models.CharField(max_length=201, blank=True, default="", verbose_name="Remarks")
    class Meta:
        ordering = ('id',)
        verbose_name = 'Stock Fittings'
        
    def __str__(self):
        return str(self.fittingsStock)
    
@receiver(post_save, sender= StockFittings)
def post_save_stockcalculate(sender, instance, **kwargs):
    # stockcheck =  StockFittings.objects.filter(fittingsStock = instance.ItemMasterid.id)
    # print('stockcheck', stockcheck)
    totalOpeningStock = 0
    totalInventory = 0
    # for stocklist in stockcheck:
    fittings = StockFittings.objects.filter(fittingsStock__id = instance.fittingsStock.id)
    print('fitting', fittings)
    for fitting in fittings:
        if fitting.stock_from == "Opening Stock":
            totalOpeningStock += float(fitting.quantity)
            print('totalopening', totalOpeningStock)
        if fitting.stock_from == "Inventory" or fitting.stock_from == "Quote":
            totalInventory += float(fitting.quantity)
            print('total inventory', totalInventory)
        availablestock = totalOpeningStock - totalInventory
        print('total stock', availablestock)
        items = ItemMaster.objects.get(id =  instance.fittingsStock.id)
        items.totalstock = availablestock
        items.save()
post_save.connect(post_save_stockcalculate, sender=StockFittings)
    
class StockReport(models.Model):
    pass

class Settings(models.Model):
    key = models.CharField(max_length=56,blank=True, default='')
    value = RichTextField(blank=True, default='')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Settings'

    def __str__(self):
        return str(self.id)
    

class GoodsReceived(models.Model):
    date = models.CharField(max_length=201, blank=True, default="", verbose_name="Date")
    invoiceno = models.CharField(max_length=201, blank=True, default="", verbose_name="Invoice Number")
    invoicefile = models.FileField(blank=True, default="")
    companyname = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True,null=True, related_name='company', verbose_name='Company Name')
    transportername = models.CharField(max_length=201, blank=True, default="", verbose_name="Transporter Name")
    transporter = models.ForeignKey('Transporter', on_delete=models.CASCADE, blank=True, null=True, related_name='goods_received', verbose_name='Transporter Name')
    transporterfile = models.FileField(blank=True, default="")
    builtyNo = models.CharField(max_length=201, blank=True, default="", verbose_name="Builty No")
    no_of_bundle = models.IntegerField(blank=True, default="", verbose_name="No of Bundle")
    contactnumber = models.CharField(max_length=12,blank=True, default="", verbose_name="Contact Number")
    received = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False, blank=True)
    projectname = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projectname', blank=True, null=True, verbose_name="Project")
    remarks = models.CharField(max_length=201, blank=True, default="", verbose_name="Remarks")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Goods Received'

    def __str__(self):
        return str(self.id)
    def save_model(self, request, obj, form, change):
        if obj.transporter and not obj.contactnumber:
            obj.contactnumber = obj.transporter.Phone
        super().save_model(request, obj, form, change)
    
class RepairingWorkStatuses(object):

    CHOICES = (
        ('Tuff', 'Tuff'),
        ('UPVC', 'UPVC'),
    )
RepairingWorkOPTIONS = [
    ('Tuff', 'Tuff'),
    ('UPVC', 'UPVC'),
]

class RepairingWork(models.Model):
    date = models.CharField(max_length=201, blank=True, default="", verbose_name="Date")
    projectname = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projectsreparing', blank=True, null=True, verbose_name="Project Name")
    
    typeofwork = models.CharField(max_length=255, blank=True, choices=RepairingWorkOPTIONS, verbose_name="Type of Work")
    # clientname = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clientname', blank=True, null=True, verbose_name="Client")
    technicianName = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='technicianName', blank=True, null=True, verbose_name="Technician Name")
    clientName = models.CharField(max_length=201, blank=True, default="", verbose_name="Client Name")
    clientNumber = models.CharField(max_length=12, blank=True, default="", verbose_name="Client Contact Number")
    workdetail = models.CharField(max_length=201, blank=True, default="", verbose_name="Details of Work")
    paymentTerms = models.CharField(max_length=356, blank=True, default="", verbose_name="Payment Terms")
    workcompleted = models.BooleanField(default=False, verbose_name= 'Work Completed')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Repairing Work'

    def __str__(self):
        return str(self.id)
    
class RepairingWorkFile(models.Model):
    repairing_work = models.ForeignKey(
        RepairingWork, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Repairing Work File'

    def __str__(self):
        return f"File for {self.repairing_work.clientName}"
    

class InstallationPayment(models.Model):
    pino = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='InstallationPiNo', blank=True, null=True, verbose_name="PI NO")
    typeofwork = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='typeofwork', blank=True, null=True, verbose_name="Type of Work")
    amount = models.CharField(max_length= 201, blank=True, default="", null=True, verbose_name= "Amount")
    foodinglodging = models.CharField(max_length= 201, blank=True, default="", null=True, verbose_name= "Fooding & Lodging")
    updownfare = models.CharField(max_length= 201, blank=True, default="", null=True, verbose_name= "Up Down Fare")
    unloading = models.CharField(max_length=201, blank=True, default="", null=True, verbose_name= "Unloading")
    totalamount = models.CharField(max_length=251, blank=True, null=True, default="", verbose_name="Total Amount")
    technicianname = models.CharField(max_length=201, blank=True, null=True, default="", verbose_name="Technician Name")
    entry = models.CharField(max_length=251, blank=True, null=True, default="", verbose_name="Entry")

    class Meta:
        ordering = ('id',)
        verbose_name = 'Installation Payment'

    def __str__(self):
        return str(self.id)
    
class ProjectReport(models.Model):
    pass

class Transporter(models.Model):
    Name        = models.CharField(max_length=201, blank=True, default="", verbose_name="Name") 
    Address     = models.CharField(max_length=201, blank=True, default="", verbose_name="Address") 
    GST         = models.CharField(max_length=201, blank=True, default="", verbose_name="GST") 
    Email       = models.CharField(max_length=201, blank=True, default="", verbose_name="Email") 
    Phone       = models.CharField(max_length=201, blank=True, default="", verbose_name="Phone") 

    class Meta:
        ordering = ('id',)
        verbose_name = 'Transporter'

    def __str__(self):
        return str(self.Name)
 