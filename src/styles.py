import streamlit as st


def apply_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap');

        :root {
          --ink: #1f302c;
          --muted: #77817d;
          --paper: #f8f8f5;
          --line: #e7e9e4;
          --green: #405d56;
          --rust: #bd7759;
        }
        .stApp { background: var(--paper); color: var(--ink); }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stSidebar"] {
          background: #f0f1ec;
          border-right: 1px solid var(--line);
        }
        [data-testid="stSidebar"] > div:first-child { padding-top: 1.4rem; }
        [data-testid="stSidebar"] [data-testid="stSidebarNav"] { padding-top: .7rem; }
        [data-testid="stSidebar"] [data-testid="stSidebarNav"] span {
          font-family: 'DM Sans', sans-serif;
          color: var(--ink);
          font-size: .9rem;
        }
        .sidebar-brand {
          display:flex; align-items:center; gap:10px; padding: 0 0 3px 8px;
          font: 600 1.28rem 'DM Sans', sans-serif; color:var(--ink); letter-spacing:-.05em;
        }
        .brand-mark {
          display:grid; place-items:center; width:31px; height:31px; border-radius:10px;
          background:var(--green); color:white; font-size:1rem; letter-spacing:-.08em;
        }
        .brand-dot { color:var(--rust); }
        .sidebar-caption {
          padding: 0 0 1.3rem 50px; color:#8b938e; font:600 .58rem 'DM Sans',sans-serif;
          letter-spacing:.13em;
        }
        .main .block-container { max-width:1120px; padding:2.2rem 2.8rem 3.5rem; }
        h1, h2, h3, p, label, button, [data-testid="stMetricValue"] {
          font-family:'DM Sans',sans-serif;
        }
        h1 { color:var(--ink); font-size:2.55rem; letter-spacing:-.055em; margin:.35rem 0 .6rem; }
        h2, h3 { color:var(--ink); letter-spacing:-.035em; }
        .eyebrow, .section-label {
          color:#8b938e; font:600 .66rem 'DM Sans',sans-serif; letter-spacing:.15em;
        }
        .hero {
          min-height:340px; margin:1.1rem 0 2.3rem; padding:2.3rem 3rem;
          background:#e9ede7; border-radius:8px; position:relative; overflow:hidden;
          display:flex; align-items:center;
        }
        .hero-copy { position:relative; z-index:2; max-width:580px; }
        .hero-kicker { color:var(--green); font:600 .78rem 'DM Sans',sans-serif; }
        .status-dot { display:inline-block; width:7px; height:7px; margin-right:7px;
          border-radius:50%; background:var(--rust); vertical-align:1px; }
        .hero h1 {
          font:500 clamp(2.6rem, 5vw, 4.35rem)/1.07 'Playfair Display',serif;
          letter-spacing:-.045em; margin:1.15rem 0 .85rem; color:var(--ink);
        }
        .hero h1 em { color:var(--rust); font-weight:500; }
        .hero-copy p { max-width:445px; color:#68736e; font-size:.98rem; line-height:1.7; }
        .hero-art { position:absolute; right:2.5%; top:0; width:42%; height:100%; overflow:hidden; }
        .art-orbit { position:absolute; border:1px solid rgba(64,93,86,.17); border-radius:50%; }
        .orbit-one { width:340px; height:340px; right:12px; top:20px; }
        .orbit-two { width:235px; height:235px; right:64px; top:72px; }
        .art-sun { position:absolute; width:110px; height:110px; border-radius:50%;
          background:#d8b99f; opacity:.72; right:75px; top:62px; }
        .art-ship {
          position:absolute; top:48%; right:18%; text-align:center;
          color:#f7f7f2; background:var(--green); padding:17px 30px 14px;
          clip-path:polygon(8% 0,92% 0,100% 77%,88% 100%,12% 100%,0 77%);
          font:600 .71rem 'DM Sans',sans-serif; letter-spacing:.12em; line-height:1.7;
          transform:rotate(-3deg); box-shadow:0 15px 35px #30443e22;
        }
        .art-ship span { color:#d5ddd5; font-size:.58rem; }
        .art-label { position:absolute; color:#84918a; font:600 .55rem 'DM Sans',sans-serif; letter-spacing:.16em; }
        .label-top { right:10%; top:18%; }
        .label-bottom { right:20%; bottom:13%; }
        .section-label { margin:1.2rem 0 .65rem; }
        .home-title { font:500 2rem 'Playfair Display',serif; margin:.15rem 0 .45rem; }
        .body-copy, .page-intro { color:var(--muted); line-height:1.75; max-width:590px; }
        .body-copy { margin:0 0 1.15rem; }
        .mini-card {
          border:1px solid var(--line); border-radius:8px; background:#fff;
          padding:1.3rem 1.45rem 1rem; margin-top:.55rem;
        }
        .mini-card-top { display:flex; align-items:center; gap:9px; color:#8b938e;
          font:600 .62rem 'DM Sans',sans-serif; letter-spacing:.13em; }
        .mini-icon { display:grid; place-items:center; background:#f4eee8; color:var(--rust);
          width:26px; height:26px; border-radius:7px; font-size:.95rem; }
        .mini-items { margin:1.1rem 0 .8rem; }
        .mini-items > div { display:flex; gap:13px; align-items:center; padding:.6rem 0;
          border-bottom:1px solid #f0f1ed; color:#46544f; font:.83rem 'DM Sans',sans-serif; }
        .mini-number { color:#b0b7b1; font-size:.68rem; }
        .mini-card-foot { color:#939b96; font:.69rem 'DM Sans',sans-serif; padding-top:.25rem; }
        .home-divider { border-top:1px solid var(--line); margin:2.3rem 0 1rem; }
        .home-footer { display:flex; justify-content:space-between; color:#9aa19c;
          font:600 .58rem 'DM Sans',sans-serif; letter-spacing:.1em; }
        .stLinkButton a, .stButton button {
          border-radius:5px !important; background:var(--green) !important;
          border-color:var(--green) !important; color:white !important;
          font-family:'DM Sans',sans-serif !important;
        }
        .page-intro { margin:0 0 1.2rem; }
        .context-note { display:flex; align-items:flex-start; gap:11px; border:1px solid var(--line);
          background:#fff; border-radius:6px; padding:.85rem 1rem; color:#6d7872;
          font:.79rem/1.6 'DM Sans',sans-serif; margin:1rem 0 1.7rem; }
        .note-mark { display:grid; place-items:center; width:19px; height:19px; flex:none;
          border-radius:50%; color:var(--green); background:#e9ede7; font-weight:700; }
        .context-note strong { color:var(--ink); }
        .section-label-spaced { margin-top:2rem; }
        [data-testid="stMetric"] { background:white; border:1px solid var(--line);
          border-radius:6px; padding:1rem 1.1rem; }
        [data-testid="stMetricLabel"] { color:#89918c; font-size:.73rem; }
        [data-testid="stMetricValue"] { color:var(--ink); font-size:1.65rem; }
        [data-testid="stPlotlyChart"], [data-testid="stDataFrame"] {
          border:1px solid var(--line); border-radius:6px; background:#fff; overflow:hidden;
        }
        [data-testid="stPlotlyChart"] { padding:.4rem; }
        [data-testid="stDataFrame"] { padding:.2rem; }
        .source-note { border-top:1px solid var(--line); margin-top:1.7rem; padding-top:.85rem;
          color:#969e99; font:.68rem 'DM Sans',sans-serif; }
        @media (max-width: 760px) {
          .main .block-container { padding:1.5rem 1rem 2.5rem; }
          .hero { padding:1.7rem 1.4rem; min-height:390px; align-items:flex-start; }
          .hero-art { width:70%; top:135px; right:-8%; opacity:.65; }
          .hero-copy { max-width:100%; }
          .hero-copy p { max-width:90%; font-size:.88rem; }
          .home-footer { flex-direction:column; gap:.45rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
