- Вставьте свой sentry token в файл sentry_config.py.
- Зарегестрируйтесь на heroku.
- Клонируйте этот репозиторий на свой компьютер.
- Создайте новый репозиторий под проект на github.
- В терминале из директории с сервером выполните команду heroku login и залогиньтесь на heroku в браузере.
- Выполните команду heroku create. Это создаст приложение heroku.
- Загрузите сервер на heroky командой: git push heroku master
- установите переменную командой: heroku config:set APP_LOCATION=heroku
- масштабируйте процесс на heroku:  heroku ps:scale web=1
- Если все ok то командой heroku open в терминале можете открыть приложение в браузере и потестить регистрацию ошибок в своем аккаунте sentry.io
Мое приложение на heroku:  https://calm-beach-75421.herokuapp.com/

