from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.


class Language(models.Model):
    name= models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

llist = Language.objects.filter(status=True)
list1 = []

for rs in llist:
    list1.append(rs.code, rs.name)
langlist = (list1)

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    titre = models.CharField(max_length=150)
    keywords = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.titre

class SettingLang(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    lang = models.CharField(max_length=50, choices=langlist)
    titre = models.CharField(max_length=150)
    keyword = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.titre

class ContactMessage(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True,max_length=150)
    email = models.EmailField(blank=True,max_length=155)
    subject = models.CharField(blank=True,max_length=50)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default='True')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True, max_length=100)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ' Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.name


class Faq(models.Model): #Frequently Ask Question (Question Frequemment Posées)
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    lang = models.CharField(max_length=50, choices=langlist, blank=True, null=True)
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=50, choices=STATUS)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question-Reponse'
        verbose_name_plural = 'Question-Frequamment-Posées'

    def __str__(self):
        return self.question



    
