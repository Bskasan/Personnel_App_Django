# PERSONNEL APP - DJANGO

* Deparment ve Personnel tablolarımız olacak bunları birbirlerine bağlayacağız. Her deparmentın altında kendisine ait personel olacak.
* Staff olan personel yeni personel listeye ekleyebilecek, update edebilecek.(staff dan kasıt yetkili olan bunu farklı cheff de diyebilirsiniz. Staff ismi django user modelinde bulunan is_staff dan geliyor )
* Dinamik url ile url de gelen isteğe göre response değişecek. Yani departmenlara ait personeli listelemek istediğimizde bunu tek bir url üzerinden yapacağız. Swagger da örneği var.
* Staff olmayanlar sadece listeleyebiliecek.
* Personeli silme yetkisi sadece superuserlarda olacak.
* Token authentication kullanacağız. Kullanıcı logout olduğunda tokeni sileceğiz.

### STEPS:

- python -m venv env
- source env/Scripts/activate
- pip install djangorestframework
- pip freeze > requirements.txt
- django-admin startproject main .
- Check if it's working or not --> python manage.py runserver
- python manage.py migrate --> to migrate your database
- Create .env and secure your SECRET_KEY by using python-decouple

Create Models;
- Department
    * name
    * user_id
    * created
    * updated
- Personal
    * first_name
    * last_name
    * gender
    * title
    * salary
    * started
    * department_id
    * user_id
    * created
    * updated