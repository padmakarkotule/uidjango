from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from django.contrib.auth import authenticate
from .form import UserForm
import json

# Create your views here.

def homepage(request):
    jwt_toke = {'uid': "paddy", 'gid': "staff", 'token': 'dskjeds@3dslklkf'}
    L = [10, 20.3, "test", 'harshal@test.com', ([25,36],222),('abc', 30, "Ajinath")]
    T = ('touple', 12)
    jwt_token = {'jwt_token':jwt_toke, 'data': L, 'T':T}
    return render(request, 'ui/home/home.html', {'jwt_token': jwt_token})


class auth_login(APIView):

    def post(self, request, format=None):
        form = UserForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print("---", username, password)
            user = authenticate(request, username=username, password=password)
            print("data type", type(user))
            #uid = json.dumps(user)
            payload = {'log_message':"Authentication Successful.", 'user':username}
            if user is not None and user.is_active:
                #return Response({'log_message':"Authentication Successful.", 'user':user}, status=status.HTTP_200_OK)
                return Response(payload, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Your username and password didn't match. Please try again."},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": form.errors.as_json()}, status=400)


""" 
            # user.is.authenticated method only check whether system has correct username and it's password.
            # It doesn't provide session.  So to get session which returns request.user value, we neet to use
            # login method.
            if user.is_authenticated:
                print("User authenticated succfully, --", user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"error": "username and password didn't match. Please try again."},
                                status=status.HTTP_404_NOT_FOUND)


           
            jwt_token = {'uid': username, 'authenticated': True, 'token': 'Sampletoekn'}
            if user is not None and user.is_active:
                # if user.is_active: # if all ok login using default fuction
                login(request, user)
                return Response(jwt_token, status=status.HTTP_200_OK)  # return response and user credentials
            else:
                return Response({"error": "Your username and password didn't match. Please try again."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": form.errors.as_json()}, status=400)
    
    
        # Without using form. It uses request.data to get data of each field.
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response('Username and password are not provided--', status=status.HTTP_404_NOT_FOUND)

        data = {
            'username': username,
            'password': password,
        }


        user = authenticate(request, username=username, password=password)

        print("---print user--",user)
        #jwt_token = "SampleToken"
        jwt_token = {'uid':username, 'authenticated':True, 'token':'Sampletoekn'}
        if user is not None and user.is_active:
            # if user.is_active:      # if all ok login using default fuction
            login(request, user)
            return Response(jwt_token, status=status.HTTP_200_OK)  # return response and user credentials
        else:
            return Response({"error": "Your username and password didn't match. Please try again."}, status=status.HTTP_404_NOT_FOUND)
"""

