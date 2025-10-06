from flask import Flask, render_template, request,redirect
# from flask_bootstrap import Bootstrap5


app = Flask(__name__)
@app.before_request
def redirect_to_canonical_domain():
    # If someone hit the Render hostname, send them to your custom domain
    if request.host == "morales-event-rentals.onrender.com":
        # Keep path & query string
        path = request.full_path
        # Flask’s full_path ends with “?” if there’s no query—trim it
        if path.endswith("?"):
            path = path[:-1]
        return redirect("https://www.moraleseventrentals.com" + path, code=308)
# bootstrap = Bootstrap5(app)

@app.route("/")
def t1():
  lang = request.args.get("lang", "en")
    # Texts for both languages
  texts = {
        "en": {
            "spsh" : "En Espanol",
            "call_now": "Call us Now!",
            "email": "info@moraleseventrentals.com" ,
            "phone": "Addidtional phone number",
            "insta": "Check us out on Instagram!",
            "abt": "About Us",
            "prph": """We’re a family-owned business based in Seaside, California, proudly rooted in our Hispanic heritage.
                                Our mission is to provide great service, fair prices, and that personal, one-on-one connection 
                                you can only get from a family-run operation. We believe in creating joyful experiences and 
                                lasting memories for our community. When you book with us, you’re not just supporting a 
                                business—you’re supporting a family that cares.""",
            "invt": "Inventory",
            "tnt": "Tents",
            "tentt": "We also offer the ability to make a tent to the size you would like(if possible) and the addition of lights with no extra cost but we also offer nicer string ligths for $20 more",
            "jh": "Jump Houses",
            "ct": "Chairs & Tables",
            "pt": "Portable Toilets",
            "ph": "Standing Portable Heaters",
            "pth": "Portable Toilets & Heaters"

        },
        "es": {
            "spsh": "English",
            "call_now": "¡Llámanos ahora!",
            "email": "info@moraleseventrentals.com" ,
            "phone": "Otro Numero para llamar",
            "insta": "siganos en el instagram!",
            "abt": "Un Poco de Nosotros",
            "prph": """Somos una empresa familiar con sede en Seaside, California, 
            orgullosamente arraigada en nuestra herencia hispana. Nuestra misión es brindar 
            un excelente servicio, precios justos y esa conexión personal e individual que solo se 
            puede obtener en una empresa familiar. Creemos en crear experiencias felices y recuerdos 
            imborrables para nuestra comunidad. Al reservar con nosotros, no solo apoya a un negocio, 
            sino a una familia que se preocupa por los demás.""",
            "invt": "Inventario",
            "tnt": "Carpas",
            "tentt": "También ofrecemos la posibilidad de hacer una carpa del tamaño que desees (si es posible).",
            "jh": "brincolines",
            "ct": "Sillas y Mesas",
            "pt": "Banos Portatil",
            "ph": "Calentador portátil de pie"
            

        }
    }
    # Pass the correct texts to the template
  return render_template("Splash_Page.html", texts=texts[lang], lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
  # return render_template("Splash_Page.html")