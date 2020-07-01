# CHARGEN
Kimlikler üretmek için oluşturulan bir modül.

## Örnek Uygulama
```python
from chargen import Date, Char

people = [Char(), Char(), Char()]

string = """
KARAKTER {}
-----------
İsim: {}
Soyisim: {}
T. C. Kimlik Numarası: {}
E-posta Adresi: {}
Doğum Tarihi: {}
İl: {}
İlçe: {}
"""

i = 1
for person in people:
    print(string.format(
        i,
        person.firstname,
        person.lastname,
        person.tckn,
        person.email,
        person.birthdate.format(),
        person.province,
        person.town
    ))
    i += 1
```
