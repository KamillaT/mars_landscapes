import os

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def ship():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.",
                      "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.gif" alt="Жди нас, Марс!">
                    <h1>Вот она какая, красная планета</h1>
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1><span style="color: #ff0000;"><strong>Жди нас, Марс!</strong></span></h1>
                    <img src="/static/img/mars.gif">
                    <div class="alert alert-primary" role="alert" style="background-color: #ff9999; color: #aa0000;">
                     Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #99ff99; color: #00aa00;">
                     Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #9999ff; color: #0000aa;">
                     Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #ffff99; color: #aaaa00;">
                     И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert" style="background-color: #ff99ff;color: #aa00aa;">
                     Присоединяйся!
                    </div>

                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Анкента предедента </h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">

                                    <input type="fullname" class="form-control" id="fullname" placeholder="Фамилия" name="fullname">
                                    <input type="name" class="form-control" id="name" placeholder="Имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас Оброзавание?</label>
                                        <select class="form-control" id="educationSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Общее среднее</option>
                                          <option>Профессионально-технологическое</option>
                                          <option>Средне специальное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <p>Какие у вас профессии?</p>
                                    <p><input type="checkbox" name="a" value="Инженер-исследователь"> Инженер-исследователь</p>
                                    <p><input type="checkbox" name="a" value="Пилот" > Пилот</p>
                                    <p><input type="checkbox" name="a" value="Строитель" > Строитель</p>
                                    <p><input type="checkbox" name="a" value="Врач"> Врач</p>
                                    <p><input type="checkbox" name="a" value="Инженер по терраформированию"> Инженер по терраформированию</p>
                                    <p><input type="checkbox" name="a" value="Астрогеолог"> Астрогеолог</p>
                                    <p><input type="checkbox" name="a" value="Климатолог"> Климатолог</p>

                                    <div class="form-group">
                                        <label for="about">Почему вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['a'])
        print(request.form['email'])
        print(request.form['name'])
        print(request.form['fullname'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewpoint" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-light" role="alert">
                        Эта планета близка к Земле;
                    </div>
                    <div class="alert alert-success" role="alert">
                        На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-dark" role="alert">
                        На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning" role="alert">
                        На ней есть небольшое мганитное поле;
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Наконец, она просто красива!
                    </div>
                  </body>
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewpoint" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {str(level)} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                        составляет {str(rating)}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():
    if request.method == "GET":
        return f"""<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="middle_text">Загрузка фотографии</h1>
                            <h2 class="middle_text">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>                                
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>"""
    elif request.method == "POST":
        file = request.files["file"]
        pth = os.path.join("static", "img", file.filename)
        file.save(pth)
        return f"""<!doctype html>
                            <html lang="ru">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 class="middle_text">Загрузка фотографии</h1>
                                <h2 class="middle_text">для участия в миссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>                                
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                            <img src="{pth}" alt="no">
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>"""


@app.route("/carousel")
def carousel():
    return f"""<!doctype html>
                <html>
                    <head>
                        <title>Пейзажи Марса</title>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="icon" href="data:;base64,=">
                        <script src="/static/js/script.js"></script>
                        <link rel="stylesheet" href="/static/css/style.css">
                    </head>
                        <h1 align="center">Пейзажи Марса</h1>
                        <body>
                            <div class="slideshow-container">
                            <div class="mySlides fade" style="display: block;">
                              <div class="numbertext">1 / 3</div>
                              <img src="/static/img/img1.jpg" style="width:100% ">
                            </div>
                            
                            <div class="mySlides fade">
                              <div class="numbertext">2 / 3</div>
                              <img src="/static/img/img2.jpg" style="width:100%">
                            </div>
                            
                            <div class="mySlides fade">
                              <div class="numbertext">3 / 3</div>
                              <img src="/static/img/img3.jpg" style="width:100%">
                            </div>
                            
                            <a class="prev" onclick="plusSlides(-1)">❮</a>
                            <a class="next" onclick="plusSlides(1)">❯</a>
                            
                            </div>
                            <br>
                            
                            <div style="text-align:center">
                              <span class="dot" onclick="currentSlide(1)"></span> 
                              <span class="dot" onclick="currentSlide(2)"></span> 
                              <span class="dot" onclick="currentSlide(3)"></span> 
                            </div>
                    </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
