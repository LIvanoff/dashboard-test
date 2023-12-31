<a href="https://colab.research.google.com/github/LIvanoff/dashboard-test/blob/master/notebook.ipynb">
<img alt="???" src="https://colab.research.google.com/assets/colab-badge.svg">
</a>

## Установка
Склонировать репозиторий в папку, в путь без пробелов и кириллицы

```shell
git clone https://github.com/LIvanoff/dashboard-test
```

Перейти в папку с проектом
```shell
cd dashboard-test
```

## Запуск приложения

Собрать образ

```shell
docker build . -t dashboard-test 
```

Запустить контейнер
```shell
docker run -p 8501:8501 dashboard-test 
```

После запуска перейти по ссылке http://127.0.0.1:8501/



## Colab

Jupyter Notebook с проведённым исследованием доступен по следующим ссылкам:
[colab](https://colab.research.google.com/github/LIvanoff/dashboard-test/blob/master/notebook.ipynb)
[github](https://github.com/LIvanoff/dashboard-test/blob/master/notebook.ipynb) 


## Требования
<li> Python 3.9+
<li> streamlit==1.29.0
<li> plotly==5.18.0
<li> pandas==2.1.4
<li> matplotlib==3.8.2
