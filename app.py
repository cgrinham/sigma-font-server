import os
from flask import jsonify, Flask, send_file, request
from flask_cors import CORS
import fonts

app = Flask(__name__)
CORS(app, resources={r"/figma/*": {"origins": "https://www.figma.com"}})
CONFIG = {"FONT_DIR": os.getenv("FONT_DIR")}


def get_font_data(font):
    """
    Get font data in format expected by figma
    """
    return {
        "postscript": fonts.get_font_postscript(font),
        "family": fonts.get_font_family_name(font),
        "id": fonts.get_font_id(font),
        "style": fonts.get_font_style(font),
        "weight": fonts.get_font_weight(font),
        "stretch": 5,
        "italic": fonts.font_is_italic(font),
    }


def get_all_fonts():
    """
    I'm pretty sure this implementation is not feature complete as there should
    be able to be multiple fonts in each list. I don't know enough about fonts
    to try implementing it.
    """
    data = {}
    for font_path in fonts.get_fonts(CONFIG.get("FONT_DIR")):
        data[font_path] = [get_font_data(fonts.get_font(font_path))]
    return data


@app.route("/figma/font-files")
def get_font_files():
    data = {
        "version": 4,
        "fontFiles": get_all_fonts()
    }
    return jsonify(data)


@app.route("/figma/font-file")
def get_font_file():
    file_path = request.args.get("file")
    return send_file(file_path)
