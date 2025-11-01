from django.contrib import admin
from django.http import HttpResponse
from .models import * 
from .forms import *
from django.utils.safestring import mark_safe
import re 
from django.template.loader import get_template
from django.urls import reverse
from django.utils.text import (
    smart_split, unescape_string_literal
)
import math
from django.shortcuts import render, redirect
from django.db.models import Q
import django_filters
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
# Register your models here.

def render_status_and_file(status, file):
    status
    if(file != None and file != "" ):
        pino= str(file)
        pi_no = re.findall(r'^PI-\d{2,3}-\d{2}-\d{4}',pino)
        if pi_no:
            pi_no = str(pi_no).replace("['","").replace("']","")
            file = mark_safe('<div><a href="/media/{0}" target="_blank"/>File</a><br>{1}</div>'.format(file,pi_no))
        else:
            file = mark_safe('<div><a href="/media/{0}" target="_blank"/>File</a></div>'.format(file))
    else:
        file = mark_safe('<span></span>')
    if status is True:
        html = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> '
)
    else:
        html = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>'
)

    return html + file

class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    fieldsets = (
        ("Personal Details",{
            "fields": (
                ('firstname', 'lastname'),
            ),
        }),
        ("Contact Details",{
            "fields": (
                ('email', 'phone_number','alternate_number'),
            ),
        }),
        ("Address",{
            "fields":(
                'building','street', 'landmark', 'city', 'zip',
            ),
        }),
    )

    list_display = ('__str__', 'id', 'email', 'phone_number', 'building',
                    'street', 'landmark', 'city', 'zip')
    search_fields = ('firstname', 'id')
admin.site.register(Client, ClientAdmin)

class TasksAdmin(admin.ModelAdmin):
    form = taskForm
    def assigned_project(self, obj):
        project_link= '<a href="/DecorStoreApp/projects/'+str(obj.project_id)+'/change">'+str(obj.project)+'</a>'
        html = format_html(project_link, str(obj.project))
        return html

    fields          = ('name', 'asigned_to', 'project', 'task_status', 'task_date', 'description')
    list_display    = ('name', 'asigned_to', 'assigned_project', 'task_status', 'task_date')

    class Media:
        css = {
            'all': ('admin/css/admin_custom_style.css',)
        }
admin.site.register(Tasks, TasksAdmin)

class StaffAdmin(admin.ModelAdmin):

    list_display = ('name',  'id', 'phone', 'alternate_number')
    search_fields = ('name', 'id')
admin.site.register(Staff, StaffAdmin)

class TaskViewTabularInline(admin.TabularInline):
    model = Tasks
    extra = 0
    verbose_name_plural = "Assigned tasks"
    
class StatusListFilter(admin.SimpleListFilter):
    title = 'Type of Works'
    parameter_name = 'type_of_work'

    def lookups(self, request, model_admin):
        print('status', Statuses.CHOICES)
        return Statuses.CHOICES

    def queryset(self, request, queryset):
        lookup_value = self.value()
        if lookup_value:
            print('clicked key: ', lookup_value)
            # filter if a choice selected
            queryset = queryset.filter(type_of_work__contains=lookup_value)
            print('all: ', queryset)
        return queryset

class DiagramFilter(admin.SimpleListFilter):
    title = 'Diagram'
    parameter_name = 'diagram_status__exact'

    filed_name = 'diagram_status'
    

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
            
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(diagram_status = True)
        if self.value() == '0':
            return queryset.filter(diagram_status = False)
        return queryset.all()

class QuoteFilter(admin.SimpleListFilter):
    title = 'Quote'
    parameter_name = 'quote_status__exact'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(quote_status = True)
        if self.value() == '0':
            return queryset.filter(quote_status = False)

class FinalizeFilter(admin.SimpleListFilter):
    title = 'Finalization'
    parameter_name = 'finalization'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        
        if self.value() == '1':
            return queryset.filter(finalize = True)
        if self.value() == '0':
            return queryset.filter(finalize = False)

class DispatchFilter(admin.SimpleListFilter):
    title = 'Dispatch'
    parameter_name = 'dispatch'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        
        if self.value() == '1':
            return queryset.filter(dispatch_status = True)
        if self.value() == '0':
            return queryset.filter(dispatch_status = False)

class MeasurementFilter(admin.SimpleListFilter):
    title = 'Measurement'
    parameter_name = 'measurement_status'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(measurement_status = True)
        if self.value() == '0':
            return queryset.filter(measurement_status = False)

class InstallationFilter(admin.SimpleListFilter):
    title = 'Installation'
    parameter_name = 'installation_status'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(installation_status = True)
        if self.value() == '0':
            return queryset.filter(installation_status = False)

class WorkFilter(admin.SimpleListFilter):
    title = 'Work Completion'
    parameter_name = 'work_completion_status'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(work_completion_status = True)
        if self.value() == '0':
            return queryset.filter(work_completion_status = False)

# class InvoiceFilter(admin.SimpleListFilter):
#     title = 'Invoice'
#     parameter_name = 'invoice_status'

#     def lookups(self, request, model_admin):
#         return (
#             ('1', 'Done'),
#             ('0', 'Pending'),
#         )
    
#     def choices(self, changelist):
#         from django.utils.encoding import force_text
#         for lookup, title in self.lookup_choices:
#             yield {
#                 'selected': self.value() == lookup,
#                 'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
#                 'display': title,
#             }

#     def queryset(self, request, queryset):
#         print()
#         if self.value() == '1':
#             return queryset.filter(invoice_status = True)
#         if self.value() == '0':
#             return queryset.filter(invoice_status = False)

class PaymentFilter(admin.SimpleListFilter):
    title = 'Material Ready'
    parameter_name = 'material_ready'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(payment_status = True)
        if self.value() == '0':
            return queryset.filter(payment_status = False)
        
class onProductionFilter(admin.SimpleListFilter):
    title = 'On Production'
    parameter_name = 'onProduction'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        print()
        if self.value() == '1':
            return queryset.filter(onProduction = True)
        if self.value() == '0':
            return queryset.filter(onProduction = False)
        
class LocationFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', label="Search")

    class Meta:
        model = Projects
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(measurement_status__exact=value) |
            Q(diagram_status__exact=value)
        )

