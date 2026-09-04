#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
從 docs/*.md 產生 pages/*.html。
用法：python3 build.py
需求：pip install markdown
"""
import os
import re
import json
import html
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
PAGES = os.path.join(ROOT, "pages")

# (檔名, 標題, 一句話說明)
NAV = [
    ("研究的基礎", [
        ("getting-started", "從零開始：研究所的第一個月", "研究所與大學的差別、第一個月的五件事、兩年節奏感"),
        ("research-basics", "研究的本質、歷程與時程", "研究到底在做什麼、四大核心能力、兩年時間表"),
        ("finding-reading", "怎麼找、怎麼讀、怎麼選題目", "檢索管道與關鍵字、三遍閱讀法、缺口的五種類型"),
        ("is-research", "資訊管理研究的範疇與取向", "研究對象、行為科學與設計科學、方法取捨、研究策略"),
        ("problem-design", "研究問題、假說與研究架構", "從實務問題到可驗證的學術問題"),
        ("literature", "文獻回顧與批判性思考", "十倍速文獻回顧、剝洋蔥式閱讀、批判角度的彙整"),
        ("theory-building", "理論的構成與評估", "構念與假說、Gregor 五型、可否證性、概化的四種形式"),
        ("theories", "常用理論家族與選用原則", "TAM 家族、SOR／SDT、組織理論與理論索引"),
    ]),
    ("研究方法", [
        ("methodology", "方法論選擇地圖", "六大方法的適用場合與相對優缺點"),
        ("method-survey", "問卷調查法", "抽樣、信效度、PLS-SEM、共同方法變異"),
        ("method-experiment", "實驗法", "操弄、控制、隨機化與內外部效度"),
        ("method-dsr", "系統發展法與設計科學研究", "Nunamaker、March &amp; Smith、Hevner 七大規範"),
        ("method-data", "演算法、最佳化與資料分析", "建模、訓練、評估指標與實驗驗證"),
        ("method-qualitative", "質性研究方法", "訪談、個案研究、紮根理論與信實度"),
    ]),
    ("論文寫作", [
        ("writing", "論文架構與各章寫作要領", "六大部分的功能、寫作次序與台灣碩論慣例"),
        ("style", "學術中文寫作紀律", "因果動詞、台灣用語、APA 7、去 AI 感"),
        ("defense", "計畫書、口試與簡報", "十二個考古題、八大核心能力、投影片架構"),
    ]),
    ("AI 輔助研究", [
        ("ai-workflow", "AI 輔助研究工作流", "三層架構、戰略聚焦單、各階段的能與不能"),
        ("tool-directory", "AI 學術研究工具指南", "依研究階段分類：檢索、引文網絡、閱讀、SLR、分析"),
        ("ai-agents", "AI 代理工具懶人包", "Claude Code、Skill／Plugin、Codex 與研究場景應用"),
        ("ai-tools", "AI 工具生態與風險", "Auto Research、去 AI 味工具的定位與紅線"),
        ("ethics", "學術倫理與 AI 揭露", "法規、期刊政策、揭露聲明範本"),
    ]),
    ("工具箱", [
        ("tools-knowledge", "文獻管理與知識庫", "Zotero／EndNote、Obsidian／Notion、筆記欄位、備份策略"),
        ("checklists", "檢查清單", "提案、文獻、方法、寫作、口試的自檢表"),
        ("prompts", "AI 提示詞範本", "文獻、批判、方法檢核、寫作潤飾"),
        ("glossary", "名詞與用語對照", "統計術語、台灣／大陸用語、英中對照"),
        ("sources", "延伸閱讀與資源指南", "書籍導讀、經典論文、線上講座、開源專案與本站來源"),
    ]),
]

SLUG_TITLE = {}
FLAT = []
for _sec, items in NAV:
    for slug, title, desc in items:
        SLUG_TITLE[slug] = title
        FLAT.append((slug, title, desc))


def nav_html(active, prefix=""):
    out = ['<nav class="sidenav" id="sidenav" aria-label="全站導覽">']
    out.append(f'<a class="brand" href="{prefix}index.html"><span class="brand-mark">◈</span>'
               f'<span class="brand-text">研究方法<br><small>知識網絡</small></span></a>')
    out.append('<div class="navsearch"><input type="search" id="navfilter" '
               'placeholder="篩選頁面…" aria-label="篩選頁面"></div>')
    for sec, items in NAV:
        out.append(f'<div class="navsec"><h2>{sec}</h2><ul>')
        for slug, title, _d in items:
            cls = ' class="active"' if slug == active else ""
            out.append(f'<li{cls}><a href="{prefix}pages/{slug}.html" '
                       f'data-title="{title}">{title}</a></li>')
        out.append("</ul></div>")
    out.append("</nav>")
    return "\n".join(out)


TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}｜研究方法與論文寫作知識網絡</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#128218;</text></svg>">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<a class="skip" href="#main">跳到主要內容</a>
<button class="navtoggle" id="navtoggle" aria-label="開啟導覽">☰</button>
{nav}
<div class="wrap">
<main id="main">
<p class="crumb"><a href="../index.html">首頁</a> ／ {section}</p>
<article class="doc">
{body}
</article>
<nav class="pager">{pager}</nav>
<footer class="foot">
<p>本站為個人學習筆記彙整，非官方規範。實際要求一律以系所規定、指導教授意見與投稿單位作者須知為準。</p>
<p><a href="../pages/sources.html">延伸閱讀與資源指南</a></p>
</footer>
</main>
<aside class="toc" id="toc"><h2>本頁目錄</h2>{toc}</aside>
</div>
<script src="../assets/site.js"></script>
</body>
</html>
"""


SEC_DESC = {
    "研究的基礎": "做研究到底在做什麼、問題怎麼問、文獻怎麼讀、理論怎麼選。",
    "研究方法": "六種方法的適用場合、執行要領與各自的代價。",
    "論文寫作": "從章節架構到用字紀律，再到口試現場。",
    "AI 輔助研究": "把 AI 放在流程中的正確位置，以及不能越過的界線。",
    "工具箱": "可以直接拿來用的清單、範本、速查表與延伸閱讀。",
}

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>研究方法與論文寫作知識網絡</title>
<meta name="description" content="社會科學／資訊管理取向的研究方法、論文寫作與 AI 輔助研究知識庫。">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#128218;</text></svg>">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">跳到主要內容</a>
<button class="navtoggle" id="navtoggle" aria-label="開啟導覽">☰</button>
{nav}
<div class="wrap solo">
<main id="main">

<header class="hero">
<span class="tag">社會科學 ／ 資訊管理取向</span>
<h1>研究方法與論文寫作<br>知識網絡</h1>
<p>把學習筆記、方法論書籍、公開規範與 AI 輔助研究的實務整理成一張可以反覆查閱的地圖。內容涵蓋研究的本質、六種研究方法、論文各章的寫作要領、學術中文的用字紀律，以及 AI 在研究流程中該站的位置。</p>
<p>本站以<strong>社會科學取向的資訊管理研究</strong>為預設情境。統計判準、章節慣例與寫作規範都有領域限定，其他領域請以自身系所規範為準。</p>
<p>站內沒有任何特定研究的題目或架構——所有範例都是通用的教科書級範例。</p>
</header>

<div class="notice">
<b>先講清楚四件事</b>
<ol>
<li>這是<strong>個人學習筆記</strong>的彙整，不是任何機構的官方文件，也不能取代系所規定。</li>
<li>實際要求一律以：系所規範 → 指導教授意見 → 研究倫理委員會 → 投稿單位作者須知 為準。</li>
<li>站內的判準門檻（信效度、統計指標、格式慣例）會因領域與期刊而異，引用前請自行查證最新版本。</li>
<li>本站內容由作者規劃、篩選與審定，撰寫過程使用 AI 工具協助蒐集資料、查證出處與草擬文字。站內引用的卷期、DOI 與連結均經工具查證並標明查證日期，但作者尚未逐篇取得原文核對——<strong>請勿直接引用本站的整理，一律回到原始文獻查證後再引用。</strong>作者對本站公開的內容負責：發現錯誤請回報，作者會更正或撤下。</li>
</ol>
</div>

<div class="homesearch">
<input type="search" id="homefilter" placeholder="搜尋主題…（例如：信效度、口試、文獻矩陣）" aria-label="搜尋主題">
</div>

<div class="flowbox">
<h2>研究的骨架：解決問題的五個階段</h2>
<div class="flow">
<div class="step"><b>問題探索</b><span>找到實務上重要、學術上有趣的問題<br><em>→ 第一章 緒論</em></span></div>
<div class="arrow">→</div>
<div class="step"><b>案例觀摩</b><span>前人做到哪裡？哪裡還不夠好？<br><em>→ 第二章 文獻探討</em></span></div>
<div class="arrow">→</div>
<div class="step"><b>方案設計</b><span>我打算怎麼做？為什麼合理？<br><em>→ 第三章 研究方法</em></span></div>
<div class="arrow">→</div>
<div class="step"><b>方案執行</b><span>實際做出來的結果是什麼？<br><em>→ 第四章 結果分析</em></span></div>
<div class="arrow">→</div>
<div class="step"><b>結果與反思</b><span>代表什麼？限制在哪？下一步？<br><em>→ 第五章 結論建議</em></span></div>
</div>
</div>

{sections}

<footer class="foot">
<p>本站為個人學習筆記彙整，非官方規範。實際要求一律以系所規定、指導教授意見與投稿單位作者須知為準。</p>
<p><a href="pages/sources.html">延伸閱讀與資源指南</a>　·　最後更新：2026-09</p>
</footer>

</main>
</div>
<script src="assets/site.js"></script>
</body>
</html>
"""


def build_index():
    parts = []
    for i, (sec, items) in enumerate(NAV, start=1):
        cards = []
        for slug, title, desc in items:
            cards.append(f'<a class="card" href="pages/{slug}.html">'
                         f'<h3>{title}</h3><p>{desc}</p></a>')
        parts.append(
            f'<section class="mapsec"><h2><span class="num">{i:02d}</span>{sec}</h2>'
            f'<p class="secdesc">{SEC_DESC.get(sec, "")}</p>'
            f'<div class="cards">{"".join(cards)}</div></section>')
    out = INDEX_TEMPLATE.format(nav=nav_html(None, prefix=""), sections="\n".join(parts))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("  ✓ index.html")


def section_of(slug):
    for sec, items in NAV:
        for s, _t, _d in items:
            if s == slug:
                return sec
    return ""


def build():
    os.makedirs(PAGES, exist_ok=True)
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "admonition"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    for i, (slug, title, desc) in enumerate(FLAT):
        src = os.path.join(DOCS, slug + ".md")
        if not os.path.exists(src):
            print("  ! 缺少", src)
            continue
        md.reset()
        text = open(src, encoding="utf-8").read()
        # 移除 Markdown 檔開頭的 H1（HTML 由樣板統一呈現）
        text = re.sub(r"\A#\s+.*\n", "", text)
        body = md.convert(text)
        # 內部連結：docs/*.md → 同目錄的 *.html
        body = re.sub(r'href="(?!https?:|#|\.\./)([A-Za-z0-9\-_]+)\.md(#[^"]*)?"',
                      lambda m: 'href="%s.html%s"' % (m.group(1), m.group(2) or ""), body)
        body = f"<h1>{title}</h1>\n<p class='lede'>{desc}</p>\n" + body
        # 讓 - [ ] 變成可勾選
        body = body.replace("<li>[ ] ", '<li class="chk"><input type="checkbox"> ')
        body = body.replace("<li>[x] ", '<li class="chk"><input type="checkbox" checked> ')
        prev_ = FLAT[i - 1] if i > 0 else None
        next_ = FLAT[i + 1] if i < len(FLAT) - 1 else None
        pager = ""
        if prev_:
            pager += f'<a class="prev" href="{prev_[0]}.html">← {prev_[1]}</a>'
        if next_:
            pager += f'<a class="next" href="{next_[0]}.html">{next_[1]} →</a>'
        toc = md.toc.replace('<div class="toc">', '<div class="toc-body">')
        out = TEMPLATE.format(title=title, desc=html.escape(desc, quote=True),
                              nav=nav_html(slug, prefix="../"), body=body,
                              toc=toc, pager=pager, section=section_of(slug))
        with open(os.path.join(PAGES, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(out)
        print("  ✓", slug + ".html")

    # 給首頁搜尋用的索引
    idx = [{"slug": s, "title": t, "desc": d, "section": section_of(s)} for s, t, d in FLAT]
    with open(os.path.join(ROOT, "assets", "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    build()
    build_index()
    print("完成。")
