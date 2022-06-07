from django.db import models
from datetime import datetime
# queryset = Courses.objects.filter(published=True).prefetch_related('modules', 'modules__lessons', 'modules__lessons__exercises')

class AbstractModel(models.Model):
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Staff_Details(AbstractModel):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default='', choices=[('Male','M'),('Female','F')])
    mobile_no = models.CharField(max_length=10)
    adhar_no = models.CharField(max_length=12)
    date_of_birth = models.DateField()



    def __str__(self):
        return self.name

class Shift_In_Timings(AbstractModel):
    name = models.ForeignKey(Staff_Details, on_delete=models.CASCADE)
    entry = models.TimeField(default = datetime.now().time(),)

    def __str__(self):
        return str(self.name)

class Shift_Out_Timings(AbstractModel):
    name = models.ForeignKey(Staff_Details, on_delete=models.CASCADE)
    out = models.TimeField(default = datetime.now().time())

    def __str__(self):
        return str(self.name)

class Staff_Leave_Details(AbstractModel):
    name = models.ForeignKey('Staff_Details', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name)