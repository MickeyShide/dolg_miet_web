$(document).ready(function(){
  $(function(){
    $('form').validate({
      rules: {
        login_input: {
          required: true,
          minlength: 2
        },
        email_input: {
          required: true,
          email: true
        },
        password_input: {
          required: true,
          minlength: 6
        },
        password_input_confirm: {
          required: true,
          minlength: 6,
          equalTo: "input[name=password_input]"
        }
      },
      messages: {
        login_input: {
          required: "Поле 'Логин' обязательно к заполнению",
          minlength: "Введите не менее 2-х символов в поле 'Логин'"
        },
        email_input: {
          required: "Поле 'E-mail' обязательно к заполнению",
          email: "Введённый e-mail не соответствует формату name@domain.com"
        },
        password_input: {
          required: "Поле 'Пароль' обязательно к заполнению",
          minlength: "Введите не менее 6-х символов в поле 'Пароль'"  
        },
        password_input_confirm: {
          required: "Поле 'Подтвердите пароль' обязательно к заполнению",
          minlength: "Введите не менее 6-х символов в поле 'Пароль'"
        }
      }
    });
  });
})