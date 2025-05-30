import os
import sys
import requests
from datetime import datetime
from fpdf import FPDF

# Constants
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATE_STRING = datetime.now().strftime("%m-%d-%Y")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"Functional_Optimization_Weight_Loss_Plan_{DATE_STRING}.pdf")

# Font URLs
NOTO_REGULAR_URL = "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSans/NotoSans-Regular.ttf"
NOTO_BOLD_URL = "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSans/NotoSans-Bold.ttf"

# Font download helper
def ensure_font(path, url):
    if not os.path.isfile(path):
        print(f"🔽 Downloading font: {os.path.basename(path)}")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.load_fonts()

    def load_fonts(self):
        regular_font = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
        bold_font = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")

        ensure_font(regular_font, NOTO_REGULAR_URL)
        ensure_font(bold_font, NOTO_BOLD_URL)

        self.add_font("NotoSans", "", regular_font)
        self.add_font("NotoSans", "B", bold_font)
        self.set_font("NotoSans", "", 10)

    def header(self):
        self.set_font("NotoSans", "B", 12)
        self.cell(0, 10, "🌿 Functional Optimization & Weight Loss Plan", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("NotoSans", "B", 11)
        if self.get_y() > self.h - 30:
            self.add_page()
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def section_body(self, body):
        self.set_font("NotoSans", "", 10)
        self.multi_cell(0, 6, body)
        self.ln()

    def add_section(self, title, body):
        self.section_title(title)
        self.section_body(body)

    def add_weekly_tracker_table(self):
        # Check space before starting
        if self.get_y() > self.h - 80:
            self.add_page()

        self.section_title("📊 Weekly Symptom Tracker")

        self.set_font("NotoSans", "", 10)
        self.multi_cell(0, 6, "Track the following symptoms on a scale from 1 (poor) to 5 (excellent):")
        self.ln(2)

        symptoms = [
            "⚡ Energy Levels",
            "🙂 Mood/Stress",
            "😴 Sleep Quality",
            "🤰 Digestion/Bloating",
            "🦵 Joint/Muscle Pain",
            "🧠 Brain Fog",
            "💊 Supplement Adherence"
        ]

        days = ["", "M", "T", "W", "T", "F", "S", "S"]
        symptom_col_width = 52
        day_col_width = (self.w - 20 - symptom_col_width) / 7  # Adjust remaining width
        row_height = 8

        # Header row
        self.set_font("NotoSans", "B", 10)
        for i, day in enumerate(days):
            if i == 0:
                self.cell(symptom_col_width, row_height, "", border=1, align="L")
            else:
                self.cell(day_col_width, row_height, day, border=1, align="C")
        self.ln(row_height)

        # Rows
        self.set_font("NotoSans", "", 10)
        for symptom in symptoms:
            self.cell(symptom_col_width, row_height, symptom, border=1)
            for _ in range(7):
                self.cell(day_col_width, row_height, "", border=1, align="C")
            self.ln(row_height)

# Generate PDF
pdf = PDF()
pdf.add_page()

# Add sections
pdf.add_section("🧪 Summary of Key Lab Results", """
- 🔻 Vitamin D is very low (8 ng/mL); optimal is 40–60 ng/mL. Supplementation is needed.
- 🧬 HDL cholesterol is low (38 mg/dL); optimal is ≥60 mg/dL. Lifestyle and omega-3s can help.
- ✅ All other labs (TSH, glucose, cholesterol, liver, kidney, electrolytes) are within healthy range.
""")

pdf.add_section("🎯 Weight Loss Goal", """
- Current weight: 310 lbs
- Goal weight: 165 lbs
- Target loss: 145 lbs
- Approach: Safe, steady loss of 1.5–2.5 lbs/week through lifestyle, nutrition, and supplements.
""")

pdf.add_section("📋 Functional Optimization Plan", """
1. 🥗 Diet: Anti-inflammatory, whole-food diet rich in greens, protein, fiber, and omega-3s.
2. 🏃‍♂️ Exercise: 30–45 mins aerobic + strength training, 5x/week. Track steps (aim for 10,000/day).
3. 😴 Sleep: 7–9 hours/night, consistent schedule, dark room.
4. 🧘 Stress: Meditation, breathing, journaling, or yoga daily.
5. 🌞 Sunlight: 15–20 mins outdoors daily (especially in the morning).
6. 💧 Hydration: 2–2.5L water/day; add electrolytes if active.
""")

pdf.add_section("💊 Supplement Recommendations", """
- 🌞 Vitamin D3 (5,000–10,000 IU) + K2 (100–200 mcg): for immune and bone health.
- 🐟 Fish Oil (1,000–2,000 mg EPA/DHA): to raise HDL and lower inflammation.
- 🌙 Magnesium Glycinate (200–400 mg): for sleep, mood, and glucose balance.
- 🌈 Multivitamin: with trace minerals to fill nutrient gaps.

Optional:
- 🦠 Probiotic: for gut health.
- 🌿 Ashwagandha or Rhodiola: for stress support.
""")

# Add the tracker table
pdf.add_weekly_tracker_table()

# Save the PDF
pdf.output(OUTPUT_FILE)
print(f"✅ PDF saved to: {OUTPUT_FILE}")