class MaterialReadyFilter(admin.SimpleListFilter):
    title = 'Glass Ready'  # Name in the filter section
    parameter_name = 'glass_ready'  # Query parameter in URL

    def lookups(self, request, model_admin):
        return [
            ('yes', 'Done'),
            ('no', 'Pending'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(project__material_ready=True).distinct()
        if self.value() == 'no':
            return queryset.exclude(project__material_ready=True).distinct()
        return queryset


class ProjectsAdmin(admin.ModelAdmin):
    # form = select2_modelform(Projects)
    form    = TypeOfWorkForm
    inlines = [TaskViewTabularInline]
    
    fieldsets = (
        ("Client Details",{
            "fields": (
                'client', 'interior_name', 'reference_name', 'project_name'
            )
        }),
        ("Measurement",{
            "fields": (
                'measurement_status', 'measurement_staff', 
            ),
        }),
        ("Project Details",{
            "fields": (
                'type_of_work',
            ),
        }),
        ("Diagram",{
            "fields": (
                'diagram_status', 'diagram_file', 'diagram_file_1', 'diagram_file_2'
            ),
        }),
        ("Quotes",{
            "fields": (
                'quote_status', 'quote_file'
            ),
        }),
        ("Finalization ",{
            "fields": (
                'finalize', 
            ),
        }),
        ("Production ",{
            "fields": (
                'onProduction', 
            ),
        }),
        ("Material",{
            "fields": (
                'payment_status',
            ),
        }),
        ("Dispatch ",{
            "fields": (
                'dispatch_status',
            ),
        }),
        ("Installation ",{
            "fields": (
               'installation_status', 'installation_staff',
            ),
        }),
        ("Square Feet",{
            "fields": (
                'totalsquareft',
            ),
        }),
        
        ("Notes",{
            "fields": (
                'notes',
            ),
        }),
        ("Work Completion",{
            "fields": (
                'status', 
            ),
        }),
        
    )

    def measurement_field(self, obj):
        obj.measurement_status
        if obj.measurement_staff == None:
            measurements_staff = ''

        else:
            measurements_staff = obj.measurement_staff
        if obj.measurement_status is True:
            html = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ' + str(measurements_staff)
        )
        else:
            html = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>' + str(measurements_staff)
        )

        return html
    measurement_field.short_description = 'Measurement'

    def diagram_field(self, obj):
        file =  render_status_and_file(obj.diagram_status, obj.diagram_file)
        files = ''
        files = format_html(files) + file
        if obj.diagram_file_1:
            file1 = mark_safe('<div><a href="/media/{0}" target="_blank"/>File</a></div>'.format(obj.diagram_file_1))
            files = format_html(files)+ file1
        if obj.diagram_file_2:
            file2 = mark_safe('<div><a href="/media/{0}" target="_blank"/>File</a></div>'.format(obj.diagram_file_2))
            files = format_html(files) + file2
        return files
    diagram_field.short_description = 'Diagram'
    
    def quote_field(self, obj):
        # Display Yes/No icon based on quote_status
        if obj.quote_status is True:
            quotefield = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ')
        else:
            quotefield = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>')

        files = '' 
        files = format_html(files) + quotefield

        # Retrieve and display associated quotes
        quotes = Quote.objects.filter(ProjectId__id=obj.id)
        for quote in quotes:
            if quote:
                quotefile = format_html(
                    '<div><a href="/print/quotepdf/{0}" target="_blank">{1} (Pdf)</a><br></div>',
                    quote.id,
                    quote.pino
                )
                quotelink = format_html(
                    '<div><a href="/DecorStoreApp/quote/{0}/change">{1} (Edit)</a></div>',
                    quote.id,
                    quote.pino
                )
                files = format_html(files) + quotefile + quotelink

        # Check for associated project files and include them
        if obj.quote_file:  # Replace `projectfile` with the actual field name for the uploaded file
            quote_file_link = format_html(
                '<div><a href="/media/{0}" target="_blank"/>{1}</a></div>',
                obj.quote_file,
                obj.quote_file
            )
            files = format_html(files) + quote_file_link

        return files

    quote_field.short_description = 'Quote Field'

    def installation_field(self, obj):
        obj.installation_status
        if obj.installation_staff == None:
            installation_staff = ''
        else:
            installation_staff = obj.installation_staff
        if obj.installation_status is True:
            html = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ' + str(installation_staff)
        )
        else:
            html = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>' + str(installation_staff)
        )

        return html
    installation_field.short_description = 'Installation'

    def onProduction_field(self, obj):
        obj.onProduction
        if obj.onProduction is True:
            html = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ' 
        )
        else:
            html = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>' 
        )

        return html
    onProduction_field.short_description = 'On Production'
    
    def client_Details(self, obj):
        return obj.client.phone_number
    client_Details.short_description = 'Client Details'

    def project(self, obj):
        return str(obj.client)+" - "+', '.join(['UPVC' if choice == 'UPVC' else choice for choice in obj.type_of_work]) if str(obj.type_of_work) else ""+"-"+str(obj.project_name)
        
    project.short_description = 'Project'

    def material(self, obj):
        filteredmaterial = Procurement.objects.filter(project__id=obj.id)
        material = ''
        for materials in filteredmaterial:
            if materials.material_ready is True:
                materialready = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ')
            else:
                materialready = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>')
        
            material = format_html(material)+ materialready
        return material
    material.short_description = 'Glass Ready'

    def Pi_NO(self,obj) -> str:
        filteredQuantity = Procurement.objects.filter(project__id=obj.id)
        # items = []
        html = ""
        if obj.finalize is True:
            html3 = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ')
        else:
            html3 = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>')
        for item in filteredQuantity:
            if(item.uploadfile != None and item.uploadfile != "" ): 
                uploadfile = '<div><a href="/media/{0}" target="_blank"/>File</a><br></div>'
                html1 = format_html(uploadfile,item.uploadfile)
                pino = '<div><a href="/DecorStoreApp/procurement/'+str(item.id)+'/change">'+str(item.pi_no)+'</a></div>'
                html2 = format_html(pino)
                html = format_html(html) + html1 + html2
            else: 
                pino = '<div><a href="/DecorStoreApp/procurement/'+str(item.id)+'/change">'+str(item.pi_no)+'</a></div>'
                pino_html = format_html(pino)
                html = format_html(html) + pino_html
        if filteredQuantity:
            return html3 + html
        else: 
            return html3
    Pi_NO.short_description = 'Finalization'

    def delivered_procurement(self, obj):
        procurement_delivered = Procurement.objects.filter(project__id = obj.id)
        dispatch = ""
        for dispatch_status in procurement_delivered:
            dispatch_status = dispatch_status.delivered
            if dispatch_status is True:
                dispatch_status = format_html('<img src="/static/admin/img/icon-yes.svg" alt="True"><br/> ')
            else:
                dispatch_status = format_html('<img src="/static/admin/img/icon-no.svg" alt="False"><br/>')
            dispatch = format_html(dispatch) + dispatch_status
        return dispatch
    delivered_procurement.short_description = 'Delivered'
    
    list_display = ('project', 'measurement_field', 'diagram_field','quote_field','Pi_NO', 'material', 'onProduction_field', 'payment_status', 'dispatch_status','installation_field', 'actual_sqft', 'notes', 'created_at', 'cancel_project') 
             
    search_fields = ('client__firstname', 'id', 'ProjectId__pino')
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Search by quote pino
        queryset |= self.model.objects.search_by_quote_pino(search_term)

        return queryset, use_distinct
    
    list_filter = ( StatusListFilter, 'measurement_staff', MeasurementFilter, DiagramFilter, QuoteFilter, FinalizeFilter,  MaterialReadyFilter, onProductionFilter, PaymentFilter, DispatchFilter, InstallationFilter, 'installation_staff',)

    ordering = ['-created_at']
    list_per_page = 20
    def get_search_results(self, request, queryset, search_term):
        print('search', search_term)
        search_queries = search_term.split(",")
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)
        project_queryset = []
        flag = True
        for q in search_queries:
            if not q.isdigit():
                flag = False
        if search_term:
            if flag == True:
                project_queryset = Quote.objects.filter(id__in = search_queries)
            procurement_pino = Procurement.objects.filter(pi_no__in = search_queries)
            for quotepino in project_queryset:
                queryset1 = Projects.objects.filter(id = quotepino.ProjectId.id) 
                queryset = queryset1
            for pino in procurement_pino:
                queryset2 = Projects.objects.filter(id = pino.project.id) 
                queryset = queryset2
            queryset3 = Projects.objects.filter(client__firstname__in = search_queries) 
            queryset = queryset | queryset3
        return queryset, may_have_duplicates

    actions = ['set_projects_to_cancelled', 'export_to_pdf' ]

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Projects.pdf"'

        buffer = []
        doc = SimpleDocTemplate(
            response,
            pagesize=A4,
            leftMargin=2 * cm,
            rightMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm
        )

        # Styles
        styles = getSampleStyleSheet()

        # Header Style
        header_style = ParagraphStyle(
            name="HeaderStyle",
            fontSize=18,
            leading=22,
            alignment=1,
            fontName="Helvetica-Bold",
            spaceAfter=20,
            textColor=colors.black
        )

        # Normal Style
        normal_style = ParagraphStyle(
            name="NormalStyle",
            fontSize=10,
            leading=12,
            fontName="Helvetica",
            textColor=colors.black
        )
        # ✅ Helper: Wrap Text
        def wrap_text(text):
            return Paragraph(str(none_to_blank(text)), normal_style)
        # ✅ Helper: Convert None to Blank
        def none_to_blank(value):
            return "" if value is None else value

        # ✅ Helper: Boolean to Colored Symbols
        def boolean_to_symbol(value):
            if value:
                return Paragraph('<para align="center"><font color="green">✔</font></para>', normal_style)
            else:
                return Paragraph('<para align="center"><font color="red">✖</font></para>', normal_style)

        # ✅ Helper: Glass Ready Logic
        def glass_ready_status(obj):
            filtered_materials = Procurement.objects.filter(project__id=obj.id)
            for material in filtered_materials:
                if material.material_ready:  # Check for material ready status
                    return boolean_to_symbol(True)
            return boolean_to_symbol(False)

        # ✅ Helper: Material Ready Logic
        def material_ready_status(obj):
            if obj.payment_status:  # Assuming material ready is based on payment_status
                return boolean_to_symbol(True)
            return boolean_to_symbol(False)

        # ✅ Add Header Title
        title = Paragraph("Projects", header_style)
        buffer.append(title)
        buffer.append(Spacer(1, 12))

        # ✅ Define Table Headers
        headers = [
            'Type of<br />Work',
            'Client',
            'Measurement<br />Status',
            'Measurement<br />Staff',
            'Diagram<br />Status',
            'OnProduction',
            'Glass<br />Ready',
            'Material<br />Ready',
            'Dispatch<br />Status',
            'Installation<br />Status',
            'Installation<br />Staff',
            'Notes'
        ]
        header_paragraphs = [Paragraph(header, normal_style) for header in headers]
        data = [header_paragraphs]

        # ✅ Helper: Format Type of Work
        def format_type_of_work(type_of_work_list):
            if isinstance(type_of_work_list, list):
                return ", ".join(type_of_work_list)
            return str(type_of_work_list)

        # ✅ Populate Table Data
        for obj in queryset:
            row = [
                wrap_text(format_type_of_work(obj.type_of_work)),
                wrap_text(none_to_blank(getattr(obj, "client", None))),
                boolean_to_symbol(obj.measurement_status),
                wrap_text(none_to_blank(getattr(obj, "measurement_staff", None))),
                boolean_to_symbol(obj.diagram_status),
                boolean_to_symbol(obj.onProduction),
                glass_ready_status(obj),  
                material_ready_status(obj),  
                boolean_to_symbol(obj.dispatch_status),
                boolean_to_symbol(obj.installation_status),
                wrap_text(none_to_blank(getattr(obj, "installation_staff", None))),
                wrap_text(obj.notes),
            ]
            data.append(row)

        # ✅ Define Table with Adjusted Column Widths
        table = Table(
            data,
            colWidths=[
                2.0 * cm,  # Type of Work
                1.6 * cm,  # Client
                1.8 * cm,  # Measurement Status
                2.0 * cm,  # Measurement Staff
                1.8 * cm,  # Diagram Status
                1.6 * cm,  # Diagram Status
                1.5 * cm,  # Dispatch Status
                1.8 * cm,  # Installation Status
                1.8 * cm,  # Installation Staff
                1.5 * cm,  # Glass Ready
                1.8 * cm,  # Material Ready
                1.6 * cm,  # Notes
            ]
        )

        # ✅ Apply Table Style with Grey Header
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),         # Grey Header Background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    # White Header Text
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),                # Center Align Headers
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),             # Vertical Align
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),     # Bold Header Font
            ('FONTSIZE', (0, 0), (-1, -1), 10),                 # Font Size for all cells
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),              # Header Padding
            ('GRID', (0, 0), (-1, -1), 1, colors.black),        # Full Grid Borders
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])  # Alternating Rows
        ])

        table.setStyle(style)

        # ✅ Add Table to Buffer
        buffer.append(table)

        # ✅ Build PDF
        doc.build(buffer)

        return response

    export_to_pdf.short_description = "Export Selected to PDF"

    def actual_sqft(self, obj):
        type_of_work_list = obj.type_of_work  # Assuming TypeOfWork is a list field

        if "UPVC" in type_of_work_list:
            return obj.totalsquareft
        grandtotal = 0
        quotes = Quote.objects.filter(ProjectId=obj.id)  
        actualsqft = LineItemGlass.objects.filter(QuoteId__in=quotes)
        for sqft in actualsqft:
            l = float(sqft.Length)
            w = float(sqft.Width)
            q = float(sqft.Quantity)
            if sqft.UnitOfMeasurement == 'mm':
                l = l / 304.8
                w = w  / 304.8
                total = l * w * q
                
            elif sqft.UnitOfMeasurement == 'inch':
                l = l / 12
                w = w / 12
                total = l * w * q
                
            else:
                total = l * w * q
            grandtotal += total    
        
        return round(grandtotal,2)
    actual_sqft.short_description = "Total Square Feet"

    def set_projects_to_cancelled(self, request, queryset):
        print('queryset', queryset)
        for project in queryset:
            print('project', project.status)
            if project.status == 1 or project.status == 2:
                count = queryset.update(status=3)
                self.message_user(request, "{} Project Cancelled successfully".format(count))
            if project.status == 3:
                count = queryset.update(status=1)
                self.message_user(request, "{} Project Updated successfully".format(count))

    def cancel_project(self, obj):
        action_name = 'set_projects_to_cancelled'
        action_index_in_action_list = '1'
        if obj.status == 1 or obj.status == 2:
            return mark_safe(f"""
                <label class="btn btn-warning">cancel
                <input type="checkbox" name="_selected_action" onchange="this.nextElementSibling.disabled=false;this.nextElementSibling.nextElementSibling.disabled=false;this.form.submit()" value="{obj.id}" style="display:none;">
                <input type="hidden" disabled name="action" value="{action_name}">
                <input type="hidden" disabled name="index" value="{action_index_in_action_list}">
                </label>"""
                )
        if obj.status == 3:
            return mark_safe(f"""
                <label class="btn btn-danger">cancelled
                <input type="checkbox" name="_selected_action" onchange="this.nextElementSibling.disabled=false;this.nextElementSibling.nextElementSibling.disabled=false;this.form.submit()" value="{obj.id}" style="display:none;">
                <input type="hidden" disabled name="action" value="{action_name}">
                <input type="hidden" disabled name="index" value="{action_index_in_action_list}">
                </label>"""
                )

    set_projects_to_cancelled.short_description = "Cancel Project"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return super().get_queryset(request).filter(status=1)

    class Media:
        css = {
            'all': ('admin/css/admin_custom_style.css','admin/css/project_procurement.css',)
        }
        js = (
             ('admin/js/projects.js',)
        )
