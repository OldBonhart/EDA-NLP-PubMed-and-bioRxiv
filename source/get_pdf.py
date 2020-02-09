from fpdf import FPDF

def encode_decode(data):
    udata = data.encode()
    return udata.decode('latin-1')

def make_pdf(site, 
             MAP,
             pdf_name,
             wc_name,
             wc_name_mask,
             name1_2d,
             name2_2d,
             sim_name,
             gif_name,
             img_promo):
    
    PROLOG = f'''Web Scraping science papers from site:
    {site} on the topic - "Connectome".'''
    EPILOG = "Top Words Cloud"
    EPILOG2 = "t-SNE"
    empty = []

    # Description
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15, style="B")

    #pdf.set_creator("Bonart")
    pdf.multi_cell(0, 8, txt=PROLOG, align="C")
    pdf.image(img_promo, x=15, y=50, w=180, link="8.8.8.8",)#
    pdf.add_page()

    # Create pdf-pages with data from dictionary
    for idx, i in enumerate([x for x in MAP.items()]):
        try:
            url = i[0]
            title = encode_decode(i[1][1])
            data = encode_decode(i[1][0][0])
            pdf.ln(10)
            pdf.set_font("Arial", size=12, style="B")
            pdf.multi_cell(0, 8, txt=title, align="L")
            pdf.set_text_color(180, 5, 100)
            pdf.cell(0, 10, txt=url, ln=1, align="L")
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 8, txt=data)
        except: 
            empty.append(idx)
            continue
    print("Amount of empty data:", len(empty))

    # Epilog
    pdf.add_page()
    pdf.set_font("Arial", size=15, style="B")
    pdf.multi_cell(0, 8, txt=EPILOG, align="C")
    pdf.image(f'{wc_name}.png', x=15, y=30, w=180, link="8.8.8.8")
    pdf.add_page()
    pdf.image(f'{wc_name_mask}.png', x=15, y=10, w=180, link="8.8.8.8")
    pdf.add_page()
    pdf.image(f'{name1_2d}.png', x=15, y=10, w=180, link="8.8.8.8")
    pdf.add_page()
    pdf.image(f'{name2_2d}.png', x=15, y=10, w=180, link="8.8.8.8")
    pdf.add_page()
    pdf.image(f'{sim_name}.png', x=15, y=10, w=180, link="8.8.8.8")
    pdf.add_page()
    pdf.image(gif_name, x=15, y=10, w=180, link="8.8.8.8")
    pdf.output(f"{pdf_name}.pdf")