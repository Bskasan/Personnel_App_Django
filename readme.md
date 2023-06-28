# PERSONNEL APP - DJANGO

* Deparment ve Personnel tablolarımız olacak bunları birbirlerine bağlayacağız. Her deparmentın altında kendisine ait personel olacak.
* Staff olan personel yeni personel listeye ekleyebilecek, update edebilecek.(staff dan kasıt yetkili olan bunu farklı cheff de diyebilirsiniz. Staff ismi django user modelinde bulunan is_staff dan geliyor )
* Dinamik url ile url de gelen isteğe göre response değişecek. Yani departmenlara ait personeli listelemek istediğimizde bunu tek bir url üzerinden yapacağız. Swagger da örneği var.
* Staff olmayanlar sadece listeleyebiliecek.
* Personeli silme yetkisi sadece superuserlarda olacak.
* Token authentication kullanacağız. Kullanıcı logout olduğunda tokeni sileceğiz.

# STEPS:

- python -m venv env
- source env/Scripts/activate
- pip install djangorestframework
- pip freeze > requirements.txt
