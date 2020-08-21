# Import libraries
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime
from helpers import apology, login_required, lookup, usd, password_check
from credit import card

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks_ = db.execute("SELECT id, user_id, symbol, name, SUM(q_shares) as q_shares FROM stocks WHERE user_id=:id_user GROUP BY user_id, symbol, name",
                        id_user=session["user_id"])
    current_price = {}
    total_share = {}
    sum_total = 0
    stocks = []

    # Get stocks and append to list
    for y in range(len(stocks_)):
        if stocks_[y]["q_shares"] > 0:
            stocks.append(stocks_[y])

    # Get Info
    for x in range(len(stocks)):
        if stocks[x]["q_shares"] > 0:
            share_x = lookup(stocks[x]["symbol"])
            total = share_x["price"] * stocks[x]["q_shares"]
            current_price[stocks[x]["symbol"]] = usd(share_x["price"])
            total_share[stocks[x]["symbol"]] = usd(total)
            sum_total = sum_total + total

    # Query db
    cash_amount = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    sum_total = sum_total + cash_amount[0]["cash"]

    # Render template
    return render_template('index.html', cash=usd(cash_amount[0]["cash"]), stocks=stocks,
                            current_price=current_price, total_share=total_share, sum_total=usd(sum_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # Check if GET render template
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Set errors
        if not request.form.get("symbol"):
            return apology("MISSING SYMBOL", 400)
        elif not lookup(str(request.form.get("symbol"))):
            return apology("INVALID SYMBOL", 400)
        elif not request.form.get("shares") or int(request.form.get("shares")) <= 0:
            return apology("MISSING SHARES", 400)
        # Check symbols, shares, prices
        symbol_input = str(request.form.get("symbol"))
        shares_input = int(request.form.get("shares"))
        symbol = lookup(symbol_input)
        price = symbol["price"]
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # Query db
        cash_amount = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = cash_amount[0]["cash"]
        cash_updated = cash - (price * shares_input)
        # Not enough money error
        if (price * shares_input) > cash:
            return apology("NOT ENOUGH CASH", 400)
        # Insert new buy stock in db
        else:
            new_share = db.execute("INSERT INTO stocks (user_id,symbol,name,q_shares,price_buy,date) VALUES(:user_id,:symbol,:name,:q_shares,:price_buy,:date)",
                          user_id=session["user_id"], symbol=symbol["symbol"], name=symbol["name"],
                          q_shares=shares_input,price_buy=symbol["price"],date=dt_string)
            # Update cash in db
            update_cash = db.execute("UPDATE users SET cash =:cash WHERE id=:user_id", cash=cash_updated, user_id=session["user_id"])
        return redirect("/")

@app.route("/change", methods=["GET", "POST"])
@login_required
def password():
    # Change password template
    if request.method == "GET":
        return render_template("change.html")
    # Check username in db
    else:
        rows = db.execute("SELECT * FROM users WHERE id = :username",
                              username=session["user_id"])
        # Error
        if not request.form.get("password"):
                return apology("MISSING PASSWORD", 400)
        elif not request.form.get("password2"):
            return apology("MISSING PASSWORD", 400)
        elif request.form.get("password") != request.form.get("password2"):
            return apology("PASSWORD DON'T MATCH", 400)
        elif len(rows) != 1:
            return apology("username error", 400)
        elif check_password_hash(rows[0]["hash"], request.form.get("password2")):
            return apology("WRITE NEW PASSWORD", 400)
        # Update password
        update_pass = db.execute("UPDATE users SET hash =:hash WHERE id=:user_id", hash=generate_password_hash(request.form.get("password")), user_id=session["user_id"])
        # Render successful password update
        return apology("password change succefully", 400)

@app.route("/add_money", methods=["GET", "POST"])
@login_required
def add_cash():
    # Render cash update
    if request.method == "GET":
        return render_template("cash.html")
    # Error
    else:
        if not request.form.get("amount"):
                return apology("Write an Amount", 400)
        elif not request.form.get("card"):
            return apology("Write Card Number", 400)
        elif not card(request.form.get("card")):
            return apology("Not valid Card Number", 400)
        else:
            # Select current ccash
            cash_amount = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
            old_cash = cash_amount[0]["cash"]
            new_cash = int(request.form.get("amount"))
            cash_updated = old_cash + new_cash
            # Update cash
            update_cash = db.execute("UPDATE users SET cash =:cash WHERE id=:user_id", cash=cash_updated, user_id=session["user_id"])
        return redirect("/")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Query db
    stocks = db.execute("SELECT * FROM stocks WHERE user_id=:id_user", id_user=session["user_id"])
    current_price = {}

    # Insert into dict the data
    for x in range(len(stocks)):
        current_price[stocks[x]["symbol"]] = usd(stocks[x]["price_buy"])

    # Render template
    return render_template('history.html', stocks=stocks, current_price=current_price)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # If get render template
    if request.method == "GET":
        return render_template("quote.html")
    else:
        # If post get quoate
        symbol_input = str(request.form.get("symbol"))
        symbol= lookup(symbol_input)
        price = usd(symbol["price"])
        return render_template("quoted.html", name=symbol["name"] ,symbol=symbol["symbol"], price=price)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # If GET render register template
    if request.method == "GET":
        return render_template("register.html")
    else:
        # Check if username exist
        us_name = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(us_name)>0:
            return apology("Username already exists", 403)
        elif not password_check(request.form.get("password")):
            # Password function check
            return apology("check your password", 403)

        # Insert new user in table
        register_user = db.execute("INSERT INTO users (username,hash) VALUES(:username,:hash)",
                          username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        # Login that user
        new_user = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        session["user_id"] = new_user[0]["id"]
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # If GET query db
    if request.method == "GET":
        shares = db.execute("SELECT id, user_id, symbol, name, SUM(q_shares) as q_shares FROM stocks WHERE user_id=:id_user GROUP BY user_id, symbol, name", id_user=session["user_id"])
        return render_template("sell.html", shares=shares)
    else:
        # Query db
        shares = db.execute("SELECT id, user_id, symbol, name, SUM(q_shares) as q_shares FROM stocks WHERE user_id=:id_user AND symbol=:symbol GROUP BY user_id, symbol, name",id_user=session["user_id"], symbol=request.form.get("symbol"))
        # Error check
        if not request.form.get("symbol"):
            return apology("MISSING SYMBOL", 400)
        elif not request.form.get("shares") or int(request.form.get("shares")) <= 0:
            return apology("MISSING SHARES", 400)
        elif shares[0]["q_shares"] < int(request.form.get("shares")):
            return apology("You can't sell more shares than what you have", 400)
        # Get values from html form
        symbol_input = str(request.form.get("symbol"))
        symbol = lookup(symbol_input)
        price = symbol["price"]
        shares_input = int(request.form.get("shares"))
        shares_input_neg = -1 * int(request.form.get("shares"))
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # Query db
        cash_amount = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = cash_amount[0]["cash"]
        cash_updated = cash + (price * shares_input)
        # Insert intodb
        new_sell = db.execute("INSERT INTO stocks (user_id,symbol,name,q_shares,price_buy,date) VALUES(:user_id,:symbol,:name,:q_shares,:price_buy,:date)",
                          user_id=session["user_id"], symbol=symbol["symbol"], name=symbol["name"],
                          q_shares=shares_input_neg,price_buy=symbol["price"],date=dt_string)
        # Update db
        update_cash = db.execute("UPDATE users SET cash =:cash WHERE id=:user_id", cash=cash_updated, user_id=session["user_id"])
        return redirect("/")


def errorhandler(e):
    """Handle error"""
    # Handle error
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    # Listen for errors
    app.errorhandler(code)(errorhandler)
