# PERSONNEL APP - DJANGO

* Deparment ve Personnel tablolarımız olacak bunları birbirlerine bağlayacağız. Her deparmentın altında kendisine ait personel olacak.
* Staff olan personel yeni personel listeye ekleyebilecek, update edebilecek.(staff dan kasıt yetkili olan bunu farklı cheff de diyebilirsiniz. Staff ismi django user modelinde bulunan is_staff dan geliyor )
* Dinamik url ile url de gelen isteğe göre response değişecek. Yani departmenlara ait personeli listelemek istediğimizde bunu tek bir url üzerinden yapacağız. Swagger da örneği var.
* Staff olmayanlar sadece listeleyebiliecek.
* Personeli silme yetkisi sadece superuserlarda olacak.
* Token authentication kullanacağız. Kullanıcı logout olduğunda tokeni sileceğiz.

EN;

* We will have Department and Personnel tables, and we will connect them to each other. Each department will have its own personnel.
* Personnel with the role of "Staff" will be able to add and update new personnel to the list. (By "Staff," we mean authorized personnel, which can also be referred to as "chef" in a different context. The term "Staff" comes from the "is_staff" field in the Django user model.)
* The response will change according to the dynamic URL. This means that when we want to list the personnel belonging to departments, we will do it through a single URL. There is an example in Swagger.
* Non-staff members will only be able to list the personnel.
* Only superusers will have the authority to delete personnel.
* We will use token authentication. When a user logs out, we will delete the token.

### STEPS:

- python -m venv env
- source env/Scripts/activate
- pip install djangorestframework
- pip freeze > requirements.txt
- django-admin startproject main .
- Check if it's working or not --> python manage.py runserver
- python manage.py migrate --> to migrate your database
- Create .env and secure your SECRET_KEY by using python-decouple
- Don't forget to make admin.register your models.

--> MODELS -> SERIALIZERS -> VIEWS -> URLS.PY <--