admin.site.register(Projects, ProjectsAdmin)


class ProcurementStatusListFilter(admin.SimpleListFilter):
    title = 'Type of Works'
    parameter_name = 'type_of_work'

    def lookups(self, request, model_admin):
        print('status', ProcurementStatuses.CHOICES)
        return ProcurementStatuses.CHOICES

    def queryset(self, request, queryset):
        lookup_value = self.value()
        if lookup_value:
            print('clicked key: ', lookup_value)
            # filter if a choice selected
            queryset = queryset.filter(materials__contains=lookup_value)
            print('all: ', queryset)
        return queryset
class ProcurementMaterialFilter(admin.SimpleListFilter):
    title = 'Glass'
    parameter_name = 'glass_status__exact'

    filed_name = 'material_ready'
    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(material_ready = True)
        if self.value() == '0':
            return queryset.filter(material_ready = False)
        return queryset.all() 

class ProcurementReceivedFilter(admin.SimpleListFilter):
    title = 'Received'
    parameter_name = 'received_status__exact'

    filed_name = 'received'
    

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
            
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(received = True)
        if self.value() == '0':
            return queryset.filter(received = False)
        return queryset.all()    

class ProcurementDeliveredFilter(admin.SimpleListFilter):
    title = 'Delivered'
    parameter_name = 'delivered_status__exact'

    filed_name = 'delivered'
    

    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
            
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(delivered = True)
        if self.value() == '0':
            return queryset.filter(delivered = False)
        return queryset.all()    

