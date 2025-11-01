from django import forms
from .models import *
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.admin import widgets
from django.forms.models import BaseInlineFormSet
from django.forms import DateInput
from django.core.files.storage import default_storage

OPTIONS = [
    ('Purchase', 'Purchase'),
    ('ClearGlass', 'Clear Glass'),
    ('ToughenedGlass', 'Toughened Glass'),
    ('UPVC', 'UPVC')  
]
class TypeOfWorkForm(forms.ModelForm):
    
    type_of_work = forms.MultipleChoiceField(choices=OPTIONS, widget=forms.CheckboxSelectMultiple(), required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define OPTIONS here
        
        initial_type_of_work = self.initial.get('type_of_work', [])
        if 'UPVC' in initial_type_of_work:
            # If 'UPVC' was previously selected, ensure 'Purchase' is included in initial data
            self.initial['type_of_work'] = ['UPVC'] + initial_type_of_work
        else:
            # Otherwise, only keep the selected options that are in OPTIONS
            self.initial['type_of_work'] = [choice for choice in initial_type_of_work if choice in [option[0] for option in OPTIONS]]
    class Meta:
        model = Projects
        fields = '__all__'
        labels = {
            "client": "Client Name",
            "measurement_staff": "Measurement Staff",
            "type_of_work": "Type of Work",
            "installation_status": "Installation Status",
            "installation_staff": "Installation Staff",
            "quote_file": "Quote File",
            "quote_file_1": "Quote File 1",
            "quote_file_2": "Quote File 2",
            "quote_status": "Quote Status",
            "interior_name": "Interior name",
            "measurement_status": "Measurement Status",
            "diagram_status": "Diagram Status",
            "diagram_file": "Diagram File",
            "payment_status": "Material Ready",
            "invoice_file": "Invoice File",
            "invoice_status": "Invoice Status"
        }
        widgets = {
            'client': AutocompleteSelect(
                Projects._meta.get_field('client').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'measurement_staff': AutocompleteSelect(
                Projects._meta.get_field('measurement_staff').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'installation_staff': AutocompleteSelect(
                Projects._meta.get_field('installation_staff').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'onProduction': forms.CheckboxInput(),
            # 'diagram_file': forms.ClearableFileInput(attrs={'multiple':True})
        }

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(TypeOfWorkForm, self).__init__(*args, **kwargs)

    # def clean_diagram_file(self):
    #     obj = super(TypeOfWorkForm, self).save(commit=False)
    #     print("CLEAN HAS REQ ", self.request.FILES)
    #     print("CLEAN HAS REQ ", self.request.FILES.getlist('diagram_file'))
    #     uploadedFilesList = self.request.FILES.getlist('diagram_file')
    #     diagram_files_list = []
    #     for diagram in uploadedFilesList:
    #         print('diagram', diagram.name)
    #         diagram_files_list.append(diagram.name)
    #         if diagram:
    #             #    obj.diagram_file=diagram
    #             #    obj.save()
    #             default_storage.save(diagram.name, diagram)
    #     joiner = ","
    #     print("LIST OF DIAGRAM ", diagram_files_list)
    #     obj.diagram_file=joiner.join(diagram_files_list) 
        # obj.save()
        
class DateInput(forms.DateInput):
    input_type = 'date'    

MaterialOPTIONS = [
    ('Tuff', 'Tuff'),
    ('UPVC', 'UPVC')
]
 
class ProcurementProjectForm(forms.ModelForm):
    # materials = forms.MultipleChoiceField(
    #     choices=MaterialOPTIONS,
    #     widget=forms.CheckboxSelectMultiple(),
    #     required=False,
    #     label="Materials Selected"  # Use the same verbose name as in the model
    # )
    class Meta:
        model = Procurement
        fields = '__all__'
        widgets = {
             
            'materials': forms.RadioSelect(),  # Display materials as a radio button group
        
            # 'companyname': AutocompleteSelect(
            #     Procurement._meta.get_field('companyname').remote_field,
            #     admin.site,
            #     attrs={'data-dropdown-auto-width': 'true'}
            # ),
            # 'project': AutocompleteSelect(
            #     Procurement._meta.get_field('project').remote_field,
            #     admin.site,
            #     attrs={'data-dropdown-auto-width': 'true'}
            # ),
            
            'date': DateInput(),
        }
       

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            "firstname": "First Name",
            "lastname": "Last Name",
            "phone_number": "Phone Number",
            "alternate_number": "Alternate Number",
        }
        error_messages = {
            'firstname': {
                'null': ("Custom error message."),
            },
        }


class taskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'asigned_to': AutocompleteSelect(
                Tasks._meta.get_field('asigned_to').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'project': AutocompleteSelect(
                Tasks._meta.get_field('project').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class QuoteForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoteForms, self).__init__(*args, **kwargs)
        self.fields['ProjectId'].required = True
        preset_terms = ""
        preset_header = ""
        for terms in Settings.objects.all():
            if terms.key == 'Terms':
                preset_terms = terms.value
            if terms.key == 'Header':
                preset_header = terms.value
        if self.instance.pk:
            if self.instance.terms == '' or self.instance.terms == None:
                self.initial['terms'] = preset_terms
            else:
                self.initial['terms'] = self.instance.terms 
            if self.instance.choose_header == 1:
                if self.instance.header:
                    self.initial['header'] = self.instance.header
                else:
                    self.initial['header'] = preset_header
            else:
                self.initial['header'] = preset_header
        else:
            self.initial['terms'] = preset_terms
    def clean_terms(self):
        termsdata = self.cleaned_data['terms']
        previousterms = ''
        for terms in Settings.objects.all():
            if terms.key == 'Terms':
                previousterms = terms.value
        if previousterms == termsdata:
            termsdata = ''
        else:
            termsdata = termsdata
        return termsdata
    def clean_header(self):
        headerdata = self.cleaned_data['header']
        previousheader = ''
        for terms in Settings.objects.all():
            if terms.key == 'Header':
                previousheader = terms.value
        if previousheader == headerdata:
            headerdata = ''
        else:
            headerdata = headerdata
        return headerdata
    
    class Meta:
        model = Quote
        fields = '__all__'
        labels = {
            "ProjectId": "ProjectId *",
        }
        widgets = {
            'discount': forms.TextInput(attrs={'type':'number'}),
            'ProjectId': AutocompleteSelect(
                Quote._meta.get_field('ProjectId').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'interiorname': AutocompleteSelect(
                Quote._meta.get_field('interiorname').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            'header': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    

class LineItemGlassForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LineItemGlassForms, self).__init__(*args, **kwargs)
        # self.fields['ItemMasterId'].required = True
        self.fields['Length'].required = True
        self.fields['Width'].required = True
        self.fields['Quantity'].required = True
        self.fields['UnitOfMeasurement'].required = True
    class Meta:
        model = LineItemGlass
        fields = ['Length', 'Width', 'Quantity', 'Rate']
        widgets = {
            'Length': forms.TextInput(attrs={'type':'number'}),
            'Width': forms.TextInput(attrs={'type':'number'}),
            'Quantity': forms.TextInput(attrs={'type':'number'}),
            'Rate': forms.TextInput(attrs={'type':'number'}),
            'Total': forms.TextInput(attrs={'type':'number'}),
            'remarks': forms.Textarea(attrs={'cols': 48, 'rows': 5}),
        }
    
total_fitting_qty = 0
class LineItemFittingsForms(forms.ModelForm):
    class Meta:
        model = LineItemFittings
        fields = '__all__'
        widgets = {
            'Quantity': forms.TextInput(attrs={'type':'number'}),
            'Rate': forms.TextInput(attrs={'type':'number'}),
            'Total': forms.TextInput(attrs={'type':'number'}),
        }
    
class LineItemMiscForms(forms.ModelForm):
    class Meta:
        model = LineItemMisc
        fields = '__all__'
        widgets = {
            'Quantity': forms.TextInput(attrs={'type':'number'}),
            'Rate': forms.TextInput(attrs={'type':'number'}),
            'Total': forms.TextInput(attrs={'type':'number'}),
            'remarks': forms.Textarea(attrs={'cols': 48, 'rows': 5}),
        }

class ItemMasterForms(forms.ModelForm):
    def clean_Name(self):
        return self.cleaned_data["Name"].upper()
        
    class Meta:
        model = ItemMaster
        fields = '__all__'
        # widgets = {
        #     'Name': forms.TextInput(attrs={'style': 'text-transform:uppercase;'}),
            
        # }

class StcksForms(forms.ModelForm):
    class Meta:
        model = StockFittings
        fields = '__all__'

        widgets = {
            'date': DateInput(),
            'remarks': forms.Textarea(attrs={'cols': 48, 'rows': 5}),
         }
        
class GoodsReceivedForm(forms.ModelForm):
    class Meta:
        model = GoodsReceived
        fields = '__all__'
        widgets = {
            'projectname': AutocompleteSelect(
                GoodsReceived._meta.get_field('projectname').remote_field,
                admin.site,
                attrs={'data-dropdown-auto-width': 'true'}
            ),
            
            'date': DateInput(),
            'remarks': forms.Textarea(attrs={'cols': 48, 'rows': 5}),
        }


class RepairingWorkForm(forms.ModelForm):
    class Meta:
        model = RepairingWork
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'paymentTerms': forms.Textarea(attrs={'cols': 48, 'rows': 5}),
            'typeofwork': forms.RadioSelect(),
        }