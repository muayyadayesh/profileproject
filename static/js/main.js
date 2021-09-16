let main = (function () {
    let selectMobile = function () {
            var input = document.querySelector("#tit_phone"),
                errorMsg = document.querySelector("#phone-error-msg"),
                errorMap = ["Invalid number", "Invalid country code", "Too short", "Too long", "Invalid number"],
                form = $("#new_user_form");
            var userTit = window.intlTelInput(input, {
                separateDialCode:true,
                nationalMode: true,
                // onlyCountries: ["sa", "ae"],
                utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@17.0.3/build/js/utils.js",
            });
            userTit.setCountry("ps");
            var reset = function () {
                errorMsg.innerHTML = "";
                errorMsg.classList.add("hide");
            };
            var numberVal
            var fillNumber = function () {
                numberVal = userTit.getNumber();
                document.getElementById("user_phone_val").value = numberVal;
                console.log(document.getElementById("user_phone_val").value)
            }
            input.addEventListener('blur', function () {
                reset();
                if (input.value.trim()) {
                    if (userTit.isValidNumber()) {
                        console.log('valid')
                    } else {
                        var errorCode = userTit.getValidationError();
                        errorMsg.innerHTML = errorMap[errorCode];
                        errorMsg.classList.remove("hide");
                    }
                }

            });
            input.addEventListener('change', reset);
            input.addEventListener('keyup', reset);
            input.addEventListener('input', fillNumber);
            form.parsley().on('form:submit', function (e) {
                return !!userTit.isValidNumber();
            })
        }

    return {
        init: function () {
            selectMobile();
        },
    };
})();

$(document).ready(function () {
    main.init();
});


function upload_img(input) {
  if (input.files && input.files[0]) {
    var src = URL.createObjectURL(input.files[0])
    $('#img_id').attr('src', src)
  }
}