class QuantityItemInline(admin.StackedInline):
    model = Quantity
    extra = 1
    fields = ["item", "quantity"]

class ProcurementResource(resources.ModelResource):
    pi_no = Field(attribute='pi_no', column_name='Pi No')
    amount = Field(attribute='amount', column_name='Amount')
    material_ready = Field(attribute='material_ready', column_name='Material Ready')
    project = Field(attribute='project', column_name='Project Name')
    companyname = Field(attribute='companyname', column_name='Supplier Name')
    # cgst = Field(attribute='cgst', column_name='CGST')
    received = Field(attribute='received', column_name='Received')
    delivered = Field(attribute='delivered', column_name='Delivered')

    class Meta:
        model = Procurement
        fields = ('pi_no', 'amount', 'material_ready', 'project', 'companyname', 'received',  'delivered')
        export_order = ('pi_no','amount', 'material_ready', 'project', 'companyname', 'received',  'delivered')


def export_as_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="material_procurements.pdf"'

    buffer = []
    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    # Styles
    styles = getSampleStyleSheet()

    # Header Style
    header_style = ParagraphStyle(
        name="HeaderStyle",
        fontSize=18,
        leading=22,
        alignment=1,
        fontName="Helvetica-Bold",
        spaceAfter=20,
        textColor=colors.black
    )

    # Normal Style
    normal_style = ParagraphStyle(
        name="NormalStyle",
        fontSize=10,
        leading=12,
        fontName="Helvetica",
        textColor=colors.black
    )

    # ✅ Helper: Convert None to Blank
    def none_to_blank(value):
        return "" if value is None else value

    # ✅ Helper: Boolean to Colored Symbols
    def boolean_to_symbol(value):
        if value:
            return Paragraph('<para align="center"><font color="green">✔</font></para>', normal_style)
        else:
            return Paragraph('<para align="center"><font color="red">✖</font></para>', normal_style)

    # ✅ Helper: Fetch Quantity Details
    def get_quantity_details(obj):
        items = obj.quantityItem.all()  # Access related Quantity items
        if not items:
            return "N/A"
        return ", ".join([f"{item.item} x {item.quantity}" for item in items])

    # ✅ Helper: Wrap Text
    def wrap_text(text):
        return Paragraph(str(none_to_blank(text)), normal_style)

    # ✅ Add Header Title
    title = Paragraph("Material Procurements", header_style)
    buffer.append(title)
    buffer.append(Spacer(1, 12))

    # ✅ Define Table Headers
    headers = ['Date', 'Company', 'Pi No', 'Project', 'Quantity', 'Type of\nWork', 'Glass\nReady', 'Received', 'Delivered']
    data = [headers]

    # ✅ Populate Table Data
    for obj in queryset:
        row = [
            wrap_text(obj.date),
            wrap_text(obj.companyname),
            wrap_text(obj.pi_no),
            wrap_text(none_to_blank(getattr(obj, "project", None))),  # ✅ Handle None Project
            wrap_text(get_quantity_details(obj)),
            wrap_text(obj.materials),
            boolean_to_symbol(obj.material_ready),
            boolean_to_symbol(obj.received),
            boolean_to_symbol(obj.delivered),
        ]
        data.append(row)

    # ✅ Define Table with Adjusted Column Widths
    table = Table(
        data,
        colWidths=[
            2.5 * cm,  # Date
            2.5 * cm,  # Company
            2.0 * cm,  # PiNO
            2.5 * cm,  # Project
            2.5 * cm,  # Quantity
            2.0 * cm,  # Type of Work
            2.5 * cm,  # Material Ready
            2.0 * cm,  # Received
            2.0 * cm   # Delivered
        ]
    )

    # ✅ Apply Table Style with Grey Header
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),         # Grey Header Background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    # White Header Text
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),               # Center Align
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),             # Vertical Align
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),     # Bold Header Font
        ('FONTSIZE', (0, 0), (-1, -1), 10),                 # Font Size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),             # Header Padding
        ('LEFTPADDING', (0, 0), (-1, -1), 6),               # Left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),              # Right padding
        ('GRID', (0, 0), (-1, -1), 1, colors.black),        # Full Grid Borders
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])  # Alternating Rows
    ])

    table.setStyle(style)

    # ✅ Add Table to Buffer
    buffer.append(table)

    # ✅ Build PDF
    doc.build(buffer)

    return response

export_as_pdf.short_description = "Export Selected to PDF"

