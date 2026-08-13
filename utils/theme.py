"""
utils/theme.py
Injects the modern dark / 3D-accent theme into a Streamlit app.
Call inject_theme() once, right after st.set_page_config(), in app.py.
"""

import streamlit as st


def inject_theme():
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">

        <style>
        :root{
            --bg:#0A0E1A;
            --surface:#121826;
            --surface-2:#171F32;
            --border:rgba(255,255,255,0.08);
            --text:#E8ECF4;
            --text-muted:#8B93A7;
            --mint:#3DDC97;
            --violet:#7C6FFF;
            --amber:#FFB454;
        }

        /* page background */
        .stApp{
            background:
                radial-gradient(circle at 15% 8%, rgba(124,111,255,0.14), transparent 40%),
                radial-gradient(circle at 85% 15%, rgba(61,220,151,0.10), transparent 45%),
                var(--bg);
            color:var(--text);
            font-family:'Inter', sans-serif;
        }

        /* headings */
        h1, h2, h3{
            font-family:'Space Grotesk', sans-serif !important;
            color:var(--text) !important;
        }

        /* sidebar */
        section[data-testid="stSidebar"]{
            background:var(--surface) !important;
            border-right:1px solid var(--border) !important;
        }

        /* buttons */
        .stButton > button{
            background:linear-gradient(100deg, var(--mint), #2BC888) !important;
            color:#04140D !important;
            border:none !important;
            border-radius:9px !important;
            font-weight:600 !important;
            padding:10px 22px !important;
            box-shadow:0 10px 30px -8px rgba(61,220,151,0.5) !important;
        }
        .stButton > button:hover{
            filter:brightness(1.05);
            transform:translateY(-1px);
        }

        /* metric cards */
        div[data-testid="stMetric"]{
            background:var(--surface);
            border:1px solid var(--border);
            border-radius:14px;
            padding:16px 18px;
        }
        div[data-testid="stMetricValue"]{
            font-family:'IBM Plex Mono', monospace !important;
            color:var(--mint) !important;
        }

        /* text input / select / textarea */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"]{
            background:var(--surface-2) !important;
            border:1px solid var(--border) !important;
            border-radius:9px !important;
            color:var(--text) !important;
        }

        /* progress bar (for readiness score) */
        div[data-testid="stProgress"] > div > div{
            background:linear-gradient(90deg, var(--mint), var(--violet)) !important;
            border-radius:99px !important;
        }

        /* expander / containers used as "cards" */
        div[data-testid="stExpander"]{
            background:var(--surface);
            border:1px solid var(--border) !important;
            border-radius:14px !important;
        }

        /* tabs */
        button[data-baseweb="tab"]{
            color:var(--text-muted) !important;
            font-family:'Space Grotesk', sans-serif !important;
        }
        button[data-baseweb="tab"][aria-selected="true"]{
            color:var(--mint) !important;
            border-bottom-color:var(--mint) !important;
        }

        /* download button */
        .stDownloadButton > button{
            background:var(--surface-2) !important;
            color:var(--text) !important;
            border:1px solid var(--border) !important;
            border-radius:9px !important;
        }

        /* native bordered containers -> used as section / week cards */
        div[data-testid="stVerticalBlockBorderWrapper"]{
            background:linear-gradient(160deg, var(--surface-2), var(--surface)) !important;
            border:1px solid var(--border) !important;
            border-radius:14px !important;
            box-shadow:0 20px 40px -28px rgba(0,0,0,0.7);
            transition:transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:hover{
            transform:translateY(-3px);
            box-shadow:0 28px 55px -25px rgba(0,0,0,0.75);
            border-color:rgba(61,220,151,0.25) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] > div{
            border-radius:14px !important;
        }

        /* ambient glow orbs, fixed behind content */
        .stApp::before{
            content:"";
            position:fixed;
            top:-10%; left:-10%;
            width:45vw; height:45vw;
            background:radial-gradient(circle, rgba(124,111,255,0.10), transparent 70%);
            pointer-events:none;
            z-index:0;
        }
        .stApp::after{
            content:"";
            position:fixed;
            bottom:-15%; right:-10%;
            width:50vw; height:50vw;
            background:radial-gradient(circle, rgba(61,220,151,0.08), transparent 70%);
            pointer-events:none;
            z-index:0;
        }

        /* metric cards get the same depth treatment */
        div[data-testid="stMetric"]{
            box-shadow:0 16px 32px -24px rgba(0,0,0,0.6);
            transition:transform 0.2s ease;
        }
        div[data-testid="stMetric"]:hover{
            transform:translateY(-2px);
        }

        /* checkboxes */
        .stCheckbox label p{
            color:var(--text) !important;
            font-size:13.5px !important;
        }
        .stCheckbox svg{
            fill:var(--text-muted) !important;
        }

        /* dataframe */
        div[data-testid="stDataFrame"]{
            border:1px solid var(--border) !important;
            border-radius:12px !important;
            overflow:hidden;
        }

        /* info / error / success boxes */
        div[data-testid="stAlert"]{
            background:var(--surface-2) !important;
            border:1px solid var(--border) !important;
            border-radius:10px !important;
            color:var(--text) !important;
        }

        /* tab panel top spacing */
        div[data-baseweb="tab-panel"]{
            padding-top:20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _eyebrow(text: str, color: str = "var(--mint)"):
    st.markdown(
        f"""
        <span style="font-family:'IBM Plex Mono';font-size:11px;letter-spacing:0.06em;
            color:{color};text-transform:uppercase;">{text}</span>
        """,
        unsafe_allow_html=True,
    )


def parse_report_sections(markdown_text: str):
    """
    Splits Gemini's '## N. Title' formatted report into
    a list of (number, title, body) tuples.
    """
    import re

    pattern = r"##\s*(\d+)\.\s*(.+?)\n(.*?)(?=(?:##\s*\d+\.)|\Z)"
    matches = re.findall(pattern, markdown_text, flags=re.S)

    if not matches:
        return [("", "Report", markdown_text)]

    return [(num.strip(), title.strip(), body.strip()) for num, title, body in matches]


def render_report_sections(markdown_text: str):
    """
    Renders a Gemini markdown report as a series of styled bordered
    cards, one per '## N. Title' section, preserving native markdown
    rendering (lists, bold, etc.) inside each card.
    """
    accents = ["var(--mint)", "var(--violet)", "var(--amber)"]
    sections = parse_report_sections(markdown_text)

    for i, (num, title, body) in enumerate(sections):
        color = accents[i % len(accents)]
        with st.container():
            _eyebrow(f"{num + '. ' if num else ''}{title}", color=color)
            st.markdown(body)


def score_gauge(label: str, score, max_score: int = 100, sublabel: str = ""):
    """
    Small horizontal 'gauge' card for a single score value,
    e.g. JD Match Score. score can be an int or a string like '81'.
    """
    try:
        pct = max(0, min(100, int(str(score).strip().rstrip("%")) / max_score * 100))
    except (ValueError, ZeroDivisionError):
        pct = 0

    st.markdown(
        f"""
        <div style="
            background:linear-gradient(160deg, var(--surface-2), var(--surface));
            border:1px solid var(--border);
            border-radius:16px;
            padding:22px 26px;
            margin-bottom:18px;
        ">
            <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:10px;">
                <div>
                    <div style="font-family:'IBM Plex Mono';font-size:11px;color:var(--text-muted);
                        text-transform:uppercase;letter-spacing:0.06em;">{label}</div>
                    <div style="font-family:'IBM Plex Mono';font-size:38px;color:var(--mint);line-height:1.1;">{score}</div>
                </div>
                <div style="font-size:12px;color:var(--text-muted);">{sublabel}</div>
            </div>
            <div style="height:7px;background:rgba(255,255,255,0.06);border-radius:99px;overflow:hidden;">
                <div style="width:{pct}%;height:100%;background:linear-gradient(90deg, var(--mint), var(--violet));border-radius:99px;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def extract_first_number(text: str, default=""):
    """Pulls the first integer found in a string — used to grab a score out of Gemini's text."""
    import re

    match = re.search(r"\d{1,3}", text)
    return match.group(0) if match else default


def readiness_console(score: int, role: str, skills: dict):
    """
    Renders a REAL interactive 3D-tilting 'console card' using an
    embedded HTML component (needed because Streamlit's st.markdown
    does not execute <script> tags — this uses components.html instead,
    which runs in its own iframe with working JS).
    skills: dict like {"SQL": 88, "Power BI": 82, "Python": 70}
    """
    import streamlit.components.v1 as components

    colors = ["#3DDC97", "#3DDC97", "#7C6FFF", "#FFB454"]
    bars = ""
    for i, (name, val) in enumerate(skills.items()):
        color = colors[i % len(colors)]
        bars += f"""
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;font-size:12px;">
            <span style="width:80px;color:#8B93A7;font-family:'IBM Plex Mono',monospace;font-size:11px;">{name}</span>
            <div style="flex:1;height:6px;background:rgba(255,255,255,0.06);border-radius:99px;overflow:hidden;">
                <div style="width:{val}%;height:100%;background:{color};border-radius:99px;"></div>
            </div>
        </div>
        """

    html = f"""
    <div style="font-family:'Inter',sans-serif; perspective:1400px; padding:14px;">
      <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
      <div id="console" style="
          position:relative;
          background:linear-gradient(160deg, #171F32, #121826);
          border:1px solid rgba(255,255,255,0.08);
          border-radius:20px;
          padding:26px;
          transform:rotateX(8deg) rotateY(-14deg);
          transform-style:preserve-3d;
          transition:transform 0.12s ease-out, box-shadow 0.3s ease;
          box-shadow:0 40px 80px -25px rgba(0,0,0,0.65);
      ">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px; transform:translateZ(30px);">
            <div>
                <h3 style="font-family:'Space Grotesk';font-size:15px;margin:0;color:#E8ECF4;">Readiness Console</h3>
                <p style="color:#8B93A7;font-size:12px;margin:4px 0 0;">Target role — {role}</p>
            </div>
            <div style="background:#0F1524;border:1px solid rgba(255,255,255,0.08);
                padding:6px 11px;border-radius:99px;font-size:11px;display:flex;align-items:center;gap:6px;
                color:#E8ECF4;flex-shrink:0;">
                <span style="width:6px;height:6px;border-radius:50%;background:#3DDC97;box-shadow:0 0 6px #3DDC97;"></span>
                Live
            </div>
        </div>

        <div style="display:flex;align-items:center;gap:18px; transform:translateZ(45px);">
            <div style="font-family:'IBM Plex Mono';font-size:44px;color:#3DDC97;line-height:1;">{score}</div>
            <div style="font-size:11px;color:#8B93A7;letter-spacing:0.05em;">READINESS<br>SCORE&nbsp;/&nbsp;100</div>
        </div>

        <div style="margin-top:20px; transform:translateZ(25px);">
            {bars}
        </div>
      </div>
    </div>

    <script>
      const card = document.getElementById('console');
      const wrap = card.parentElement.parentElement;
      wrap.addEventListener('mousemove', (e) => {{
        const rect = wrap.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        const rotY = x * 16 - 10;
        const rotX = -y * 12 + 5;
        card.style.transform = `rotateX(${{rotX}}deg) rotateY(${{rotY}}deg)`;
      }});
      wrap.addEventListener('mouseleave', () => {{
        card.style.transform = 'rotateX(8deg) rotateY(-14deg)';
      }});
    </script>
    """

    components.html(html, height=370)