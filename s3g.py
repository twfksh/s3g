import os

from liquid import Liquid

# project constants
COLLECTION = dict()
ASSETS_DIR_PATH = "assets"
MODELS_DIR_PATH = "models"
OUTPUT_DIR_PATH = "public"


# helper functions
def parse_template(model, template="template.html"):
    tfp = os.path.join(MODELS_DIR_PATH, model, template)
    with open(tfp, "r") as fp:
        template = fp.read()

    return template


def render_html(template, collection=COLLECTION):  # model is data container
    liq = Liquid(template, from_file=False)
    ret = liq.render(collection=collection)
    return ret


def write_page(html_str, model):
    ofp = os.path.join(OUTPUT_DIR_PATH, model) + ".html"
    with open(ofp, "w") as fp:
        fp.write(html_str)
    print(f"[info] - written {ofp}")


# scan for models
COLLECTION["models"] = [
    d
    for d in os.listdir(MODELS_DIR_PATH)
    if os.path.isdir(os.path.join(MODELS_DIR_PATH, d))
]

links = """{% for model in collection.models %}
    <a href="{{ model }}.html">{{ model }}</a>
{% endfor %}"""

COLLECTION["links"] = render_html(links)

for model in COLLECTION["models"]:
    template = parse_template(model)
    html_string = render_html(template)
    write_page(html_string, model)