class ProcurementAdmin(admin.ModelAdmin):
    inlines = [QuantityItemInline]
    form = ProcurementProjectForm 
    actions = [export_as_pdf]
    fieldsets = (
         ('Procurement Details', {
            'fields': (('date', 'pi_no'),('amount','Quantity'),('project', 'companyname', 'uploadfile',  ),('material_ready','received', 'delivered'), ('materials'))
        }),
        )
    
    readonly_fields= ('Quantity',) 
    
    #show quantity between the fields in forms
    def Quantity(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response
    
    #redirect the project url
    def assigned_project(self, obj):
        project_link= '<a href="/DecorStoreApp/projects/'+str(obj.project_id)+'/change">'+str(obj.project)+'</a>'
        html = format_html(project_link, str(obj.project))
        return html

    #to show Quantity list
    def quantity(self,obj) -> str:
        filteredQuantity = Quantity.objects.filter(qty__id=obj.id)
        items = []
        text= []
        for item in filteredQuantity:
            item = {
                'Quantity': str(item.item)+ '-' +str(item.quantity)
            }
            items.append((item['Quantity']))
            text = '\n'.join(items)
        return text
    quantity.short_description = 'Quantity'

    list_display = ('date', 'pi_no', 'quantity', 'amount', 'materials',  'assigned_project', 'uploadfile', 'companyname', 'material_ready', 'received', 'delivered')

    search_fields = ['project__client__firstname','pi_no']
    list_display_links = ['pi_no']
    list_filter = (ProcurementStatusListFilter, ProcurementMaterialFilter, ProcurementReceivedFilter, ProcurementDeliveredFilter,  'companyname', )
    list_per_page = 10
    # prepopulated_fields = {'amount': ('pi_no',)}
    def get_search_results(self, request, queryset, search_term):
        print('search', search_term)
        search_queries = search_term.split(",")
        print('search split', search_queries)
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)

        if search_term:
            project_queryset = Procurement.objects.filter(project__client__firstname__in = search_queries)
            pino_queryset = Procurement.objects.filter(pi_no__in = search_queries)
            search_queriesquote = str(search_queries).replace("[", "").replace("]", "").replace("'", "")
            quotepino_queryset = Quote.objects.filter(pino__contains = search_queriesquote)
            print('aaa', project_queryset, pino_queryset, quotepino_queryset, search_queriesquote)
            if project_queryset and  pino_queryset:
                # queryset = Procurement.objects.filter(pi_no__in =search_queries)
                queryset = Procurement.objects.filter(project__client__firstname__in =search_queries, pi_no__in = search_queries) 
            elif project_queryset:
                queryset = Procurement.objects.filter(project__client__firstname__in = search_queries) 
            elif pino_queryset:
                queryset = Procurement.objects.filter(pi_no__in = search_queries) 
            # elif quotepino_queryset:
            #     queryset = Quote.objects.filter(pino__contains = search_queriesquote) 
                print('querys', queryset)
            print("MY QS IS ", queryset)
        return queryset, may_have_duplicates
    class Media:
        css = { 
            'all': ('admin/css/project_procurement.css','admin/css/procurement.css',)
        }
        js = (
             ('admin/js/procurements.js','admin/js/procurement.js',)
        )
admin.site.register(Procurement, ProcurementAdmin)

class LineItemGlassViewStackedInline(admin.StackedInline):
    form = LineItemGlassForms
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'ItemMasterId':
            kwargs['queryset'] = ItemMaster.objects.filter(TypeOfItem='Glass')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    fieldsets = (
       ("None",{
             "fields": (
                'ItemMasterId', 'UnitOfMeasurement', 'Length', 'Width', 'Quantity', 'Rate', 'Total', 
                'billedlength', 'billedwidth'
             )
         }),
        (" ",{
            "fields": (
                'crystal', 'crystalRate', 'Beveling1', 'Beveling1Rate', 'Beveling2', 'Beveling2Rate', 'Beveling3', 'Beveling3Rate', 'Beveling4', 'Beveling4Rate', 'Beveling5', 'Beveling5Rate', 'Beveling6', 'Beveling6Rate','frosting', 'frostingRate','digital_printing', 'printingRate', 'etching', 'etchingRate', 'double_stroke',  'strokeRate', 'Polish','PolishRate', 'Polishfeet',  'lacquered', 'lacqueredRate',  'hole', 'holeQty', 'holeRate','cutout', 'cutoutQty', 'cutoutRate', 'spacer_hole', 'spacerholeQty', 'spacerholeRate', 'screw_hole', 'screwholeQty', 'screwholeRate', 'remarks'
            ),
        }),
       
        
    )

    model = LineItemGlass
    extra = 0
    verbose_name = "Line Items Glass"
    verbose_name_plural = "Line Items Glasses"

class LineItemVFittingsiewStackedInline(admin.StackedInline):
    form = LineItemFittingsForms
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'ItemMasterid':
            kwargs['queryset'] = ItemMaster.objects.filter(TypeOfItem='Fittings')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
   
    fields = ['ItemMasterid', 'Quantity', 'Rate', 'Total', ]
    # readonly_fields = ['Total']
    model = LineItemFittings
    extra = 0
    verbose_name = "Line Items Fitting"
    verbose_name_plural = "Line Items Fittings"

class LineItemMiscViewStackedInline(admin.StackedInline):
    form = LineItemMiscForms
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'ItemMasterIdMisc':
            kwargs['queryset'] = ItemMaster.objects.filter(TypeOfItem='Misc')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    fields = ['ItemMasterIdMisc', 'remarks', 'Quantity', 'Rate', 'Total', ]
    # readonly_fields = ['Total']
    model = LineItemMisc
    extra = 0
    verbose_name = "Line Items Misc"
    verbose_name_plural = "Line Items Miscs"

class GLassFilter(admin.SimpleListFilter):
    title = 'Glass'
    parameter_name = 'glass'
    def lookups(self, request, model_admin):
        print('status', Statuses.CHOICES)
        return Statuses.CHOICES

    def queryset(self, request, queryset):
        lookup_value = self.value()
        if lookup_value:
            queryset = queryset.filter(ProjectId__type_of_work__contains=lookup_value)
            print('VALUE', queryset)
            return queryset

