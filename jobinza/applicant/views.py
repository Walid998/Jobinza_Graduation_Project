from django.shortcuts import render , redirect
from company.models import CreatePost, Match_Results
from applicant.models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from company.views import skillsToList , update_status
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from applicant.forms import uploadForm ,contactform
from applicant.models import contacts,Resume_Parsed
<<<<<<< HEAD
from applicant.forms import contactform
from applicant.forms import editprofileForm
=======
from applicant.utils import Comparison 
>>>>>>> def80024541f2bfe469e71677376c240e5199560
from django.conf import settings
from pyresparser import ResumeParser
from django.contrib import messages
import os
<<<<<<< HEAD
import sys
=======
from django.db.models import Q
from django.core.paginator import Paginator
>>>>>>> def80024541f2bfe469e71677376c240e5199560
# Create your views here.


@login_required(login_url='login')
def job_details(request , job_id):
    user = request.user
    job = CreatePost.objects.get(id=job_id)
    isNewUser = False
    prof = ''
    isApplied = False
    try:
        prof =Profile.objects.get(author = user.id)
    except:
        isNewUser = True

    try:
        res = Match_Results.objects.get(author = user.id,job_id=job_id)
        if res.status == 'pending':
            isApplied = True
    except:
        print('not apply yet',user.id)

    context = {
        'skills':skillsToList(job.skills),
        'job': job,
        'isapplied':isApplied,
        'newuser': isNewUser
    }

    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['cv']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            
            try:
                prof =Profile.objects.get(author = user.id)
                prof.resume = uploaded_file
                prof.save()
            except:
                prof = Profile()
                prof.author = user
                prof.resume = uploaded_file
                prof.save()
            parser_r(uploaded_file,uploaded_file.name,user)
            fs.delete(uploaded_file.name)
            isNewUser=False
            return render(request,'applicant/job_details.html',{'skills':skillsToList(job.skills),'job': job,'isapplied':isApplied,'newuser': isNewUser,'applynow':True} )
        except:
            prof = Profile.objects.get(author = user) # profile details
            pars_obj = Resume_Parsed.objects.get(usrname = user)
            if isApplied == False:
                match = Match_Results()
                match.resume = prof.resume
                match.author = user
                match.job_id = job.id
                reslt =Comparison(skillsToList(job.skills), skillsToList(pars_obj.skills))
                match.skills_rslt = reslt
                match.status = 'pending'
                match.save()
                return render(request,'applicant/job_details.html',{'skills':skillsToList(job.skills),'job': job,'isapplied':True} )
            else:
                return render(request,'applicant/job_details.html', context)
            
            
    return render(request,'applicant/job_details.html', context)

def home(request):   
    update_status()
    listusers = User.objects.all()
    listpost=CreatePost.objects.all()
    paginator = Paginator(listpost,2)
    page = request.GET.get('page')
    listpost = paginator.get_page(page)
    return render(request,'applicant/guest.html' , {'posts':listpost , 'users': listusers})

def contact(request):
    if request.method =='POST':
            post=contacts()
            post.fullname=request.POST.get('fullname')
            post.email=request.POST.get('email')
            post.phone=request.POST.get('phone')
            post.message=request.POST.get('message')
            post.save()
            
    
    return render(request,'applicant/contact.html')



@login_required(login_url='login')
def profile_info(request,user_name):
    user_info = User.objects.get(username=user_name)
    pk = User.objects.get(username=user_name).pk
    try:
        p_info = Profile.objects.get(author = pk)
        return render(request,'applicant/profile.html', {'result': user_info , 'info':p_info } )
    except:
        return render(request,'applicant/profile.html', {'result': user_info , 'info':'' })


@login_required(login_url='login')
def editProfile (request):    
    if request.method == 'POST':
        uname = request.user
        auth = User.objects.get(username=uname)
        pk = User.objects.get(username=uname).pk
        try:
            pinfo = Profile.objects.get(author = pk)
            print("***********<<<<<<< pinfo has data >>>>>>>***********")
            form = editprofileForm(request.POST ,instance = pinfo)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                #messages.success(request,f'Job has been updated successfully !!')
                return redirect(f'/applicant/profile/{request.user}')
        except:
            form = editprofileForm(request.POST , request.FILES)
            if form.is_valid():
                print("<<< pinfo has no data >>>")
                inst = Profile()
                inst.image = form.cleaned_data.get('image')
                print ('**************************',inst.image)
                inst.phonenumber = form.cleaned_data.get('phonenumber')
                inst.address = form.cleaned_data.get('address')
                inst.author = auth
                inst.save()
                return redirect(f'/applicant/profile/{request.user}')

@login_required(login_url='login')
def list_applicant(request):
    update_status()
    listusers = User.objects.all()
    listpost=CreatePost.objects.all()
    paginator = Paginator(listpost,5)
    page = request.GET.get('page')
    listpost = paginator.get_page(page)
    return render(request,'applicant/home.html', {'posts' : listpost , 'users': listusers} )

#####################################
########____UPLOAD RESUME____########
def parser_r(resume,resume_name,user):
    pars=Resume_Parsed()
    parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume_name))
    data = parser.get_extracted_data()
    pars.usrname = user
    pars.resume = resume
    pars.name = data.get('name')
    pars.email              = data.get('email')
    pars.mobile_number      = data.get('mobile_number')
    if data.get('degree') is not None:
        pars.education      = ', '.join(data.get('degree'))
    else:
        pars.education      = None
    pars.company_names      = data.get('company_names')
    pars.college_name       = data.get('college_name')
    pars.designation        = data.get('designation')
    pars.total_experience   = data.get('total_experience')
    if data.get('skills') is not None:
        pars.skills         = ', '.join(data.get('skills'))
    else:
        pars.skills         = None
    if data.get('experience') is not None:
        pars.experience     = ', '.join(data.get('experience'))
    else:
        pars.experience     = None
    pars.save()

###################search################################

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        print('>>>>>>>>>>>>>>>>>>>>> ', srch)
        if srch:
            match = CreatePost.objects.filter(
                Q(jobtitle__icontains=srch)|Q(city__icontains=srch)
            )
            if match:
                return render(request,'applicant/search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'applicant/search.html')