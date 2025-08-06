from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_password():
    try:
        length = int(request.form.get("length"))

        if length < 4:
            return render_template(
                "index.html", error="رمز عبور باید حداقل 4 کاراکتر باشد."
            )

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols),
        ]

        all_chars = lower + upper + digits + symbols
        for _ in range(length - 4):
            password.append(random.choice(all_chars))

        random.shuffle(password)
        final_password = "".join(password)

        return render_template("index.html", password=final_password, length=length)

    except (ValueError, TypeError):
        return render_template("index.html", error="لطفاً یک عدد معتبر وارد کنید.")


if __name__ == "__main__":
    app.run(debug=True)