class QuoteAdmin(admin.ModelAdmin):
    form = QuoteForms
    inlines=[
        LineItemGlassViewStackedInline, 
        LineItemVFittingsiewStackedInline, 
        LineItemMiscViewStackedInline
        ]
    class Media:
        js = (
             ('admin/js/my_script.js','admin/js/quotemodel.js', 'admin/js/frostingrate.js', 'admin/js/termsconditions.js','admin/js/savequote.js', 'admin/js/quotecollapse.js')
        )
        css = {
            'all': ('admin/css/quote.css',)
        }

    def download_pdf(self, obj):
        return format_html(
            '<a class="btn btn-success" href="/print/quotepdf/%s">Download</a>' % (obj.id),
            )
    download_pdf.short_description = "Print PDF"

    def billed_sqft(self, obj):
        grandtotal = 0
        billedsqft = LineItemGlass.objects.filter(QuoteId__id=obj.id)
        for sqft in billedsqft:
            l = float(sqft.Length)
            w = float(sqft.Width)
            q = float(sqft.Quantity)
            if sqft.UnitOfMeasurement == 'mm':
                l = math.ceil((l / 304.8) /0.5) * 0.5
                w = math.ceil((w  / 304.8) /0.5) * 0.5
                total = ((l*w*q))
                
            elif sqft.UnitOfMeasurement == 'inch':
                l = math.ceil((l / 12) /0.5) * 0.5
                w = math.ceil((w / 12) /0.5) * 0.5
                total = ((l*w*q))
                
            else:
                total = float((l*w*q))
            grandtotal += total    
        # print('total', grandtotal)
        return round(grandtotal,2)
    billed_sqft.short_description = "Billed Sqft Total"

    def actual_sqft(self, obj):
        grandtotal = 0
        actualsqft = LineItemGlass.objects.filter(QuoteId__id=obj.id)
        for sqft in actualsqft:
            l = float(sqft.Length)
            w = float(sqft.Width)
            q = float(sqft.Quantity)
            if sqft.UnitOfMeasurement == 'mm':
                l = l / 304.8
                w = w  / 304.8
                total = l * w * q
                
            elif sqft.UnitOfMeasurement == 'inch':
                l = l / 12
                w = w / 12
                total = l * w * q
                
            else:
                total = l * w * q
            grandtotal += total    
        # print('total', grandtotal)
        return round(grandtotal,2)
    actual_sqft.short_description = "Actual Sqft Total"

    def type_of_work(self, obj):
        typeofwork = obj.ProjectId.type_of_work
        return typeofwork
    type_of_work.short_description = "Type of Work"

    def projects(self, obj):
        project = obj.ProjectId.id
        projectlink = '<div><a href="/DecorStoreApp/projects/'+str(project)+'/change">'+str(project)+'</a></div>'
        link = format_html(projectlink)
        return link
    projects.short_description = 'Project Id'

    def totalamount(self, obj):
        totalamount = 0
        glasses = LineItemGlass.objects.filter(QuoteId__id=obj.id)
        totalglass = 0
        totalareas = 0
        for glass in glasses:
            if glass:
                rate = float(glass.Rate)
                totalarea = float(glass.Total)
                total = rate * totalarea
            totalareas += totalarea
            totalglass += total
        fittings = LineItemFittings.objects.filter(Quoteid__id=obj.id)
        totalfitting = 0
        for fitting in fittings:
            if fitting:
                total = float(fitting.Total)
            totalfitting += total
        miscs = LineItemMisc.objects.filter(Quote_id__id=obj.id)
        totalmisc = 0
        total = 0
        for misc in miscs:
            miscName = (misc.ItemMasterIdMisc.Name).lower()
            if misc:
                if miscName == 'installation':
                    rate = float(misc.Rate)
                    qty = totalareas
                    total = rate * qty
                elif miscName != 'installation':
                    total = float(misc.Total)
            totalmisc += total
        totalamount = totalglass + totalfitting + totalmisc
        return totalamount
    totalamount.short_description = 'Total Amount'
    fieldsets = [
        (None, {
            'fields': [
                'ProjectId',
                ('discount_type', 'discount'),  # Show these two in the same row
                'interiorname',
                'gst', 'igst', 'cgst',
                'diagramfile',
                'preparedBy',
                'choose_terms', 'terms',
                'choose_header', 'header'
            ]
        }),
    ]
    list_display = ("ProjectId", 'projects', 'type_of_work', 'pino', 'actual_sqft', 'billed_sqft',  'created_at', "download_pdf") #'totalamount',
    list_filter = [GLassFilter]
    search_fields = ['ProjectId__client__firstname', 'pino', 'ProjectId__client__phone_number',]
    ordering = ['-created_at']
    def response_add(self, request, obj, post_url_continue="../%s/"):
        if '_continue' not in request.POST:
            return redirect('/print/quotepdf/'+str(obj.id))
        else:
            return super(QuoteAdmin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if '_continue' not in request.POST:
            return redirect('/print/quotepdf/'+str(obj.id))
        else:
            return super(QuoteAdmin, self).response_change(request, obj)
admin.site.register(Quote, QuoteAdmin)

admin.site.register(Supplier)

admin.site.register(PreparedBy)

class ItemMasterAdmin(admin.ModelAdmin):
    forms = ItemMasterForms
    list_filter = ['TypeOfItem']
    # def Stocklist(self, obj):
    #     if obj.TypeOfItem == 'Fittings':
    #         stocklist = StockFittings.objects.filter(fittingsStock__id = obj.id)
    #         totalOpeningStock = 0
    #         totalInventory = 0
    #         stock = []
    #         for stocks in stocklist:
    #             if stocks.stock_from == "Opening Stock":
    #                 totalOpeningStock += float(stocks.quantity)
    #             if stocks.stock_from == "Inventory" or stocks.stock_from == "Quote":
    #                 totalInventory += float(stocks.quantity)
    #         availablestock = totalOpeningStock - totalInventory
    #         stock.append(availablestock)
    #         return stock
    #     else:
    #         stock = ''
    #         return stock
    # Stocklist.short_description = 'Stcoks'
    list_display = ['Name', 'totalstock', 'TypeOfItem']
    search_fields =['Name',]
admin.site.register(ItemMaster, ItemMasterAdmin)

class StockFittingsAdmin(admin.ModelAdmin):
    form = StcksForms
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'fittingsStock':
            kwargs['queryset'] = ItemMaster.objects.filter(TypeOfItem='Fittings')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def stockto_Details(self, obj):
        if obj.stock_to == 'Quote':
            return str(obj.stock_to) + str(obj.quote.id) if str(obj.quote.id) else ""
            
        else:
            return obj.stock_to
    stockto_Details.short_description = 'Stcok To'


    fields = ('fittingsStock', 'stock_from', 'stock_to','quote',  'quantity', 'remarks', 'date')

    list_display = ['fittingsStock', 'stock_from', 'stockto_Details', 'quantity', 'isauto', 'date']
    search_fields =['fittingsStock__Name']
    exclude = ['isauto', ]
    ordering = ['-date']
    list_display_links = None

    class Media:
        js = (
             ('admin/js/stock.js',)
        )
admin.site.register(StockFittings, StockFittingsAdmin)

admin.site.register(LineItemGlass)

admin.site.register(LineItemFittings)

admin.site.register(LineItemMisc)

class InteriorAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Interior, InteriorAdmin)

class StockReportAdmin(admin.ModelAdmin):
    class Media:
        js = (
             ('admin/js/stockreport.js',)
        )
    change_list_template = 'custom-templates/stock_report.html'
admin.site.register(StockReport, StockReportAdmin)

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value',)
admin.site.register(Settings, SettingsAdmin)


class ReceivedgoodsFilter(admin.SimpleListFilter):
    title = 'Received'
    parameter_name = 'received__exact'

    filed_name = 'received'
    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(received = True)
        if self.value() == '0':
            return queryset.filter(received = False)
        return queryset.all() 


class ReceivedgoodsDeliveredFilter(admin.SimpleListFilter):
    title = 'Delivered'
    parameter_name = 'delivered__exact'

    filed_name = 'delivered'
    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(delivered = True)
        if self.value() == '0':
            return queryset.filter(delivered = False)
        return queryset.all() 

