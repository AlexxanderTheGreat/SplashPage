from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.before_request
def redirect_to_canonical_domain():
    # If someone hit the Render hostname, send them to your custom domain
    if request.host == "morales-event-rentals.onrender.com":
        path = request.full_path
        if path.endswith("?"):
            path = path[:-1]
        return redirect("https://www.moraleseventrentals.com" + path, code=308)


@app.route("/")
def t1():
    """Splash Page — new redesign.
       Translation is now handled client-side via data-en/data-es attributes,
       so no `texts` dict is needed. To add new languages, just add data-fr etc.
       in the template and extend the JS toggle at the bottom of Splash_Page.html."""
    lang = request.args.get("lang", "en")
    return render_template("Splash_Page.html", lang=lang)


# ──────────────────────────────────────────────────────────────────
# Old route preserved at /old in case you want to compare side-by-side.
# Comment this out (and delete templates/Splash_Page_OLD.html) when you
# no longer need it.
# ──────────────────────────────────────────────────────────────────
OLD_TEXTS = {
    "en": {
        "spsh": "En Espanol", "call_now": "Call to Book!",
        "email": "info@moraleseventrentals.com",
        "phone": "Addidtional phone number",
        "insta": "Check us out on Instagram!",
        "abt": "About Us",
        "prph": "We're a family-owned business based in Monterey, California, proudly rooted in our Hispanic heritage. Our mission is to provide great service, fair prices, and that personal, one-on-one connection you can only get from a family-run operation. We believe in creating joyful experiences and lasting memories for our community. When you book with us, you're not just supporting a business, you're supporting a family that cares.",
        "invt": "Inventory", "tnt": "Tents",
        "tentt": "We also offer the ability to make a tent to the size you would like(if possible) and the addition of lights with no extra cost but we also offer nicer string ligths for $20 more",
        "jh": "Jump Houses", "ct": "Chairs & Tables",
        "pt": "Portable Toilets", "ph": "Standing Portable Heaters",
        "pth": "Portable Toilets & Heaters",
    },
    "es": {
        "spsh": "English", "call_now": "¡Llámanos para empezar la fiesta!",
        "email": "info@moraleseventrentals.com",
        "phone": "Otro Numero para llamarnos",
        "insta": "siganos en el instagram!",
        "abt": "Un Poco de Nosotros",
        "prph": "Somos una empresa familiar con sede en Seaside, California, orgullosamente arraigada en nuestra herencia hispana. Nuestra misión es brindar un excelente servicio, precios justos y esa conexión personal e individual que solo se puede obtener en una empresa familiar. Creemos en crear experiencias felices y recuerdos imborrables para nuestra comunidad. Al reservar con nosotros, no solo apoya a un negocio, sino a una familia que se preocupa por los demás.",
        "invt": "Inventario", "tnt": "Carpas",
        "tentt": "También ofrecemos la posibilidad de hacer una carpa del tamaño que desees (si es posible).",
        "jh": "brincolines", "ct": "Sillas y Mesas",
        "pt": "Banos Portatil", "ph": "Calentador portátil de pie",
    }
}

@app.route("/old")
def old_splash():
    """Original splash page kept for reference. Delete this route when no longer needed."""
    lang = request.args.get("lang", "en")
    return render_template("Splash_Page_OLD.html", texts=OLD_TEXTS[lang], lang=lang)


if __name__ == "__main__":
    app.run(debug=True)
