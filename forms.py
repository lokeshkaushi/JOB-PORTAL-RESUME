django import forms
form .models import Resume

class ResumeForm(forms.modelForm):
    class meta:
        Model =resume
        Fields = ['name','gender','locality','city','pin','state','mobile','email','job_city','Address',
        'linkedin','objective','workexperience','hsc','subject','passingyear','percentage','univercity',
        'diploma','dbranch','dpassingyear','dpercentage','dunivercity','degree','gbranch','gpassingyear',
        'gpercentage','gunivercity','pbranch','ppassingyear','postgraduation',' ppercentage','']