class CompanyNameFilter(admin.SimpleListFilter):
    title = ('Company Name')  # Display name in the admin panel
    parameter_name = 'companyname'  # URL parameter for filtering

    def lookups(self, request, model_admin):
        """Returns a list of tuples for the filter options"""
        companies = Supplier.objects.all().values_list('id', 'Name')
        return companies

    def queryset(self, request, queryset):
        """Filters the queryset based on the selected company"""
        if self.value():
            return queryset.filter(companyname_id=self.value())  # Filter by selected company
        return queryset

admin.site.register(Transporter)

class GoodsReceivedAdmin(admin.ModelAdmin):
    form = GoodsReceivedForm
    def invoicedetails(self, obj):
        if obj.invoicefile:
            file = mark_safe('<div>'+str(obj.invoiceno)+'</div>')
            file1 = mark_safe('<div><a href="/media/{0}" target="_blank"/>File</a></div>'.format(obj.invoicefile))
            files = file+ file1
        if not obj.invoicefile:
            file = mark_safe('<div>'+str(obj.invoiceno)+'</div>')
            files = file
        
        return files
    invoicedetails.short_description = 'Invoice'

    from django.utils.safestring import mark_safe

    def transporterdetails(self, obj):
        # Helper function to return a blank string if value is None
        def none_to_blank(value):
            return "" if value is None else value

        transporter_name = none_to_blank(obj.transporter)  # Check for None and replace with blank
        if obj.transporterfile:
            file = mark_safe(f'<div>{transporter_name}</div>')
            file1 = mark_safe(f'<div><a href="/media/{obj.transporterfile}" target="_blank">File</a></div>')
            files = file + file1
        else:
            files = mark_safe(f'<div>{transporter_name}</div>')
        
        return files

    transporterdetails.short_description = 'Transporter'

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="GoodsReceived.pdf"'

        buffer = []
        doc = SimpleDocTemplate(
            response,
            pagesize=A4,
            leftMargin=2 * cm,
            rightMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm
        )

        # Styles
        styles = getSampleStyleSheet()

        # Header Style
        header_style = ParagraphStyle(
            name="HeaderStyle",
            fontSize=18,
            leading=22,
            alignment=1,
            fontName="Helvetica-Bold",
            spaceAfter=20,
            textColor=colors.black
        )

        # Normal Style
        normal_style = ParagraphStyle(
            name="NormalStyle",
            fontSize=10,
            leading=12,
            fontName="Helvetica",
            textColor=colors.black
        )

        # ✅ Helper: Convert None to Blank
        def none_to_blank(value):
            return "" if value is None else value

        # ✅ Helper: Boolean to Colored Symbols
        def boolean_to_symbol(value):
            if value:
                return Paragraph('<para align="center"><font color="green">✔</font></para>', normal_style)
            else:
                return Paragraph('<para align="center"><font color="red">✖</font></para>', normal_style)

        # ✅ Helper: Fetch Quantity Details
        def get_quantity_details(obj):
            items = obj.quantityItem.all()  # Access related Quantity items
            if not items:
                return "N/A"
            return ", ".join([f"{item.item} x {item.quantity}" for item in items])

        # ✅ Helper: Wrap Text
        def wrap_text(text):
            return Paragraph(str(none_to_blank(text)), normal_style)

        # ✅ Add Header Title
        title = Paragraph("Goods Received", header_style)
        buffer.append(title)
        buffer.append(Spacer(1, 12))

        # ✅ Define Table Headers
        headers = [
            'Invoice No',
            'Company<br />Name',
            'Transporter<br />Name',
            'No of<br />Bundle',
            'Received',
            # 'Project<br />Name',
            'Remarks',
        ]
        header_paragraphs = [Paragraph(header, normal_style) for header in headers]
        data = [header_paragraphs]
        # ✅ Helper: Format Type of Work
        def format_type_of_work(type_of_work_list):
            if isinstance(type_of_work_list, list):
                return ", ".join(type_of_work_list)
            return str(type_of_work_list)
        # ✅ Populate Table Data
        for obj in queryset:
            row = [
                wrap_text(obj.invoiceno),
                wrap_text(none_to_blank(getattr(obj, "companyname", None))),
                wrap_text(obj.transportername),  
                wrap_text(obj.no_of_bundle),
                boolean_to_symbol(obj.received),
                # wrap_text(none_to_blank(getattr(obj, "projectname", None))),
                wrap_text(obj.remarks),
                
            ]
            data.append(row)
        total_width = A4[0] - (4 * cm)
        # ✅ Define Table with Adjusted Column Widths
        table = Table(
            data,
              # Account for margins
            colWidths = [
                total_width * 0.20,  # Type of Work
                total_width * 0.20,  # Client
                total_width * 0.20,  # Measurement Status
                total_width * 0.20,  # Measurement Staff
                total_width * 0.20,  # Diagram Status
                # total_width * 0.12,  # Dispatch Status
                total_width * 0.20,  # Installation Status
                
            ]
        )

        # ✅ Apply Table Style with Grey Header
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),         # Grey Header Background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    # White Header Text
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),                # Center Align Headers
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),             # Vertical Align
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),     # Bold Header Font
            ('FONTSIZE', (0, 0), (-1, -1), 10),                 # Font Size for all cells
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),              # Header Padding
            ('GRID', (0, 0), (-1, -1), 1, colors.black),        # Full Grid Borders
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])  # Alternating Rows
        ])

        table.setStyle(style)

        # ✅ Add Table to Buffer
        buffer.append(table)

        # ✅ Build PDF
        doc.build(buffer)

        return response
    export_to_pdf.short_description = "Export Selected to PDF"
    
    actions = ['export_to_pdf']
    list_filter = ( ReceivedgoodsFilter, ReceivedgoodsDeliveredFilter, CompanyNameFilter  )
    list_display = ('invoicedetails', 'date', 'companyname', 'transporterdetails', 'builtyNo', 'no_of_bundle', 'contactnumber', 'received', 'delivered', 'projectname', 'remarks') #
    search_fields = ('companyname__Name',  'remarks', 'transporter__Name', 'builtyNo', 'projectname__client__firstname','projectname__client__lastname',) #'transportername',
    exclude = ('transportername',)
    ordering = ['-id']
    class Media:
        js = ('admin/js/transporter.js',)
admin.site.register(GoodsReceived, GoodsReceivedAdmin)

class RepairingWorkStatusListFilter(admin.SimpleListFilter):
    title = 'Type of Works'
    parameter_name = 'type_of_work'

    def lookups(self, request, model_admin):
        print('status', RepairingWorkStatuses.CHOICES)
        return RepairingWorkStatuses.CHOICES

    def queryset(self, request, queryset):
        lookup_value = self.value()
        if lookup_value:
            print('clicked key: ', lookup_value)
            # filter if a choice selected
            queryset = queryset.filter(typeofwork__contains=lookup_value)
            print('all: ', queryset)
        return queryset

class WorkCompletedFilter(admin.SimpleListFilter):
    title = 'work Completed'
    parameter_name = 'workcompleted__exact'

    filed_name = 'workcompleted'
    def lookups(self, request, model_admin):
        return (
            ('1', 'Done'),
            ('0', 'Pending'),
        )
    def choices(self, changelist):
        from django.utils.encoding import force_text
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }
    def queryset(self, request, queryset): 
        if self.value() == '1':
            return queryset.filter(workcompleted = True)
        if self.value() == '0':
            return queryset.filter(workcompleted = False)
        return queryset.all() 

