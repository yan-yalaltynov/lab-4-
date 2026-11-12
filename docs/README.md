## Общее описание решения:
Эта библиотека написана для вычесления периметра и площади фигур.

## Описание каждой функции с примерами вызова:

### circle.py:
Содержит функции `area(r)` и `perimeter(r)`, которые соответсвенно возвращают площадь и периметр круга, где `r` - радиус круга.

### rectangle.py:
Содержит функции `area(a, b)` и `perimeter(a, b)`, которые соответсвенно возвращают площадь и периметр прямоугольника , где `a` и `b` - стороны прямоугольника.

### square.py:
Содержит функции `area(a)` и `perimeter(a)`, которые соответсвенно возвращают площадь и периметр квадрата, где `a` - сторона квадрата.

### triangle.py:
Содержит функции `area(a, h)` и `perimeter(a, b, c)`, которые соответсвенно возвращают площадь и периметр треугольника, где `a`, `b` и `c` - стороны треугольника, а `h` - его высота.

### Примеры вызова:
```python
circle.area (1)
circle. perimeter (1)
```

```python
rectangle.area (1, 2)
rectangle.perimeter (1, 2)
```

```python
square. area (1)
square. perimeter (1)
```

```python
triangle.area (1, 2)
triangle perimeter (1, 2, 3)
```

## История изменения проекта с хешами комитов:
- b65f8fd (HEAD -> new_features_528620) добавил описание к фун кциям в rectangle.py
- bfda9ae добавил описание к фун кциям в circle.py
- 254d7f8 добавил описание к фун кциям в triangle.py
- efff0dd добавил описание к функциям в square.py
- 84e74de ошибка в def perimetr в triangle.py была исправлена
- de845ce был добавлен новый файл triangle.py
- da0a023 был добавлен новый фай rectangle.py
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- 8ba9aeb L-03: Circle and square added