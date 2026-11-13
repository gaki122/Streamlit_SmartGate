"""
Smart Gate - Informative Website (Streamlit)
A Face Recognition-Based Entry and Exit Management System
for Samtse College of Education.

Module : Python GUI Programming  |  BED IT 'C'  |  Academic Year 2026
Run    : streamlit run app.py
"""

import base64
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Smart Gate | Face Recognition Entry & Exit System",
    page_icon="🍂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# GLOBAL WARM EARTH THEME (CSS)
# ----------------------------------------------------------------------------
EARTH_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

:root{
  --abyss:#302920; --deep:#4b3b2e; --sea:#6d5a45; --teal:#8b6548;
  --aqua:#b86f4a; --foam:#704b37; --mist:#74685b; --coral:#b85f48; --sun:#b68537; --ok:#657b55;
  --maroon:#70283f; --maroon-deep:#4d1d30; --maroon-soft:#a65367; --maroon-wash:rgba(112,40,63,.10);
  --glass:rgba(255,255,255,.72); --line:rgba(105,79,56,.20);
}
html, body, [class*="css"], .stApp { font-family:'Inter',sans-serif; }
.stApp{
  background:
    radial-gradient(1200px 600px at 85% -10%, rgba(184,111,74,.12), transparent 60%),
    radial-gradient(900px 500px at -10% 30%, rgba(115,128,90,.12), transparent 60%),
    linear-gradient(180deg,#faf7f1 0%,#f3ede3 55%,#eee5d8 100%);
  background-attachment: fixed;
  color:#3c332b;
}
#MainMenu, footer, header[data-testid="stHeader"]{ visibility:hidden; height:0; }
.block-container{ max-width:1240px; padding-top:1.2rem; padding-bottom:3rem; }
h1,h2,h3,h4{ font-family:'Poppins',sans-serif !important; }

/* ---------- HERO ---------- */
.hero{
  position:relative; overflow:hidden; border-radius:28px; padding:48px;
  background:
    radial-gradient(circle at 88% 18%,rgba(231,181,166,.18),transparent 25%),
    linear-gradient(118deg,#4d1d30 0%,#70283f 38%,#80664d 76%,#454335 100%);
  border:1px solid rgba(255,248,235,.35); box-shadow:0 24px 60px rgba(72,54,38,.22);
}
.hero-inner{ position:relative; z-index:1; max-width:900px; }
.hero-kicker{
  display:inline-flex; align-items:center; gap:9px; padding:8px 14px; border-radius:999px;
  background:rgba(255,248,235,.10); border:1px solid rgba(255,248,235,.24);
  color:#f3d9ac; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase;
}
.hero h1{ font-size:clamp(3.2rem,7vw,5.2rem); line-height:1; margin:20px 0 24px; font-weight:800; color:#fffaf2; }
.hero h1 span{ color:#f3d9ac; }
.hero-topic{
  max-width:820px; padding:21px 24px; border-left:5px solid #d9a475; border-radius:4px 18px 18px 4px;
  background:linear-gradient(100deg,rgba(255,248,235,.14),rgba(255,248,235,.05));
  box-shadow:0 12px 30px rgba(40,20,24,.12);
}
.hero-topic-label{ color:#f0cba6; font-size:.72rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
.hero-topic p{ margin:8px 0 6px; color:#fffaf2; font-family:'Poppins',sans-serif; font-size:clamp(1.3rem,2.4vw,1.8rem); font-weight:700; line-height:1.4; }
.hero-topic-school{ color:#f0e2d0; font-size:1rem; }
.hero-meta{ display:flex; flex-wrap:wrap; gap:10px 24px; margin-top:20px; color:#f0e2d0; font-size:.9rem; }
.hero-meta span{ display:inline-flex; align-items:center; gap:8px; }
.hero-meta i{ color:#e7b5a6; }
.hero-mark{
  position:absolute; right:7%; top:50%; display:flex; align-items:center; justify-content:center;
  width:190px; height:190px; border:1px solid rgba(255,248,235,.24); border-radius:50%;
  color:rgba(255,248,235,.76); font-size:5rem; transform:translateY(-50%);
  box-shadow:0 0 0 18px rgba(255,248,235,.035),0 0 0 38px rgba(255,248,235,.025);
}
.hero-photo{ position:absolute; inset:0 0 0 auto; width:49%; overflow:hidden; pointer-events:none; }
.hero-photo img{ width:100%; height:100%; object-fit:cover; opacity:.88; }
.hero-photo::after{
  content:""; position:absolute; inset:0;
  background:linear-gradient(90deg,#4d1d30 0%,rgba(77,29,48,.48) 28%,rgba(48,41,32,.08) 100%),
    linear-gradient(0deg,rgba(48,41,32,.24),transparent 65%);
}

/* ---------- SECTIONS & CARDS ---------- */
.sec-title{ display:flex; align-items:center; gap:14px; margin:30px 0 6px; }
.sec-title .ico{
  width:46px; height:46px; border-radius:14px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,#22d3ee,#0e7490); color:#031525; font-size:1.25rem;
  box-shadow:0 8px 22px rgba(34,211,238,.35);
}
.sec-title h2{ margin:0; font-size:1.8rem; color:#fff; font-weight:700; }
.sec-sub{ color:var(--mist); margin:0 0 20px 60px; }
.grid{ display:grid; gap:18px; margin:6px 0 18px; }
.g2{ grid-template-columns:repeat(2,1fr);} .g3{ grid-template-columns:repeat(3,1fr);}
.g4{ grid-template-columns:repeat(4,1fr);} .g5{ grid-template-columns:repeat(5,1fr);} .g6{ grid-template-columns:repeat(6,1fr);}
@media (max-width:1000px){ .g3,.g4,.g5,.g6{ grid-template-columns:repeat(2,1fr);} }
@media (max-width:760px){ .hero-mark,.hero-photo{display:none;} }
@media (max-width:640px){ .g2,.g3,.g4,.g5,.g6{ grid-template-columns:1fr;} .hero{padding:34px 22px;} .hero-topic{padding:17px;} }
.card{
  position:relative; padding:22px; border-radius:20px; background:var(--glass); border:1px solid var(--line);
  backdrop-filter:blur(10px); transition:all .3s ease; overflow:hidden;
}
.card::before{
  content:""; position:absolute; inset:0 0 auto 0; height:3px;
  background:linear-gradient(90deg,#22d3ee,#0e7490,transparent); opacity:.8;
}
.card:hover{ transform:translateY(-6px); border-color:rgba(34,211,238,.6); box-shadow:0 18px 40px rgba(34,211,238,.16); }
.card .ico{
  width:50px; height:50px; border-radius:15px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,rgba(34,211,238,.28),rgba(14,116,144,.5)); color:var(--foam);
  font-size:1.35rem; margin-bottom:14px; border:1px solid var(--line);
}
.card h4{ margin:0 0 6px; color:#fff; font-size:1.05rem; font-weight:600; }
.card p{ margin:0; color:var(--mist); font-size:.93rem; line-height:1.55; }
.card .tag{ display:inline-block; margin-top:12px; font-size:.72rem; padding:3px 10px; border-radius:999px;
  background:rgba(34,211,238,.14); color:var(--foam); border:1px solid var(--line); }
.card.warn::before{ background:linear-gradient(90deg,#ff8a7a,#fbbf24,transparent);}
.card.warn .ico{ background:linear-gradient(135deg,rgba(255,138,122,.3),rgba(251,191,36,.25)); color:#ffd6cf;}
.num-badge{ position:absolute; top:14px; right:16px; font-family:'Poppins'; font-weight:800; font-size:1.7rem; color:rgba(165,243,252,.18); }

.stat{ text-align:center; padding:22px 10px; border-radius:20px; background:var(--glass); border:1px solid var(--line); }
.stat .n{ font-family:'Poppins'; font-size:2.2rem; font-weight:800;
  background:linear-gradient(90deg,#67e8f9,#22d3ee); -webkit-background-clip:text; color:transparent; }
.stat .l{ color:var(--mist); font-size:.85rem; margin-top:2px; }

.callout{
  padding:22px 26px; border-radius:20px; margin:12px 0 18px; border:1px solid var(--line);
  background:linear-gradient(135deg,rgba(34,211,238,.16),rgba(14,116,144,.10));
}
.callout h4{ margin:0 0 6px; color:var(--foam); font-size:1rem; letter-spacing:.04em; text-transform:uppercase; }
.callout p{ margin:0; color:#e6f6ff; font-size:1.02rem; line-height:1.65; }
.callout i{ color:var(--aqua); margin-right:8px; }

/* ---------- COMPARISON TABLE ---------- */
.cmp{ width:100%; border-collapse:separate; border-spacing:0 8px; }
.cmp th{ text-align:left; padding:10px 16px; color:var(--foam); font-size:.8rem; text-transform:uppercase; letter-spacing:.08em; }
.cmp td{ padding:14px 16px; background:var(--glass); color:#e6f6ff; font-size:.93rem; vertical-align:top; }
.cmp td:first-child{ border-radius:14px 0 0 14px; font-weight:600; color:#fff; }
.cmp td:last-child{ border-radius:0 14px 14px 0; }
.cmp .bad i{ color:var(--coral); margin-right:8px; } .cmp .good i{ color:var(--ok); margin-right:8px; }

/* ---------- PIPELINE ---------- */
.pipe{ display:flex; gap:10px; align-items:stretch; flex-wrap:wrap; margin:10px 0 18px; }
.step{ flex:1 1 150px; position:relative; padding:20px 16px; border-radius:18px; text-align:center;
  background:var(--glass); border:1px solid var(--line); }
.step .ico{ width:52px; height:52px; margin:0 auto 10px; border-radius:50%; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,#22d3ee,#0e7490); color:#031525; font-size:1.25rem; box-shadow:0 0 22px rgba(34,211,238,.4); }
.step h5{ margin:0 0 4px; font-size:.95rem; color:#fff; font-family:'Poppins'; }
.step p{ margin:0; font-size:.82rem; color:var(--mist); }
.step .no{ position:absolute; top:8px; left:12px; font-size:.7rem; color:var(--foam); opacity:.7; font-weight:600; }
.arrow{ display:flex; align-items:center; color:var(--aqua); font-size:1.1rem; }
@media (max-width:900px){ .arrow{ display:none; } }

/* ---------- RESULT CARDS (simulator) ---------- */
.result{ padding:26px; border-radius:22px; text-align:center; border:1px solid; margin-top:6px; }
.result i{ font-size:3rem; margin-bottom:8px; display:block; }
.result h3{ margin:0; font-size:1.6rem; } .result p{ margin:6px 0 0; font-size:.95rem; }
.result.ok{ background:linear-gradient(135deg,rgba(52,211,153,.22),rgba(14,116,144,.15)); border-color:rgba(52,211,153,.6); }
.result.ok i,.result.ok h3{ color:var(--ok); }
.result.bad{ background:linear-gradient(135deg,rgba(255,138,122,.22),rgba(127,29,29,.18)); border-color:rgba(255,138,122,.6); }
.result.bad i,.result.bad h3{ color:var(--coral); }
.result.wait{ background:linear-gradient(135deg,rgba(251,191,36,.20),rgba(14,116,144,.12)); border-color:rgba(251,191,36,.6); }
.result.wait i,.result.wait h3{ color:var(--sun); }

/* ---------- ROADMAP ---------- */
.tl{ position:relative; margin:10px 0 18px 14px; padding-left:30px; border-left:2px dashed rgba(125,226,255,.3); }
.tl-item{ position:relative; margin-bottom:14px; padding:14px 18px; border-radius:16px; background:var(--glass); border:1px solid var(--line); }
.tl-item::before{ content:""; position:absolute; left:-41px; top:18px; width:18px; height:18px; border-radius:50%;
  background:#0a3d5c; border:3px solid rgba(125,226,255,.45); }
.tl-item.done::before{ background:var(--ok); border-color:#065f46; }
.tl-item.now{ border-color:var(--aqua); box-shadow:0 0 28px rgba(34,211,238,.25); }
.tl-item.now::before{ background:var(--aqua); border-color:#fff; box-shadow:0 0 14px var(--aqua); }
.tl-item .wk{ font-size:.75rem; color:var(--foam); letter-spacing:.08em; text-transform:uppercase; }
.tl-item .ac{ color:#fff; font-weight:600; }
.tl-item.done .ac{ color:var(--mist); }

/* ---------- TEAM ---------- */
.member{ text-align:center; padding:26px 14px; border-radius:22px; background:var(--glass); border:1px solid var(--line); transition:.3s; }
.member:hover{ transform:translateY(-6px); border-color:var(--aqua); }
.avatar{ width:78px; height:78px; margin:0 auto 12px; border-radius:50%; display:flex; align-items:center; justify-content:center;
  font-family:'Poppins'; font-weight:700; font-size:1.5rem; color:#031525; background:linear-gradient(135deg,#a5f3fc,#22d3ee,#0e7490);
  box-shadow:0 0 0 5px rgba(34,211,238,.15), 0 10px 26px rgba(34,211,238,.35); }
.avatar img{ width:100%; height:100%; display:block; border-radius:inherit; object-fit:cover; }
.member h4{ margin:0; color:#fff; font-size:1rem; } .member p{ margin:4px 0 0; color:var(--mist); font-size:.82rem; }

.footer{ margin-top:40px; padding:26px; text-align:center; border-top:1px solid var(--line); color:var(--mist); font-size:.88rem; }
.footer i{ color:var(--aqua); margin:0 4px; }

/* ---------- STREAMLIT WIDGET OVERRIDES ---------- */
.stTabs [data-baseweb="tab-list"]{ gap:6px; background:rgba(255,255,255,.05); padding:6px; border-radius:16px;
  border:1px solid var(--line); overflow-x:auto; margin:22px 0 10px; }
.stTabs button[data-baseweb="tab"]{ border-radius:11px; padding:10px 18px; color:var(--mist); font-weight:500; white-space:nowrap; }
.stTabs button[data-baseweb="tab"][aria-selected="true"]{ background:linear-gradient(135deg,#22d3ee,#0e7490); color:#031525 !important; font-weight:700; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"]{ display:none; }
div[data-testid="stExpander"]{ border:1px solid var(--line) !important; border-radius:16px !important; background:var(--glass); margin-bottom:8px; }
div[data-testid="stExpander"] summary{ font-weight:600; color:#fff; }
div[data-testid="stRadio"] label p, div[data-testid="stSelectbox"] label p, div[data-testid="stSlider"] label p,
div[data-testid="stTextInput"] label p{ color:var(--foam) !important; font-weight:500; }
div[data-testid="stDataFrame"]{ border-radius:16px; overflow:hidden; border:1px solid var(--line); }

/* ---------- WARM EARTH PALETTE ---------- */
.sec-title .ico,.step .ico{
  background:linear-gradient(135deg,#9b5365,#70283f);
  color:#fffaf2;
  box-shadow:0 8px 22px rgba(112,40,63,.2);
}
.sec-title h2{ color:#3c332b; position:relative; }
.sec-title h2::after{ content:""; display:block; width:44px; height:3px; margin-top:5px; border-radius:4px; background:linear-gradient(90deg,var(--maroon),#c99578); }
.card{ box-shadow:0 8px 24px rgba(72,54,38,.04); }
.card::before{ height:4px; background:linear-gradient(90deg,var(--maroon),#c88359,#84906a,transparent); }
.card:hover{ transform:translateY(-5px); border-color:rgba(112,40,63,.38); box-shadow:0 18px 40px rgba(112,40,63,.12); }
.card .ico{ background:linear-gradient(135deg,rgba(112,40,63,.13),rgba(213,154,104,.2)); color:var(--maroon); }
.card h4,.cmp td:first-child,.step h5,.tl-item .ac,.member h4{ color:#3c332b; }
.card p,.stat .l,.step p,.member p{ color:#74685b; }
.card .tag{ background:var(--maroon-wash); color:var(--maroon); border-color:rgba(112,40,63,.17); }
.card.warn .ico{ background:linear-gradient(135deg,rgba(184,95,72,.14),rgba(182,133,55,.14)); color:#9b503f; }
.num-badge{ color:rgba(139,101,72,.2); }
.stat{ box-shadow:0 8px 24px rgba(72,54,38,.04); transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease; }
.stat:hover{ transform:translateY(-4px); border-color:rgba(112,40,63,.3); box-shadow:0 14px 30px rgba(112,40,63,.1); }
.stat .n{ background:linear-gradient(90deg,#70283f,#a86646); }
.callout{ background:linear-gradient(120deg,rgba(112,40,63,.08),rgba(213,154,104,.13),rgba(115,128,90,.08)); border-left:4px solid var(--maroon); }
.callout h4{ color:var(--maroon); }
.callout p{ color:#51473d; }
.callout i{ color:var(--maroon); }
.cmp th{ color:var(--maroon); }
.cmp td{ color:#51473d; }
.cmp tr:hover td{ background:rgba(112,40,63,.07); }
.result.ok{ background:linear-gradient(135deg,rgba(101,123,85,.16),rgba(115,128,90,.08)); border-color:rgba(101,123,85,.5); }
.result.bad{ background:linear-gradient(135deg,rgba(184,95,72,.16),rgba(138,72,56,.08)); border-color:rgba(184,95,72,.5); }
.result.wait{ background:linear-gradient(135deg,rgba(182,133,55,.16),rgba(213,154,104,.08)); border-color:rgba(182,133,55,.5); }
.step{ transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease; }
.step:hover{ transform:translateY(-4px); border-color:rgba(112,40,63,.28); box-shadow:0 12px 26px rgba(112,40,63,.08); }
.step .ico{ box-shadow:0 0 22px rgba(112,40,63,.16); }
.step .no,.tl-item .wk{ color:var(--maroon); }
.tl{ border-left-color:rgba(105,79,56,.3); }
.tl-item::before{ background:#8b6548; border-color:rgba(105,79,56,.35); }
.tl-item.done::before{ background:var(--ok); border-color:#4e6240; }
.tl-item.now{ border-color:var(--maroon-soft); box-shadow:0 0 24px rgba(112,40,63,.14); }
.tl-item.now::before{ background:var(--maroon); border-color:#fffaf2; box-shadow:0 0 12px var(--maroon-soft); }
.tl-item.done .ac{ color:#74685b; }
.member:hover{ border-color:var(--maroon-soft); box-shadow:0 14px 30px rgba(112,40,63,.1); }
.avatar{
  color:#fffaf2;
  background:linear-gradient(135deg,#70283f,#a86646,#77845f);
  box-shadow:0 0 0 5px rgba(112,40,63,.1),0 10px 26px rgba(116,83,56,.18);
}
.footer{ color:#74685b; }
.footer i{ color:var(--maroon); }
.stTabs [data-baseweb="tab-list"]{ background:rgba(105,79,56,.06); }
.stTabs button[data-baseweb="tab"]{ color:#74685b; }
.stTabs button[data-baseweb="tab"][aria-selected="true"]{
  background:linear-gradient(135deg,#70283f,#91465a);
  color:#fffaf2 !important;
  box-shadow:0 5px 14px rgba(112,40,63,.2);
}
.stTabs button[data-baseweb="tab"]:hover{ color:var(--maroon) !important; background:rgba(112,40,63,.07); }
div[data-testid="stExpander"]{ background:rgba(255,255,255,.58); }
div[data-testid="stExpander"] summary{ color:#3c332b; }
div[data-testid="stRadio"] label p, div[data-testid="stSelectbox"] label p, div[data-testid="stSlider"] label p,
div[data-testid="stTextInput"] label p{ color:var(--maroon) !important; }
div[data-testid="stDataFrame"]{ background:rgba(255,255,255,.65); }
.st-key-dashboard_navigation [role="radiogroup"]{
  width:100%; display:flex; flex-wrap:wrap; gap:6px; padding:6px;
  border:1px solid var(--line); border-radius:16px; background:rgba(105,79,56,.06);
}
.st-key-dashboard_navigation [role="radio"]{
  min-height:42px; padding:9px 16px; border-radius:11px; color:#74685b; font-weight:600;
  transition:background .2s ease,color .2s ease,box-shadow .2s ease;
}
.st-key-dashboard_navigation [role="radio"] p{ color:inherit !important; }
.st-key-dashboard_navigation [role="radio"]:hover{ background:rgba(112,40,63,.07); color:var(--maroon); }
.st-key-dashboard_navigation [role="radio"][aria-checked="true"]{
  background:linear-gradient(135deg,#70283f,#91465a); color:#fffaf2;
  box-shadow:0 5px 14px rgba(112,40,63,.2);
}
.st-key-dashboard_navigation [role="radio"][aria-checked="true"] p{ color:#fffaf2 !important; }
div[class*="st-key-summary_"] [data-testid="stButton"] button{
  min-height:112px; padding:16px 8px; border:1px solid var(--line); border-radius:20px;
  background:rgba(255,255,255,.78); box-shadow:0 8px 24px rgba(72,54,38,.06);
  color:#74685b; white-space:pre-line; transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease;
}
div[class*="st-key-summary_"] [data-testid="stButton"] button p{ line-height:1.55; }
div[class*="st-key-summary_"] [data-testid="stButton"] button strong{
  color:var(--maroon); font-family:'Poppins',sans-serif; font-size:1.6rem; font-weight:800;
}
div[class*="st-key-summary_"] [data-testid="stButton"] button:hover{
  transform:translateY(-4px); border-color:rgba(112,40,63,.42); color:var(--maroon);
  box-shadow:0 14px 30px rgba(112,40,63,.12);
}
div[class*="st-key-summary_"] [data-testid="stButton"] button:focus-visible{
  outline:3px solid rgba(112,40,63,.3); outline-offset:2px;
}
</style>
"""

# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def md(html: str) -> None:
    """Render raw HTML safely: strip indentation/blank lines so Markdown never turns it into a code block."""
    cleaned = "\n".join(line.strip() for line in html.strip().splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def image_data_uri(filename: str) -> str:
    image = Path(__file__).with_name(filename).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(image).decode("ascii")


def section(icon: str, title: str, sub: str = "") -> None:
    md(f'<div class="sec-title"><div class="ico"><i class="{icon}"></i></div><h2>{title}</h2></div>'
       + (f'<p class="sec-sub">{sub}</p>' if sub else ""))


def card(icon: str, title: str, text: str, tag: str = "", cls: str = "", num: str = "") -> str:
    tag_html = f'<span class="tag">{tag}</span>' if tag else ""
    num_html = f'<div class="num-badge">{num}</div>' if num else ""
    return (f'<div class="card {cls}">{num_html}<div class="ico"><i class="{icon}"></i></div>'
            f'<h4>{title}</h4><p>{text}</p>{tag_html}</div>')


def grid(items: list[str], cols: str = "g3") -> None:
    md(f'<div class="grid {cols}">' + "".join(items) + "</div>")


def callout(icon: str, title: str, text: str) -> None:
    md(f'<div class="callout"><h4><i class="{icon}"></i>{title}</h4><p>{text}</p></div>')


# ----------------------------------------------------------------------------
# CONTENT (taken from the Smart Gate proposal and presentation)
# ----------------------------------------------------------------------------
PROBLEMS = [
    ("fa-solid fa-users-viewfinder", "Hard to distinguish", "Guards struggle to quickly tell students, lecturers and visitors apart."),
    ("fa-solid fa-id-card", "Cards must be carried", "ID cards can be forgotten, misplaced or lost."),
    ("fa-solid fa-hourglass-half", "Slow manual checks", "Verification takes extra time when many people enter or leave together."),
    ("fa-solid fa-clock-rotate-left", "No automatic records", "There is no convenient system for exact entry and exit times."),
    ("fa-solid fa-folder-open", "Hard to retrieve data", "Management cannot easily monitor and retrieve records."),
]

OBJECTIVES = [
    ("fa-solid fa-window-restore", "User-friendly interface", "A clear graphical interface for managing the Smart Gate system."),
    ("fa-solid fa-camera", "Webcam registration", "Register users with their basic details and webcam face images."),
    ("fa-solid fa-user-check", "Verify faces", "Recognise registered users and show “Unknown” if not registered."),
    ("fa-solid fa-ban", "One person, one ID", "Prevent one person from holding more than one ID."),
    ("fa-solid fa-stopwatch", "Automatic time stamps", "Record entry and exit date and time automatically."),
    ("fa-solid fa-file-export", "Search and export", "Search, view and export entry and exit records."),
]

FEATURES = [
    ("fa-solid fa-user-plus", "User Registration", "Form with live validation and a webcam photo for students, lecturers and guests.", "Feature 1"),
    ("fa-solid fa-fingerprint", "Duplicate Face Check", "A face already registered under another ID is blocked: one person, one ID.", "Feature 2"),
    ("fa-solid fa-face-smile-beam", "Face Verification", "YOLO finds the face, SFace identifies it. Registered: green box and “Identity Verified”. Otherwise “Unknown”.", "Feature 3"),
    ("fa-solid fa-right-left", "Entry / Exit Recording", "Records identity, date and time; the next action is the opposite of the last one.", "Feature 4"),
    ("fa-solid fa-magnifying-glass-chart", "Records, Search and Export", "Search by name, ID or date, filter Inside/Outside, sort, and export to CSV.", "Feature 5"),
    ("fa-solid fa-gauge-high", "Dashboard and Reports", "Live counts, who is inside, recent activity and entry activity by time of day.", "Feature 6"),
    ("fa-solid fa-user-shield", "Staff Accounts and Roles", "Administrator adds staff, assigns roles and resets passwords. Pages depend on the role.", "Feature 7"),
]

# name, purpose, icon, category
TECH = [
    ("Python 3", "Main programming language", "fa-brands fa-python", "Core"),
    ("Tkinter and ttk", "GUI: screens, tables, forms", "fa-solid fa-window-maximize", "Core"),
    ("YOLOv8n-face", "Pretrained model that finds faces (Ultralytics)", "fa-solid fa-crosshairs", "Vision / AI"),
    ("SFace (OpenCV)", "Pretrained model that recognises faces", "fa-solid fa-face-smile", "Vision / AI"),
    ("OpenCV", "Webcam frames and image handling", "fa-solid fa-video", "Vision / AI"),
    ("NumPy", "Face “fingerprints” as arrays", "fa-solid fa-table-cells", "Vision / AI"),
    ("Pillow (PIL)", "Shows camera frames in Tkinter", "fa-solid fa-image", "Core"),
    ("threading", "Camera runs in background", "fa-solid fa-diagram-project", "Core"),
    ("SQLite (sqlite3)", "Local database for users, logs, staff", "fa-solid fa-database", "Data"),
    ("PNG image files", "Registered face photos", "fa-solid fa-file-image", "Data"),
    ("datetime", "Entry/exit time in Bhutan Time (UTC+6)", "fa-solid fa-calendar-days", "Data"),
    ("CSV", "Exports records for reports", "fa-solid fa-file-csv", "Data"),
    ("hashlib and hmac", "Salted PBKDF2 password hashing", "fa-solid fa-key", "Security"),
    ("Figma", "Designing the wireframe", "fa-brands fa-figma", "Design"),
]

USERS = {
    "Students": ("fa-solid fa-graduation-cap", "Verify identity at the gate and record entry and exit."),
    "Lecturers": ("fa-solid fa-chalkboard-user", "Verify identity and record campus entry and exit."),
    "Security Guards": ("fa-solid fa-user-shield", "Verify users and monitor entry and exit activities."),
    "College Management": ("fa-solid fa-building-columns", "View, search and manage entry and exit records."),
    "System Administrator": ("fa-solid fa-user-gear", "Register users and manage system information."),
}

IN_SCOPE = [
    "Registration with webcam face capture", "Face detection (YOLO) and recognition (SFace)", "Duplicate-face check",
    "Recording entry and exit times", "Storing data in SQLite", "Searching, viewing and exporting records",
    "Simple dashboard for guards and management", "Staff accounts with role-based access",
]
OUT_SCOPE = [
    "Real-time connection to the entire college security infrastructure", "CCTV integration and recognition of faces in crowds",
    "Liveness detection (a printed photo may be accepted)", "Training our own face models and fingerprint hardware",
    "Mobile application development", "Online / cloud-based access to records", "Integration with official college ID-card systems",
]

SCREENS = [
    ("fa-solid fa-right-to-bracket", "Login / First Setup", "Allows authorised security guards or administrators to access the system."),
    ("fa-solid fa-house-chimney", "Home / Dashboard", "Displays the main functions of the Smart Gate system."),
    ("fa-solid fa-user-plus", "User Registration", "Enter details and capture face photos through the webcam."),
    ("fa-solid fa-camera-retro", "Face Verification", "Live camera, detects and recognises the face, shows the result."),
    ("fa-solid fa-door-open", "Entry / Exit", "Displays and records the user's entry or exit information."),
    ("fa-solid fa-table-list", "Records / Search", "Search, view and export entry and exit records."),
]

PHASES = [  # start week, end week, activity, icon
    (1, 2, "Project Topic Selection & Research", "fa-solid fa-lightbulb"),
    (3, 4, "Proposal Writing", "fa-solid fa-pen-to-square"),
    (5, 5, "Proposal Presentation", "fa-solid fa-person-chalkboard"),
    (6, 6, "Feedback & Revision", "fa-solid fa-comments"),
    (7, 10, "System Design", "fa-solid fa-pen-ruler"),
    (11, 11, "Implementation", "fa-solid fa-code"),
    (12, 12, "Integration", "fa-solid fa-puzzle-piece"),
    (13, 13, "Testing & Debugging", "fa-solid fa-bug"),
    (14, 14, "Final Write-up & Preparation", "fa-solid fa-file-lines"),
    (15, 15, "Final Presentation & Submission", "fa-solid fa-flag-checkered"),
]

RISKS = [
    ("Limited Python knowledge", "Use Python/Tkinter tutorials, documentation and consult the module tutor."),
    ("Webcam not detected or blocked on the PC", "Test the camera early with a separate test script, allow camera access in Windows privacy settings, and close other programs using the camera."),
    ("Recognition errors in poor or changing lighting", "Capture 25 photos per person with small head movements, and tune the match threshold during testing."),
    ("Same person registered under two IDs", "Run a duplicate-face check with its own threshold at capture and again at registration, and test it with real faces."),
    ("Lookalikes or a photo held to the camera may be accepted", "State this as a known limitation; liveness detection can be future work."),
    ("OpenCV version problems", "Install a compatible OpenCV build and show a clear error message if the wrong version is found."),
    ("Database connection problems", "Design and test the SQLite database early."),
    ("Limited development time", "Prioritise the core features before adding optional features."),
    ("GUI design difficulties", "Create a wireframe before beginning implementation."),
    ("Privacy and data security of face images", "Store face data only on the local PC and restrict access to records through an administrator/security login."),
    ("Testing difficulties", "Test each module separately before integrating the complete system."),
]

TEAM = [
    ("Chimi Wangmo", "Chimi Wangmo.jpg"),
    ("Dema Lhamo", "Dema Lhamo.jpg"),
    ("Lekzin Cheki Wangmo", "Lekzin Cheki Wangmo.jpg"),
    ("Rinzin Wangmo", "Rinzin Wangmo.jpg"),
    ("Tshering Choden", "Tshering Choden.jpg"),
]

# ----------------------------------------------------------------------------
# INJECT THEME + HERO
# ----------------------------------------------------------------------------
md(EARTH_CSS)

md(f"""
<div class="hero">
  <div class="hero-photo"><img src="{image_data_uri('college.jpeg')}" alt="Samtse College of Education campus"></div>
  <div class="hero-inner">
    <div class="hero-kicker"><i class="fa-solid fa-leaf"></i> Smart Gate Project</div>
    <h1>Smart <span>Gate</span></h1>
    <div class="hero-topic">
      <div class="hero-topic-label">Our project topic</div>
      <p>Face Recognition-Based Entry and Exit Management System</p>
      <div class="hero-topic-school">Samtse College of Education</div>
    </div>
    <div class="hero-meta">
      <span><i class="fa-solid fa-graduation-cap"></i> Python GUI Programming</span>
      <span><i class="fa-solid fa-calendar-days"></i> Academic Year 2026</span>
    </div>
  </div>
</div>
""")

# ----------------------------------------------------------------------------
# NAVIGATION
# ----------------------------------------------------------------------------
NAV_ITEMS = [
    "Overview",
    "Problem & Solution",
    "Features",
    "Technology",
    "How It Works",
    "Users & Scope",
    "Database",
    "Roadmap & Risks",
]


def navigate_to(page: str) -> None:
    st.session_state["dashboard_navigation"] = page


if "dashboard_navigation" not in st.session_state:
    st.session_state["dashboard_navigation"] = NAV_ITEMS[0]

selected_page = st.segmented_control(
    "Dashboard navigation",
    NAV_ITEMS,
    selection_mode="single",
    key="dashboard_navigation",
    label_visibility="collapsed",
)

# ============================ 1. OVERVIEW ====================================
if selected_page == NAV_ITEMS[0]:
    section("fa-solid fa-leaf", "Welcome to Smart Gate", "What Smart Gate is, in one minute")
    callout("fa-solid fa-lightbulb", "Our idea",
            "A webcam at the college gate captures a person's face, compares it with registered students and lecturers, "
            "shows the identity, and automatically records the entry or exit time. A face is always with the person, "
            "so there is no ID card to forget, misplace or lose.")
    callout("fa-solid fa-bullseye", "Project aim",
            "To develop a Smart Gate entry and exit management system using Python GUI and face recognition that "
            "efficiently verifies students and lecturers and maintains their campus entry and exit records.")

    metrics = [
        ("7", "Core features", "Features", "features"),
        ("6", "Objectives", "Overview", "objectives"),
        ("5", "User roles", "Users & Scope", "roles"),
        ("128", "Numbers per face", "How It Works", "face_numbers"),
        ("0.60", "Match threshold", "How It Works", "match_threshold"),
        ("6", "Frames to confirm", "How It Works", "frames"),
    ]
    metric_columns = st.columns(6)
    for column, (value, label, destination, key) in zip(metric_columns, metrics):
        with column:
            st.button(
                f"**{value}**  \n{label}",
                key=f"summary_{key}",
                on_click=navigate_to,
                args=(destination,),
                use_container_width=True,
                type="secondary",
            )

    section("fa-solid fa-list-check", "Project objectives", "What the finished application will do")
    grid([card(i, t, d, num=f"0{n}") for n, (i, t, d) in enumerate(OBJECTIVES, 1)], "g3")

    section("fa-solid fa-desktop", "Interface at a glance", "A clean Tkinter interface built around a central dashboard")
    grid([card(i, t, d) for i, t, d in SCREENS], "g3")

# ======================= 2. PROBLEM & SOLUTION ===============================
if selected_page == NAV_ITEMS[1]:
    section("fa-solid fa-triangle-exclamation", "The problem",
            "The guard currently relies mainly on identification cards")
    grid([card(i, t, d, cls="warn") for i, t, d in PROBLEMS], "g3")

    section("fa-solid fa-life-ring", "Our answer", "Why face recognition fits the college gate")
    callout("fa-solid fa-face-smile-beam", "One simple idea",
            "A face is always with the person, so face recognition removes the need to carry or show a card.")

    md("""
    <table class="cmp">
      <tr><th>Area</th><th>Today: ID card check</th><th>With Smart Gate</th></tr>
      <tr><td>Verification</td>
          <td class="bad"><i class="fa-solid fa-circle-xmark"></i>Guard checks a card by eye</td>
          <td class="good"><i class="fa-solid fa-circle-check"></i>Webcam recognises the face</td></tr>
      <tr><td>Forgotten or lost card</td>
          <td class="bad"><i class="fa-solid fa-circle-xmark"></i>Cards can be forgotten, misplaced or lost</td>
          <td class="good"><i class="fa-solid fa-circle-check"></i>Nothing to carry</td></tr>
      <tr><td>Entry / exit records</td>
          <td class="bad"><i class="fa-solid fa-circle-xmark"></i>No convenient record of exact times</td>
          <td class="good"><i class="fa-solid fa-circle-check"></i>Date and time saved automatically</td></tr>
      <tr><td>Finding records</td>
          <td class="bad"><i class="fa-solid fa-circle-xmark"></i>Hard for management to retrieve</td>
          <td class="good"><i class="fa-solid fa-circle-check"></i>Search by name, ID or date and export to CSV</td></tr>
    </table>
    """)

# ============================== 3. FEATURES ==================================
if selected_page == NAV_ITEMS[2]:
    section("fa-solid fa-wand-magic-sparkles", "Proposed features", "Seven features that make up Smart Gate")
    grid([card(i, t, d, tag=g) for i, t, d, g in FEATURES], "g3")

    section("fa-solid fa-magnifying-glass", "Explore a feature", "Pick one to see it in focus")
    names = [f[1] for f in FEATURES]
    pick = st.selectbox("Feature", names, label_visibility="collapsed", key="feat_pick")
    f = FEATURES[names.index(pick)]
    callout(f[0], f[1], f[2])

# ============================= 4. TECHNOLOGY =================================
if selected_page == NAV_ITEMS[3]:
    section("fa-solid fa-microchip", "Technologies and tools", "Everything Smart Gate is built with")
    cats = ["All", "Core", "Vision / AI", "Data", "Security", "Design"]
    cat = st.radio("Filter by category", cats, horizontal=True, key="tech_cat")
    shown = [t for t in TECH if cat == "All" or t[3] == cat]
    grid([card(ic, n, p, tag=c) for n, p, ic, c in shown], "g4")
    callout("fa-solid fa-circle-info", "Pretrained models",
            "Smart Gate uses pretrained YOLO and SFace models. We do not train our own face models.")

# ============================= 5. HOW IT WORKS ===============================
if selected_page == NAV_ITEMS[4]:
    section("fa-solid fa-diagram-project", "Proposed system workflow", "From camera frame to saved record")
    md("""
    <div class="pipe">
      <div class="step"><span class="no">STEP 1</span><div class="ico"><i class="fa-solid fa-video"></i></div><h5>Webcam captures a frame</h5><p>Live view at the gate</p></div>
      <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
      <div class="step"><span class="no">STEP 2</span><div class="ico"><i class="fa-solid fa-crosshairs"></i></div><h5>YOLO finds the face</h5><p>Face is located in the frame</p></div>
      <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
      <div class="step"><span class="no">STEP 3</span><div class="ico"><i class="fa-solid fa-fingerprint"></i></div><h5>SFace makes 128 numbers</h5><p>A face “fingerprint”</p></div>
      <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
      <div class="step"><span class="no">STEP 4</span><div class="ico"><i class="fa-solid fa-scale-balanced"></i></div><h5>Match ≥ 0.60</h5><p>Same person for 6 frames</p></div>
      <div class="arrow"><i class="fa-solid fa-chevron-right"></i></div>
      <div class="step"><span class="no">STEP 5</span><div class="ico"><i class="fa-solid fa-database"></i></div><h5>Entry / Exit saved</h5><p>Stored in SQLite</p></div>
    </div>
    """)
    grid([
        card("fa-solid fa-circle-check", "Registered person",
             "Green box with the name, an “Identity Verified” card, then the Entry/Exit screen.", tag="Match"),
        card("fa-solid fa-circle-question", "Any other face",
             "Red box labelled “Unknown”; no entry or exit is recorded.", tag="No match", cls="warn"),
    ], "g2")

    section("fa-solid fa-sliders", "Try the gate yourself",
            "A small simulation of the decision rule: a match score of at least 0.60, held for 6 frames")
    left, right = st.columns([1, 1], gap="large")
    with left:
        score = st.slider("Face match score (similarity)", 0.00, 1.00, 0.72, 0.01, key="sim_score")
        frames = st.slider("Consecutive frames with the same person", 0, 10, 6, key="sim_frames")
        last = st.radio("Last recorded action for this person", ["None yet", "Entry", "Exit"],
                        horizontal=True, key="sim_last")
        st.progress(min(frames / 6, 1.0), text=f"Confirmation progress: {min(frames, 6)} / 6 frames")
    with right:
        if score < 0.60:
            md('<div class="result bad"><i class="fa-solid fa-circle-xmark"></i><h3>Unknown</h3>'
               '<p>Score is below 0.60. Red box shown. No entry or exit is recorded.</p></div>')
        elif frames < 6:
            md(f'<div class="result wait"><i class="fa-solid fa-hourglass-half"></i><h3>Verifying…</h3>'
               f'<p>Good match, but only {frames} of 6 frames so far. Keep looking at the camera.</p></div>')
        else:
            nxt = "EXIT" if last == "Entry" else "ENTRY"
            now = datetime.now(timezone(timedelta(hours=6))).strftime("%d/%m/%Y  %I:%M %p")
            md(f'<div class="result ok"><i class="fa-solid fa-circle-check"></i><h3>Identity Verified</h3>'
               f'<p>Recorded: <b>{nxt}</b> &nbsp;•&nbsp; {now} (Bhutan Time)</p></div>')

    callout("fa-solid fa-shield-halved", "Known limitation",
            "Smart Gate has no liveness detection, so a printed photo held to the camera may be accepted. "
            "This is stated as a limitation and noted as future work.")

# ============================ 6. USERS & SCOPE ===============================
if selected_page == NAV_ITEMS[5]:
    section("fa-solid fa-users", "Target users", "Who will use Smart Gate and how")
    grid([card(i, r, d) for r, (i, d) in USERS.items()], "g3")
    role = st.selectbox("See it from a role's point of view", list(USERS.keys()), key="role_pick")
    callout(USERS[role][0], role, USERS[role][1])

    section("fa-solid fa-crop-simple", "Project scope", "What we will and will not build")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        md('<div class="callout"><h4><i class="fa-solid fa-circle-check" style="color:#657b55"></i>In scope</h4></div>')
        for s in IN_SCOPE:
            st.markdown(f":material/check_circle: {s}")
    with c2:
        md('<div class="callout"><h4><i class="fa-solid fa-circle-xmark" style="color:#b85f48"></i>Out of scope</h4></div>')
        for s in OUT_SCOPE:
            st.markdown(f":material/cancel: {s}")

# ============================== 7. DATABASE ==================================
if selected_page == NAV_ITEMS[6]:
    section("fa-solid fa-database", "Database design", "One user has many logs. Data stays on the local PC in SQLite.")
    st.graphviz_chart("""
    digraph ERD {
      rankdir=LR; bgcolor="transparent"; nodesep=0.6; ranksep=1.2;
      node [shape=plaintext, fontname="Helvetica", fontcolor="#51473d"];
      edge [color="#8b6548", fontcolor="#80543b", fontname="Helvetica", penwidth=2];
      USERS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7" COLOR="#8b6548">
        <TR><TD BGCOLOR="#d9a475"><B>USERS</B></TD></TR>
        <TR><TD ALIGN="LEFT">uid (PK)</TD></TR><TR><TD ALIGN="LEFT">name</TD></TR>
        <TR><TD ALIGN="LEFT">role (Student / Lecturer)</TD></TR><TR><TD ALIGN="LEFT">programme</TD></TR>
        <TR><TD ALIGN="LEFT">face photo location</TD></TR></TABLE>>];
      LOGS [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7" COLOR="#8b6548">
        <TR><TD BGCOLOR="#d9a475"><B>LOGS</B></TD></TR>
        <TR><TD ALIGN="LEFT">uid (links to users.uid)</TD></TR><TR><TD ALIGN="LEFT">date</TD></TR>
        <TR><TD ALIGN="LEFT">time</TD></TR><TR><TD ALIGN="LEFT">entry / exit status</TD></TR></TABLE>>];
      STAFF [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7" COLOR="#8b6548">
        <TR><TD BGCOLOR="#d9a475"><B>STAFF</B></TD></TR>
        <TR><TD ALIGN="LEFT">guard / admin login</TD></TR><TR><TD ALIGN="LEFT">salted PBKDF2 hash</TD></TR>
        <TR><TD ALIGN="LEFT">role</TD></TR></TABLE>>];
      APP_META [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7" COLOR="#8b6548">
        <TR><TD BGCOLOR="#d9a475"><B>APP_META</B></TD></TR><TR><TD ALIGN="LEFT">application information</TD></TR></TABLE>>];
      USERS -> LOGS [label=" 1 : many "];
    }
    """)
    st.caption("The link between logs.uid and users.uid is made in the application code (no SQL FOREIGN KEY is declared). "
               "STAFF and APP_META are standalone.")

    section("fa-solid fa-table", "Example record", "What one gate activity looks like")
    st.dataframe(pd.DataFrame([{
        "User ID": "08230220", "Full Name": "Karma Wangchuk", "Role": "Student",
        "Face data": "Face scan saved", "Entry/Exit Status": "Entry", "Date": "07/08/2026", "Time": "08:15 AM",
    }]), hide_index=True)

    callout("fa-solid fa-lock", "Privacy first",
            "Face data is stored only on the local PC, passwords use salted PBKDF2 hashing, and access to records "
            "is restricted through an administrator/security login.")

# ========================== 8. ROADMAP & RISKS ===============================
if selected_page == NAV_ITEMS[7]:
    section("fa-solid fa-route", "Project road map", "Slide the week to see where we are in the 15-week plan")
    week = st.slider("Current week", 1, 15, 5, key="road_week")
    st.progress(week / 15, text=f"Week {week} of 15")
    items = []
    for a, b, act, ic in PHASES:
        state = "done" if b < week else ("now" if a <= week <= b else "")
        wk = f"Week {a}" if a == b else f"Weeks {a}–{b}"
        items.append(f'<div class="tl-item {state}"><div class="wk">{wk}</div>'
                     f'<div class="ac"><i class="{ic}" style="color:#a86646;margin-right:10px"></i>{act}</div></div>')
    md('<div class="tl">' + "".join(items) + "</div>")

    section("fa-solid fa-life-ring", "Risks and challenges", "What could go wrong, and how we plan to handle it")
    q = st.text_input("Search risks", placeholder="e.g. webcam, lighting, privacy…", key="risk_q")
    hits = [r for r in RISKS if q.lower() in (r[0] + r[1]).lower()]
    if not hits:
        st.info("No matching risk found.")
    for r, s in hits:
        with st.expander(f":material/warning: {r}"):
            st.markdown(f":material/lightbulb: **Possible solution:** {s}")

# ----------------------------------------------------------------------------
# TEAM + FOOTER (always visible)
# ----------------------------------------------------------------------------
section("fa-solid fa-people-group", "Meet the crew", "BED IT ‘C’  •  Python GUI Programming  •  Tutor: Phurba Dorji Tamang")
grid([f'<div class="member"><div class="avatar"><img src="{image_data_uri(filename)}" alt="Portrait of {name}"></div>'
      f'<h4>{name}</h4><p>Smart Gate team</p></div>'
      for name, filename in TEAM], "g5")

md("""
<div class="footer">
  <i class="fa-solid fa-leaf"></i> Smart Gate &nbsp;•&nbsp; Samtse College of Education &nbsp;•&nbsp; Academic Year 2026<br>
  Built with <i class="fa-brands fa-python"></i> Python and Streamlit
</div>
""")
