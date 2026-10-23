# 學術工作流程整合：盤點（2026-10）

為之後的「學術工作流程整合」頁做的盤點，把本站、thesis-toolkit（[mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills)）、[thesis-notes-template](https://github.com/wayhong0928/thesis-notes-template)、[claude-workflow-template](https://github.com/wayhong0928/claude-workflow-template) 對到同一組階段。這次只盤點，網站內容沒有改。

| 項目 | 內容 |
|---|---|
| 盤點日期 | 2026-10-23 |
| 本站版本 | `main` 0999a09（新增閱讀追蹤頁：勾選讀過的頁面，紀錄存在瀏覽器） |
| mis-thesis-skills | ca763e0（2026-10-17），thesis-toolkit 0.5.4 |
| thesis-notes-template | 9cf3783（2026-10-15） |
| claude-workflow-template | 9b234a8（2026-10-15） |
| 執行環境 | 雲端容器，Python 3.13.16；對外連線一律經過代理，github.com 網頁與 API 依 session 權限擋下，git clone 不受影響 |

## 結論摘要

| 項目 | 結果 |
|---|---|
| 1. build | 第一次跑失敗（沒裝 `markdown` 套件）。照 build.py 開頭的需求 `pip install markdown` 之後，44 個檔案全部產生、沒有警告。產出跟 repo 裡的版本只差 `theories`、`method-data` 兩頁的 `data-updated` 時間戳，原因是容器裡是淺層 clone，跟內容無關 |
| 2. 站內連結 | 85 個檔案、3,009 個站內連結（261 個不重複目標），**0 個**連到不存在的檔案 |
| 2. 外部連結 | 260 個不重複網址：191 個正常；4xx 共 **42** 個，全是 403，看起來都是站方擋自動請求，沒有任何 404／410；5xx **2** 個（同一個網站維護中）；逾時 0；無法連線 25 個（其中 20 個 github.com 用 git 確認過 repo 存在） |
| 3. 階段對照 | 8 列 × 3 欄 = 24 格，**8 格「缺」**；本站頁面欄沒有缺，缺的集中在 thesis-toolkit（讀文獻到口試這幾段本來就不管）和 thesis-notes-template（找方向、稽核題目、口試） |
| 4. prompt 一致性 | 第六節 11 個程式碼區塊和 `00_總覽/prompt.md` 的 11 個區塊**逐字一致**（diff 沒有輸出） |
| 4. 安裝／更新步驟 | 安裝指令全站一致，沒有跟 README 矛盾的地方。主要差在本站沒寫的部分：thesis-toolkit 的手動更新指令、`/reload-plugins`、Cowork 安裝；claude-workflow-template 在 `docs/` 完全沒有出現 |

---

## 一、build 結果

用法照 `build.py` 開頭：`python3 build.py`，需求 `pip install markdown`。為了不動到工作目錄，把整個 repo（含 `.git`）複製到暫存資料夾再跑。

### 1.1 第一次執行：失敗

容器裡沒有 `markdown` 套件，照指示只記錄、不修：

```text
$ python build.py
Traceback (most recent call last):
  File ".../build.py", line 13, in <module>
    import markdown
ModuleNotFoundError: No module named 'markdown'
EXIT=1
```

這是執行環境缺套件，不是 build.py 的錯。repo 裡沒有 `requirements.txt`，需求只寫在 build.py 開頭和 CONTRIBUTING.md。

### 1.2 裝好需求後：成功

`pip install markdown`（3.11.2）之後再跑一次：

```text
$ python build.py
  ✓ getting-started.html
  ✓ research-basics.html
  ✓ finding-reading.html
  ✓ venues.html
  ✓ is-research.html
  ✓ problem-design.html
  ✓ literature.html
  ✓ theory-building.html
  ✓ theories.html
  ✓ methodology.html
  ✓ research-ethics-data.html
  ✓ systematic-review.html
  ✓ quant-analysis-basics.html
  ✓ method-survey.html
  ✓ method-experiment.html
  ✓ method-dsr.html
  ✓ method-data.html
  ✓ method-secondary-data.html
  ✓ method-qualitative.html
  ✓ writing.html
  ✓ style.html
  ✓ defense.html
  ✓ post-defense.html
  ✓ ai-workflow-map.html
  ✓ ai-quickstart.html
  ✓ ai-quickstart-agent.html
  ✓ ai-workflow.html
  ✓ ai-case-study.html
  ✓ ai-tools.html
  ✓ ethics.html
  ✓ claude-tools-overview.html
  ✓ ai-agents.html
  ✓ harness.html
  ✓ skill-build.html
  ✓ tools-knowledge.html
  ✓ thesis-notes-template.html
  ✓ tool-directory.html
  ✓ checklists.html
  ✓ prompts.html
  ✓ glossary.html
  ✓ sources.html
  ✓ about.html
  ✓ index.html
  ✓ reading.html
完成。
EXIT=0
```

沒有出現 `! 缺少` 或舊錨點對不到的警告。

### 1.3 產出跟 repo 裡的版本比對

`git diff --stat`：44 個檔案、91 行增 91 行刪。逐行看過，全部是同一件事：導覽列裡 `theories`、`method-data` 兩個連結的 `data-updated`，從 `1788520745` 變成 `1788525613`（`theories.html`、`method-data.html` 本身的 `<article data-updated>` 也一樣）。

原因：容器裡的 clone 是淺層的（`git rev-parse --is-shallow-repository` 回 `true`），`source_updated()` 用 `git log` 查最後修改時間，只查得到淺層邊界那一筆 commit（ac81165，`1788525613`），比實際的修改時間晚。在完整 clone 上跑應該不會有這個差異。內文沒有任何變動。

---

## 二、連結檢查

### 2.1 做法

暫時腳本放在 repo 外面，沒有 commit。

- **範圍**：`docs/*.md`（42 個）、`pages/*.html`（42 個）、`index.html`，共 85 個檔案。
- **抽連結**：Markdown 抽 `[文字](網址)`、`<網址>`、內嵌 HTML 的 `href`／`src`，以及裸網址；HTML 抽 `href`／`src`。程式碼區塊和行內程式碼裡的網址不算（提示詞裡的 `api.github.com`、`127.0.0.1:23119` 這類不是連結）。
- **站內**：去掉 `#錨點` 和 `?參數`，照檔案所在位置解析路徑，查檔案存不存在。`docs/` 連到 `xxx.md` 的，另外查 `pages/xxx.html` 有沒有產生出來。這次只查檔案，沒查錨點（錨點有 `scripts/check_anchors.py`）。先用一組故意寫錯的假檔案試過，三個壞連結都抓得到。
- **外部**：每個不重複網址送一次請求，先 HEAD，回 4xx／5xx 再改 GET，逾時 20 秒，帶一般瀏覽器的 User-Agent。代理擋下、連線被重設的標「無法連線」，不算壞連結。

### 2.2 站內連結：0 個壞連結

| 項目 | 數量 |
|---|---|
| 掃描檔案 | 85 |
| 站內連結（含重複） | 3,009 |
| 不重複目標 | 261 |
| 連到不存在的檔案 | **0** |

### 2.3 外部連結總表

腳本一共抽到 262 個不重複網址，其中 2 個是誤抓，扣掉後是 260 個：

- `https://doi.org/10.xxx`：`docs/style.md` 第 273 行表格裡的 DOI 格式示意，是純文字，`pages/style.html` 裡也沒有變成連結。
- `https://language.chinadaily.com.cn/2015-09/01/content_21765083.htm`：裸網址規則從 `docs/style.md` 第 452 行網頁典藏站連結的網址中段抓出來的。原文本來就寫明原轉載頁已失效、連結改指向典藏站，所以這個 404 是預期的。

| 結果 | 數量 | 怎麼看 |
|---|---|---|
| 200 | 191 | 其中 5 個 Python 回憑證錯誤，改用 curl 都是 200，見 2.4 |
| 4xx | **42** | 全部是 403，沒有 404／410，見 2.5 |
| 5xx | **2** | 同一個網站維護中，見 2.6 |
| 逾時 | 0 | |
| 無法連線 | 25 | github.com 20 個、連線被重設 3 個、憑證驗證失敗 2 個，見 2.7 |
| 合計 | 260 | |

### 2.4 Python 回憑證錯誤、curl 正常（不算壞連結）

Python 3.13 預設開嚴格的 X.509 檢查，下面幾個政府與學術網站的憑證缺 Subject Key Identifier，Python 會拒絕；curl 都回 200。瀏覽器可以正常開。

| 網址 | curl |
|---|---|
| <https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093> | 200 |
| <https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021> | 200 |
| <https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020176> | 200 |
| <https://edu.law.moe.gov.tw/LawContent.aspx?id=GL001869> | 200 |
| <https://ndltd.ncl.edu.tw/> | 200 |

### 2.5 4xx：42 個，全是 403

sciencedirect.com 的 403 回應帶 Cloudflare 的 `__cf_bm` cookie，是站方的機器人防護頁；其他是出版社（INFORMS、SAGE、AOM、T&F、Wiley、OUP、ACM、MISQ）和工具官網，同樣是擋自動請求的常見對象。這些很可能用瀏覽器打得開，**要人工點開確認**，不能直接當成失效。按網域分：sciencedirect.com 8、pubsonline.informs.org 7（含 2 個 doi.org 轉址）、journals.sagepub.com 3（含 1 個 doi.org 轉址）、journals.aom.org 2、misq.umn.edu 2、tandfonline.com 2，其餘 18 個網域各 1。

| # | 網址 | 出現在 |
|---|---|---|
| 1 | <https://academic.oup.com/jamia/pages/About> | `docs/venues.md` |
| 2 | <https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/> | `docs/tool-directory.md` |
| 3 | <https://dl.acm.org/doi/10.1145/1273445.1273458> | `docs/about.md`、`docs/finding-reading.md`、`docs/sources.md` |
| 4 | <https://docs.consensus.app/consensus-mcp> | `docs/tool-directory.md` |
| 5 | <https://doi.org/10.1177/014920639101700108> | `docs/theories.md` |
| 6 | <https://doi.org/10.1287/isre.13.4.416.71> | `docs/about.md`、`docs/is-research.md` |
| 7 | <https://doi.org/10.1287/isre.14.3.221.16560> | `docs/about.md`、`docs/theory-building.md` |
| 8 | <https://endnote.com/> | `docs/tools-knowledge.md` |
| 9 | <https://help.consensus.app/en/articles/10087865-subscription-plans> | `docs/tool-directory.md` |
| 10 | <https://help.openai.com/en/articles/10169521-projects-in-chatgpt> | `docs/ai-quickstart.md` |
| 11 | <https://help.quillbot.com/hc/en-us/articles/35855733045143-What-is-the-difference-between-free-and-Premium-in-the-Quillbot-Paraphraser> | `docs/tool-directory.md` |
| 12 | <https://is.theorizeit.org/> | `docs/theories.md` |
| 13 | <https://journals.aom.org/doi/10.5465/AMR.1989.4308374> | `docs/about.md`、`docs/theory-building.md` |
| 14 | <https://journals.aom.org/doi/10.5465/amr.1989.4308371> | `docs/about.md`、`docs/is-research.md` |
| 15 | <https://journals.sagepub.com/aims-scope/jin> | `docs/venues.md` |
| 16 | <https://journals.sagepub.com/doi/10.1177/000276428102500205> | `docs/about.md`、`docs/is-research.md` |
| 17 | <https://misq.umn.edu/misq/article/19/2/189/1161/Computer-Self-Efficacy-Development-of-a-Measure> | `docs/about.md`、`docs/theories.md` |
| 18 | <https://misq.umn.edu/pages/Overview> | `docs/venues.md` |
| 19 | <https://onlinelibrary.wiley.com/page/journal/13652575/homepage/productinformation.html> | `docs/venues.md` |
| 20 | <https://pubsonline.informs.org/doi/10.1287/isre.2.3.192> | `docs/about.md`、`docs/theories.md` |
| 21 | <https://pubsonline.informs.org/doi/10.1287/isre.3.1.60> | `docs/about.md`、`docs/theories.md` |
| 22 | <https://pubsonline.informs.org/doi/10.1287/mnsc.32.5.554> | `docs/about.md`、`docs/theories.md` |
| 23 | <https://pubsonline.informs.org/doi/10.1287/orsc.5.2.121> | `docs/about.md`、`docs/theories.md` |
| 24 | <https://pubsonline.informs.org/page/isre/editorial-statement> | `docs/venues.md` |
| 25 | <https://quillbot.com/> | `docs/tool-directory.md` |
| 26 | <https://www.dcard.tw/f/graduate_school> | `docs/finding-reading.md`、`docs/sources.md` |
| 27 | <https://www.emerald.com/jkm> | `docs/venues.md` |
| 28 | <https://www.icpsr.umich.edu/sites/ICPSR/manage-data/prepare-deposit/guide> | `docs/sources.md` |
| 29 | <https://www.mendeley.com/> | `docs/tools-knowledge.md` |
| 30 | <https://www.scholarcy.com/> | `docs/tool-directory.md` |
| 31 | <https://www.sciencedirect.com/journal/computers-and-education> | `docs/venues.md` |
| 32 | <https://www.sciencedirect.com/journal/computers-and-security> | `docs/venues.md` |
| 33 | <https://www.sciencedirect.com/journal/computers-in-human-behavior> | `docs/venues.md` |
| 34 | <https://www.sciencedirect.com/journal/decision-support-systems> | `docs/venues.md` |
| 35 | <https://www.sciencedirect.com/journal/electronic-commerce-research-and-applications> | `docs/venues.md` |
| 36 | <https://www.sciencedirect.com/journal/international-journal-of-human-computer-studies> | `docs/venues.md` |
| 37 | <https://www.sciencedirect.com/journal/international-journal-of-information-management> | `docs/venues.md` |
| 38 | <https://www.sciencedirect.com/journal/the-journal-of-strategic-information-systems> | `docs/venues.md` |
| 39 | <https://www.scopus.com/> | `docs/tool-directory.md` |
| 40 | <https://www.ssrn.com/> | `docs/tool-directory.md` |
| 41 | <https://www.tandfonline.com/journals/mmis20/about-this-journal> | `docs/venues.md` |
| 42 | <https://www.tandfonline.com/journals/tjis20/about-this-journal> | `docs/venues.md` |

### 2.6 5xx：2 個

| # | 網址 | 狀態 | 出現在 |
|---|---|---|---|
| 1 | <https://www.csim.org.tw/> | 503（頁面標題是「網站正在進行維護」） | `docs/venues.md` |
| 2 | <https://www.csim.org.tw/conference> | 503（頁面標題是「網站正在進行維護」） | `docs/venues.md` |

兩個都是中華民國資訊管理學會，回應內容是站方自己的維護頁，過一陣子再查。

### 2.7 無法連線：25 個（不算壞連結）

#### github.com：20 個

代理回 403，內容是「GitHub access to this repository is not enabled for this session」，是這個執行環境的權限設定，跟連結本身無關。改用 git 協定查過：14 個第三方 repo 用 `git ls-remote` 都有回應，`elicit/api-examples` 底下確實有 `integrations/mcp`；6 個 wayhong0928 的網址對照本地 clone，三個 SKILL 資料夾都在，README 也有「## 安裝方式」標題，`#安裝方式` 錨點對得到。

| # | 網址 | 出現在 |
|---|---|---|
| 1 | <https://github.com/Consensus-NLP/consensus-mcp> | `docs/ai-quickstart-agent.md`、`docs/tool-directory.md` |
| 2 | <https://github.com/Future-House/paper-qa> | `docs/ai-tools.md`、`docs/sources.md` |
| 3 | <https://github.com/Imbad0202/academic-research-skills> | `docs/sources.md` |
| 4 | <https://github.com/LearningCircuit/local-deep-research> | `docs/ai-tools.md` |
| 5 | <https://github.com/SakanaAI/AI-Scientist> | `docs/ai-tools.md` |
| 6 | <https://github.com/SamuelSchmidgall/AgentLaboratory> | `docs/ai-tools.md` |
| 7 | <https://github.com/ammosu/awesome-claude-skills-zh-TW> | `docs/sources.md` |
| 8 | <https://github.com/assafelovic/gpt-researcher> | `docs/ai-tools.md`、`docs/sources.md` |
| 9 | <https://github.com/bytedance/deer-flow> | `docs/ai-tools.md` |
| 10 | <https://github.com/elicit/api-examples/tree/main/integrations/mcp> | `docs/ai-quickstart-agent.md`、`docs/tool-directory.md` |
| 11 | <https://github.com/langchain-ai/open_deep_research> | `docs/ai-tools.md` |
| 12 | <https://github.com/pedrohcgs/claude-code-my-workflow> | `docs/sources.md` |
| 13 | <https://github.com/retorquere/zotero-better-bibtex/releases/latest> | `docs/tools-knowledge.md` |
| 14 | <https://github.com/stanford-oval/storm> | `docs/ai-tools.md`、`docs/sources.md` |
| 15 | <https://github.com/wayhong0928/mis-thesis-skills> | `docs/about.md`、`docs/ai-case-study.md`、`docs/ai-quickstart-agent.md`、`docs/finding-reading.md`、`docs/getting-started.md`、`docs/problem-design.md`、`docs/prompts.md`、`docs/skill-build.md`、`docs/sources.md`、`docs/style.md`、`docs/writing.md` |
| 16 | <https://github.com/wayhong0928/mis-thesis-skills#安裝方式> | `docs/ai-workflow-map.md`、`docs/prompts.md` |
| 17 | <https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/academic-writing-discipline> | `docs/ai-workflow-map.md` |
| 18 | <https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/research-direction-finding> | `docs/ai-workflow-map.md` |
| 19 | <https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/research-question-audit> | `docs/ai-workflow-map.md` |
| 20 | <https://github.com/wayhong0928/thesis-notes-template> | `docs/thesis-notes-template.md` |

#### 其他：5 個

| 網址 | 出現在 | 錯誤 |
|---|---|---|
| <https://web.archive.org/web/20210410224558/https://language.chinadaily.com.cn/2015-09/01/content_21765083.htm> | `docs/style.md` | 連線被重設（代理紀錄：tunnel closed mid exchange） |
| <https://tanet2026.ntunhs.edu.tw/> | `docs/venues.md` | 連線被重設（同上） |
| <https://www.ntuh.gov.tw/RECO/Fpage.action?fid=5536> | `docs/research-ethics-data.md`、`docs/sources.md` | 伺服器沒有回應內容（curl: Empty reply from server） |
| <https://eclab.nkust.edu.tw/> | `docs/venues.md` | 憑證驗證失敗（curl: unable to get local issuer certificate），可能是站方憑證鏈不完整，也可能是環境因素，沒辦法分辨 |
| <https://eclab.nkust.edu.tw/submitjim/JIM_Call_for_Paper.pdf> | `docs/venues.md` | 同上 |

---

## 三、階段對照

### 3.1 thesis-toolkit 的 skill 清單

來源：`plugins/thesis-toolkit/skills/*/SKILL.md`，plugin 版本 0.5.4。

| skill | 做什麼 | 不做什麼 |
|---|---|---|
| `research-direction-finding` | 沒方向或只有大領域時，用收斂漏斗（領域→主題→子題→題目→研究問題）一次推一層，收出一句話的研究想法，每輪寫進度筆記 | 不稽核收出來的題目；不代讀文獻 |
| `research-question-audit` | 稽核已有的研究問題，七個檢查點（A 缺口分類、B 收斂程度、C 題目定案六問、D 壞題目長相、E 句型與常見錯誤、F 一致性檢查鏈、G 對抗式審查），之後可逐項引導 | 不從零想題目；不管問卷題項、統計實跑 |
| `academic-writing-discipline` | 稽核中文學術文字：因果動詞、構句、台灣學術用語、APA 7、去 AI 感、章節結構 | 不管研究設計邏輯；0.3.0 起不檢查文獻回顧的論證鏈 |
| `thesis-roadmap` | 判斷使用者在哪一段、指出下一個 SKILL；toolkit 不管的需求指到本站頁面 | 不做任何稽核；不強制順序 |

### 3.2 thesis-roadmap 定義的階段

`thesis-roadmap/SKILL.md` 第 1 節的表定義了四段，第 3 節再把「toolkit 不管」那段拆成六種需求，各指到本站一頁：

| 第 1 節：手上有什麼 | 階段 | 下一個 SKILL |
|---|---|---|
| 什麼都沒有，或只有一個大領域 | 找方向 | `research-direction-finding` |
| 老師給了研究計畫，要從裡面找題目 | 找方向（計畫延伸） | `research-direction-finding` |
| 寫得出一句話的研究想法 | 稽核題目 | `research-question-audit` |
| 題目稽核過了，正在讀文獻、設計方法 | thesis-toolkit 不管 | 無，見第 3 節 |
| 正在寫或改章節文字 | 稽核寫法 | `academic-writing-discipline` |

| 第 3 節：toolkit 不管的需求 | 指到本站 |
|---|---|
| 找文獻、讀文獻 | `finding-reading`、`literature` |
| 假說與研究架構 | `problem-design` |
| 選研究方法、設計問卷 | `methodology`、`method-survey` |
| 統計分析怎麼跑 | `quant-analysis-basics` |
| 各章要寫什麼 | `writing` |
| 計畫書、口試、簡報 | `defense` |

第 2 節的轉換條件：收出一句話的研究想法就從「找方向」換到「稽核題目」；稽核結論「可進行」就往下，「需重新收斂」退回找方向；寫作中發現問題出在研究問題本身，退回稽核題目。

### 3.3 對照表

**列**：第 1 節的四段，「讀文獻、設計方法」照第 3 節拆成四列；「各章要寫什麼」併進「稽核寫法」；「計畫書、口試、簡報」在第 1 節沒有對應的段，單獨一列放最後。

**判定規則**：

- 本站欄列出內容主要在處理這一段的頁面，括號是節次。同一頁可以出現在好幾列。
- thesis-toolkit 欄照 thesis-roadmap 自己的界定：roadmap 寫「toolkit 不管」的段一律標「缺」。skill 順帶碰到的部分寫在表下的註，不算填滿。
- thesis-notes-template 欄列出設計來做這一段工作的資料夾、檔案或 prompt 段落；只是剛好記錄這一段結果的不算。

| # | 階段 | 本站頁面 | thesis-toolkit | thesis-notes-template |
|---|---|---|---|---|
| 1 | 找方向（含計畫延伸） | `getting-started`（§九）、`finding-reading`（選題目、收斂漏斗）、`venues`、`is-research`、`tool-directory`（階段一）、`prompts`（§一、§十）、`ai-workflow-map`（第 1 站）、`ai-case-study`（3.1） | `research-direction-finding` | **缺** ¹ |
| 2 | 稽核題目 | `problem-design`、`finding-reading`（缺口五類型）、`checklists`（§一）、`prompts`（§四、§十）、`ai-workflow-map`（第 4 站）、`ai-case-study`（3.4） | `research-question-audit` | **缺** ² |
| 3a | 讀文獻、設計方法：找文獻、讀文獻 | `finding-reading`、`literature`、`systematic-review`、`tools-knowledge`、`thesis-notes-template`、`tool-directory`（階段二～七）、`prompts`（§二、§三、§七）、`checklists`（§二）、`ai-workflow`（§五～七）、`ai-workflow-map`（第 2、3 站）、`ai-case-study`（3.2、3.3） | **缺** ³ | `03_文獻筆記/`、`07_模板/` 三型文獻筆記、`00_總覽/文獻筆記填寫規則.md`、`文獻矩陣.base`、`術語表.md`、prompt 第 2 段（寫筆記）、第 3 段（核對筆記） |
| 3b | 讀文獻、設計方法：假說與研究架構 | `problem-design`、`theory-building`、`theories`、`ai-workflow`（§十 框架建構） | **缺** ⁴ | `01_理論/`、`02_變數/`、`05_假設推演/`、`研究設計速查.md`（假說表、構念對假說）、`範例_模型圖.png`、prompt 第 1 段（從計畫書填速查）、第 4 段（收料進構念卡）、第 5 段（推演卡健檢） |
| 3c | 讀文獻、設計方法：選研究方法、設計問卷 | `methodology`、`research-ethics-data`、`method-survey`、`method-experiment`、`method-dsr`、`method-data`、`method-secondary-data`、`method-qualitative`、`systematic-review`（當研究方法用）、`is-research`（研究取向）、`checklists`（§三）、`prompts`（§五） | **缺** ⁵ | `06_方法/`、`07_模板/06_方法.md`、`07_模板/03_文獻筆記_方法型.md` |
| 3d | 讀文獻、設計方法：統計分析 | `quant-analysis-basics`、`method-survey`（PLS-SEM）、`method-data`（評估指標）、`glossary`（統計術語）、`tool-directory`（階段八）、`prompts`（§五）、`checklists`（§四） | **缺** | `06_方法/` 的分析步驟與門檻值卡（例：`方法_PLS-SEM`）⁶ |
| 4 | 稽核寫法（含各章要寫什麼） | `writing`、`style`、`glossary`（台灣／大陸用語）、`checklists`（§五、§六）、`prompts`（§六、§十）、`tool-directory`（階段九）、`ethics`（§四 揭露聲明）、`ai-workflow-map`（第 5 站）、`ai-case-study`（3.5） | `academic-writing-discipline` | `04_論文草稿/`、`術語表.md`（構念標準中譯）、README「寫作流程」第 5、6 步 |
| 5 | 計畫書、口試、簡報（roadmap 第 3 節） | `defense`、`checklists`（§七）、`ethics`、`tool-directory`（階段十）、`ai-workflow-map`（第 6 站）、`ai-case-study`（3.6） | **缺** ⁷ | **缺** |

「缺」共 **8 格**：thesis-toolkit 5 格（3a、3b、3c、3d、5），thesis-notes-template 3 格（1、2、5）。本站頁面欄沒有缺。

註：

1. 範本預設使用者已經有題目和計畫書草稿（prompt 第 1 段的前提就是「手上有計畫書草稿」）。
2. `研究設計速查.md` 第一節「研究問題」只用來放定案的題目，沒有檢查功能。
3. `research-direction-finding` 的 `references/handoff-to-literature.md` 會在收斂不動時把使用者送去讀文獻，並交代要查什麼、用什麼檢索式；那是交棒，不是讀文獻本身。
4. `research-question-audit` 的檢查點 F「一致性檢查鏈」會看「目的→問題→假說→架構→分析→結論」有沒有斷點，但 roadmap 把這段歸為 toolkit 不管。
5. `research-question-audit` 的檢查點 C、引導模式會碰到資料可得性與可行性，同上，不算填滿。
6. 只有分析方法和門檻值的出處，沒有放分析紀錄或結果的位置。
7. `academic-writing-discipline` 的 description 把「研究計畫書、口試講稿」列為檢查對象，但只看文字層級，不管簡報架構和題庫。

### 3.4 不屬於 roadmap 任何一段的本站頁面

roadmap 的範圍是「論文 0→1」，下面這些頁面落在範圍外，或是跨所有階段：

| 頁面 | 性質 |
|---|---|
| `research-basics` | 研究的本質與兩年時間表，跨階段 |
| `post-defense` | 口試後修訂、典藏、結案，roadmap 的範圍在口試前就結束 |
| `ai-quickstart`、`ai-quickstart-agent` | 建立 AI 助手，對應 `ai-workflow-map` 第 0 站「地基」，不是 roadmap 的任何一段 |
| `ai-workflow`（§一～四、§八～十二）、`ai-tools`、`ethics`（§一～三） | AI 使用原則、風險、法規，跨階段 |
| `claude-tools-overview`、`ai-agents`、`harness`、`skill-build` | 已搬到 ai-agent-notes 的導引頁 |
| `sources`、`about` | 延伸閱讀、關於本站 |

42 頁都已經出現在 3.3 或 3.4（`ai-workflow-map`、`ai-case-study`、`checklists`、`prompts`、`tool-directory` 跨好幾列）。

### 3.5 claude-workflow-template 放哪裡

這個 repo 管的是 Claude Code 專案的工作方式（接續進度的 session_log、派工模板、`verifier` 獨立驗收、控制字元與 context 長度的 hook、`--protect` 保護原始資料），不對應論文的任何一個階段，比較像 `ai-workflow-map` 第 0 站「地基」的進階選項。跟階段有直接關係的只有兩處：

- README「核對引用與主張」：派 `verifier` 核對第二章引用，可以接在第 4 段（稽核寫法）和第 5 段（送審前）之後。
- `--protect`：鎖住 PDF、問卷原始檔，對應 3c、3d 的資料管理（本站 `research-ethics-data`）。

本站 `docs/` 裡沒有任何一頁提到這個 repo，只有 repo 根目錄 `README.md` 的「從哪裡開始」表和 `README.en.md` 的「Where to start」表各有一行。

### 3.6 寫整合頁時要先處理的事

本站自己已經有好幾套階段切法，跟 roadmap 不同：

| 出處 | 切法 |
|---|---|
| thesis-roadmap | 找方向 → 稽核題目 →（讀文獻、設計方法）→ 稽核寫法，另列計畫書口試 |
| `ai-workflow-map` | 第 0 站地基＋六站：找方向、找文獻、讀與筆記、缺口與研究問題、寫作、送審與口試 |
| `ai-case-study` §三 | 六階段：找方向與研究問題、查文獻、文獻筆記、缺口、寫作與改寫、送出前審查 |
| `ai-workflow` §十 | 卡關診斷四階段：問題界定、框架建構、研究設計、分析規劃 |
| `tool-directory` | 十個階段：題目探索到投稿與誠信 |
| `research-basics` §四 | 碩士兩年四個階段 |

最明顯的不一致：roadmap 把「稽核題目」放在讀文獻**之前**，`ai-workflow-map` 把「缺口與研究問題」放在找文獻、讀與筆記**之後**（第 4 站）。整合頁用哪一套當主軸、其他幾套怎麼對過去，要先決定。

---

## 四、一致性

### 4.1 第六節程式碼區塊 vs `00_總覽/prompt.md`

做法：從 `docs/thesis-notes-template.md` 第 97～307 行（「## 六、提示詞：安裝一段、工作五段」到「## 七」之前）和 `prompt.md` 全檔，依序抽出所有 ```` ``` ```` 圍起來的區塊，各自寫成一份文字檔（每個區塊前加一行 `<<<BLOCK n info=… lines=…>>>`），再用 `diff` 比。

兩邊各 11 個區塊，資訊字串都是 `text`，行數依序是 17、8、6、10、17、10、11、9、7、7、6。

```text
$ diff site_blocks.txt repo_blocks.txt
$ echo $?
0

$ sha256sum site_blocks.txt repo_blocks.txt
a57f8911c6f9843e43104aa1869aa48875decbec9ec0f2b931d5a82c3cfdd3d3  site_blocks.txt
a57f8911c6f9843e43104aa1869aa48875decbec9ec0f2b931d5a82c3cfdd3d3  repo_blocks.txt
```

**結果：逐字一致。**

順便比了區塊外的說明文字（本站第 105～306 行 vs `prompt.md` 第 14～219 行）。差異只有標題層級和分隔線：本站寫 `### 6.0`～`### 6.5`，`prompt.md` 寫 `## 0.`～`## 5.`，`prompt.md` 段與段之間多一條 `---`。「什麼時候用」「AI 回來後你要檢查」的文字兩邊相同。

```diff
1c1
< ### 6.0 安裝與匯入（只有 CLI 版）
---
> ## 0. 安裝與匯入（只有 CLI 版）
27c27,29
< ### 6.1 快速設定：從計畫書填出術語表和研究設計速查
---
> ---
> 
> ## 1. 快速設定：從計畫書填出術語表和研究設計速查
56a59
> ---
58c61
< ### 6.2 寫文獻筆記
---
> ## 2. 寫文獻筆記
100a104
> ---
102c106
< ### 6.3 核對文獻筆記（一定要開新對話）
---
> ## 3. 核對文獻筆記（一定要開新對話）
138a143
> ---
140c145
< ### 6.4 收料進構念卡
---
> ## 4. 收料進構念卡
171a177
> ---
173c179
< ### 6.5 推演卡健檢
---
> ## 5. 推演卡健檢
201,202d206
< 
< ---
```

### 4.2 安裝與更新步驟 vs 各 repo README

#### mis-thesis-skills（thesis-toolkit）

本站寫到安裝指令的地方：`ai-quickstart-agent` §六、`ai-case-study` §五、`finding-reading`、`problem-design`、`writing`（三個 tip 框）、`prompts` 開頭、`ai-workflow-map` 第 0 站。

| 項目 | README 目前寫法 | 本站 | 一致嗎 |
|---|---|---|---|
| Claude Code 安裝 | `/plugin marketplace add wayhong0928/mis-thesis-skills`、`/plugin install thesis-toolkit@mis-thesis-skills` | 上面 7 處都是同樣兩行 | 一致 |
| Codex 安裝 | SKILL 資料夾複製到 `.agents/skills/`，或建 symlink 跟 `.claude/skills/` 共用 | `ai-quickstart-agent` 6.2：下載 ZIP，把 `plugins/thesis-toolkit/skills/` 下四個資料夾複製到專案或家目錄的 `.agents/skills/` | 一致；本站沒提 symlink，多寫了家目錄的選項和 `/skills`、`$skill名` 用法 |
| Claude Code 更新 | 終端機 `claude plugin marketplace update mis-thesis-skills`、`claude plugin update thesis-toolkit@mis-thesis-skills`；或 `/plugin` → Marketplaces → **Update marketplace**；同一處 **Enable auto-update**；正在用的 session 用 `/reload-plugins` 套用 | `ai-quickstart-agent` 6.2 最後一段只寫「到 `/plugin` 的 Marketplaces 分頁選這個市集，開啟自動更新」 | **本站少寫**：手動更新的兩行指令、Update marketplace、`/reload-plugins` |
| Codex 更新 | 沒寫 | 「要自己重新下載，再覆蓋那四個資料夾」 | README 沒有對應段落 |
| Claude Cowork | Customize → Plugins → Add marketplace | 沒寫 | **本站少寫** |
| Claude.ai 網頁版 | SKILL 資料夾包成 zip 手動上傳；或改用本站 `prompts.html#skill-lite` | `ai-case-study` 指到 GitHub；`ai-workflow-map` 網頁版路線指到 `prompts` §十 | 一致 |
| `#安裝方式` 錨點 | README 有「## 安裝方式」 | `ai-workflow-map`、`prompts` 都連這個錨點 | 對得到 |

SKILL 數量的寫法也不一致（不是安裝步驟，但寫整合頁會碰到）：README 和 plugin.json 是「三個稽核 SKILL＋一個流程導覽」，本站 `ai-quickstart-agent` 寫法相同；`sources.md` 第 165 行寫「收錄……三個 SKILL」，`ai-case-study` §五只列三個，都沒有 `thesis-roadmap`。

#### thesis-notes-template

本站：`thesis-notes-template` 第二節「下載與開啟」、6.0 安裝 prompt。

| 項目 | README 目前寫法 | 本站 | 一致嗎 |
|---|---|---|---|
| 用 AI 安裝 | 把 `prompt.md` 第 0 段貼給 Claude Code 或 Codex | 把第六節 6.0 貼給它 | 一致（6.0 跟第 0 段逐字相同，見 4.1） |
| 自己來 1 | Code → Download ZIP，解壓縮到想放的地方（例：`文件/碩士論文/02_筆記`） | Code → Download ZIP，解壓縮到放論文檔案的地方 | 一致，README 多一個路徑例子 |
| 自己來 2 | Obsidian「開啟資料夾作為儲存庫」 | 同 | 一致 |
| 自己來 3 | 先讀 `00_總覽/開始使用.md` | 先讀 `開始使用.md`，再開三份示範 | 一致，本站多一句 |
| Obsidian 版本 | 沒寫 | 文獻矩陣用核心外掛 Bases，版本太舊打不開，先更新到最新版 | README 沒寫 |
| 更新範本 | 沒寫 | 沒寫 | 兩邊都沒有 |

沒有矛盾。README 引用本站的兩處也對得到：「範本說明頁第七節」（本站有「## 七、這些提示詞測過哪些」）、文獻管理頁 2.3.8（`tools-knowledge` 有「#### 2.3.8 中文文獻：作者姓名與語言欄」，6.0 提到的 2.3.6 也在）。

#### claude-workflow-template

本站 `docs/` 沒有寫任何安裝或更新步驟，沒有可以比對的地方。README 的安裝方式供整合頁參考：

- 方法一：在專案資料夾開 Claude Code 或 Codex，貼 README 裡的安裝 prompt（檢查環境 → 下載到暫存資料夾 → `install.py --dry-run` → 正式執行 → 跑測試，結果要是「25/25 通過」→ 填 CLAUDE.md）。
- 方法二：下載 ZIP，`python install.py "<專案>" --session-log --dry-run`，確認後拿掉 `--dry-run`。
- 更新：下載新版再跑一次 `install.py`；移除：`--uninstall`。
- 需求：Claude Code 2.1.292 以上、Python 3.8 以上；session_log 在非 Windows 平台要 PowerShell 7。