class RepairingWorkFileInline(admin.StackedInline):  # Using StackedInline
    model = RepairingWorkFile
    extra = 1  # Number of empty file upload fields
    verbose_name = "File"
    verbose_name_plural = "Uploaded Files"

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">View File</a>', obj.file.url)
        return "No File"
    
    file_link.allow_tags = True
    file_link.short_description = "File Link"

    readonly_fields = ("file_link",)

class RepairingWorkAdmin(admin.ModelAdmin):
    form = RepairingWorkForm
    list_filter = (RepairingWorkStatusListFilter, WorkCompletedFilter, )
    inlines = [RepairingWorkFileInline]
    actions = ['export_to_pdf']


    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="RepairingWork.pdf"'

        buffer = []
        doc = SimpleDocTemplate(
            response,
            pagesize=A4,
            leftMargin=2 * cm,
            rightMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm
        )

        # Styles
        styles = getSampleStyleSheet()

        # Header Style
        header_style = ParagraphStyle(
            name="HeaderStyle",
            fontSize=18,
            leading=22,
            alignment=1,
            fontName="Helvetica-Bold",
            spaceAfter=20,
            textColor=colors.black
        )

        # Normal Style
        normal_style = ParagraphStyle(
            name="NormalStyle",
            fontSize=10,
            leading=12,
            fontName="Helvetica",
            textColor=colors.black
        )
        # ✅ Helper: Wrap Text
        def wrap_text(text):
            return Paragraph(str(none_to_blank(text)), normal_style)
        # ✅ Helper: Convert None to Blank
        def none_to_blank(value):
            return "" if value is None else value

        # ✅ Helper: Boolean to Colored Symbols
        def boolean_to_symbol(value):
            if value:
                return Paragraph('<para align="center"><font color="green">✔</font></para>', normal_style)
            else:
                return Paragraph('<para align="center"><font color="red">✖</font></para>', normal_style)

        # ✅ Add Header Title
        title = Paragraph("Repairing Work", header_style)
        buffer.append(title)
        buffer.append(Spacer(1, 12))

        # ✅ Define Table Headers
        headers = [
            'Date',
            'Project Name',
            'Type of Work',
            'Client Name',
            'Client Number',
            'Details of Work',
            'Payment Terms',
            'Technician Name',
            'Work Completed',
            
        ]
        header_paragraphs = [Paragraph(header, normal_style) for header in headers]
        data = [header_paragraphs]

        # ✅ Populate Table Data
        for obj in queryset:
            row = [
                wrap_text(obj.date),
                wrap_text(none_to_blank(getattr(obj, "projectname", None))),
                wrap_text(obj.typeofwork),
                wrap_text(obj.clientName),
                wrap_text(obj.clientNumber),
                wrap_text(obj.workdetail),
                wrap_text(obj.paymentTerms),
                wrap_text(none_to_blank(getattr(obj, "technicianName", None))),
                boolean_to_symbol(obj.workcompleted),
                
                
            ]
            data.append(row)

        # ✅ Define Table with Adjusted Column Widths
        table = Table(
            data,
            colWidths=[
                1.8 * cm,  
                2.6 * cm,  
                2.6 * cm, 
                2.4 * cm,  
                2.0 * cm,  
                2.0 * cm,  
                2.0 * cm,  
                2.4 * cm,  
                2.2 * cm,  
            ]
        )

        # ✅ Apply Table Style with Grey Header
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),         # Grey Header Background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),    # White Header Text
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),                # Center Align Headers
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),             # Vertical Align
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),     # Bold Header Font
            ('FONTSIZE', (0, 0), (-1, -1), 10),                 # Font Size for all cells
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),              # Header Padding
            ('GRID', (0, 0), (-1, -1), 1, colors.black),        # Full Grid Borders
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])  # Alternating Rows
        ])

        table.setStyle(style)

        # ✅ Add Table to Buffer
        buffer.append(table)

        # ✅ Build PDF
        doc.build(buffer)

        return response

    export_to_pdf.short_description = "Export Selected to PDF"

    def uploaded_files(self, obj):
        """
        Displays all uploaded files in a stacked format as clickable links.
        """
        files = obj.files.all()  # This fetches all RepairingWorkFile instances related to this RepairingWork instance
        if files.exists():
            return format_html(
                '<br>'.join(f'<a href="{file.file.url}" target="_blank">File {idx+1}</a>' for idx, file in enumerate(files))
            )
        return "No File"

    uploaded_files.short_description = "Uploaded Files"

    fieldsets = (
        ("Basic Details", {
            "fields": ("date", "projectname"),
        }),
        ("Work Information", {
            "fields": ("typeofwork",),  
        }),
        
        ("Work and Client Details", {
            "fields": ("clientName", "clientNumber", "workdetail", "paymentTerms", "technicianName", "workcompleted"),
        }),
    )
    list_display = ('date', 'projectname', 'typeofwork', 'uploaded_files', 'clientName', 'clientNumber', 'workdetail', 'paymentTerms', 'technicianName',  'workcompleted')
    search_fields = ('technicianName', 'clientName')
    class Media:
        js = (
            ('admin/js/RepairingWork.js',)
        )
    
admin.site.register(RepairingWork, RepairingWorkAdmin)


class InstallationPaymentAdmin(admin.ModelAdmin):
    def ClientName(self,obj):
        clientname = str(obj.typeofwork.client.firstname) +  " " + str(obj.typeofwork.client.lastname)
        return clientname
    ClientName.short_description = 'Client Name'
    def TypeofWork(self,obj):
        typeofwork = obj.typeofwork.type_of_work
        return typeofwork
    TypeofWork.short_description = 'Type of Work'

    def TotalSqft(self, obj):
        grandtotal = 0
        actualsqft = LineItemGlass.objects.filter(QuoteId__id=obj.pino.id)
        for sqft in actualsqft:
            l = float(sqft.Length)
            w = float(sqft.Width)
            q = float(sqft.Quantity)
            if sqft.UnitOfMeasurement == 'mm':
                l = l / 304.8
                w = w  / 304.8
                total = l * w * q
                
            elif sqft.UnitOfMeasurement == 'inch':
                l = l / 12
                w = w / 12
                total = l * w * q
                
            else:
                total = l * w * q
            grandtotal += total    
        # print('total', grandtotal)
        return round(grandtotal,2)
    TotalSqft.short_description = "Total Sqft"

    list_display = ('pino', 'ClientName', 'TypeofWork', 'TotalSqft', 'amount', 'foodinglodging', 'updownfare', 'unloading', 'totalamount', 'technicianname', 'entry')
    # search_fields = ('technicianName', 'clientName')
    
admin.site.register(InstallationPayment, InstallationPaymentAdmin)

class ProjectReportAdmin(admin.ModelAdmin):
    change_list_template = 'custom-templates/projectReport.html'
admin.site.register(ProjectReport, ProjectReportAdmin)