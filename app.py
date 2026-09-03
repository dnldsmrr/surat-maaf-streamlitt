"""
Surat Maaf — versi Streamlit
=============================
Halaman minta maaf interaktif. Klik "iya" untuk lanjut ke pesan berikutnya,
tombol "nggak" akan kabur setiap kali didekati.

Cara jalanin:
    pip install -r requirements.txt
    streamlit run app.py

Cara kustomisasi: ubah GIRLFRIEND_NAME dan isi PAGES / FINAL di bawah ini.
Tidak perlu menyentuh bagian HTML/CSS/JS.
"""

import streamlit.components.v1 as components
import streamlit as st

# ---------------------------------------------------------------------------
# 1. KONTEN — edit bagian ini sesuka kamu
# ---------------------------------------------------------------------------

GIRLFRIEND_NAME = "Raisa Sayangku Cintaku"  # ganti dengan nama panggilannya kalau mau

PAGES = [
    {
        "eyebrow": "satu pesan kecil",
        "heading": f"buat {GIRLFRIEND_NAME},",
        "body": "sebelum u tutup ini &mdash; boleh i minta waktu bentar buat ngomong?",
        "yes": "boleh, lanjut",
        "no": "nggak dulu",
    },
    {
        "eyebrow": "satu",
        "heading": "i tau i salah.",
        "body": "dan i tau, kata &ldquo;maaf&rdquo; doang kadang kedengeran gampang banget "
                "diucapin &mdash; padahal yang u rasain ngga sesimpel itu.",
        "yes": "iya, lanjutin",
        "no": "cukup segini aja",
    },
    {
        "eyebrow": "dua",
        "heading": "yang paling i sesali...",
        "body": "bukan cuma bikin u kecewa, tapi caranya sampai bikin u ngerasa nggak "
                "diprioritasin. itu nggak seharusnya terjadi, sama sekali.",
        "yes": "terusin",
        "no": "udahan aja",
    },
    {
        "eyebrow": "tiga",
        "heading": "i pengen berubah, bukan cuma janji.",
        "body": "i mau belajar lebih sabar dengerin i, lebih peka sama hal-hal kecil, "
                "dan nggak ngulang kesalahan yang sama lagi.",
        "yes": "i percaya",
        "no": "belum yakin",
    },
    {
        "eyebrow": "empat",
        "heading": "boleh i dapet satu kesempatan lagi?",
        "body": "nggak buat ngebenerin semuanya sekaligus &mdash; tapi buat mulai pelan-pelan "
                "jadi lebih baik. bareng kamu.",
        "yes": "boleh",
        "no": "nanti dulu",
    },
]

FINAL = {
    "eyebrow": "selesai",
    "heading": "makasih udah mau baca sampai sini.",
    "body": f"itu aja udah cukup buat i ngerasa masih ada harapan. maaf, ya, {GIRLFRIEND_NAME}.",
    "sign": "dari i , dengan sayang.",
}

COMPONENT_HEIGHT = 860

# ---------------------------------------------------------------------------
# 2. TEMPLATE HTML/CSS/JS — biasanya tidak perlu diubah
# ---------------------------------------------------------------------------

_PAGE_TEMPLATE = """
<section class="page{active_cls}" data-index="{index}">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{heading}</h1>
  <p class="body-text">{body}</p>
  <div class="actions">
    <button class="btn-yes" type="button">{yes}</button>
    <button class="btn-no" type="button">{no}</button>
  </div>
  <p class="taunt"></p>
</section>
"""

_FINAL_TEMPLATE = """
<section class="page final" data-index="{index}">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{heading}</h1>
  <p class="body-text">{body}</p>
  <p class="sign">{sign}</p>
  <button class="restart" type="button" id="restart">baca ulang dari awal</button>
  <div class="burst" id="burst"></div>
</section>
"""

