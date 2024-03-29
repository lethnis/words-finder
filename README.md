# Искатор А-42 🧐 <a href=https://streamlit.io/>Made with<img src=https://github.com/lethnis/rembg-and-crop/assets/88483002/466e152a-9a43-48a3-8e4a-a4b767431ed2 width=180></a>
# <a href=https://words-finder.streamlit.app/>Попробовать онлайн</a>
### Программа для поиска слов среди русских существительных.  
<a href=https://github.com/Harrix/Russian-Nouns/blob/main/dist/russian_nouns.txt>Источник слов</a>


## Как использовать
Доступно 5 фильтров.
1. Длина слова.
2. Известные буквы.
3. Неизвестные буквы.
4. Буквы, которые есть в слове и места которых известны.
5. Буквы, которые есть в слове и известно в каких местах этих букв нет.  

Пример. Я знаю, что слово состоит из 5 букв. Я знаю, что в нём есть буквы 'т' и 'в'. Я знаю, что букв 'праодхз' в слове нет. Я знаю, что буква 'т' на 5ом месте, а буква 'в' не на 1ом месте. Ввожу информацию.  
<img src=https://github.com/lethnis/words-finder/assets/88483002/b2ca5542-8cbf-438d-8c88-a863d2fc9b8f width=500>  
Нажимаю Поиск и получаю список возможных слов.  
<img src=https://github.com/lethnis/words-finder/assets/88483002/8ff55f35-b173-411b-a022-5c2b4017f977 width=200>  


## Как установить локально

Создать копию репозитория любым удобным способом, например:  
`git clone https://github.com/lethnis/words-finder.git`  

Создать виртуальную среду (использовался `python 3.11.8`)  
`python -m venv .venv`  

Установить streamlit  
`pip install streamlit`  

Запустить программу  
`streamlit run main.py`
