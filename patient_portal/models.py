import datetime
import random

from django.db import models

state_choices = [("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra")]
# city_choices = [('Ambi Bk', 'Ambi Bk'), ('Ambi Kh', 'Ambi Kh'), ('Anjangaon', 'Anjangaon'), ('Baburdi', 'Baburdi'), ('Bajrangwadi late', 'Bajrangwadi late'), ('Bajrangwadi rular', 'Bajrangwadi rular'), ('Baburdi', 'Baburdi'), ('Bharhanpur', 'Bharhanpur'), ('Bharhanpur', 'Bharhanpur'), ('Bhondvewadi', 'Bhondvewadi'), ('Chandgudewadi', 'Chandgudewadi'), ('Chaudharwadi', 'Chaudharwadi'), ('Chopadaj', 'Chopadaj'), ('Chopadaj', 'Chopadaj'), ('Deulagaon Rasal', 'Deulagaon Rasal'), ('Karanje', 'Karanje'), ('Dhakale', 'Dhakale'), ('Dhekalwadi', 'Dhekalwadi'), ('Dhumalwadi', 'Dhumalwadi'), ('Dorlewadi', 'Dorlewadi'), ('Gadadarwadi', 'Gadadarwadi'), ('Gadikhel', 'Gadikhel'), ('Ghadagewadi', 'Ghadagewadi'), ('Gojubabi', 'Gojubabi'), ('Gunwadi', 'Gunwadi'), ('Hol', 'Hol'), ('Jainakwadi', 'Jainakwadi'), ('Jalakewadi-Mudhale', 'Jalakewadi-Mudhale'), ('Jalgaon-Kade-Pathar', 'Jalgaon-Kade-Pathar'), ('Jalgaon-Supe', 'Jalgaon-Supe'), ('Jalochi', 'Jalochi'), ('Jaradwadi', 'Jaradwadi'), ('Jogwadi', 'Jogwadi'), ('Kalkhairewadi', 'Kalkhairewadi'), ('Kamagalwadi-dhakale', 'Kamagalwadi-dhakale'), ('Kambleshvar', 'Kambleshvar'), ('Kanadwadi-Chopadaj', 'Kanadwadi-Chopadaj'), ('Kanheri', 'Kanheri'), ('Karanje', 'Karanje'), ('Karnajpul', 'Karnajpul'), ('Karahati', 'Karahati'), ('Karhavagaj', 'Karhavagaj'), ('Kharkhel', 'Kharkhel'), ('Katewadi', 'Katewadi'), ('Katphal', 'Katphal'), ('Chandgudewadi', 'Chandgudewadi'), ('Khandaj-Khandaj', 'Khandaj-Khandaj'), ('Khandobachiwadi', 'Khandobachiwadi'), ('Kharadewadi', 'Kharadewadi'), ('Kololi', 'Kololi'), ('Korhale-Bk', 'Korhale-Bk'), ('Korhale-Kh', 'Korhale-Kh'), ('Kurnewadi', 'Kurnewadi'), ('Kutavalwadi', 'Kutavalwadi'), ('Late', 'Late'), ('Lonibhapkar', 'Lonibhapkar'), ('Magarwadi', 'Magarwadi'), ('Malad', 'Malad'), ('Malegaon-Bk', 'Malegaon-Bk'), ('Malegaon-Kh', 'Malegaon-Kh'), ('Malshikare-Wadi-Korhale-Bk', 'Malshikare-Wadi-Korhale-Bk'), ('Malwadilate', 'Malwadilate'), ('Manppawasti', 'Manppawasti'), ('Masalwadi', 'Masalwadi'), ('Medad', 'Medad'), ('Mekhali', 'Mekhali'), ('Modhave', 'Modhave'), ('Moralwadi', 'Moralwadi'), ('Moragon', 'Moragon'), ('Mudhale', 'Mudhale'), ('Murti', 'Murti'), ('Murum', 'Murum'), ('Naroli', 'Naroli'), ('Nepat-Valan-Bharhanpur', 'Nepat-Valan-Bharhanpur'), ('Nimbodi', 'Nimbodi'), ('Nimbut', 'Nimbut'), ('Niravagaj', 'Niravagaj'), ('Palshiwadi', 'Palshiwadi'), ('Pandare', 'Pandare'), ('Pandharwadi-Shirashne', 'Pandharwadi-Shirashne'), ('Pansarewadi', 'Pansarewadi'), ('Parwadi', 'Parwadi'), ('Pawaimal', 'Pawaimal'), ('Pavanewadi', 'Pavanewadi'), ('Pimpalewasti-Shirashne', 'Pimpalewasti-Shirashne'), ('Pimpali', 'Pimpali'), ('Rui', 'Rui'), ('Sablewadi', 'Sablewadi'), ('Sadobachiwadi', 'Sadobachiwadi'), ('Sangavi', 'Sangavi'), ('Sastewadi', 'Sastewadi'), ('Sawal', 'Sawal'), ('Sawantwadi-Gojubabi', 'Sawantwadi-Gojubabi'), ('Sayabachiwadi', 'Sayabachiwadi'), ('Sherechiwadi-Baburdi', 'Sherechiwadi-Baburdi'), ('Shiravali', 'Shiravali'), ('Shirsuphal', 'Shirsuphal'), ('Shirashne', 'Shirashne'), ('Songaon', 'Songaon'), ('Sonkaswadi', 'Sonkaswadi'), ('Sonvdisupe', 'Sonvdisupe'), ('Sortewadi', 'Sortewadi'), ('Supe', 'Supe'), ('Tandulwadi', 'Tandulwadi'), ('Tardoli', 'Tardoli'), ('Thopatewadi', 'Thopatewadi'), ('Umbarwadi-Modhave', 'Umbarwadi-Modhave'), ('Undawadi-K-P', 'Undawadi-K-P'), ('Untwadi-Supe', 'Untwadi-Supe'), ('Vadgaon-Ni', 'Vadgaon-Ni'), ('Vadhane', 'Vadhane'), ('Vanjarwadi', 'Vanjarwadi'), ('Vaghalwadi', 'Vaghalwadi'), ('Vaki', 'Vaki'), ('Wanewadi', 'Wanewadi'), ('Yelewasti-Malegaon-Bk', 'Yelewasti-Malegaon-Bk'), ('Zargadwadi', 'Zargadwadi')]
city_choices = [('Ambi Bk', 'Ambi Bk'), ('Ambi Kh', 'Ambi Kh'), ('Anjangaon', 'Anjangaon'), ('Baburdi', 'Baburdi'), ('Bajrangwadi late', 'Bajrangwadi late'), ('Bajrangwadi rular', 'Bajrangwadi rular')]

