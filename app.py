from flask import Flask, render_template, request, send_file
import io
from fpdf import FPDF
import os

app = Flask(__name__)

# Hardcoded list of valid names
team_names = [
    "innov8rs", "team ahx", "timepass techies", "ctrlc+ctrlv", "tech buddies",
    "innovators united", "musafir", "tech redux", "dead neurons society", "nexa",
    "codexinitiate", "hashtag", "hackstreet boys", "syntax terminators", "quantum coders",
    "powerpuff girls", "web wizards", "bummerz", "codecrafters", "binary wizards",
    "cyber knights", "pixel pirates", "jacked nerds", "hw destroyers", "delta coders",
    "just some nerds", "knights", "digital dreamers", "humble inferno", "ok google",
    "tech smugglers", "virtual voyagers", "the invincible", "team phoenix",
    "elite coders", "team mouse", "competitiondestroyers", "hack hive", "codebots",
    "pinkberry", "innoventures", "team 404", "code fusion"
]


certificate_template_path = 'static/certificate.png'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name').strip().lower()

    if name in team_names:
        pdf = FPDF('L', 'mm', 'A4')  # Landscape orientation, A4 size
        pdf.add_page()

        pdf.image(certificate_template_path, x=0, y=0, w=297, h=210)  # A4 size in mm (297x210)

        # Customize text on top of the template
        pdf.set_font("Arial", 'B', 24)
        pdf.set_text_color(255, 255, 255)  # Set text color to black
        pdf.set_xy(27, 120)  # Set position (adjust based on your template)
        pdf.cell(297, 10, txt=f"{name.title()}", ln=True, align='C')

        pdf_output = io.BytesIO()
        pdf_output.write(pdf.output(dest='S').encode('latin1'))
        pdf_output.seek(0)

        return send_file(pdf_output, download_name="certificate.pdf", as_attachment=True)
    else:
        return "Sorry, your team name is not on the list, if you think is a mistake, kindly contact any Tech Team member", 403


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))

