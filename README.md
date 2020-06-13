# CHARGEN
Kimlikler üretmek için oluşturulan bir modül.

## Örnek Uygulama
```python
from chargen import *

text = "İsim: {}\nSoyisim: {}\nTCKN: {}\nDoğum Tarihi: {}".format(genFirstName(), genLastName(), genTCKN(), genDate(1960, 2010).format('dd.mm.yyyy'))
print(text)
```

## Fonksiyonlar
- genTCKN() : T. C. kimlik numarası üretir.
- genFirstName() : İsim üretir.
- genLastName() : Soyisim üretir.
- genFullName() : İsim ve soyisim üretir.
- genDate(minYear, maxYear) : Belirttiğiniz yıllar arasında tarih üretir. Date objesi döndürür.