number = random.choice(['AB','PD','GH','WF'])+str(random.randint(100000,999999))
class Patient_Details(models.Model):
    gender_choice = [
        ('Male','Male'),
        ('Female', 'Female'),
        ('Other','Other'),
    ]

    pid = models.CharField(max_length=8, primary_key=False, default=number, unique=True)
    name = models.CharField(max_length=50 )
    gender = models.CharField(max_length=10, choices=gender_choice)
    addres = models.CharField(max_length=50, choices=city_choices, default='')
    mobile_no = models.CharField(max_length=10)
    opd = models.ForeignKey('OPD_Department_Details', default='OPD', on_delete=models.CASCADE)
    opd_sub_department = models.ForeignKey('OPD_Sub_Department_Details', on_delete=models.CASCADE)
    medecine_issued = models.ManyToManyField('Patient_Medecines_details' )



    def __str__(self):
        return self.pid

class Patient_Department_IPD(models.Model):

    patient_id = models.ForeignKey('Patient_Details', on_delete=models.CASCADE)
    ipd = models.ForeignKey('IPD_Department_Details', default='IPD', on_delete=models.CASCADE, null=True)
    ipd_sub_department = models.ForeignKey('IPD_Sub_Department_Details', on_delete=models.CASCADE,blank=True, null=True)

    bed_allot = models.OneToOneField('IPD_Patient_Beds', on_delete=models.CASCADE, blank=True, null=True)
    date_joining = models.DateField(auto_now_add=True, blank=True,  null=True)
    date_discharge = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.pid


class State(models.Model):
    state_name = models.CharField(choices=state_choices, max_length=255, null=True)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(choices=city_choices, max_length=255, null=True)
    state_ptr = models.ForeignKey(State, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.city_name

class OPD_Department_Details(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class OPD_Sub_Department_Details(models.Model):
    name = models.CharField(max_length=20)
    opd = models.ForeignKey('OPD_Department_Details', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Investigation_Test(models.Model):
    name = models.CharField(max_length=100)
    test_result = models.CharField(max_length=150)
    test_diagnosis = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class IPD_Department_Details(models.Model):
    ward = [('GEN','General'),('ICU','ICU')]
    name = models.CharField(max_length=20, choices=ward)
    def __str__(self):
        return self.name


class IPD_Sub_Department_Details(models.Model):
    name = models.CharField(max_length=20)
    opd = models.ForeignKey('IPD_Department_Details', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Patient_Medecines_details(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=50)
    patient_diagnosis = models.ForeignKey('Investigation_Test', on_delete=models.CASCADE)

class IPD_Patient_Beds(models.Model):
    name = models.CharField(max_length=50, choices=[('A1','A1'),('A2','A2'),('B1','B1'),('B2','B2'),('C1','C1'),('C2','C2'),('D1','D1')],
                            unique=True, error_messages = {'unique': "Dublicate Bed Entered"})

    def __str__(self):
        return self.name

class IPD_Patient_Status(models.Model):
    name = models.CharField(max_length=50, choices=[('IN','IN'),('OUT','OUT')])

    def __str__(self):
        return self.name

class medicine_issued_Count_details(models.Model):
    pass