_DOC_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Surat Maaf</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,500;1,9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Caveat:wght@500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#fff3ef;
    --bg-2:#ffe3da;
    --surface:#ffffff;
    --surface-2:#ffefea;
    --ink:#2e1f26;
    --muted:#8c6f7a;
    --accent:#e0486b;
    --accent-ink:#fff8f7;
    --accent-2:#ffb86b;
    --line:#f1d9dc;
    --shadow:rgba(155,40,70,0.20);
    --dot-off:rgba(140,111,122,0.28);
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --bg:#1b1116; --bg-2:#241620; --surface:#2a1b22; --surface-2:#351f29;
      --ink:#fbeaee; --muted:#c9a3af; --accent:#ff6b8b; --accent-ink:#2a1119;
      --accent-2:#ffb86b; --line:#3a2530; --shadow:rgba(0,0,0,0.45);
      --dot-off:rgba(201,163,175,0.28);
    }
  }
  *{ box-sizing:border-box; }
  html,body{ margin:0; height:100%; }
  body{
    min-height:100%;
    background:
      radial-gradient(60% 50% at 85% 8%, color-mix(in srgb, var(--accent-2) 30%, transparent), transparent),
      linear-gradient(155deg, var(--bg), var(--bg-2));
    color:var(--ink);
    font-family:"Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:2.5rem 1.25rem;
    position:relative;
    overflow-x:hidden;
  }
  .float-heart{
    position:fixed; top:100%; font-size:1.4rem; color:var(--accent);
    opacity:0.35; pointer-events:none; animation:drift linear infinite;
    will-change:transform; z-index:0;
  }
  @keyframes drift{
    0%{ transform:translateY(0) translateX(0) rotate(0deg); opacity:0; }
    10%{ opacity:0.35; } 90%{ opacity:0.25; }
    100%{ transform:translateY(-115vh) translateX(var(--drift-x,20px)) rotate(25deg); opacity:0; }
  }
  @media (prefers-reduced-motion: reduce){ .float-heart{ display:none; } }
  .letter{
    position:relative; width:100%; max-width:428px; background:var(--surface);
    border-radius:26px; padding:2.25rem 1.9rem 2rem;
    box-shadow:0 24px 60px -18px var(--shadow), 0 2px 0 var(--line) inset;
    transform:rotate(-1.1deg); z-index:1;
  }
  .letter::before, .letter::after{
    content:""; position:absolute; inset:0; background:var(--surface-2);
    border-radius:inherit; z-index:-1;
  }
  .letter::before{ transform:rotate(2.4deg); }
  .letter::after{ transform:rotate(-3.4deg); opacity:0.7; }
  .stamp{
    position:absolute; top:-14px; right:22px; width:46px; height:46px;
    border-radius:50%; background:var(--accent); color:var(--accent-ink);
    display:flex; align-items:center; justify-content:center; font-size:1.35rem;
    box-shadow:0 8px 18px -6px var(--shadow); transform:rotate(8deg);
  }
  .progress{ display:flex; gap:7px; justify-content:center; margin-bottom:1.5rem; }
  .dot{
    width:9px; height:9px; border-radius:50%; background:var(--dot-off);
    transition:background .3s ease, transform .3s ease;
  }
  .dot.done{ background:var(--accent); }
  .dot.current{ background:var(--accent-2); transform:scale(1.35); }
  .pages{ position:relative; min-height:236px; }
  .page{ display:none; flex-direction:column; }
  .page.active{ display:flex; animation:rise .38s cubic-bezier(.2,.8,.3,1); }
  @keyframes rise{ from{ opacity:0; transform:translateY(10px); } to{ opacity:1; transform:translateY(0); } }
  @media (prefers-reduced-motion: reduce){ .page.active{ animation:none; } }
  .eyebrow{
    font-size:0.72rem; font-weight:600; letter-spacing:0.11em; text-transform:uppercase;
    color:var(--muted); margin:0 0 0.6rem;
  }
  h1{
    font-family:"Fraunces", ui-serif, Georgia, serif; font-style:italic; font-weight:500;
    font-size:clamp(1.55rem, 6.5vw, 2.05rem); line-height:1.18; margin:0 0 0.85rem;
    text-wrap:balance; color:var(--ink);
  }
  p.body-text{ font-size:1.02rem; line-height:1.65; color:var(--ink); margin:0; max-width:38ch; }
  .actions{ position:relative; height:104px; margin-top:1.6rem; }
  button{
    font-family:inherit; border:none; cursor:pointer; border-radius:999px; font-weight:600;
    font-size:0.96rem; padding:0.8rem 1.5rem; position:absolute; top:0;
    transition:transform .18s ease, box-shadow .18s ease, left .22s cubic-bezier(.3,.9,.4,1), top .22s cubic-bezier(.3,.9,.4,1);
  }
  button:focus-visible{ outline:2px solid var(--accent); outline-offset:3px; }
  .btn-yes{
    left:0; background:var(--accent); color:var(--accent-ink);
    box-shadow:0 10px 22px -8px var(--shadow); transform:scale(var(--yes-scale, 1));
    transform-origin:left center;
  }
  .btn-yes:hover{ box-shadow:0 14px 26px -8px var(--shadow); }
  .btn-no{ left:calc(100% - 128px); background:transparent; color:var(--muted); border:1.5px solid var(--line); }
  .taunt{ min-height:1.1rem; margin:0.7rem 0 0; font-size:0.85rem; color:var(--muted); font-style:italic; }
  .final{ text-align:left; }
  .final .sign{ font-family:"Caveat", cursive; font-size:1.9rem; color:var(--accent); margin:1.1rem 0 0; }
  .restart{
    display:inline-block; margin-top:1.4rem; font-size:0.85rem; color:var(--muted);
    text-decoration:underline; text-underline-offset:3px; cursor:pointer; background:none;
    border:none; padding:0; font-family:inherit; position:static;
  }
  .burst{ position:absolute; inset:0; pointer-events:none; overflow:visible; }
  .burst span{
    position:absolute; left:var(--x); top:60%; font-size:var(--s); color:var(--accent);
    animation:pop 1.1s ease-out forwards; animation-delay:var(--d); opacity:0;
  }
  @keyframes pop{
    0%{ transform:translateY(0) scale(0.4) rotate(0deg); opacity:0; }
    18%{ opacity:0.9; }
    100%{ transform:translateY(-130px) scale(1) rotate(20deg); opacity:0; }
  }
