### 💻QuerySet API

- gt(greater than)

  ```python
  # Queryset API
  Entry.objects.filter(id__gt=4)
  # SQL
  SELECT * FROM Entry WHERE id > 4;
  ```

- gte(greater than or equal)

  `Entry.objects.filter(id__get=4)` => `SELECT * FROM Entry WHERE id >= 4;`

마찬가지로 미만, 이하는 각각

`Entry.objects.filter(id__lt=4)`

`Entry.objects.filter(id__lte=4)`

로 표기한다.

- in

`Entry.objects.filter(id__in=[1,3,4])`

`Entry.objects.filter(headline__in='abc')` 는 SQL 문으로

`SELECT * FROM Entry WHERE id IN (1,3,4);`

`SELECT * FROM Entry WHERE headline IN ('a','b','c');`

- startswith

`Entry.objects.filter(headline__startswith='Lennon')`

`SELECT ... WHERE headline LIKE 'Lennon%;`

- istartswith(대소문자 구분안함, insensitive)

`Entry.objects.filter(headline__istartswith='Lennon')`

`SELECT ... WHERE headline LIKE 'Lennon%;`

- contains

  ```python
      Entry.objects.
  ```

- range

  ```python
    import datetime
    start_date =
    end_date =
    Entry.objects.filter()

    # SQL
    SELECT ... WHERE pub_date
    BETWEEN '2005-01-01' AND '2005-03-03'
  ```

- 복합 활용

  ```python
    inner_qs = Blog.objects.filter(name__contains = 'Cheddar')
    entries = Entry.objects.filter(blog__in = inner_qs)


  ```

- 활용

  ```python
    Entry.objects.all()[0]

    # SQL
    SELECT ...
    LIMIT 1;

    # 만약에 슬라이싱을 한다면
    Entry.objects.all()[M:N]

    # SQL
    SELECT ...
    LIMIT M OFFSET N;
  ```

  ```python
    Entry.objects.order_by('id')

    SELECT ...
    ORDER BY id;

    Entry.objects.order_by('-id')

    SELECT ...
    ORDER BY id DESC;
  ```

### 💻ORM 확장(1대 N)

```python
class Genre(models.Model):
    name = models.CharField(max_length = 30)

class Artist(models.Model):
    name = models.CharField(max_length = 30)
    debut = models.DateField()

class Album(models.Model):
    name = models.CharField(max_length = 30)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

# 특정 id를 지니는 인스턴스를 get으로 가져와서 Foreign Key로 설정해준다.
genre = Genre.objects.get(id=1)
album.genre = genre
album.artist = Artist.objects.get(id=1)
album.save()

album = Album.objects.get(id = 1) # 앨범 객체를 뜻함
album.artist

# 역참조 (1 => N)
# id가 1인 장르의 모든 앨범은?
g1 = Genre.objects.get(id = 1)
g1.album_set.all()

참조와 역참조의 차이:
앨범입장에서 참조는 직접 참조하고 있는 것이다??? 그래서 직접 쓰면된다.

역참조는 album.name

별도의 설명이 없다면 역참조는 항상 _소문자를 붙인다.

따라서 album_set.all 이 되는 것이다. (앨범의 인스턴스를 모두 조회?)
```

🍯쿼리셋 API를 사용시에 어떤 장점/단점이 있을까?

장점:

1. 유지보수가 편하다. DB 변경 시 Setting.py만 바꿔주면 된다.

단점:
