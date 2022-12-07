from quart import Quart, render_template, request, redirect
from database import get_forms, create_form, delete_form

# Создаём приложение, указываем папку с шаблонами
app = Quart(__name__, template_folder="templates")


# Маршрут для главной страницы
@app.route("/")
async def index():
    # Получаем список форм
    forms, error = get_forms()
    # Если произошла ошибка, выводим её
    if error:
        print(error)
        return await render_template("error.html", error=error.msg)

    # Возвращаем главную страницу с формами
    return await render_template("index.html", forms=forms)


# Маршрут для страницы с формой
@app.route("/newform")
async def newform():
    # Возвращаем страницу с формой
    return await render_template("form.html")


# Маршрут для обработки формы
@app.post("/postform")
async def postForm():
    # Получаем данные из формы
    form = await request.form
    email = form["email"]
    title = form["title"]
    text = form["text"]
    # Создаём форму
    error = create_form(email, title, text)
    # Если произошла ошибка, выводим её
    if error:
        print(error)
        return await render_template("error.html", error=error.msg)

    # Перенаправляем на главную страницу
    return redirect("/")


# Маршрут для удаления формы
@app.route("/removeform/<id>")
async def remove_form(id):
    # Удаляем форму
    error = delete_form(id)
    # Если произошла ошибка, выводим её
    if error:
        print(error)
        return await render_template("error.html", error=error.msg)

    # Перенаправляем на главную страницу
    return redirect("/")


# Запускаем приложение
if __name__ == "__main__":
    # Указываем, что приложение запускается в режиме отладки
    app.run(debug=True)
