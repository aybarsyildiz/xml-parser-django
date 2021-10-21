from allauth import socialaccount
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
import xml.etree.ElementTree as elementTree
from urllib.request import urlopen
from .forms import XMLForm
from django.core.mail import send_mail
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from .models import XMLmodel
import lxml.etree as ET

def xml_parser(xml_url):
    try:
        var_url = urlopen(xml_url)
        xmldoc = elementTree.parse(var_url)
    except elementTree.ParseError:
        return False
    return xmldoc


def change_word_from_xml(unparsed_xml):
    banned_word = 'Shade'
    replacement = 'aybars'
    root = ET.fromstring(unparsed_xml)

    for item in root.xpath('//*[. = "%s"]' % banned_word):
        item.text = item.text.replace(banned_word,replacement)
    
    return ET.tostring(root)



def download_xml_file(request):
    if request.method == 'POST':
        form = XMLForm(request.POST)
    
        if form.is_valid():
            user_mail_adress = request.user.email
            cleaned_xml_data = form.cleaned_data['xml_link']
            print(cleaned_xml_data)
            parsed_xml = xml_parser(cleaned_xml_data)
            parsed_xml_root = parsed_xml.getroot()
            if(parsed_xml != False):
                xml_str = elementTree.tostring(parsed_xml_root,encoding='unicode')
                XMLmodel.objects.create(email_of_user=request.user.email,XMLlist=xml_str)
                changed_xml = change_word_from_xml(xml_str)
                send_mail(
                    'Changed XML',
                    'All your Shade light attributed plants changed to aybars.',
                    's.aybars.yildiz@gmail.com',
                    [user_mail_adress],
                    fail_silently=False,
                )
                

                pass
            else:
                
                send_mail(
                    'XML Error',
                    'The XML file that you sent was unable to parse, please check if your XML file is accurate',
                    's.aybars.yildiz@gmail.com',
                    [user_mail_adress],
                    fail_silently=False,
                )
                

            print (form.cleaned_data['xml_link'])
            return HttpResponseRedirect('/')
    
    else:
        form = XMLForm()
    
    return render(request,'index.html', {'form': form})

    


