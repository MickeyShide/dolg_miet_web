$(document).ready(function(){
  $(function(){
    $('form').validate({
      rules: {
        login_input: {
          required: true,
          minlength: 2
        },
        password_input: {
          required: true,
          minlength: 6
        }
      },
      messages: {
        login_input: {
          required: "Поле 'Логин' обязательно к заполнению",
          minlength: "Введите не менее 2-х символов в поле 'Логин'"
        },
        password_input: {
          required: "Поле 'Пароль' обязательно к заполнению",
          minlength: "Введите не менее 6-х символов в поле 'Пароль'"  
        }
      }
    });
  });
})