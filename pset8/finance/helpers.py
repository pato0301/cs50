# Import library
import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def password_check(passwd):

    SpecialSym =["$", "@", "#", "%", "*", "&","-", "_", "!"]

    # Check for password validation
    if len(passwd) < 8:
        print('length should be at least 8')
        return False
    elif len(passwd) > 25:
        print('length should be not be greater than 25')
        return False
    elif not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        return False
    elif not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        return False
    elif not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        return False
    elif not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $ @ # % * & - _ ! &')
        return False
    else:
        return True
