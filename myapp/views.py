from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from IPython import embed

from django.contrib.auth.decorators import login_required


from myapp.forms import MemberForm

from myapp.models import Member
# Create your views here.


def member(request,member_id):
    member = Member.objects.get(id=member_id)

    response = render(request,'myapp/member_detail.html',{
        'member':member
        })
    return response

def member_list(request):
    members = Member.objects.all()

    response=render(request,'myapp/member_list.html',{
            'members':members
    })
    return response

@login_required
def member_update(request,member_id):
    member = Member.objects.get(id=member_id)
    if request.method=="POST":
        form = MemberForm(request.POST, instance=member) # populates the form fields with POST data
        if member.this_user!=request.user:
            return HttpResponseRedirect(reverse('member_profile',kwargs={'member_id':member_id}))
            
        elif form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_profile',kwargs={'member_id':member_id}))
        
        else:
            return HttpResponseRedirect('/')

    form = MemberForm(instance=member)
    return render(request,'myapp/member_update.html',{
            'form':form
        })
