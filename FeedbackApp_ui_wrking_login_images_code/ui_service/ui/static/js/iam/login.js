        $(document).ready(function(){
            height = $(window).height();
            $(".dboard").css("height", height);

            window.addEventListener("resize", function myFunction() {
                height = $(window).height();
                $(".backdiv").css("height", height-50);
                $(".dboard").css("height", height);
            });
        });

        {% block script %}
           //Add Catalog
    function add_catalog(){
        $("#add_catalog").submit(function(e) {

            var formData = new FormData(this);
            var add_url = "{{ add_url }}";
            /*for (var value of formData.values()) {
                console.log(value);
            }*/
            //console.log(formData);
            $.ajax({
                "url": add_url,
                "dataType": "json",
                "type": "POST",
                "data": formData,
                "cache": false,
                "processData": false,
                "contentType":false,
                "success": function (data) {
                    alert(" Resistered successfully ");
                    window.location.assign("{% url 'login' %}");
                },
            });
        });
    }
        {% endblock script %}