from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import LoginForm
import json
from django.contrib import messages
#from django import template
import os.path
from django.conf import settings

# Create your views here.


#def get_header(request):
#    try:
#        jwt_token = request.session['jwt_token']
#        header = {'token': jwt_token}
#        return header
#    except:
#        redirect('login')

#register = template.Library()


def homepage(request):
    jwt_toke = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
    L = [10, 20.3, "test", 'harshal@test.com', ([25,36],222),('abc', 30)]
    T = ('touple', 12)
    jwt_token = {'jwt_token':jwt_toke, 'data': L, 'T':T}
    return render(request, 'ui/home/home.html', {'jwt_token': jwt_token})


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            # query_json = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
            # jwt_token = json.dumps(query_json)

            # Get logged in user i.e. uid
            uid = form.cleaned_data['username']

            #@register.filter
            def get_profile_image(uid):
                # User images path
                STATIC_ROOT = settings.STATIC_ROOT
                path_sep = "\\" + 'images' + "\\" + 'uid_{}'.format(uid) + "\\"
                path_sep1 = "\\" + 'images' + "\\" + 'images_product' + "\\"
                #print("ssss", STATIC_ROOT)
                folder_path = STATIC_ROOT + path_sep
                file = folder_path + 'uid_{}.jpg'.format(uid)
                #default_file = folder_path + 'blank-profile-picture.png'
                if os.path.exists(file):
                    image_path = path_sep + 'uid_{}.jpg'.format(uid)
                    #image_path = image_folder + 'uid_{}.jpg'.format(uid)
                    return image_path
                else:
                    default_image_path = path_sep1 + 'blank-profile-picture.png'
                    return default_image_path

            profile_image = get_profile_image(uid)

            # uid = 'paddy'
            gid = 'staff'
            token = get_token()
            message = 'Login Success !'

            payload = {'uid': uid, 'gid': gid, 'token': token, 'message': message, 'profile_image': profile_image}
            # print(payload)

            jwt_token = payload['token']
            # print(jwt_token)
            request.session['jwt_token'] = payload['token']
            request.session['uid'] = payload['uid']
            request.session['profile_image'] = payload['profile_image']
            request.session['gid'] = payload['gid']
            request.session['message'] = payload['message']

            if jwt_token:
                #return render(request, 'ui/home/home.html', {'message': payload, 'jwt_token': jwt_token})
                return redirect('enquiry')
            else:
                return render(request,'500.html', {'error' : "System error, token not generated."})
    else:
        return render(request, 'ui/iam/loginform.html', {'form': form})


def user_logout(request):
    try:
        del request.session['jwt_token']
        del request.session['uid']
        del request.session['gid']
        del request.session['profile_image']
        del request.session['message']
        #del request.session['token']
        #del request.session['uid']
        #del request.session['gid']

    except:
        pass
    #return HttpResponse("<strong>You are logged out.</strong>")
    return render(request, 'ui/iam/logout.html')


def user_signup(request):
    return render(request, 'ui/iam/signup.html')


#def login_form(request):
#    pass
#    form = LoginForm()
#    return render(request, 'ui/iam/loginform.html', {'form': form})

def enquiry(request):
    try:
        #header = get_header(request)
        #jwt_token = header['token']
        jwt_token = request.session['jwt_token']
    except:
        return redirect('login')

    if jwt_token is not None:
        pp = request.session['profile_image']
        data = {'fname': "Padmakar", 'lname':'Kotule', 'gid': "staff", 'token':jwt_token, 'profile_image':pp}
        return render(request, 'ui/enquiry/enquiry.html', {'data': data})


def get_token():
    jwt_token = "1234@ddds"
    return jwt_token
