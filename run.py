import random
from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.route("/")
def template_test():
    list_of_quotes = [
        "Logic will get you from A to B. Imagination will take you everywhere."
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it, \
            so simple that there are obviously no deficiencies and the other is to make \
            it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]

    random_index = random.randrange(0, len(list_of_quotes))
    quote_to_display = list_of_quotes[random_index]

    return render_template(
        "index.html",
        quote_to_display=quote_to_display,
        repo_link="https://github.com/johantannh/simple-web",
        image_name="nyanko.png",
        image_size_in_pct=[75, 75]
    )


if __name__ == '__main__':
    app.run()
