# Syspets

**A simple django web blog with pet themes.**

Requeriments:

- Install python.
- Create virtual environment. ~> python -m venv "namevenv"
- Install pip. ~> python -m pip install --upgrade pip
- Install dependencies. ~> pip install "package" -> Show requeriments/base.txt
- Create database postgres ~> DB and account user admin
- Migrate models to database. ~> python manage.py makemigrations users adnews registration
- Execute migrations ~> python manage.py migrate
- Create account superuser admin. ~> python manage.py createsuperuser
- Run server. ~> python manage.py runserver 
- Server ~> http://127.0.0.1:8000

Captures:

<table>
  <tr>
    <td><img src="https://github.com/robertogarcor/django-blog/blob/master/syspets_images/Captura_00.PNG width="300" height="300""></td>
    <td><img src="https://github.com/robertogarcor/django-blog/blob/master/syspets_images/Captura_01.PNG width="300" height="300""></td>
  </tr>
  <tr>
    <td><img src="https://github.com/robertogarcor/django-blog/blob/master/syspets_images/Captura_02.PNG width="300" height="300""></td>
    <td><img src="https://github.com/robertogarcor/django-blog/blob/master/syspets_images/Captura_03.PNG width="300" height="300""></td>
  </tr>
</table>

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />Este obra está bajo una <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">licencia de Creative Commons Reconocimiento-NoComercial-SinObraDerivada 4.0 Internacional</a>.