</style>
</head>
<body>

<div class="letter">
  <div class="stamp">&#128140;</div>
  <div class="progress" id="progress"></div>
  <div class="pages" id="pages">
___PAGES___
  </div>
</div>

<script>
(function(){
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if(!reduceMotion){
    var heartsLayer = document.createElement('div');
    document.body.appendChild(heartsLayer);
    for(var i=0;i<7;i++){
      var h = document.createElement('span');
      h.className = 'float-heart';
      h.textContent = '♥';
      h.style.left = (Math.random()*94 + 2) + 'vw';
      h.style.setProperty('--drift-x', (Math.random()*60 - 30) + 'px');
      h.style.animationDuration = (14 + Math.random()*10) + 's';
      h.style.animationDelay = (Math.random()*12) + 's';
      h.style.fontSize = (1 + Math.random()*0.9) + 'rem';
      heartsLayer.appendChild(h);
    }
  }

  var pages = Array.prototype.slice.call(document.querySelectorAll('.page'));
  var progressEl = document.getElementById('progress');
  var totalSteps = pages.length - 1;
  var current = 0;
  var dodgeCount = 0;

  var taunts = [
    'eh, kok lari?', 'gak semudah itu~', 'coba tangkep dulu deh', 'yaah, meleset',
    'sabar dong, Sayang', 'ngaku aja, ini lucu kan', 'tombolnya emang nakal'
  ];

  for(var d=0; d<totalSteps; d++){
    var dot = document.createElement('span');
    dot.className = 'dot';
    progressEl.appendChild(dot);
  }

  function renderProgress(){
    var dots = progressEl.children;
    for(var i=0;i<dots.length;i++){
      dots[i].className = 'dot' + (i < current ? ' done' : (i === current ? ' current' : ''));
    }
  }

  function showPage(i){
    pages.forEach(function(p, idx){ p.classList.toggle('active', idx === i); });
    renderProgress();
    if(i === pages.length - 1){ launchBurst(); }
  }

  function placeNoButton(btn, actions){
    var aRect = actions.getBoundingClientRect();
    var bRect = btn.getBoundingClientRect();
    var maxLeft = Math.max(aRect.width - bRect.width, 0);
    var maxTop = Math.max(aRect.height - bRect.height, 0);
    var left = Math.random() * maxLeft;
    var top = Math.random() * maxTop;
    if(left < bRect.width * 0.8){ left = Math.min(maxLeft, left + bRect.width * 0.9); }
    btn.style.left = left + 'px';
    btn.style.top = top + 'px';
  }

  function bumpYes(page){
    var yes = page.querySelector('.btn-yes');
    var scale = Math.min(1 + dodgeCount * 0.028, 1.32);
    yes.style.setProperty('--yes-scale', scale);
  }

  function dodge(e, page){
    e.preventDefault();
    var btn = e.currentTarget;
    var actions = btn.closest('.actions');
    placeNoButton(btn, actions);
    dodgeCount++;
    bumpYes(page);
    var taunt = page.querySelector('.taunt');
    if(taunt){ taunt.textContent = taunts[dodgeCount % taunts.length]; }
  }

  pages.forEach(function(page){
    var yesBtn = page.querySelector('.btn-yes');
    var noBtn = page.querySelector('.btn-no');
    if(!noBtn) return;
    ['pointerenter','touchstart','focus','click'].forEach(function(evt){
      noBtn.addEventListener(evt, function(e){ dodge(e, page); }, { passive:false });
    });
    yesBtn.addEventListener('click', function(){
      if(current < pages.length - 1){ current++; showPage(current); }
    });
  });

  var restartBtn = document.getElementById('restart');
  if(restartBtn){
    restartBtn.addEventListener('click', function(){
      current = 0; dodgeCount = 0;
      pages.forEach(function(page){
        var yes = page.querySelector('.btn-yes');
        if(yes) yes.style.setProperty('--yes-scale', 1);
        var noBtn = page.querySelector('.btn-no');
        if(noBtn){ noBtn.style.left = ''; noBtn.style.top = ''; }
        var taunt = page.querySelector('.taunt');
        if(taunt) taunt.textContent = '';
      });
      showPage(0);
    });
  }

  function launchBurst(){
    if(reduceMotion) return;
    var burst = document.getElementById('burst');
    if(!burst) return;
    burst.innerHTML = '';
    var glyphs = ['♥','♡','❤️'];
    for(var i=0;i<18;i++){
      var s = document.createElement('span');
      s.textContent = glyphs[i % glyphs.length];
      s.style.setProperty('--x', (Math.random()*90 + 2) + '%');
      s.style.setProperty('--s', (0.9 + Math.random()*1.1) + 'rem');
      s.style.setProperty('--d', (Math.random()*0.5) + 's');
      burst.appendChild(s);
    }
  }

  renderProgress();
})();
</script>
</body>
</html>
"""


def _build_pages_html() -> str:
    blocks = []
    for i, page in enumerate(PAGES):
        blocks.append(
            _PAGE_TEMPLATE.format(
                active_cls=" active" if i == 0 else "",
                index=i,
                eyebrow=page["eyebrow"],
                heading=page["heading"],
                body=page["body"],
                yes=page["yes"],
                no=page["no"],
            )
        )
    blocks.append(
        _FINAL_TEMPLATE.format(
            index=len(PAGES),
            eyebrow=FINAL["eyebrow"],
            heading=FINAL["heading"],
            body=FINAL["body"],
            sign=FINAL["sign"],
        )
    )
    return "\n".join(blocks)


def build_document() -> str:
    return _DOC_TEMPLATE.replace("___PAGES___", _build_pages_html())


# ---------------------------------------------------------------------------
# 3. APLIKASI STREAMLIT
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Surat Maaf", page_icon="💌", layout="centered")

st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      .stApp { background: #fff3ef; }
      iframe { border: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_document(), height=COMPONENT_HEIGHT, scrolling=True)
