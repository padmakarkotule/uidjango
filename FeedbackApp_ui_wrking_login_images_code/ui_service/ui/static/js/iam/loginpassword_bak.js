        	function cript(){
				var  password = $('#password').val();
				var encodedpassword = btoa(password);
                console.log(encodedpassword);
                $('#password').val(encodedpassword);
                  var  username = $('#username').val();
                var encodedusername = btoa(username);
                console.log(encodedusername);
                $('#username2').val(encodedusername);

				}
			function cript1(){

				}

        function user_login(){
            $('#user_login').submit(function(e) {
                e.preventDefault();
                var formData = new FormData(this);
                                for (var value of formData.keys()) {
                  console.log(value);
                }
                   for (var value of formData.values()) {
                     console.log(value);
                }
                console.log(formData);
                $.ajax({
                    "url": "http://feedback-service:8001/user/login/",
                    "dataType": "json",
                    "type": "POST",
                    "data": formData,
                    "cache": false,
                    "processData": false,
                    "contentType":false,
                    "success": function (data) {
                        alert(" User login successfully ");
                        window.location.assign("{% url 'home' %}");
                    },
                    "error": function(data) {
                        alert("Invalid username or password");
                        window.location.assign("{% url 'login' %}");
                    },
                });
            });
        }