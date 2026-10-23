# 內容查核報告（2026-10）

- 查核日期：2026-10-23（價格、方案、功能、網址、政策這類會變的資訊，都以這一天為準，各條另外標註）
- 查核對象：`main` 分支 commit `0999a09`
- 性質：**只查核、不改網站**。這份報告是唯一的新增檔案，網站內容一個字都沒動。

---

## 一、範圍與方法

### 1.1 查了哪些頁面

站上的內容來源是 `docs/*.md`，共 40 頁。`pages/*.html` 由 `build.py` 從 docs 產生，內容一樣，所以報告裡的位置一律寫 `docs/檔名.md:行號`，對應的網頁是 `pages/同名.html`。`index.html` 的文字只是各頁標題與一句話說明（出自 `build.py` 的 `NAV`），唯一可查證的「Hevner 七大規範」併入 MTH-06／MTH-07。`reading.html` 是閱讀追蹤工具，沒有可查證的主張。

| 代號 | 範圍 | 頁面 |
|---|---|---|
| STAT | 統計門檻與量化判準 | method-survey、glossary（統計表） |
| APA | APA 7 格式與寫作規則 | style、writing、defense、post-defense、checklists |
| REF | 全站引用文獻書目，以及理論頁中歸給特定作者的觀點 | 全站書目；about、sources、theories、theory-building、is-research、finding-reading、literature、research-basics、getting-started、problem-design |
| TOOL | 研究工具的功能、價格、版本、操作步驟 | tool-directory、tools-knowledge、thesis-notes-template |
| AI | AI 產品功能、方案、操作步驟、官方文件說法 | ai-tools、ai-workflow、ai-workflow-map、ai-quickstart、ai-quickstart-agent、ai-case-study、prompts、claude-tools-overview、ai-agents、harness、skill-build |
| ETH／VEN | 法規、期刊 AI 政策；期刊與研討會清單 | ethics、research-ethics-data；venues |
| MTH | 被歸給特定作者的方法學主張 | methodology、method-dsr、method-data、method-secondary-data、method-qualitative、method-experiment、systematic-review、quant-analysis-basics |

只抽可以查證的具體主張：統計門檻、APA 規則、工具功能與價格、操作步驟、法規條文、歸給特定作者的觀點，以及書目（作者、年份、篇名、刊名、卷期、頁碼、DOI）。個人建議、寫作心法、純意見不列。同一主張在多處出現時只列一條，位置全部列出。

### 1.2 怎麼查

- **原始出處優先**：原始論文、apastyle.apa.org、軟體與服務的官方文件與價格頁、全國法規資料庫、期刊官網、GitHub 原始碼。二手教科書與部落格最多當線索。
- **統計門檻追到最初提出的論文**。拿得到全文的直接貼原文；拿不到的，每條都標出實際讀到的是哪一層（全文、出版社摘要、軟體官方文件、開放取用文獻的逐字轉引）。
- **書目**：用 Crossref API 逐筆比對作者、年份、篇名、刊名、卷期與頁碼，再確認 `https://doi.org/<DOI>` 能解析。書籍改查出版社或書店書目。
- **逐字原文**：報告裡用引號貼出的英文或中文，都是查核時實際在來源上讀到的文字。拿不到原文的條目會明寫「未取得全文」，不憑記憶重建引文。
- **判定四選一**：
  - **正確**：原始出處支持站上的寫法。
  - **不精確**：大方向對，但門檻歸屬、適用條件、範圍、年份或措辭有出入，或簡化到可能誤導讀者。
  - **錯誤**：和原始出處矛盾，或書目資訊有錯，或描述的現況已經不成立。
  - **查不到**：找不到原始出處，或拿不到可以核對的原文。各條都寫明試過哪些地方。

### 1.3 限制（讀這份報告前要知道）

1. **付費牆**：下列原始文獻沒有取得全文，相關條目只核到摘要、官方文件或轉引層級：Fornell & Larcker (1981)、Hulland (1999)、Hair et al. (2019, *EBR*)、Cohen (1988)、Nunnally (1978)、Podsakoff et al. (2003)、Hu & Bentler (1999)、Davis (1989)、March & Smith (1995)、Nunamaker et al. (1990)、Yin、Lincoln & Guba (1985)、McGrath (1981)、Lee & Baskerville (2003)、Bacharach (1989)。有這些全文的人可以再補核。
2. **機器人防護**：apastyle.apa.org 與 help.openai.com 直接抓會回空白頁或 403，改用 r.jina.ai 網頁轉文字服務讀取官方頁面全文。pubsonline.informs.org、journals.aom.org、sagepub、dl.acm.org、misq.umn.edu、aisnet.org、COPE、quillbot.com 對程式抓取回 403；這是對方的防護，**不代表連結失效**，報告沒有因此判連結錯誤。
3. **網路環境**：查核環境的 HTTPS 經過代理。檢查網站憑證時用 `curl -v` 經 CONNECT 通道讀取原站憑證，另外用憑證透明度紀錄（crt.sh）交叉確認，沒有關閉 TLS 驗證。
4. **會變的資訊**：價格、方案、產品名稱、track 數、投稿方式、憑證狀態都可能在查核後又改變。VEN-19 就是一例：站上 2026-09 寫的時候是對的，查核當天已經不成立。

---

## 二、總表

| 代號 | 條數 | 正確 | 不精確 | 錯誤 | 查不到 |
|---|---:|---:|---:|---:|---:|
| STAT 統計門檻 | 19 | 12 | 7 | 0 | 0 |
| APA 格式與寫作 | 31 | 15 | 10 | 2 | 4 |
| REF 書目與理論歸屬 | 79 | 55 | 17 | 3 | 4 |
| TOOL 研究工具 | 50 | 34 | 12 | 2 | 2 |
| AI 工具與流程 | 36 | 28 | 8 | 0 | 0 |
| ETH／VEN 倫理與期刊清單 | 45 | 30 | 8 | 5 | 2 |
| MTH 方法學 | 28 | 15 | 8 | 1 | 4 |
| **合計** | **288** | **189** | **70** | **13** | **16** |

- REF 的 79 條包含 53 筆書目（第五節的彙整表）與 26 條觀點。13 個 DOI 全部能從 doi.org 解析。
- 同一個事實錯誤出現在兩頁時分開計數，並互相加註：彭明輝《論文寫作完全求生手冊》的出版年（APA-12 在 `style.md:249`、REF-53 在 `sources.md:37`），以及不平衡資料的 AUC 說法（STAT-18 在 `glossary.md:102`、MTH-12 在 `method-data.md`）。
- TOOL-41 原本因為拿不到 Henseler (2015) 全文判「查不到」。彙整時改用 STAT 節取得的全文補核，改判「正確」。

---

## 三、建議優先處理

### 3.1 錯誤（13 條）

| 代號 | 位置 | 問題 | 建議 |
|---|---|---|---|
| APA-01 | `docs/style.md:236` | 同一括號引用多篇時寫「依年份排列」。APA 7 原文："place the citations in alphabetical order"；只有同一作者的多篇才依年份排 | 改成「分號隔開，依第一作者姓氏字母排序；同作者多篇依年份」 |
| APA-12 | `docs/style.md:249` | 範例「彭明輝（2017）。論文寫作完全求生手冊。」年份錯，實為 2023/01/05 出版，也漏了副書名 | 改成 2023 並補副書名，詳見該條 |
| REF-53 | `docs/sources.md:37` | 同上，書目寫成聯經 2017 | 改成 2023 |
| REF-65 | `docs/theories.md:68`、`:325` | 說 TAM 的隱藏假設是「使用者沒有選擇不用的自由」，和 Davis et al. (1989) 要解釋的「accept or reject」相反 | 改寫成組織內、使用者自主決定是否使用的情境，詳見該條 |
| REF-67 | `docs/theories.md:126`、`:327` | 說 ELM 的周邊路徑「只能影響注意，進而影響涉入」。Petty et al. (1983) 顯示低涉入時周邊線索會直接改變態度；涉入是條件，不是結果。也和同頁的表格矛盾 | 改成「周邊路徑也會改變態度，但較短暫」 |
| TOOL-30 | `docs/tools-knowledge.md:109-110` | 說「以識別碼新增項目」和自動下載 PDF 沒有關係，和 Zotero 官方說明矛盾，也和同頁 2.3.1 打架 | 依官方說明改寫 |
| TOOL-31 | `docs/tools-knowledge.md:114-118` | citekey 日期問題的原理寫錯：Zotero 不論介面語言都認得「年月日」；是 Better BibTeX 自己的解析器不認得中文日期，會把原字串整串塞進 key | 改寫原理；「一律填 YYYY-MM-DD」的修法本身正確，保留 |
| VEN-02 | `docs/venues.md:40`、`:65` | ICIS 2026 官方 track 是 24 個，不是 12 個 | 改數字，或改成依官方 track 分組 |
| VEN-03 | `docs/venues.md:40` | 說電子商務、人機互動、醫療資訊、數位學習「ICIS 沒單獨列出」，實際上都有獨立 track（只有知識管理沒有） | 刪除或改寫 |
| VEN-06 | `docs/venues.md:67` | PACIS 2026 的 track 是 17 個（CFP 文字寫 18 個），不是 22 個 | 改數字並附官方頁 |
| VEN-12 | `docs/venues.md:83` | 把 submit.jim@gmail.com 寫成資訊管理學報的「投稿信箱」。官方："submissions by email are no longer accepted"。編輯部網址已轉到 jim-tw.com，投稿說明 PDF 已 404 | 改成線上投稿系統，信箱只用來詢問進度 |
| VEN-19 | `docs/venues.md:94-95`、`:119` | 「CSIM 官網 SSL 憑證已過期」查核當天不成立：2026-09-21 起已換成有效憑證，現在的狀況是網站維護（503） | 刪除憑證警告，改成維護中的說明 |
| MTH-17 | `docs/method-qualitative.md:169-173`、`:282` | Kember 反思模型的第一層寫成「描述」。Kember et al. (2000) 原文是 "habitual action"（習慣性行動），站上也沒附出處 | 改成「習慣性行動 → 理解 → 反思 → 批判性反思」並補出處 |

### 3.2 影響最大的「不精確」

這些不算寫錯，但很容易讓碩士生照著做錯：

- **STAT-06／STAT-07（HTMT、Fornell–Larcker）**：原始論文裡 0.85 和 0.90 是兩個並列的門檻選項，要看構念在概念上是否相近來選，不是「0.85–0.90 需說明」的灰色地帶。Fornell–Larcker 和交叉負荷在 PLS-SEM 中幾乎抓不到區辨效度問題，站上卻和 HTMT 並列。
- **STAT-15（PLS-SEM「樣本要求較寬鬆」）**：Goodhue et al. (2012, *MISQ*) 指出這正是資管圈流傳的迷思；小樣本時 PLS 一樣會損失檢定力。
- **STAT-03（信度 0.70）**：Nunnally 原本把 0.70 定位成研究初期可接受的下限，基礎研究他建議 0.80。
- **MTH-07（Hevner 七大規範）**：站上說論文「必須明確回應這七點」，但 Hevner et al. (2004, p. 82) 明寫 "we advise against mandatory or rote use of the guidelines"。
- **APA-15（圖說位置）**：站上寫「圖說置於圖下」，APA 7 是圖號與圖題在圖的上方，只有圖註在下方。
- **AI-03（改寫工具與 AI 偵測）**：站上用沒有出處的「社群實測」說規避無效，已發表的研究結論相反。結論（不要靠規避）可以保留，但理由要改成學術誠信。
- **AI-10（NotebookLM）**：Google 在 2026-07-16 把它改名為 Gemini Notebook，舊說明頁會轉址。

### 3.3 站內前後矛盾（查核時順帶發現）

| 位置 A | 位置 B | 矛盾 |
|---|---|---|
| `docs/method-survey.md:46`（前測「樣本取得極困難時可斟酌」） | `docs/method-survey.md:347`（「兩者都不能跳過」） | 前測能不能省略 |
| `docs/checklists.md:184`（「投影片十張左右，每張約兩分鐘」） | `docs/defense.md:175-177`（頁數依系所而異，每頁約一至兩分鐘） | 口試投影片頁數與時間 |
| `docs/theories.md:126`（周邊路徑只影響注意） | `docs/theories.md:117-120`（表格：周邊路徑造成短暫的態度改變） | 見 REF-67 |
| `docs/theories.md:69`（TAM 終點是意圖） | `docs/theories.md:60-64`（圖上畫到實際使用） | 見 REF-64 |
| `docs/tools-knowledge.md:109-110` | 同頁 2.3.1 的 note 框 | 識別碼新增與 PDF 下載，見 TOOL-30 |
| `docs/writing.md:116`（圖說置於圖下） | `docs/writing.md:107`（採 APA 第七版） | 見 APA-15 |
| `docs/prompts.md:658`（SKILL 只能在 Claude 用） | `docs/ai-quickstart-agent.md:122`、`docs/ai-quickstart.md:62` | 見 AI-35 |
| `docs/method-survey.md:169`、`:349`（「大於 0.7」） | `docs/method-survey.md:225`（「≥ 0.70」） | 信度門檻寫法不一致，見 STAT-03 |

### 3.4 全部「不精確」與「查不到」代號

- 不精確（70）：STAT-03、06、07、11、15、16、18｜APA-03、05、09、10、11、14、15、17、26、29｜REF-04、05、07、11、16、32、33、36、37、40、59、63、64、66、72、74、79｜TOOL-02、04、08、10、17、19、23、27、32、39、40、45｜AI-02、03、07、10、19、34、35、36｜ETH-02、06、07、15、16、VEN-14、15、18｜MTH-03、07、09、10、11、12、19、23
- 查不到（16）：APA-13、22、25、27｜REF-57、58、62、81｜TOOL-18、50｜VEN-13、17｜MTH-02、05、20、24

---

以下第四到第十節是逐條查核紀錄，依代號分節。每條的格式：位置、站上寫法、原始出處（附網址與逐字原文）、判定、說明、建議改法，會變的資訊另外標查核日期。

## 四、STAT：統計門檻與量化判準

範圍：`docs/method-survey.md`、`docs/glossary.md` 統計表、`docs/tools-knowledge.md` 範本中的門檻範例。

**原文取得層級**：統計門檻多出自付費期刊或絕版書。每條都標出實際讀到的是哪一層：
- 【全文】讀到原始論文全文（開放取用）
- 【摘要】只讀到原始論文的出版社摘要（Crossref／OpenAlex 收錄的摘要）
- 【官方文件】讀到軟體官方文件，文件中寫明門檻出處
- 【轉引】原文未取得，引用的是開放取用的學術論文對原文的逐字轉引

判定欄的「正確」若不是【全文】或【摘要】層級，代表原文的逐字內容**沒有直接讀到**，是靠官方文件與轉引交叉確認。以下列出的原文全部是實際讀到的文字，沒有任何一句憑記憶重建。

#### STAT-01　PLS-SEM 判準表整體出自 SmartPLS 官方文件
- 位置：`docs/method-survey.md:218`–`240`
- 站上寫法：「以下為 SmartPLS 官方文件所列的判準門檻（依 Hair 等人的建議）」，表中列出 outer loading ≥ 0.70、α ≥ 0.70、ρ_a／ρ_c ≥ 0.70、AVE ≥ 0.50、HTMT ≤ 0.85／0.85–0.90／> 0.90、VIF ≤ 3／3–5／> 5、p ≤ 0.05、f² 0.02／0.15／0.35、Q²_predict > 0、RMSE 對 LM、MGA p ≤ 0.05、MICOM。
- 原始出處：SmartPLS, *Result Color Thresholds in SmartPLS Reports*，<https://smartpls.com/documentation/functionalities/thresholds/>【官方文件】
  - 原文："The thresholds summarized on this page are primarily based on recommendations in the PLS-SEM literature, especially Hair, Hult, Ringle, and Sarstedt (2027) and Hair, Sarstedt, Ringle, and Gudergan (2024). Depending on the research objective, model type, discipline, and publication requirements, researchers may need to justify different cut-off values."
  - 表格逐列：Outer loading ">= 0.70"；Cronbach's alpha ">= 0.70"；rho_a、rho_c ">= 0.70"；AVE ">= 0.50"；HTMT "<= 0.85 | > 0.85 and <= 0.90 | > 0.90"；VIF "<= 3.00 | > 3.00 and <= 5.00 | > 5.00"；Bootstrapping p value "<= 0.05"；Q²_predict ">= 0"；"PLS-SEM < LM"；Permutation MGA p value "<= 0.05"。
- 判定：正確
- 說明：站上每個數字都和官方頁一致。不過官方頁本身是二手彙整，每個門檻各有原始出處，見下面各條。另外官方頁引用的是 Hair et al.（2027）第 4 版 *Primer*，出版年在查核日之後，讀者照抄引用時會覺得奇怪。
- 建議改法：加上官方頁網址與查核日期；建議論文中引用各門檻的原始論文（見 STAT-02 起各條），不要只寫「依 SmartPLS」。
- 查核日期：2026-10-23

#### STAT-02　外部負荷量 ≥ 0.70
- 位置：`docs/method-survey.md:224`、`docs/glossary.md:78`
- 站上寫法：「外部負荷量（outer loading）｜ ≥ 0.70」
- 原始出處：SmartPLS 官方門檻頁（同上）【官方文件】；最常被引的源頭為 Hulland (1999), *Strategic Management Journal*, 20(2), 195–204, <https://doi.org/10.1002/(SICI)1097-0266(199902)20:2<195::AID-SMJ13>3.0.CO;2-7>（付費，未取得全文）
  - 原文（官方頁）："Loadings of 0.70 or higher are generally desirable because they indicate that the construct explains more than half of the indicator's variance (0.70² is approximately 0.50). ... Indicators with loadings between 0.40 and 0.70 should only be removed if their removal increases composite reliability or AVE above the recommended threshold."；"outer loadings of 0.60 or higher can be acceptable in exploratory research"
- 判定：正確
- 說明：門檻本身正確。站上沒交代 0.40–0.70 之間「不必一律刪除」的條件，學生容易看到 0.68 就刪題。
- 建議改法：在表後補一句「0.40–0.70 的題項，只有刪除後能讓 CR 或 AVE 達標時才考慮刪；探索性研究可接受 0.60」。

#### STAT-03　Cronbach's α ≥ 0.70／「信度通常要求大於 0.7」
- 位置：`docs/method-survey.md:169`、`docs/method-survey.md:225`、`docs/method-survey.md:349`、`docs/glossary.md:75`
- 站上寫法：「測量結果的一致性與穩定性。**通常要求大於 0.7。**」；「Cronbach's α ｜ ≥ 0.70」；「信度 > 0.7」
- 原始出處：Nunnally, J. C. (1978). *Psychometric theory* (2nd ed.), p. 245（書籍，未取得）。逐字轉引：
  - Ellis, J. L. (2013). A standard for test reliability in group research. *Behavior Research Methods*, 45(1), 16–24. <https://doi.org/10.3758/s13428-012-0223-z>（PMC 全文 <https://pmc.ncbi.nlm.nih.gov/articles/PMC3578733/>）【轉引】："Authors who wish to determine whether their computed reliability is sufficiently high often cite Nunnally (1978, p. 245; Nunnally & Bernstein, 1994), who stated that “increasing reliabilities much beyond .80 is often wasteful of time and funds” in basic research"
  - Gross, T. (2023). arXiv:2308.08322, <https://arxiv.org/pdf/2308.08322>【轉引，引 Lance, Butts & Michels, 2006, *ORM*, 9(2), 202–220】："The often quoted 𝛼 ≥ .70 was described by Nunnally only to “save time and energy,” whereas a greater threshold of .80 was endorsed for basic research"
- 判定：不精確
- 說明：0.70 是 SmartPLS／Hair 的通用門檻，寫在 PLS 表裡沒有問題。但第 169 行與第 349 行把它寫成信度的普遍要求，這不符合 Nunnally 的原意：0.70 是研究早期階段可以接受的下限，基礎研究他建議 0.80。另外站上「大於 0.7」和「≥ 0.70」兩種寫法混用。
- 建議改法：第 169 行改成「常見門檻為 0.70（Nunnally, 1978 原本是針對研究初期的量表；基礎研究他建議 0.80），應依研究階段與所引用的判準說明」；第 349 行統一寫成「≥ 0.70」。

#### STAT-04　組合信度 ρ_a、ρ_c ≥ 0.70；> 0.95 可能是題項冗餘
- 位置：`docs/method-survey.md:174`、`docs/method-survey.md:226`、`docs/glossary.md:76`
- 站上寫法：「組合信度 ρ_a、ρ_c ｜ ≥ 0.70（過高如 > 0.95 反而可能是題項冗餘）」
- 原始出處：SmartPLS 官方門檻頁【官方文件】；ρ_A 的原始論文是 Dijkstra, T. K., & Henseler, J. (2015). *MIS Quarterly*, 39(2), 297–316. <https://doi.org/10.25300/MISQ/2015/39.2.02>（Crossref 書目已核對，未取得全文）
  - 原文（官方頁）："Values of 0.70 or higher indicate satisfactory reliability; note that very high values (above 0.95) may indicate redundant indicators."
- 判定：正確
- 說明：和官方文件一致。另外，CR 最早常被引的門檻是 Bagozzi & Yi (1988) *JAMS*, 16(1), 74–94 的 0.60（Crossref 書目已核對，全文付費未讀到逐字原文，所以這裡不下結論），讀者看到別的論文用 0.60 時不要以為是錯的。
- 建議改法：不需修改。

#### STAT-05　AVE ≥ 0.50
- 位置：`docs/method-survey.md:227`、`docs/glossary.md:77`、`docs/problem-design.md:73`
- 站上寫法：「平均變異抽取量 AVE ｜ ≥ 0.50」
- 原始出處：Fornell, C., & Larcker, D. F. (1981). Evaluating structural equation models with unobservable variables and measurement error. *Journal of Marketing Research*, 18(1), 39–50. <https://doi.org/10.1177/002224378101800104>（付費，只讀到摘要）；SmartPLS 官方門檻頁把 AVE 門檻歸給這篇【官方文件】
  - 原文（官方頁）："Average variance extracted (AVE) | >= 0.50 | — | < 0.50 | Fornell & Larcker (1981); Hair et al. (2027)"；"AVE values of 0.50 or higher indicate that the construct explains at least half of the variance of its indicators."
  - 原文（F&L 摘要）："the authors develop and apply a testing system based on measures of shared variance within the structural model, measurement model, and overall model."（摘要沒有寫數字）
- 判定：正確（原文逐字未取得）
- 說明：門檻與歸屬一致。Fornell & Larcker 內文的 0.50 那句沒有讀到，所以這條沒辦法貼出原始論文的逐字原文。
- 建議改法：不需修改；引用時請引 Fornell & Larcker (1981)。

#### STAT-06　HTMT ≤ 0.85 為佳；0.85–0.90 需說明；> 0.90 有問題
- 位置：`docs/method-survey.md:228`、`docs/glossary.md:81`（`docs/tools-knowledge.md:590` 的範例另列於 TOOL-41）
- 站上寫法：「HTMT（區辨效度）｜ ≤ 0.85 為佳；0.85–0.90 需說明；> 0.90 有問題」；glossary：「≤ .85 為佳；> .90 有問題」
- 原始出處：Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity in variance-based structural equation modeling. *Journal of the Academy of Marketing Science*, 43(1), 115–135. <https://doi.org/10.1007/s11747-014-0403-8>【全文，CC BY 4.0】
  - 原文（p. 121）："The exact threshold level of the HTMT is debatable; after all, “when is a correlation close to one”? Some authors suggest a threshold of 0.85 (Clark and Watson 1995; Kline 2011), whereas others propose a value of 0.90 (Gold et al. 2001; Teo et al. 2008)."
  - 原文（討論）："Take, for example, the technology acceptance model and its variations (Davis 1989; Venkatesh et al. 2003), which include the constructs intention to use and the actual use. Although these constructs are conceptually different, they may be difficult to distinguish empirically in all research settings. Therefore, the choice of a more liberal HTMT criterion in terms of specificity (i.e., HTMT.90 or HTMTinference, depending on the sample size) seems warranted. Conversely, if the strictest standards are followed, this requires HTMT.85 to assess discriminant validity."
  - SmartPLS FAQ【官方文件】："Values between 0.85 and 0.90 may be acceptable when constructs are conceptually similar, but should be interpreted carefully."
- 判定：不精確
- 說明：數字沒錯，但原始論文裡 0.85 和 0.90 是兩個**並列的門檻選項**，要看構念在概念上是否相近、研究者要多保守來選，不是「0.85–0.90 是灰色地帶」。原論文還提出用信賴區間檢定的 HTMT_inference，站上沒提。
- 建議改法：「HTMT ≤ 0.85（較嚴格）；構念在概念上相近（如使用意圖與實際使用）時可採 0.90（Henseler et al., 2015）；也可用 bootstrap 信賴區間檢定 HTMT 是否顯著小於 1（HTMT_inference）。論文中要寫明採用哪一個門檻與理由。」glossary 同步。

#### STAT-07　Fornell–Larcker 準則與交叉負荷列為區辨效度指標，沒有提醒其限制
- 位置：`docs/method-survey.md:185`、`docs/method-survey.md:250`
- 站上寫法：「區辨（區別）效度 ｜……｜ Fornell–Larcker、交叉負荷、HTMT」；「區別效度（HTMT、Fornell-Larcker）」
- 原始出處：Henseler et al. (2015)，同上【全文】
  - 原文："results clearly show that the two standard approaches to assessing the discriminant validity in variance-based SEM— the Fornell-Larcker criterion and the assessment of crossloadings—have an unacceptably low sensitivity, which means that they are largely unable to detect a lack of discriminant validity. In particular, the assessment of the cross-loadings completely fails to detect discriminant validity issues."
- 判定：不精確
- 說明：站上把三者並列，讀者會以為只做 Fornell–Larcker 或交叉負荷就夠了。原始論文的模擬結果顯示這兩種方法在 PLS-SEM 中幾乎抓不到區辨效度問題。
- 建議改法：表格改成「HTMT（主要判準）；Fornell–Larcker 與交叉負荷可附報，但 Henseler et al. (2015) 指出兩者在 PLS-SEM 中敏感度很低，不能單獨作為證據」。

#### STAT-08　VIF ≤ 3 為佳；3–5 需留意；> 5 有問題
- 位置：`docs/method-survey.md:234`、`docs/glossary.md:82`（`docs/tools-knowledge.md:590` 的範例另列於 TOOL-41）
- 站上寫法：「VIF（共線性）｜ ≤ 3.00 為佳；3.00–5.00 需留意；> 5.00 有問題」
- 原始出處：SmartPLS 官方門檻頁【官方文件】；這套三分法出自 Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report the results of PLS-SEM. *European Business Review*, 31(1), 2–24. <https://doi.org/10.1108/EBR-11-2018-0203>（付費；SSRN 版回 403，未取得全文）
  - 原文（官方頁）："VIF values of 3.00 or lower indicate that collinearity among indicators or predictor constructs is not a critical issue; values above 5.00 indicate critical collinearity problems."
- 判定：正確（原文逐字未取得）
- 說明：和官方文件一致。傳統迴歸文獻常見的是 VIF > 10，O'Brien (2007) *Quality & Quantity*, 41(5), 673–690（<https://doi.org/10.1007/s11135-006-9018-6>，Crossref 已核對）專門討論這類經驗法則不能機械套用；讀者看到 10 不要以為站上寫錯。
- 建議改法：可補一句「這是 PLS-SEM 的慣例（Hair et al., 2019）；一般迴歸文獻常見 VIF > 10 的較寬鬆門檻」。

#### STAT-09　效果量 f²：0.02 小、0.15 中、0.35 大
- 位置：`docs/method-survey.md:236`、`docs/glossary.md:84`
- 站上寫法：「效果量 f² ｜ ≥ 0.02 小、≥ 0.15 中、≥ 0.35 大」
- 原始出處：Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum（書籍，未取得）；SmartPLS 官方門檻頁【官方文件】
  - 原文（官方頁）："Following Cohen (1988), f² values of 0.02, 0.15, and 0.35 represent small, medium, and large effects."
- 判定：正確（原文逐字未取得）
- 說明：數字與出處一致。Cohen 自己強調這組慣例只在缺乏領域基準時使用；這句話我沒讀到原書，所以不寫進建議。
- 建議改法：不需修改；引用時引 Cohen (1988)。

#### STAT-10　Q²_predict > 0；「Q² / Q²_predict > 0 表示有預測相關性」
- 位置：`docs/method-survey.md:237`、`docs/glossary.md:85`
- 站上寫法：「預測相關性 Q²_predict ｜ > 0」；glossary：「Q² / Q²_predict ｜ > 0 表示有預測相關性」
- 原始出處：Shmueli, G., Sarstedt, M., Hair, J. F., Cheah, J.-H., Ting, H., Vaithilingam, S., & Ringle, C. M. (2019). Predictive model assessment in PLS-SEM: Guidelines for using PLSpredict. *European Journal of Marketing*, 53(11), 2322–2347. <https://doi.org/10.1108/EJM-02-2019-0189>（讀到摘要）；SmartPLS 官方門檻頁【官方文件】
  - 原文（官方頁）："A Q²_predict value of zero or higher indicates that the PLS-SEM model outperforms the naive indicator-mean benchmark for the respective indicator."
- 判定：正確
- 說明：門檻正確。glossary 把 blindfolding 的 Q²（Stone–Geisser，樣本內）和 PLSpredict 的 Q²_predict（樣本外，和指標平均數比）寫成同一格，兩者算法與意義不同，讀者可能混用。
- 建議改法：glossary 分成兩列：「Q²（blindfolding）：> 0 表示有預測相關性」「Q²_predict（PLSpredict）：> 0 表示預測優於以指標平均數預測的基準」。

#### STAT-11　樣本外預測：「PLS-SEM 的 RMSE 應低於線性迴歸基準（LM）」
- 位置：`docs/method-survey.md:238`
- 站上寫法：「樣本外預測 ｜ PLS-SEM 的 RMSE 應低於線性迴歸基準（LM）」
- 原始出處：Shmueli et al. (2019)，同上（摘要）；SmartPLS 官方門檻頁【官方文件】
  - 原文（官方頁）："For the root mean squared error (RMSE) and the mean absolute error (MAE), lower prediction errors indicate better predictive performance. SmartPLS marks the PLS-SEM value in green when it is lower than the corresponding linear model (LM) benchmark. The share of indicators for which the PLS-SEM model outperforms the LM benchmark indicates whether the model has high, medium, low, or no predictive power."
- 判定：不精確
- 說明：原始判準是**逐題比較**，再看「有多少比例的指標贏過 LM」，分成高／中／低／無四級預測力；也可以改用 MAE。站上寫成一條是非題門檻，讀者會以為有一題輸給 LM 就不合格。
- 建議改法：「逐一比較每個依變數指標的 PLS-SEM 與 LM 預測誤差（RMSE，誤差分布明顯不對稱時用 MAE）。全部指標都低於 LM 為高預測力，多數為中、少數為低，都沒有則缺乏預測力（Shmueli et al., 2019）。」

#### STAT-12　Bootstrapping p ≤ 0.05
- 位置：`docs/method-survey.md:235`
- 站上寫法：「路徑係數顯著性 ｜ Bootstrapping p ≤ 0.05」
- 原始出處：SmartPLS 官方門檻頁【官方文件】
  - 原文："In bootstrapping reports, SmartPLS marks p values of 0.05 or lower in green. ... Depending on the study, other significance levels (e.g., 1% or 10%) may be appropriate and should be justified."
- 判定：正確
- 建議改法：不需修改。

#### STAT-13　跑 MGA 前先做 MICOM；Permutation MGA p ≤ 0.05
- 位置：`docs/method-survey.md:240`、`docs/glossary.md:91`
- 站上寫法：「Permutation MGA p ≤ 0.05 表示群組間差異顯著；跑 MGA 前應先做 MICOM 測量不變性檢驗。」；glossary：「MICOM / measurement invariance ｜ 跑 MGA 前必做」
- 原始出處：Henseler, J., Ringle, C. M., & Sarstedt, M. (2016). Testing measurement invariance of composites using partial least squares. *International Marketing Review*, 33(3), 405–431. <https://doi.org/10.1108/IMR-09-2014-0304>【摘要】
  - 原文："Researchers in international marketing and other disciplines need to conduct this kind of assessment before undertaking multigroup analyses."
  - SmartPLS 官方頁："Permutation MGA p value | <= 0.05"；"MICOM Step 2 p value | >= 0.05"
- 判定：正確
- 說明：補充一點：MICOM 第 2 步的 p 值方向與其他步驟相反（≥ 0.05 才代表組成不變性成立），學生常看反。
- 建議改法：可補「MICOM 第 2 步 p ≥ 0.05 才表示組成不變性成立，方向與 MGA 相反」。

#### STAT-14　形成性構念不適用 Cronbach's α
- 位置：`docs/method-survey.md:214`
- 站上寫法：「例如對形成性構念檢查 Cronbach's α 是沒有意義的。」
- 原始出處：SmartPLS 官方門檻頁【官方文件】
  - 原文："Reliability statistics such as Cronbach's alpha, rho_a, rho_c, and AVE are not meaningful for formative constructs."
- 判定：正確
- 建議改法：不需修改；可補「AVE、CR 同樣不適用；形成性構念看冗餘分析、指標 VIF 與外部權重」。

#### STAT-15　PLS-SEM「樣本量相對寬鬆」「樣本要求較寬鬆」
- 位置：`docs/method-survey.md:199`、`docs/glossary.md:73`
- 站上寫法：「樣本量 ｜ 相對寬鬆 ｜ 需求較大」；「預測導向、樣本要求較寬鬆」
- 原始出處：Goodhue, D. L., Lewis, W., & Thompson, R. (2012). Does PLS have advantages for small sample size or non-normal data? *MIS Quarterly*, 36(3), 981–1001. <https://doi.org/10.2307/41703490>【摘要】
  - 原文："There is a pervasive belief in the MIS research community that PLS has advantages over other techniques when analyzing small sample sizes or data with non-normal distributions. ... When used with small sample sizes, PLS, like the other techniques, suffers from increased standard deviations, decreased statistical power,and reduced accuracy. All three techniques were remarkably robust against moderate departures from normality, and equally so."
  - Kock, N., & Hadaya, P. (2018). Minimum sample size estimation in PLS-SEM: The inverse square root and gamma-exponential methods. *Information Systems Journal*, 28(1), 227–261. <https://doi.org/10.1111/isj.12131>【摘要】："The ‘10-times rule’ has been a favourite because of its simplicity of application, even though it tends to yield imprecise estimates."
- 判定：不精確
- 說明：說 PLS-SEM 可以在比 CB-SEM 小的樣本下**收斂、算得出結果**沒有錯，但資管領域的模擬研究指出，小樣本時 PLS 一樣會損失檢定力與準確度。「樣本要求較寬鬆」容易被讀成「小樣本可以用 PLS」，這正是 Goodhue et al. 點名的迷思。method-survey.md 第 138 行已經寫了事前樣本規劃，但這兩張表沒有呼應。
- 建議改法：表格改成「可估計較小樣本，但小樣本一樣損失檢定力（Goodhue et al., 2012）；樣本數應事前估算，例如反平方根法（Kock & Hadaya, 2018）」；glossary 改為「預測導向；可處理較小樣本，但不代表小樣本就夠」。

#### STAT-16　SRMR 常見門檻 < .08
- 位置：`docs/glossary.md:86`
- 站上寫法：「標準化殘差均方根 ｜ SRMR ｜ 常見門檻 < .08」
- 原始出處：Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1–55. <https://doi.org/10.1080/10705519909540118>【摘要】
  - 原文："The results suggest that, for the ML method, a cutoff value close to .95 for TLI, BL89, CFI, RNI, and Gamma Hat; a cutoff value close to .90 for Mc; a cutoff value close to .08 for SRMR; and a cutoff value close to .06 for RMSEA are needed ... Furthermore, the 2-index presentation strategy is required to reject reasonable proportions of various types of true-population and misspecified models."
- 判定：不精確
- 說明：原始門檻是「接近 .08」，針對 CB-SEM 的 ML 估計，而且要搭配另一個指標（如 CFI、RMSEA）一起報告，不是單一指標的硬門檻。glossary 這一格放在 PLS-SEM 相關詞條之間，沒有交代脈絡，讀者容易拿來當 PLS-SEM 的模型適配判準。
- 建議改法：「CB-SEM（ML 估計）常引 Hu & Bentler (1999)：SRMR 接近 .08 以下，並搭配 CFI 或 RMSEA 一起判讀。PLS-SEM 的適配指標仍有爭議，使用時要說明依據。」

#### STAT-17　Harman 單因子檢定「最常見，但也最受質疑」
- 位置：`docs/method-survey.md:289`、`docs/method-survey.md:249`、`docs/checklists.md:64`
- 站上寫法：「Harman 單因子檢定（最常見，但也最受質疑；通過不代表沒有問題）」
- 原始出處：Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research. *Journal of Applied Psychology*, 88(5), 879–903. <https://doi.org/10.1037/0021-9010.88.5.879>（付費，未取得全文。MIS Quarterly 線上附錄有轉引 p. 889 的 "actually does nothing to statistically control for (or partial out) method effects"，但該 PDF 直接下載回 403，只在搜尋摘要看到，不算逐字核對）
- 判定：正確（原文逐字未取得）
- 說明：方向與一般方法論文獻一致，站上的提醒恰當。原文沒有讀到，所以沒有附逐字原文。
- 建議改法：可補引 Podsakoff et al. (2003) 作為出處。

#### STAT-18　AUC「類別不平衡時比 Accuracy 可靠」
- 位置：`docs/glossary.md:102`
- 站上寫法：「曲線下面積 ｜ AUC ｜ 類別不平衡時比 Accuracy 可靠」
- 原始出處：Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLoS ONE*, 10(3), e0118432. <https://doi.org/10.1371/journal.pone.0118432>【摘要】
  - 原文："We show here that the visual interpretability of ROC plots in the context of imbalanced datasets can be deceptive with respect to conclusions about the reliability of classification performance, owing to an intuitive but wrong interpretation of specificity. PRC plots, on the other hand, can provide the viewer with an accurate prediction of future classification performance"
- 判定：不精確
- 說明：（同一問題在 `docs/method-data.md` 另見 MTH-12。）「比 Accuracy 可靠」大方向沒錯，但只寫 AUC 會被讀成 ROC-AUC。在極度不平衡的資料上，ROC-AUC 本身也可能誤導，PR-AUC 比較合適。
- 建議改法：「ROC-AUC 不受分類門檻影響，比 Accuracy 不易被多數類別灌水；類別極度不平衡時建議改看或同時報告 PR-AUC（Saito & Rehmsmeier, 2015）。」

#### STAT-19　精確率、召回率、F1 定義
- 位置：`docs/glossary.md:99`–`101`
- 站上寫法：「預測為正的當中，真的是正的比例」「實際為正的當中，被抓出來的比例」「精確率與召回率的調和平均」
- 原始出處：scikit-learn 官方文件 *precision_recall_fscore_support*，<https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html>【官方文件】
  - 原文："The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives."；"The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives."；"The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall ... beta == 1.0 means recall and precision are equally important."
- 判定：正確
- 建議改法：不需修改。

#### 本節附帶發現（站內前後矛盾，不計入主張數）
- `docs/method-survey.md:46` 寫前測「樣本取得極困難時可斟酌，但要在限制中說明」，但 `docs/method-survey.md:347` 重點回顧寫「預試看『懂不懂』，前測看『準不準』，兩者都不能跳過」。兩句互相矛盾，建議把第 347 行改成「預試不能跳過；前測只有在樣本極難取得時才可省略，並寫進限制」。

### 小計（STAT）
- 查核 19 條：正確 12、不精確 7、錯誤 0、查不到 0
- 正確的 12 條中，有 4 條（STAT-05、08、09、17）原始論文或原書全文付費、沒有讀到逐字原文，是用軟體官方文件或開放取用文獻的轉引交叉確認；STAT-02 的原始論文 Hulland (1999) 也沒有讀到全文。
- 不精確：STAT-03、06、07、11、15、16、18

---

## 五、APA：格式與寫作規則

範圍：`docs/style.md`、`docs/writing.md`、`docs/defense.md`、`docs/post-defense.md`、`docs/checklists.md`。統計門檻不在本報告範圍。

取得方式說明：
- apastyle.apa.org 對 curl／WebFetch 一律回 Incapsula 防機器人頁（空白內容），網頁典藏站（web.archive.org）在本環境連不上。所以 APA 官方頁面改用 r.jina.ai 這個閱讀器服務抓取，它回傳的是 apastyle.apa.org 頁面本身的文字。以下 APA 引文都逐字取自這些抓回的官方頁面或 APA 官方 PDF 指南（What's New 7e Guide、Numbers and Statistics Guide），不是搜尋摘要。
- 書目一律用 Crossref API 核對。
- 法規條文取自全國法規資料庫（law.moj.gov.tw）與教育部主管法規共用系統（edu.law.moe.gov.tw）。
- 這五頁沒有出現 AI 工具的引用格式、標題層級、二手引用格式或參考文獻作者數上限這幾類 APA 規則，所以這些項目沒有可查的站上主張。

---

#### APA-01　同一括號引用多篇文獻時「依年份排列」
- 位置：`docs/style.md:236`
- 站上寫法：「| 同括號多篇 | 分號隔開，依年份排列 | （Davis, 1989; Venkatesh et al., 2012） |」
- 原始出處：APA Style，〈Citing multiple works〉，<https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/multiple-works>（Publication Manual 7th ed., §8.12）
  - 原文："When citing multiple works parenthetically, place the citations in alphabetical order, separating them with semicolons."；"Arrange two or more works by the same authors by year of publication."；"Give the authors’ surnames once; for each subsequent work, give only the date."
- 判定：錯誤
- 說明：APA 7 規定不同作者的多篇文獻依第一作者姓氏的字母順序排列，只有同一作者的多篇才依年份排。站上範例 Davis 與 Venkatesh 剛好字母和年份順序一致，所以看不出問題，但規則本身寫錯了。照站上規則，（Venkatesh et al., 2012; Davis, 2014）這種排法會被當成正確。我重讀過原文第二次，確認判定無誤。
- 建議改法：「分號隔開，依第一作者姓氏字母排序（與參考文獻清單順序相同）；同一作者的多篇依年份排列，姓名只寫一次，如（Davis, 1989, 1993）」。
- 查核日期：2026-10-23

#### APA-02　APA 7 三位以上作者從第一次引用起就用「第一作者等人／et al.」
- 位置：`docs/style.md:234`、`docs/style.md:272`（APA 7 欄）
- 站上寫法：「| 英文 3 位以上作者 | 第一作者等人（年份） | Venkatesh 等人（2012） |」；「| 三位以上作者首次引用 | 列出所有作者 | 首次起即用「第一作者等人」 |」
- 原始出處：APA Style，〈Author–date citation system〉，<https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/author-date>；書目用 Crossref 核對 DOI 10.2307/41410412
  - 原文："For a work with three or more authors, include the name of only the first author plus “et al.” in every citation (even the first citation)."
  - Crossref：Venkatesh, V.; Thong, J. Y. L.; Xu, X.（2012），"Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology"，*MIS Quarterly*, 36(1), 157–178，DOI 10.2307/41410412。共三位作者。
- 判定：正確
- 說明：規則與範例（三位作者）都符合 APA 7。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### APA-03　兩位作者的範例「Hair 與 Risher（2019）」
- 位置：`docs/style.md:233`
- 站上寫法：「| 英文 2 位作者 | 姓氏與姓氏（年份） | Hair 與 Risher（2019） |」
- 原始出處：Crossref 查詢（作者 Hair＋Risher，2019 年）；DOI 10.1108/EBR-11-2018-0203
  - Crossref：Hair, J. F.; Risher, J. J.; Sarstedt, M.; Ringle, C. M.（2019），"When to use and how to report the results of PLS-SEM"，*European Business Review*, 31(1), 2–24。共四位作者。Crossref 查不到只有 Hair 與 Risher 兩位作者的 2019 年文獻。
  - APA 原文（author-date 頁）："For a work with one or two authors, include the author name(s) in every citation."
- 判定：不精確
- 說明：這個範例看起來像在引用資管讀者最熟悉的那篇 PLS-SEM 報告指南，但那篇有四位作者，依 APA 7 要寫 Hair 等人（2019）。照抄範例的讀者會寫錯作者數。規則本身沒錯，錯的是範例。
- 建議改法：換成真的只有兩位作者的文獻，例如 Crossref 查得的 Hair 與 Sarstedt（2019）（*Project Management Journal*，DOI 10.1177/8756972819882132）；或明確標示「⟨姓氏⟩與⟨姓氏⟩（年份）」為虛構範例。

#### APA-04　同作者同年的多篇文獻加 a、b
- 位置：`docs/style.md:235`
- 站上寫法：「| 同作者同年多篇 | 加 a, b | （Liu et al., 2024a, 2024b） |」
- 原始出處：APA Style，〈Citing works with the same author and date〉，<https://apastyle.apa.org/style-grammar-guidelines/citations/basic-principles/same-year-author>（§8.19）
  - 原文："When multiple references have an identical author (or authors) and publication year, include a lowercase letter after the year. These letters are assigned when the references are placed in order in the reference list (alphabetically by title, following the guidelines in Section 9.47)."
- 判定：正確
- 說明：規則正確。小補充：a、b 是依參考文獻清單中的篇名字母順序指定，而且必須是完全相同的作者群才適用。
- 建議改法：不需修改。可選擇補一句「a、b 依篇名字母順序指定，且作者群須完全相同」。
- 查核日期：2026-10-23

#### APA-05　APA 6 規定三位以上作者首次引用「列出所有作者」
- 位置：`docs/style.md:272`
- 站上寫法：「| 三位以上作者首次引用 | 列出所有作者 | 首次起即用「第一作者等人」 |」
- 原始出處：APA，*What's New in the Seventh Edition*（官方 PDF 指南），<https://apastyle.apa.org/instructional-aids/whats-new-7e-guide.pdf>
  - 原文："In-text citations have been simplified and made easier: For works with three or more authors, include the name of only the first author and the abbreviation “et al.” in every in-text citation, even the first time a citation appears."；"Sixth edition style: First citation: Smith, Ellenio, and Pruitt (2019) or (Smith, Ellenio, & Pruitt, 2019); subsequent citation: Smith et al. (2019) or (Smith et al., 2019)"
- 判定：不精確
- 說明：APA 官方對照只拿三位作者當例子，證實第 6 版首次引用要列出全部作者。但站上寫成「三位以上一律列出所有作者」。多個二手來源（例如大學圖書館 FAQ）指出，第 6 版只有 3–5 位作者時首次全列，6 位以上首次就用 et al.。這一點我沒拿到 APA 第 6 版手冊原文（官方第 6 版資源頁已 404），所以只能判不精確，不判錯誤。
- 建議改法：APA 6 欄改成「3–5 位作者首次列出全部，之後用 et al.」，或加註「（第 6 版細則另有 6 位以上的例外）」。

#### APA-06　DOI 寫法：APA 6 用 doi:10.xxx，APA 7 用 https://doi.org/10.xxx
- 位置：`docs/style.md:273`
- 站上寫法：「| DOI 格式 | doi:10.xxx | https://doi.org/10.xxx |」
- 原始出處：APA Style，〈DOIs and URLs〉，<https://apastyle.apa.org/style-grammar-guidelines/references/dois-urls>；What's New 7e Guide（同上）
  - 原文："The preferred format of the DOI has changed over time. Although older works use previous formats (e.g., “http:/dx.doi.org/” or “doi:” or “DOI:” before the DOI number), in your reference list, standardize DOIs into the current preferred format for all entries."；（What's New）"The label “DOI:” is no longer used before a DOI. DOIs should begin with the prefix https://doi.org/"
- 判定：正確
- 說明：符合官方說明。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### APA-07　APA 7 不列出版地
- 位置：`docs/style.md:274`
- 站上寫法：「| 出版地 | 需列出 | 不需列出 |」
- 原始出處：APA Style，〈Book references〉，<https://apastyle.apa.org/style-grammar-guidelines/references/examples/book-references>；What's New 7e Guide
  - 原文："Do not include the publisher location."；（What's New）"Do not include physical locations for publishers in any reference type. Whereas a sixth edition reference included “Washington, DC: SAGE.,” a seventh edition reference now says only “SAGE.”"
- 判定：正確
- 說明：符合官方說明。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### APA-08　APA 7 不用 "Retrieved from"
- 位置：`docs/style.md:275`
- 站上寫法：「| "Retrieved from" | 需要 | 不需要（直接附 URL） |」
- 原始出處：What's New 7e Guide；〈DOIs and URLs〉頁
  - 原文："The words “Retrieved from” are used before a URL only when a retrieval date is also needed; otherwise, URLs are presented without a label."；"Because a hyperlink leads readers directly to the content, it is not necessary to include the words “Retrieved from” or “Accessed from” before a DOI or URL."
- 判定：正確
- 說明：一般情況不需要。只有需要擷取日期（內容會變動的頁面）時才保留 "Retrieved [date], from"。
- 建議改法：不需修改。可選擇補「需要擷取日期時例外」。
- 查核日期：2026-10-23

#### APA-09　頁碼範圍用 en dash，站上卻稱為「半形連字號」
- 位置：`docs/style.md:265`、`docs/style.md:464`、`docs/checklists.md:155`
- 站上寫法：「頁碼用半形連字號 `–`（en dash），不用全形 `—`」
- 原始出處：APA Style，〈Page numbers〉，<https://apastyle.apa.org/style-grammar-guidelines/citations/quotations/page-numbers>；〈Journal article references〉範例
  - 原文："For multiple pages, use the abbreviation “pp.” and separate the page range with an en dash (e.g., pp. 34–36)."；範例："_Psychology of Popular Media Culture_, _8_(3), 207–217."
- 判定：不精確
- 說明：用 en dash（–）是對的。但「半形連字號」通常指 hyphen（-，U+002D），不是 en dash（–，U+2013）。中文讀者照字面會打成 `207-217`。對照的「全形 `—`」其實是 em dash（U+2014）。
- 建議改法：「頁碼範圍用 en dash（–，U+2013，Word 可按 Ctrl＋數字鍵盤減號），不用連字號（-）也不用 em dash（—）」。
- 查核日期：2026-10-23

#### APA-10　斜體範圍：站上只寫「書名、期刊名用斜體」
- 位置：`docs/style.md:263`
- 站上寫法：「書名、期刊名用斜體」
- 原始出處：APA Style，〈Italics〉，<https://apastyle.apa.org/style-grammar-guidelines/italics-quotations/italics>
  - 原文："Titles of periodicals and periodical volume numbers (but not the comma between them)"（範例 "_American Journal of Nursing_, _119_(9), 47–53."）；"Titles of books, reports, webpages, and other stand-alone works"
- 判定：不精確
- 說明：APA 7 期刊卷號也要斜體，期號與括號則不斜體。站上漏了卷號。另外，中文文獻是否斜體各校慣例不同（有的系所用粗體），APA 官方沒有規範中文。
- 建議改法：「書名、期刊名與卷號用斜體（期號與括號不斜體）；中文文獻用斜體或粗體依系所規定」。
- 查核日期：2026-10-23

#### APA-11　Davis（1989）英文參考文獻範例
- 位置：`docs/style.md:256-257`
- 站上寫法：「Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340.」
- 原始出處：Crossref，DOI 10.2307/249008；APA〈DOIs and URLs〉頁
  - Crossref：Davis, Fred D.，"Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology"，*MIS Quarterly*，vol. 13，issue 3，pages 319-340，1989。
  - APA 原文："Include a DOI for all works that have a DOI, regardless of whether you used the online version or the print version."
- 判定：不精確
- 說明：作者、年份、篇名、卷期、頁碼都正確，但這篇有 DOI，APA 7 範例應附上。另外放在 code block 裡無法顯示 *MIS Quarterly*, *13* 的斜體（見 APA-10）。
- 建議改法：「Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, *13*(3), 319–340. https://doi.org/10.2307/249008」，並改用不會吃掉斜體的呈現方式，或加註「刊名與卷號應為斜體」。

#### APA-12　中文參考文獻範例「彭明輝（2017）。論文寫作完全求生手冊。聯經出版。」
- 位置：`docs/style.md:249`（相關：`docs/style.md:229-230` 的內文引用範例；`docs/sources.md:37` 也寫 2017）
- 站上寫法：「彭明輝（2017）。論文寫作完全求生手冊。聯經出版。」
- 原始出處：三民網路書店商品頁 <https://www.sanmin.com.tw/Product/index/011322659>；華藝 iRead eBooks 書目 <https://www.airitibooks.com/Detail/Detail?PublicationID=P20230508029&DetailSourceType=2>。聯經官方商店（store.linkingbooks.com.tw）回 403，未取得。
  - 三民頁面文字：「論文寫作完全求生手冊：「精準表達，以理服人」的技藝」；「ISBN13 ： 9789570866926 出版社 ： 聯經 作者 ： 彭明輝 出版日 ： 2023/01/05 裝訂／頁數 ： 平裝／272頁」
  - 華藝頁面文字：「出版日期 ： 2023/01/01」；「ISBN ： 9789570866926」
  - 對照：2017 年出版的是另一本書。關鍵評論網刊出的書摘頁註明「本文摘錄自《研究生完全求生手冊：方法、秘訣、潛規則》，聯經出版」，配圖網址年份為 2017（<https://www.thenewslens.com/article/80644>）。
- 判定：錯誤
- 說明：（`docs/sources.md:37` 的同一錯誤另列於 REF-53。）《論文寫作完全求生手冊》是 2023 年出版，不是 2017 年。2017 年那本是《研究生完全求生手冊》。範例年份錯，也漏了副書名，等於示範了一筆錯誤書目。我用兩家書商的書目各查一次，結果一致。
- 建議改法：「彭明輝（2023）。*論文寫作完全求生手冊：「精準表達，以理服人」的技藝*。聯經。」內文範例同步改成（彭明輝，2023）。若想保留 2017，就改成「彭明輝（2017）。*研究生完全求生手冊：方法、秘訣、潛規則*。聯經。」`docs/sources.md:37` 一併修正（見 REF-53）。

#### APA-13　APA 7「中文化」慣例：等人、與、全形逗號、頓號、中文在前按筆畫排序
- 位置：`docs/style.md:229-230, 233, 240-242, 249-250, 262, 266`、`docs/checklists.md:155`
- 站上寫法：「英文作者之間用中文「**與**」，不用 "&" 或 "and"」；「括號引用時，英文文獻用半形逗號和分號，中文文獻用全形逗號」；「作者之間用頓號「、」，最後兩位用「與」」；「同一括號中多篇：中文在前按筆畫排序，英文在後按字母排序」
- 原始出處：APA Style〈Author–date citation system〉（英文規則對照）；台灣層級的官方出處未取得
  - APA 原文："In parenthetical citations, use an ampersand (&) between names for a work with two authors or before the last author when all names must be included to avoid ambiguity."；"In narrative citations, always spell out the word “and.”"
- 判定：查不到
- 說明：APA 手冊沒有規範中文文獻，這些是台灣學界常見的在地化慣例，各期刊與系所差異不小。例如英文文獻放在括號引用時，不少台灣期刊仍保留 "&"。我試過《中華心理學刊》投稿須知的搜尋結果（只寫到可依 APA 7 或該刊格式）、國家教育研究院期刊格式 PDF（本環境連線被拒）、臺師大 APA7 中文說明 PDF（下載到的是 HTML），都沒取得可逐字引用的官方規定。站上把它們列在「APA 7 中文化」標題下、口氣像統一規則，容易讓讀者以為是 APA 官方規定。
- 建議改法：在 3.1／3.2 開頭加註「以下為台灣常見慣例，APA 手冊本身未規範中文；與系所或投稿期刊規定不同時，以後者為準」。「英文作者之間不用 &」改成「中文行文的敘述引用用『與』；英文文獻的括號引用是否保留 &，依系所規定」。

#### APA-14　統計符號寫法：「β = .37, p < .001」
- 位置：`docs/style.md:92`、`docs/style.md:104`
- 站上寫法：「「X 正向預測 Y（β = .37, p < .001）」」
- 原始出處：APA，*Numbers and Statistics Guide*（7th ed. 官方 PDF），<https://apastyle.apa.org/instructional-aids/numbers-statistics-guide.pdf>；〈Italics〉頁
  - 原文："Do not use a zero before a decimal when the statistic cannot be greater than 1 (proportion, correlation, level of statistical significance)."；"However, report p values less than .001 as “ p < .001.”"；"Put a space before and after a mathematical operator (e.g., minus, plus, greater than, less than)."；"Use italics for letters used as statistical symbols or algebraic variables (e.g., contained 587 t-test p values; R2 = .12)"；"However, use standard (nonitalic) type for Greek letters."
- 判定：不精確
- 說明：p 值省略前導 0、運算子前後空格、β 不斜體都正確。但 *p* 是英文字母統計符號，APA 要求斜體，站上兩處都是正體。
- 建議改法：改成「β = .37, *p* < .001」（Markdown 寫 `*p*`）。
- 查核日期：2026-10-23

#### APA-15　圖說放在圖下、表題放在表上
- 位置：`docs/writing.md:116`
- 站上寫法：「圖放在正文第一次提及之後，圖說置於圖下；表題置於表上。圖表位置與標示仍以系所範本為準。」
- 原始出處：APA Style，〈Figure setup〉，<https://apastyle.apa.org/style-grammar-guidelines/tables-figures/figures>；〈Table setup〉，<https://apastyle.apa.org/style-grammar-guidelines/tables-figures/tables>
  - 原文："The figure number (e.g., Figure 1) appears above the figure title and image in bold font."；"The figure title appears one double-spaced line below the figure number."；"note: Three types of notes (general, specific, and probability) can appear below the figure"；"The table number (e.g., Table 1) appears above the table title and body in bold font."；"The first is to embed figures in the text after each is first mentioned (or “called out”)"
- 判定：不精確
- 說明：表題放在表上、圖放在第一次提及之後都符合 APA 7。但 APA 7 的圖號與圖題也放在圖的上方，只有圖註（note）在下方。站上的「圖說置於圖下」是台灣許多系所範本的傳統做法，不是 APA 7。同一節第 107 行要讀者「採 APA 第七版」，兩處容易衝突。
- 建議改法：「表號與表題置於表上。若採 APA 7，圖號與圖題同樣置於圖上，圖註置於圖下；不少系所範本要求圖題置於圖下，以系所範本為準。」
- 查核日期：2026-10-23

#### APA-16　Zotero Word 外掛的插入引用與插入書目
- 位置：`docs/writing.md:107-109`
- 站上寫法：「全文引用完成後，在參考文獻章節使用 Zotero 的插入書目功能，統一產生全文書目。」
- 原始出處：Zotero Documentation，〈Using the Zotero Word Processor Plugins〉，<https://www.zotero.org/support/word_processor_plugin_usage>
  - 原文："Add/Edit Bibliography Insert a bibliography at the cursor location or edit an existing bibliography. Document Preferences Open the Document Preferences window, e.g. to change the citation style."
- 判定：正確
- 說明：功能描述正確。站上的「插入書目」對應 Add/Edit Bibliography，引用樣式則在 Document Preferences 裡切換。
- 建議改法：不需修改。可選擇標出按鈕英文名稱（Add/Edit Citation、Add/Edit Bibliography）。
- 查核日期：2026-10-23

#### APA-17　Swales（1990）CARS model：三個 move 與各步驟，及「依序完成三個 move 才算完整」
- 位置：`docs/writing.md:172-190`（重點在 `:172`、`:174-178`、`:182`、`:186-190`）
- 站上寫法：「Swales, J. M. (1990). *Genre Analysis: English in Academic and Research Settings*. Cambridge University Press. 提出的 CARS（Create A Research Space）model 主張，學術論文導論依序完成三個 move 才算完整。」
- 原始出處：書本身未取得全文。書目以 Crossref 收錄的書評核對（Jernudd 1993，DOI 10.1017/s0272263100011773，篇名欄為 "Genre Analysis: English in Academic and Research Settings. John M. Swales. Cambridge: Cambridge University Press, 1990. Pp. 288."）。內容以站上引用的 USC Libraries〈The C.A.R.S. Model〉核對：<https://libguides.usc.edu/writingguide/CARS>（二手來源）。
  - USC 原文："His model attempts to explain and describe the organizational pattern of writing the introduction to scholarly research studies."；"Move 1: Establishing a Territory [the situation]"；"Move 2: Establishing a Niche [the problem]"；"Step 1a -- Counter-claiming, or ... Step 1b -- Indicating a gap, or ... Step 1c -- Question-raising, or ... Step 1d -- Continuing a tradition"；"Move 3: Occupying the Niche [the solution]"；"Step 2 -- Announcing principle findings"；"Step 3 -- Indicating article structure"
- 判定：不精確
- 說明：書目（作者、年份、書名、出版社）正確，三個 move 的名稱與 4.1 表格的步驟也和 USC 整理一致。但 USC 把這個模型描述成「解釋並描述」導論的常見組織模式，沒有說成缺一個 move 就不完整的規範性標準。「依序完成三個 move 才算完整」是站方加強語氣後的寫法。原書全文未取得，無法確認 Swales 有沒有這樣主張。
- 建議改法：「Swales 依期刊論文導論歸納出 CARS model，描述導論常見的三個 move；它是描述性的分析框架，可當寫作檢核參考，不是每篇導論都必須依序完整具備的規定。」
- 查核日期：2026-10-23（USC 頁面）

#### APA-18　writing.md 引用的方法論網址還能不能開
- 位置：`docs/writing.md:182`（Wikipedia CARS model、USC）、`docs/writing.md:219`（Enago、CASRAI）、`docs/writing.md:232`（APA JARS 兩個網址）
- 站上寫法：「APA,〈Journal Article Reporting Standards〉<https://www.apa.org/pubs/journals/resources/apa-style-jars.html> 與 APA Style,〈Quantitative research design (JARS–Quant)〉<https://apastyle.apa.org/jars/quantitative>」等
- 原始出處：實際連線
  - apa.org JARS 頁回 HTTP 200。apastyle.apa.org/jars/quantitative 頁面標題 "Quantitative research design (JARS–Quant)"，內含 "General quantitative reporting standards"、"Experimental and nonexperimental designs" 等段落。
  - CASRAI 頁面標題 "Method vs. Methodology: The Key Difference — CASRAI"。Enago、en.wikipedia CARS_model、USC 都回 200。
- 判定：正確
- 說明：所有網址都能開，標題與站上描述相符。JARS 條目只取分類架構，站上已自己說明「實際條目請以原文件為準」。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### APA-19　Shmueli（2010）*To Explain or to Predict?* 的書目
- 位置：`docs/style.md:62`
- 站上寫法：「Shmueli（2010）的 *To Explain or to Predict?* 說明因果解釋與經驗預測是不同的建模目標」，連結 `projecteuclid.org/.../10.1214/10-STS330.pdf`
- 原始出處：Crossref，DOI 10.1214/10-STS330
  - Crossref：Shmueli, Galit，"To Explain or to Predict?"，*Statistical Science*，vol. 25，issue 3，pages 289-310，2010。
- 判定：正確
- 說明：作者、年份、篇名、DOI 都正確。站上的 Project Euclid PDF 連結用 curl 抓到的是 HTML（可能是防機器人頁），DOI 本身可以解析。
- 建議改法：不需修改。可選擇補完整書目：*Statistical Science*, *25*(3), 289–310. https://doi.org/10.1214/10-STS330

#### APA-20　Hernán 與 Robins《Causal Inference: What If》免費公開
- 位置：`docs/style.md:61`
- 站上寫法：「Hernán 與 Robins 免費公開的教科書 *Causal Inference: What If* 區分觀察到的組間關聯與介入下的反事實因果對比」
- 原始出處：站上連結的 PDF（<https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf>，轉址到 squarespace 靜態檔，HTTP 200）
  - 原文（封面與版權頁）："Causal Inference: What If / Miguel A. Hernán, James M. Robins / January 2, 2025"；"Suggested citation: Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC."；"This book is available online at https://miguelhernan.org/whatifbook"；目錄有 "1.5 Causation versus association"
- 判定：正確
- 說明：可以免費下載，內容主題與站上描述相符。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### APA-21　臺大寫作教學中心蔡柏盈〈學術寫作的構句原則與技巧〉是以簡御繁、話題—陳述、中間肥大的出處
- 位置：`docs/style.md:451`（另見 `:396`、`:399`、`:411`）
- 站上寫法：「臺大寫作教學中心（AWEC）蔡柏盈〈學術寫作的構句原則與技巧〉——以簡御繁、話題—陳述、中間肥大的原始出處。」
- 原始出處：台大寫作教學中心，〈專題1：學術寫作的構句原則與技巧〉，站上所附網址（頁面標題「專題1：學術寫作的構句原則與技巧 – 台大寫作教學中心」）
  - 原文：「學術寫作的構句原則與技巧 文／蔡柏盈 (臺大寫作教學中心博士後研究員)」；「學術寫作的構句只有一個要訣：以簡御繁。」；「就是善用「話題—陳述」句型。」；「四、避免中間肥大」；「老一輩語言學家呂叔湘就說：這叫做「大肚子病」」
- 判定：正確
- 說明：作者、篇名、三個概念都能在原文找到。「大肚子病」一詞原文歸給呂叔湘。
- 建議改法：不需修改。可選擇在 7.2 註明「大肚子病」是呂叔湘的用語。
- 查核日期：2026-10-23

#### APA-22　余光中〈怎樣改進英式中文？〉的網頁典藏連結
- 位置：`docs/style.md:452`
- 站上寫法：「余光中〈怎樣改進英式中文？〉——弱動詞、「存在」濫用、抽象名詞化主語、冗詞的病句範例原文（原轉載頁已失效，連結是網頁典藏站 2021 年的存檔）。」
- 原始出處：未取得
- 判定：查不到
- 說明：web.archive.org 在本環境連線一律被重置，無法打開存檔。搜尋也沒找到有逐字全文的其他可靠轉載（香港教育局 PDF 回 404）。這篇文章本身存在是學界常識，但病句範例是否出自該文，我無法逐字核對。
- 建議改法：請能連上典藏站的人手動確認存檔可以開、內容確實包含所列的病句類型；可以的話補上原始出版資訊（收錄的書名與年份）。

#### APA-23　「後來成為社會學經典的論文，第一次投稿被退稿」的故事
- 位置：`docs/writing.md:140-143`
- 站上寫法：「一篇後來成為社會學經典的論文，第一次投稿時被直接退稿，因為作者把它包裝成對某個既有理論的再探討，而評審認定他誤解了那個理論。他把該理論的討論全數移除、徹底聚焦在自己真正的貢獻上之後，論文被頂尖期刊接受。」
- 原始出處：Stanford Report（2023-07），〈The strength of weak ties〉訪談 Mark Granovetter，<https://news.stanford.edu/stories/2023/07/strength-weak-ties>（經 r.jina.ai 讀取）；書目用 Crossref 核對 DOI 10.1086/225469
  - 原文："when he first submitted his now classic study to the _American Sociological Review_ in 1969, it had a different title: “Alienation Reconsidered: The Strength of Weak Ties,” which prompted the editor to send it to alienation theorists for review who swiftly rejected it, arguing that Granovetter didn’t understand the concept. Granovetter removed all references to alienation, and in 1972 resubmitted the paper to the _American Journal of Sociology_, and it was then accepted and published in May of 1973."
  - Crossref：Granovetter, Mark S.，"The Strength of Weak Ties"，*American Journal of Sociology*，vol. 78，issue 6，pages 1360-1380，1973-05。
- 判定：正確
- 說明：故事細節與當事人的說法一致（站上沒點名，應是 Granovetter 1973）。
- 建議改法：不需修改。建議補出處：「Granovetter（1973）〈The Strength of Weak Ties〉，最初以 "Alienation Reconsidered" 為題投 ASR 被退」，讓讀者可查。

#### APA-24　小麥價格與工資的經典圖表
- 位置：`docs/writing.md:306-309`
- 站上寫法：「一張比較兩百多年來小麥價格與工資變化的經典圖表，因為縱軸變數選得不好，看不出作者想傳遞的訊息。把縱軸改成「購買固定份量小麥所需的工時」之後，「實質工資大幅提升」這個結論就一目了然。」
- 原始出處：R 套件 HistData 的 `Wheat` 資料說明（Friendly 整理），<https://search.r-project.org/CRAN/refmans/HistData/html/Wheat.html>（二手、學術整理）
  - 原文："Playfair (1821) used a graph, showing parallel time-series of the price of wheat and the typical weekly wage for a "good mechanic" from 1565 to 1821 to argue that working men had never been as well-off in terms of purchasing power as they had become toward the end of this period. His graph is a classic in the history of data visualization, but commits the sin of showing two non-commensurable Y variables on different axes. Scatterplots of wages vs. price or plots of ratios (e.g., wages/price) are in some ways better, but both of these ideas were unknown in 1821."
- 判定：正確
- 說明：應是 William Playfair（1821）的圖，涵蓋 1565–1821 年，與「兩百多年」相符。「雙縱軸不可比、改畫比值更清楚」的說法有學術整理支持。Playfair 原書未取得。
- 建議改法：不需修改。建議補出處：「Playfair（1821）的小麥價格與工資圖；比值重繪見 Friendly & Denis（2005）」。

#### APA-25　「研究顯示，很多審查委員讀完摘要與導論就已有初步評價」
- 位置：`docs/writing.md:198-200`
- 站上寫法：「研究顯示，很多審查委員在讀完摘要與導論之後就已經對論文有初步評價，而這個第一印象跟讀完全文後的評價常常相去不遠。」
- 原始出處：未找到
- 判定：查不到
- 說明：站上寫「研究顯示」卻沒附出處。搜尋只找到期刊給審稿人的指引與廠商部落格，指引只建議先快速通讀形成初步印象；沒有找到比較「初步印象」與「最終評價」一致性的實證研究。
- 建議改法：補上具體研究出處；找不到的話，改成「不少審查委員會先讀摘要與導論形成初步印象」，並刪掉「研究顯示」。

#### APA-26　共同作者的「國際上較務實的三項要件」
- 位置：`docs/writing.md:445-451`
- 站上寫法：「若是共同掛名，國際上較務實的三項要件是：1. 對論文有**重大貢獻**…… 2. **仔細讀過完稿全文**並同意其出版 3. 對自己的貢獻**負責**……」
- 原始出處：ICMJE，〈Defining the Role of Authors and Contributors〉，<https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html>
  - 原文："The ICMJE recommends that authorship be based on the following 4 criteria: Substantial contributions to the conception or design of the work; or the acquisition, analysis, or interpretation of data for the work; AND Drafting the work or reviewing it critically for important intellectual content; AND Final approval of the version to be published; AND Agreement to be accountable for all aspects of the work in ensuring that questions related to the accuracy or integrity of any part of the work are appropriately investigated and resolved."；"Those who do not meet all four criteria should be acknowledged"
- 判定：不精確
- 說明：目前最常被引用的國際標準 ICMJE 是四項，四項都要符合。站上把「撰寫與重大改寫」塞進第 1 項的「或」選項裡，變成只要有構想設計就可能達標；ICMJE 則把「撰寫或批判性修改」列為另一項必要條件。站上的三項接近 ICMJE 舊版的寫法。
- 建議改法：依 ICMJE 改成四項（重大貢獻；撰寫或批判性修改；同意最終版本；同意對整體工作負責），並註明「四項都須符合；不符合者列於致謝」。附 ICMJE 網址。
- 查核日期：2026-10-23

#### APA-27　口試考題出自「十二個被反覆提出的問題」，前十題對應十個研究階段
- 位置：`docs/defense.md:85`（另見 `:83`、`:262`、`:321`、`:334`、`docs/checklists.md:188`）
- 站上寫法：「國外學者歸納訪談結果，發現博士論文口試的考題高度可預期，都出自十二個被反覆提出的問題。前十個剛好對應一個研究者依序經歷的十個階段。」
- 原始出處：原始研究未取得全文。可追到的轉述是彭明輝《研究生完全求生手冊》書摘（關鍵評論網，<https://www.thenewslens.com/article/80644>，經 r.jina.ai 讀取）；最接近的原始研究推測是 Trafford, V., & Leshem, S. (2002). Starting at the end to undertake doctoral research: Predictable questions as stepping stones. *Higher Education Review, 34*(1), 31–49（書目取自 ERIC 全文 EJ1329236 的參考文獻）。
  - 書摘原文：「兩位英國的學者歸納訪談結果，發現博士論文口試的考題可以高度預期，都是出自十二個被反覆提出的問題」；「這十二個問題中只有前面十個跟論文有關，剛好對應著一個博士生在進行研究時，會依序經歷的十個階段」
- 判定：查不到
- 說明：站上的寫法與彭明輝書中的轉述一致，但書摘沒有點名那兩位學者。Trafford 與 Leshem 的原文我沒拿到（Higher Education Review 沒有開放全文），無法確認「十二題」「十個階段」是不是原研究的分法。另外 Leshem 任職於以色列，書中「兩位英國的學者」本身也可能不精確。
- 建議改法：補「整理自彭明輝（2017）《研究生完全求生手冊》轉述的國外研究（可能出自 Trafford & Leshem, 2002）」，讓讀者知道是二手轉述。

#### APA-28　Hevner 的「七大規範」
- 位置：`docs/checklists.md:78`
- 站上寫法：「Hevner 七大規範，論文裡逐條找得到對應段落嗎？」
- 原始出處：Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105（Crossref 頁碼欄為 75-106），DOI 10.2307/25148625。全文取自公開 PDF <https://www.in.th-nuernberg.de/professors/Holl/Personal/Hevner_DesignScience_ISRes.pdf>
  - 原文："Table 1 summarizes the seven guidelines."；"Following Klein and Myers (1999), we advise against mandatory or rote use of the guidelines."；"However, we contend that each of these guidelines should be addressed in some manner for design-science research to be complete."
- 判定：正確
- 說明：七項 guidelines 正確，「逐條找得到對應」也符合原文「each ... should be addressed in some manner」。這是四位作者的論文，正式引用要寫 Hevner 等人（2004）。原文同時提醒不要機械式套用。
- 建議改法：不需修改。可選擇寫成「Hevner 等人（2004）的七項設計科學研究準則（guidelines）」，並補一句「原作者提醒不宜機械式逐條套用，但每條都應以某種方式回應」。

#### APA-29　「教育部層級」規定就是《學位授予法》與〈作業要點〉
- 位置：`docs/writing.md:4-5`
- 站上寫法：「教育部層級的規定主要是《學位授予法》與〈大專校院學位論文送存國家圖書館典藏作業要點〉，處理送存、授權、個資隱蔽與延後公開」
- 原始出處：全國法規資料庫〈學位授予法〉第 16 條，<https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=H0030010&flno=16>；教育部主管法規共用系統〈大專校院學位論文送存國家圖書館典藏作業要點〉，<https://edu.law.moe.gov.tw/LawContent.aspx?id=GL001869>
  - 學位授予法第 16 條："取得博士、碩士學位者，應將其取得學位之論文、書面報告、技術報告或專業實務報告，經由學校以文件、錄影帶、錄音帶、光碟或其他方式，連同電子檔送國家圖書館及所屬學校圖書館保存之。"；"但涉及機密、專利事項或依法不得提供，並經學校認定者，得不予提供或於一定期間內不為提供。"（法規類別：「行政 ＞ 教育部 ＞ 高等教育目」）
  - 作業要點："發文字號： 國圖事字第1150100010A號 令"；"一、國家圖書館（以下簡稱本館）為執行學位授予法第十六條完整保存學位論文，特訂定本要點。"；"九、本要點經本館館務會議通過後施行，修正時亦同。"
- 判定：不精確
- 說明：兩部規定的內容範圍（送存、授權書、個資隱蔽、延後公開）描述正確。但《學位授予法》是法律，教育部是主管機關；〈作業要點〉則是國家圖書館依該法訂定、經館務會議通過的行政規則，發文單位是國家圖書館，不是教育部。
- 建議改法：「國家層級的規定主要是《學位授予法》（教育部主管）第 16 條，以及國家圖書館據此訂定的〈大專校院學位論文送存國家圖書館典藏作業要點〉……」
- 查核日期：2026-10-23

#### APA-30　2026 年 1 月修正的〈作業要點〉內容：學校送存、授權書、個資隱蔽、延後公開
- 位置：`docs/post-defense.md:124`（主要查核來源連結見 `:185-188`）
- 站上寫法：「依 2026 年 1 月修正的「大專校院學位論文送存國家圖書館典藏作業要點」，學位論文由學校送存國家圖書館，電子全文送存時應檢附授權書；論文中的 Email、電話、住址、身分證字號等個人資訊應抽出或隱蔽。延後公開限於涉及機密、專利事項或依法不得提供等情形，且須經學校權責單位認定、備妥簽章與證明，再由學校提出。」
- 原始出處：教育部主管法規共用系統 GL001869（同上）；國家圖書館表單下載頁 <https://www.ncl.edu.tw/form-downloads/0Q099526045144197574>
  - 原文："修正日期： 民國 115 年 01 月 14 日"；"（六）學位論文內之個人資訊，如電子郵件、電話、住址、身分證字號等，應抽出或隱蔽。"；"（一）學位論文涉及機密、專利事項或依法不得提供者，須由學校權責單位認定後，經由學校向本館提出申請。"；"（二）填寫學校學位論文延後公開申請書（附件三），經論文作者、指導教授親筆簽名，須於學位考試時由考試委員審核確認，以及學校權責單位核章，並檢附證明文件，經由學校向本館提出申請。"；"八、各校送存學位論文電子全文檔時，應檢附碩博士論文授權書（附件五）予本館。"
  - 國圖頁："發布日期 | 2026-01-14 | 發布單位 | 館藏組 | 115年1月14日國圖事字第1150100010A 號令"
- 判定：正確
- 說明：修正日期與各項內容都符合原文，兩個連結都能開、標題正確。小細節：要點列舉的延後公開事由就是這三種，站上的「等情形」可以拿掉。另外原文要求申請書「須於學位考試時由考試委員審核確認」，這個時間點對讀者很實用，站上沒提。
- 建議改法：不需修改（可選擇刪「等」，並補「延後公開申請書須於學位考試時由考試委員審核確認」）。
- 查核日期：2026-10-23

#### APA-31　著作權只保護表達，不保護觀念、方法、程序與事實
- 位置：`docs/post-defense.md:106`、`docs/post-defense.md:198`
- 站上寫法：「著作權保護具體表達，不保護觀念、方法、程序與事實本身。」
- 原始出處：全國法規資料庫〈著作權法〉第 10-1 條，<https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0070017&flno=10-1>；同法第 9 條
  - 第 10-1 條原文："依本法取得之著作權，其保護僅及於該著作之表達，而不及於其所表達之思想、程序、製程、系統、操作方法、概念、原理、發現。"
  - 第 9 條第 1 項第 4 款原文："單純為傳達事實之新聞報導所作成之語文著作。"
- 判定：正確
- 說明：觀念、方法、程序都有第 10-1 條明文支持。「事實」沒有寫在第 10-1 條裡，但第 9 條把單純傳達事實的新聞報導排除在保護之外，事實本身不具原創性、不受保護也是通說，整體寫法沒有誤導。
- 建議改法：不需修改。可選擇補「（著作權法第 10-1 條）」，方便讀者查證。

---

### 小計

總共查了 31 條，各判定的條數如下：
- 正確：15 條（APA-02、04、06、07、08、16、18、19、20、21、23、24、28、30、31）
- 不精確：10 條（APA-03、05、09、10、11、14、15、17、26、29）
- 錯誤：2 條（APA-01、12）
- 查不到：4 條（APA-13、22、25、27）

合計 15＋10＋2＋4＝31 條。

錯誤：APA-01、APA-12
不精確：APA-03、APA-05、APA-09、APA-10、APA-11、APA-14、APA-15、APA-17、APA-26、APA-29

附註（不在查核範圍，順手記下）：`docs/checklists.md:184` 寫「投影片十張左右，每張約兩分鐘」，`docs/defense.md:175-177` 則說頁數依系所而異、「每頁約一至兩分鐘作為排練起點」，兩頁說法不一致。

---

## 六、REF：引用文獻書目與理論歸屬

查核日期：2026-10-23
範圍：全站 `docs/*.md` 的書目（DOI 與「作者 (年). 篇名. 刊名, 卷(期), 頁碼」型式），以及 about／sources／theories／theory-building／is-research／finding-reading／literature／research-basics／getting-started／problem-design 這些頁面裡被歸給特定作者的觀點。

### 方法

- 抽取：先用 `grep -P '10\.\d{4,9}/…'` 抽 DOI（全站共 25 處，去重後 13 個 DOI），再用 `\((19|20)\d{2}\)\.\s` 抽 APA 型書目；about.md 1.4 節的文獻表逐列抽取，theories.md 第七節索引表只寫「作者 (年)＋刊名卷期」的也一併收進來。
- 批次腳本：以 Python 逐筆查 Crossref（腳本與結果檔未納入 repo）。站上有寫 DOI 的，打 `api.crossref.org/works/<DOI>`；沒寫 DOI 的，用 `query.bibliographic` 找出 DOI 再比對。比對欄位有作者、年份、篇名、刊名、卷、期、頁碼，並對 `https://doi.org/<DOI>` 送 HEAD、不跟轉址，確認回傳的是 3xx。
- 補充來源：OpenAlex（頁碼、摘要）、AIS eLibrary 的 bepress citation meta、IDEAS/RePEc、Open Library（書籍）、出版社或書店頁（彭明輝兩本書）。
- 原文：拿得到的全文有 Keshav (2007)、Gregor (2006)、Hevner et al. (2004)、Webster & Watson (2002)、Whetten (1989，ReadKong 轉錄本)、彭明輝部落格兩頁。摘要層級（出版社摘要，經 OpenAlex／IDEAS 取得）的有 Davis (1989)、Davis, Bagozzi & Warshaw (1989)、Venkatesh et al. (2003, 2012)、Orlikowski & Iacono (2001)、Berthon et al. (2002)、Benbasat & Zmud (2003)、Bacharach (1989)、Lee & Baskerville (2003)、Straub et al. (2004)、Palvia et al. (2004)、Bhattacherjee (2001)、DeLone & McLean (1992, 2003)、Ajzen (1991)、Barney (1991)、Petty, Cacioppo & Schumann (1983)。
- 拿不到全文的：aisel.aisnet.org 的 PDF（Cloudflare 擋）、pubsonline.informs.org、journals.aom.org、journals.sagepub.com、dl.acm.org、misq.umn.edu 用程式抓都回 403（機器人防護，不代表連結失效）。McGrath (1981)、Lee & Baskerville (2003)、Bacharach (1989) 找不到開放全文。
- 下面寫「原文」的，都是我實際在來源上讀到、再貼過來的英文；標「摘要」的就是摘要層級，不是全文。

---

### 一、書目彙整表

判定欄只寫結論；判「不精確」或「錯誤」的，在第二節詳列。Crossref 欄的「OK」表示作者、年、篇名、刊名、卷、期、頁碼都和 Crossref 一致，DOI 也能解析（302 轉到出版社）。

| 代號 | 位置 | 書目（站上寫法摘要） | Crossref／其他查核結果 | 判定 |
|---|---|---|---|---|
| REF-01 | about.md:44；theories.md:235 | Ajzen (1991). TPB. *OBHDP*, 50(2), 179–211. doi:10.1016/0749-5978(91)90020-T | OK；DOI 302 → linkinghub.elsevier.com；編出來的 HTML href 含括號，完整 | 正確 |
| REF-02 | about.md:45；theory-building.md:72 | Bacharach (1989). *AMR*, 14(4), 496–515. 連結 journals.aom.org/doi/10.5465/AMR.1989.4308374 | 10.5465/AMR.1989.4308374 現在是 10.2307/258555（JSTOR）的 **HS_ALIAS**（doi.org 回 301 → 10.2307/258555 → JSTOR）；Crossref 只有起頁 496，卷期年一致；止頁 515 未能從原文確認 | 正確（附註：主 DOI 已改為 10.2307/258555） |
| REF-03 | about.md:46；theories.md:277 | Barney (1991). *JOM*, 17(1), 99–120. doi:10.1177/014920639101700108 | OK | 正確 |
| REF-04 | about.md:47；is-research.md:27 | Benbasat & Zmud (2003). The identity crisis within the IS discipline. *MISQ*, 27(2), 183–194 | Crossref 10.2307/30036527：卷期頁一致；篇名少了副標「: Defining and Communicating the Discipline's Core Properties」；is-research.md:27 沒寫頁碼 | 不精確（見 REF-50） |
| REF-05 | about.md:48 | Berthon et al. (2002). Potential research space in MIS. *ISR*, 13(4), 416–427. doi:10.1287/isre.13.4.416.71 | OK；about.md 的篇名截掉副標（is-research.md:103 是完整篇名） | 不精確（見 REF-50） |
| REF-06 | is-research.md:103 | 同上，完整篇名 | OK | 正確 |
| REF-07 | about.md:49；theories.md:241 | Bhattacherjee (2001). Understanding information systems continuance. *MISQ*, 25(3), 351–370 | Crossref 10.2307/3250921：卷期頁一致；篇名少了「: An Expectation-Confirmation Model」 | 不精確（見 REF-50） |
| REF-08 | about.md:50 | Blau (1964). *Exchange and Power in Social Life*. Wiley. | Open Library：1964，J. Wiley | 正確 |
| REF-09 | about.md:51 | Breiman (1996). *Machine Learning*, 24(2), 123–140 | Crossref 10.1023/A:1018054314350 OK | 正確 |
| REF-10 | about.md:52；theories.md:132,273 | Coase (1937). *Economica*, 4(16), 386–405 | Crossref 10.1111/j.1468-0335.1937.tb00002.x OK | 正確 |
| REF-11 | about.md:53；theories.md:252 | Compeau & Higgins (1995). Computer self-efficacy. *MISQ*, 19(2), 189–211 | Crossref 10.2307/249688：卷期頁一致；篇名少了「: Development of a Measure and Initial Test」 | 不精確（見 REF-50） |
| REF-12 | about.md:54；theories.md:263 | Daft & Lengel (1986). *Management Science*, 32(5), 554–571. doi:10.1287/mnsc.32.5.554 | OK | 正確 |
| REF-13 | about.md:55；theories.md:236；style.md:256 | Davis (1989). *MISQ*, 13(3), 319–340 | Crossref 10.2307/249008 OK | 正確 |
| REF-14 | about.md:56；theories.md:288 | DeLone & McLean (1992). *ISR*, 3(1), 60–95. doi:10.1287/isre.3.1.60 | OK | 正確（書目本身；內容見 REF-63） |
| REF-15 | about.md:57；theories.md:289 | DeLone & McLean (2003). *Journal of MIS*, 19(4), 9–30 | Crossref 10.1080/07421222.2003.11045748：年卷期頁一致（Crossref 沒有作者欄，OpenAlex 有 DeLone、McLean）；刊名在 about.md 縮寫成「Journal of MIS」 | 正確（刊名縮寫見 REF-50） |
| REF-16 | about.md:58；theories.md:279 | DeSanctis & Poole (1994). Capturing the complexity in advanced technology use. *Org Science*, 5(2), 121–147 | Crossref OK；篇名少了「: Adaptive Structuration Theory」 | 不精確（見 REF-50） |
| REF-17 | about.md:59；theories.md:32,234 | Fishbein & Ajzen (1975). *Belief, Attitude, Intention, and Behavior*. Addison-Wesley. | Open Library：1975，Addison-Wesley（theories.md:234 書名漏了 Intention 後面的逗號，無礙） | 正確 |
| REF-18 | about.md:60 | Freund & Schapire (1997). *JCSS*, 55(1), 119–139 | Crossref 10.1006/jcss.1997.1504 OK | 正確 |
| REF-19 | about.md:61；theories.md:242 | Goodhue & Thompson (1995). *MISQ*, 19(2), 213–236 | Crossref 10.2307/249689 OK | 正確 |
| REF-20 | about.md:62；theories.md:291；theory-building.md:39 | Gregor (2006). *MISQ*, 30(3), 611–642 | Crossref 10.2307/25148742 OK；全文首頁「Vol. 30, No. 3 (Sep., 2006), pp. 611-642」 | 正確 |
| REF-21 | about.md:63；sources.md:80 | Hair et al. (2019). *European Business Review*, 31(1), 2–24 | Crossref 10.1108/EBR-11-2018-0203 OK | 正確 |
| REF-22 | about.md:64；sources.md:79；is-research.md:45；theories.md:290 | Hevner et al. (2004). *MISQ*, 28(1), 75–105 | Crossref 10.2307/25148625 的頁碼是 **75–106**；全文 PDF 正文與作者簡介止於 p.105，p.106 是空白頁 | 正確（75–105 是通行寫法，與內容相符） |
| REF-23 | about.md:65；theories.md:274 | Katz & Shapiro (1985). *AER*, 75(3), 424–440 | 無 Crossref DOI（JSTOR 時期 AER）；IDEAS/RePEc handle「RePEc:aea:aecrev:v:75:y:1985:i:3:p:424-40」，作者與篇名一致 | 正確 |
| REF-24 | about.md:66；theory-building.md:206 | Lee & Baskerville (2003). *ISR*, 14(3), 221–243. doi:10.1287/isre.14.3.221.16560 | OK | 正確（書目本身；內容見 REF-58） |
| REF-25 | about.md:67；sources.md:67 | Lincoln & Guba (1985). *Naturalistic Inquiry*. Sage. | Open Library：1985，Sage | 正確 |
| REF-26 | about.md:68 | March & Smith (1995). *DSS*, 15(4), 251–266 | Crossref 10.1016/0167-9236(94)00041-2 OK | 正確 |
| REF-27 | about.md:69；sources.md:82；finding-reading.md:194 | Keshav (2007). How to read a paper. *ACM SIGCOMM CCR*, 37(3), 83–84. dl.acm.org/doi/10.1145/1273445.1273458 | OK；全文頁尾「ACM SIGCOMM Computer Communication Review 83 … Volume 37, Number 3, July 2007」 | 正確 |
| REF-28 | about.md:70；is-research.md:67 | McGrath (1981). Dilemmatics: The study of research choices and dilemmas. *ABS*, 25(2), 179–210 | Crossref OK（Crossref 篇名只有「Dilemmatics」，副標沒登錄，屬元資料差異） | 正確 |
| REF-29 | about.md:71；theories.md:95 | Mehrabian & Russell (1974). MIT Press. | Open Library：1974，The MIT Press | 正確 |
| REF-30 | about.md:72；theories.md:239 | Moore & Benbasat (1991). *ISR*, 2(3), 192–222 | OK | 正確 |
| REF-31 | about.md:73 | Nunamaker, Chen, & Purdin (1990). *Journal of MIS*, 7(3), 89–106 | Crossref 10.1080/07421222.1990.11517898 OK（刊名縮寫見 REF-50） | 正確 |
| REF-32 | about.md:74；is-research.md:26 | Orlikowski & Iacono (2001). Desperately seeking the "IT" in IT research. *ISR*, 12(2), 121–134 | Crossref 10.1287/isre.12.2.121.9700：卷期頁一致；正式篇名是「Research Commentary: Desperately Seeking the "IT" in IT Research—A Call to Theorizing the IT Artifact」 | 不精確（見 REF-50） |
| REF-33 | about.md:75；is-research.md:133 | Palvia, P., et al. Research methodologies in MIS: An update. *CAIS*, 14(24). | Crossref 10.17705/1CAIS.01424：**2004**，作者 6 人（Palvia, Leary, Mao, Midha, Pinjani, Salam） | 不精確（見 REF-51） |
| REF-34 | about.md:76；theories.md:113 | Petty & Cacioppo (1986). *Communication and Persuasion*. Springer. | Crossref 10.1007/978-1-4612-4964-1：1986，Springer New York | 正確 |
| REF-35 | about.md:77；theories.md:159,276 | Pfeffer & Salancik (1978). Harper & Row. | Open Library：1978，Harper & Row | 正確 |
| REF-36 | about.md:78；sources.md:81 | Podsakoff et al. (2003). Common method biases in behavioral research. *JAP*, 88(5), 879–903 | Crossref OK；篇名少了「: A critical review of the literature and recommended remedies」 | 不精確（見 REF-50） |
| REF-37 | about.md:79 | Ryan & Deci (2000). Self-determination theory and the facilitation of intrinsic motivation. *AmPsy*, 55(1), 68–78 | Crossref OK；篇名少了「, social development, and well-being」 | 不精確（見 REF-50） |
| REF-38 | about.md:80；is-research.md:125 | Straub, Boudreau, & Gefen (2004). *CAIS*, 13(24), 380–427 | Crossref 10.17705/1CAIS.01324：年、卷一致，沒有頁碼；Crossref 作者漏了 Boudreau，AIS eLibrary 的 citation meta 有列 Boudreau；380–427 的頁碼因 PDF 被擋，沒能從原文確認 | 正確（頁碼未逐頁核對） |
| REF-39 | about.md:81；theories.md:237 | Venkatesh et al. (2003). *MISQ*, 27(3), 425–478 | Crossref 10.2307/30036540 OK | 正確 |
| REF-40 | about.md:82 | Venkatesh, Thong, & Xu (2012). Consumer acceptance and use of information technology. *MISQ*, 36(1), 157–178 | Crossref 10.2307/41410412：卷期頁一致；篇名少了「: Extending the Unified Theory of Acceptance and Use of Technology」 | 不精確（見 REF-50） |
| REF-41 | about.md:83；sources.md:78；literature.md:214；tools-knowledge.md:183 | Webster & Watson (2002). *MISQ*, 26(2), xiii–xxiii | Crossref 10.2307/4132319 OK；全文首頁「pp. xiii-xxiii」 | 正確 |
| REF-42 | about.md:84；theories.md:168,277 | Wernerfelt (1984). *SMJ*, 5(2), 171–180 | Crossref 10.1002/smj.4250050207 OK | 正確 |
| REF-43 | about.md:85；is-research.md:87 | Whetten (1989). *AMR*, 14(4), 490–495. journals.aom.org/doi/10.5465/amr.1989.4308371 | 10.5465 DOI 是 10.2307/258554 的 alias（301）；轉錄本頁碼與 490–495 相符 | 正確（附註同 REF-02） |
| REF-44 | about.md:86；theories.md:132,273 | Williamson (1985). Free Press；另寫 Williamson (1975) | Open Library：*Economic Institutions of Capitalism* 1985 Free Press；*Markets and Hierarchies* 1975 Free Press | 正確 |
| REF-45 | theories.md:240 | Oliver (1980). *JMR*, 17(4), 460–469 | Crossref 10.2307/3150499：卷期與起頁 460 一致（止頁沒登錄） | 正確 |
| REF-46 | theories.md:256 | Katz, Blumler & Gurevitch (1973–74). *POQ*, 37(4), 509–523 | Crossref 10.1086/268109：1973，37(4)，起頁 509 | 正確 |
| REF-47 | sources.md:78 | Watson & Webster (2020). "A roadmap for release 2.0", *Journal of Decision Systems* | Crossref 10.1080/12460125.2020.1798591：2020，29(3)，129–147 | 正確 |
| REF-48 | style.md:62 | Shmueli (2010). To Explain or to Predict? projecteuclid 連結內含 10.1214/10-STS330 | Crossref：Statistical Science 25(3) 289–310, 2010；DOI 302；PDF 連結回 200 | 正確 |
| REF-49 | theories.md:149,238,251,264,275,278,282；writing.md:182 | Homans (1958)；Rogers (1962 起)；Bandura (1986)；Short, Williams & Christie (1976)；Giddens (1984)；Nolan (1973, 1979)；Swales (1990, CUP) | Crossref：Homans 1958 *AJS* 63(6) 597–606；Nolan 1973 *CACM* 16(7) 399–405。Open Library：Rogers 1962 Free Press；Bandura 1986 Prentice-Hall；Short et al. 1976 Wiley；Giddens 1984。Swales 1990 Cambridge UP（Crossref 書評條目） | 正確 |
| REF-52 | sources.md:27 | 彭明輝《研究生完全求生手冊：方法、祕訣、潛規則》（聯經，2017） | 金石堂：出版日 2017/09/05，ISBN 9789570849929 | 正確 |
| REF-53 | sources.md:37 | 彭明輝《論文寫作完全求生手冊：「精準表達，以理服人」的技藝》（聯經，**2017**） | 聯經官方書店：出版日期 **2023-01-05**，EAN 9789570866926 | **錯誤**（見 REF-53 詳列） |
| REF-54 | sources.md:68 | 梁定澎、陳灯能、彭志宏，《資訊管理理論》（前程文化） | 大學課綱：前程文化，2021 年 9 月二版，ISBN 9789860679663（站上沒寫年份，無誤） | 正確 |
| REF-55 | finding-reading.md:268 | 彭明輝，〈如何選研究的主題〉，部落格 2022/11 | 頁面標題「如何選研究的主題」，2022年11月1日 | 正確 |

---

### 二、書目有誤或不精確的詳列

#### REF-50　about.md 文獻表有 9 筆篇名截掉副標題，另有刊名縮寫
- 位置：`docs/about.md:47`、`:48`、`:49`、`:53`、`:58`、`:74`、`:78`、`:79`、`:82`；`docs/is-research.md:26`、`:27`；`docs/sources.md:81`（Podsakoff）；刊名縮寫在 `docs/about.md:57`、`:73`（Journal of MIS）、`:75`、`:80`（Communications of the AIS）
- 站上寫法：例「Bhattacherjee, A. (2001). Understanding information systems continuance. *MIS Quarterly*, 25(3), 351–370.」；「Benbasat, I., & Zmud, R. W. (2003). The Identity Crisis Within the IS Discipline. *MIS Quarterly*, 27(2).」（is-research.md:27 沒寫頁碼）
- 原始出處：Crossref 元資料（api.crossref.org/works/…）
  - 原文（Crossref title 欄）："The Identity Crisis Within the IS Discipline: Defining and Communicating the Discipline's Core Properties"；"Understanding Information Systems Continuance: An Expectation-Confirmation Model"；"Computer Self-Efficacy: Development of a Measure and Initial Test"；"Capturing the Complexity in Advanced Technology Use: Adaptive Structuration Theory"；"Research Commentary: Desperately Seeking the "IT" in IT Research—A Call to Theorizing the IT Artifact"；"Common method biases in behavioral research: A critical review of the literature and recommended remedies."；"Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being."；"Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology"；"Potential Research Space in MIS: A Framework for Envisioning and Evaluating Research Replication, Extension, and Generation"
- 判定：不精確
- 說明：作者、年、卷、期、頁碼都對，只是篇名省略副標題、刊名用縮寫。這張表有寫「不要直接複製」的警語，但它看起來就是 APA 格式；讀者照抄的話，APA 7 要求的完整篇名和刊名都會缺。
- 建議改法：補上完整篇名（照上面 Crossref 的寫法，換成 APA 的句首大寫），刊名寫全名 *Journal of Management Information Systems*、*Communications of the Association for Information Systems*；is-research.md:27 補上「, 183–194」。另一個做法是把表頭改成「出處（簡寫）」，讓讀者知道這不是可以直接用的書目。

#### REF-51　Palvia et al. 這筆缺年份與作者
- 位置：`docs/about.md:75`、`docs/is-research.md:133`
- 站上寫法：「Palvia, P., et al. Research methodologies in MIS: An update. *Communications of the AIS*, 14(24).」
- 原始出處：Crossref 10.17705/1CAIS.01424；AIS eLibrary 頁 <https://aisel.aisnet.org/cais/vol14/iss1/24/>
  - 原文（AIS 頁 Recommended Citation）："Palvia, P., Leary, D., Mao, E., Midha, V., Pinjani, P., & Salam, A. (2004). Research Methodologies in MIS: An Update. Communications of the Association for Information Systems , 14 , pp-pp. https://doi.org/10.17705/1CAIS.01424"
- 判定：不精確
- 說明：沒有年份，APA 書目必備的元素就少了一個；而且 APA 7 在作者 20 人以內時要全部列出，不能用 et al.。
- 建議改法：「Palvia, P., Leary, D., Mao, E., Midha, V., Pinjani, P., & Salam, A. F. (2004). Research methodologies in MIS: An update. *Communications of the Association for Information Systems*, 14, Article 24. https://doi.org/10.17705/1CAIS.01424」

#### REF-53　《論文寫作完全求生手冊》的出版年寫成 2017，實為 2023
- 附註：`docs/style.md:249` 參考文獻範例的同一錯誤另見 APA-12。
- 位置：`docs/sources.md:37`
- 站上寫法：「### 2.2 彭明輝《論文寫作完全求生手冊：「精準表達，以理服人」的技藝》（聯經，2017）」
- 原始出處：聯經出版官方書店 <https://store.linkingbooks.com.tw/product/152138>；華藝 iRead eBooks <https://www.airitibooks.com/Detail/Detail?PublicationID=P20230508029&DetailSourceType=2>
  - 原文（聯經頁）：「出版日期：2023-01-05 作者：彭明輝 裝訂：平裝 EAN：9789570866926 系列：彭明輝作品集」；作者簡介列到「2017年出版《研究生完全求生手冊：方法、秘訣、潛規則》（聯經）」「2020年出版《欲望的美學…》」，2017 年只有前一本。
  - 原文（華藝頁）：「出版日期 ： 2023/01/01 … ISBN ： 9789570866926」
- 判定：錯誤
- 說明：出版社自己的頁面寫 2023-01-05。我第二次查核用的是另一個獨立來源（華藝），一樣是 2023。站上的章節導讀（第 3–4 章論文架構與寫作次序、第 9–10 章結果與討論、第 12 章口試與簡報）跟聯經頁的目次對得上，所以錯的只有年份。
- 建議改法：「彭明輝《論文寫作完全求生手冊：「精準表達，以理服人」的技藝》（聯經，2023）」。
- 查核日期：2026-10-23

---

### 三、被歸給特定作者的觀點

#### REF-56　Gregor (2006) 理論的五種類型
- 位置：`docs/theory-building.md:24-34`、`:233`；`docs/theories.md:291`
- 站上寫法：「I 分析型（Analysis）…不做因果宣稱｜II 解釋型（Explanation）…有機制，但不預測｜III 預測型（Prediction）…準確但不解釋｜IV 解釋暨預測型（EP）…TAM、UTAUT 這類含假說的模型｜V 設計與行動型（Design & Action）」
- 原始出處：Gregor, S. (2006). MISQ 30(3), 611–642（ANU 開放典藏全文 <https://openresearch-repository.anu.edu.au/bitstreams/77077d0f-f636-40a8-89fb-d2d2365ad7ad/download>）
  - 原文（摘要）："Five interrelated types of theory are distinguished: (1) theory for analyzing, (2) theory for explaining, (3) theory for predicting, (4) theory for explaining and predicting, and (5) theory for design and action."
  - 原文（Table 2）："The theory does not extend beyond analysis and description. No causal relationships among phenomena are specified and no predictions are made."；"The theory provides explanations but does not aim to predict with any precision. There are no testable propositions."；"The theory provides predictions and has testable propositions but does not have well-developed justificatory causal explanations."
  - 原文（Type IV 例子）："The Technology Acceptance Model (TAM) (Davis et al. 1989) and DeLone and McLean's dynamic model of information success (1992 2003) both aim to explain and predict."；Type III 的研究方法："Neural net techniques allow models to be constructed that give an accurate prediction of outcomes from input variables, although the reasons for the weightings applied to input values are not transparent."
- 判定：正確
- 說明：五型的名稱、各型的界定、TAM 屬第 IV 型、機器學習屬預測型，原文都支持。
- 建議改法：不需修改

#### REF-57　Bacharach (1989) 的構念／變項／命題／假說圖示，以及「可否證性、實用性」兩個判準
- 位置：`docs/theory-building.md:70`、`:76-96`、`:235`
- 站上寫法：「構念之間的連結是命題，變項之間的連結是假說，構念與變項之間的連結是操作化，而整個系統外圍還有一圈邊界假設…時間、空間與價值觀」「Bacharach 提出的兩個判準…可否證性（falsifiability）…實用性（utility）…解釋力…預測力」
- 原始出處：Bacharach (1989), AMR 14(4)。未取得全文（JSTOR、AOM 都要登入，也找不到開放全文），以下是出版社摘要（經 OpenAlex 取得）
  - 原文（摘要）："a matrix of criteria for evaluating the variables, constructs, and relationships that together compose a theory is developed … Finally, a discussion of the way theories fit together to give a somewhat broader picture of empirical reality reveals the lines of tension between the two main criteria for evaluating theory."
- 判定：查不到
- 說明：摘要證實有「兩個主要判準」，也有針對 variables、constructs、relationships 的評估矩陣，但沒寫出兩判準的名稱，邊界假設的三個面向也沒提。名稱我只在學習卡片網站（brainscape）看到，那是二手。試過 JSTOR、journals.aom.org（403）、Semantic Scholar（429）、OpenAlex（沒有 OA 版本）、WebSearch。整體方向和摘要一致，沒有看到矛盾。
- 建議改法：內容可以先保留；之後有機會從圖書館取得原文，就補一句原文引文並標頁碼。

#### REF-58　Lee & Baskerville (2003) 概化的四種形式（EE／ET／TE／TT），以及「只有一種需要統計抽樣」
- 位置：`docs/theory-building.md:195-204`、`:237`
- 站上寫法：「他們把概化拆成四種，其中只有一種需要統計抽樣」；表中「TT｜理論 → 其他理論｜把某領域的理論移植到新領域」「EE｜實證資料 → 其他實證描述｜從樣本推論母體的比例｜需要」
- 原始出處：Lee & Baskerville (2003), ISR 14(3)。未取得全文（INFORMS 403，找不到開放全文），以下是摘要
  - 原文（摘要）："The framework organizes the different forms into four types, which are defined by the distinction between empirical and theoretical kinds of statements. On the one hand, the framework affirms the bounds within which statistical, sampling-based generalizability is legitimate. On the other hand, the framework indicates ways in which researchers … may properly lay claim to generalizability … even when their inquiry falls outside the bounds of sampling-based research."
  - 二手（Amrit et al., arXiv:1201.4142，不是原文）："Type EE: Generalising from data to description / Type ET: Generalising from description to theory / Type TE: Generalising from theory to description / Type TT: Generalising from concepts to theory"
- 判定：查不到
- 說明：「四型由實證／理論陳述區分」「統計抽樣式概化只在特定範圍內成立」，摘要都支持。但「只有一種需要統計抽樣」的精確說法，以及四型各自的定義，都沒能從原文核對。依二手來源，TT 是「從概念到理論」，和站上的「把某領域的理論移植到新領域」不同；EE 是「從資料到描述」，範圍比「樣本推論母體」廣。這兩格很可能是站方的轉述。
- 建議改法：TT 一欄改成「從概念（構念、命題）歸納成理論」，EE 一欄改成「從資料到描述（例如樣本統計量推論母體參數，是其中一種）」；取得原文之後，再確認「只有 EE 涉及統計抽樣」是不是原文的說法。

#### REF-59　Keshav (2007) 三遍閱讀法每一遍做什麼
- 位置：`docs/finding-reading.md:186-196`；`docs/sources.md:82`
- 站上寫法：「第一遍｜5–10 分鐘｜標題、摘要、模型圖、各節標題、結論｜…我要不要讀第二遍？」「第二遍｜約 1 小時｜正文（跳過推導細節）、看懂所有圖表」「第三遍｜數小時｜逐行重建，假設自己是作者」；接著：「大部分論文你只需要第一遍。一輪文獻回顧裡，第一遍：第二遍：第三遍的比例大概是 30：8：2。」
- 原始出處：Keshav, S. (2007). How to read a paper. CCR 37(3), 83–84（全文 <http://ccr.sigcomm.org/online/files/p83-keshavA.pdf>）
  - 原文："This pass should take about five to ten minutes and consists of the following steps: 1. Carefully read the title, abstract, and introduction 2. Read the section and sub-section headings, but ignore everything else 3. Read the conclusions 4. Glance over the references, mentally ticking off the ones you've already read"
  - 原文："In the second pass, read the paper with greater care, but ignore details such as proofs. … Look carefully at the figures, diagrams and other illustrations in the paper." "The second pass should take up to an hour."
  - 原文："The key to the third pass is to attempt to virtually re-implement the paper: that is, making the same assumptions as the authors, re-create the work." "This pass can take about four or five hours for beginners, and about an hour for an experienced reader."
- 判定：不精確
- 說明：時間、第二遍、第三遍都對，但第一遍的內容不對：原文要讀「緒論」和「掃過參考文獻」，站上漏了這兩項，卻多了原文沒有的「模型圖」（Keshav 是在第二遍才看圖）。第一遍結束要回答的 five Cs（Category、Context、Correctness、Contributions、Clarity）站上也沒提。「30：8：2」的比例在原文找不到；原文的文獻回顧做法是先找 3–5 篇近期論文各讀一遍，再對關鍵論文讀兩遍。這個比例緊接在 Keshav 的書目後面，容易被讀成是 Keshav 的主張。
- 建議改法：第一遍改成「標題、摘要、緒論；各節標題；結論；掃過參考文獻」，讀完要能回答 five Cs；第二遍補「圖表要仔細看，並標出還沒讀過的相關文獻」；「30：8：2」前面加上「本站經驗值，非 Keshav 原文」，或直接刪掉。

#### REF-60　Whetten (1989) 理論貢獻的四要素與「換情境不算貢獻」
- 位置：`docs/is-research.md:73-87`、`:159`
- 站上寫法：「Whetten（1989）的這篇短文只有六頁…What｜哪些因素…應該被納入？｜How｜這些因素之間怎麼連結？｜Why｜為什麼是這樣連？…｜Who / When / Where｜這個理論在什麼條件下成立？…換情境本身不是貢獻；論證出情境會造成差異才是」
- 原始出處：Whetten (1989), AMR 14(4), 490–495（ReadKong 轉錄本 <https://www.readkong.com/page/what-constitutes-a-theoretical-contribution-2124381>）
  - 原文："What. Which factors (variables, constructs, concepts) logically should be considered as part of the explanation of the social or individual phenomena of interest?"
  - 原文："How. Having identified a set of factors, the researcher's next question is, How are they related? Operationally this involves using "arrows" to connect the "boxes.""
  - 原文："Why. What are the underlying psychological, economic, or social dynamics that justify the selection of factors and the proposed causal relationships? This rationale constitutes the theory's assumptions—the theoretical glue that welds the model together."
  - 原文："Who, Where, When. These conditions place limitations on the propositions generated from a theoretical model."
  - 原文："applying an old model to a new setting and showing that it works as expected is not instructive by itself. This conclusion has theoretical merit only if something about the new setting suggests the theory shouldn't work under those conditions."
  - 原文："the addition of a new variable to an existing list should not be mistaken as a theoretical contribution. Relationships, not lists, are the domain of theory."
- 判定：正確
- 說明：四要素、加變數不算貢獻、換情境要先論證為何會有差異，原文都支持。頁碼 490–495 是六頁。轉錄本是兩欄混排，上面引文是我照同一欄的文字接起來的，沒有改字。
- 建議改法：不需修改

#### REF-61　Hevner et al. (2004) 七大規範，以及「真理與效用不可分割」
- 位置：`docs/is-research.md:43`；`docs/theories.md:290`；`docs/sources.md:79`
- 站上寫法：「行為科學追求真理（truth），設計科學追求效用（utility），而「真理與效用是不可分割的」」；「七大規範：人工物、問題相關性、設計評估、研究貢獻、研究嚴謹性、設計即搜尋、成果溝通」
- 原始出處：Hevner et al. (2004), MISQ 28(1)（全文 <https://www.in.th-nuernberg.de/professors/Holl/Personal/Hevner_DesignScience_ISRes.pdf>）
  - 原文："The goal of behavioral-science research is truth. The goal of design-science research is utility. As argued above, our position is that truth and utility are inseparable."
  - 原文（Table 1 標題）："Guideline 1: Design as an Artifact … Guideline 2: Problem Relevance … Guideline 3: Design Evaluation … Guideline 4: Research Contributions … Guideline 5: Research Rigor … Guideline 6: Design as a Search Process … Guideline 7: Communication of Research"
- 判定：正確
- 說明：引文和七項規範的名稱都和原文一致。
- 建議改法：不需修改

#### REF-62　McGrath (1981) 方法選擇的三難與各方法的強弱
- 位置：`docs/is-research.md:52-67`、`:158`
- 站上寫法：「他主張任何研究策略都在三個目標之間取捨，而且不可能三個同時最大化」；表格：「普遍性｜誰最強：問卷調查、次級資料｜誰最弱：個案研究、實驗室實驗」「真實性｜個案研究、田野研究｜實驗室實驗」「精確性｜實驗室實驗、模擬｜個案研究」；「McGrath 的原話大意是：研究者不是在「選一個最好的方法」，而是在選擇要接受哪一種缺陷」
- 原始出處：McGrath (1981), ABS 25(2), 179–210, doi:10.1177/000276428102500205
  - 未取得全文：SAGE 回 403、OpenAlex 沒有摘要也沒有開放版本、WebSearch 只找到二手資料（學習卡片、引用文）。
- 判定：查不到
- 說明：三個目標（generalizability、precision、realism）和「不能同時最大化」是常見轉述，我找不到原文可以逐字核對。表格把「個案研究」「次級資料」「模擬」放進強弱欄，這些不是 McGrath 八種研究策略的原名稱（記憶所及，未經核對），所以這張表很可能是站方自己對應的。站上已用「原話大意」，沒有冒充引文。
- 建議改法：表格標題加註「本站依 McGrath 的三難整理之對應，非原文表格」；有原文之後，再補一句原文引文。

#### REF-63　DeLone & McLean：1992 原版模型被寫成「品質 → 使用／滿意 → 淨效益」
- 位置：`docs/theories.md:288`（以及 `:181-187` 的圖標「1992；2003 修訂」）
- 站上寫法：「IS 成功模式｜DeLone & McLean (1992)｜品質 → 使用／滿意 → 淨效益」
- 原始出處：DeLone & McLean (1992), ISR 3(1), 60–95（摘要）；DeLone & McLean (2003), JMIS 19(4)（摘要）
  - 原文（1992 摘要）："This taxonomy posits six major dimensions or categories of I/S success—SYSTEM QUALITY, INFORMATION QUALITY, USE, USER SATISFACTION, INDIVIDUAL IMPACT, and ORGANIZATIONAL IMPACT."
  - 原文（2003 摘要）："we propose minor refinements to the model and propose an updated DeLone and McLean IS Success Model."
- 判定：不精確
- 說明：1992 年版的結果端是 individual impact 和 organizational impact；「淨效益」以及第 5 節圖中的「服務品質」都是 2003 年修訂版才有的（站上 :289 那一列寫對了）。:288 把 2003 年的結果端套到 1992 年。
- 建議改法：「IS 成功模式｜DeLone & McLean (1992)｜系統品質、資訊品質 → 使用、使用者滿意 → 個人影響 → 組織影響」；第 5 節的圖標改成「（2003 修訂版）」。

#### REF-64　TAM 被描述成「TRA + TPB 的科技化版本」，終點是「意圖」
- 位置：`docs/theories.md:58`、`:69`、`:236`、`:324`
- 站上寫法：「TAM ≈ TRA + TPB 的科技化版本」；「TAM 是兩階段架構：有用易用 → 意圖。它的終點是意圖，不及於後續的使用深度、依賴或轉換。」；索引表「知覺有用性與知覺易用性決定使用意圖」；「行為意圖家族：TRA → TPB → TAM → UTAUT → ECM，一脈相承」
- 原始出處：Davis (1989), MISQ 13(3)（摘要）；Davis, Bagozzi & Warshaw (1989), Management Science 35(8), 982–1003, doi:10.1287/mnsc.35.8.982（摘要）；Ajzen (1991)（摘要）
  - 原文（Davis 1989）："Perceived usefulness was significantly correlated with both self-reported current usage (r = .63, Study 1) and self-predicted future usage (r = .85, Study 2)."
  - 原文（Davis et al. 1989，篇名就是「A Comparison of Two Theoretical Models」，比較 TAM 和 TRA）："This research addresses the ability to predict peoples' computer acceptance from a measure of their intentions … intentions to use a specific system … were correlated 0.35 with system use 14 weeks later."
  - 原文（Ajzen 1991）："Research dealing with various aspects of the theory of planned behavior (Ajzen, 1985, Ajzen, 1987) is reviewed"
- 判定：不精確
- 說明：(1) TAM 是由 TRA 改編而來，Davis et al. (1989) 比較的對象就是 TRA；TPB 跟 TAM 是平行發展的，TAM 不是從 TPB 衍生，而站上的「TRA → TPB → TAM」又引用 Ajzen 1991，時間順序反過來了。(2) Davis (1989) MISQ 那篇的結果變數是使用（現在使用、預期未來使用），Davis et al. (1989) 也是意圖 → 實際使用，所以 TAM 的終點包含使用行為，不止於意圖。站上 2.3 節的圖其實也畫了「實際使用」，和文字自相矛盾。
- 建議改法：「TAM 改編自 TRA，把態度的信念前因換成知覺有用性與知覺易用性」；「TAM 的結果變數是使用意圖與實際使用；它不處理持續使用、使用深度或依賴」；索引表「…決定使用意圖與使用行為（意圖構念見 Davis, Bagozzi & Warshaw, 1989）」；回顧句改成「TRA 衍生出 TPB 與 TAM 兩支，UTAUT 整合兩者在內的八個模型，ECM 處理持續使用」。

#### REF-65　TAM 的「隱藏假設：使用者沒有選擇不用的自由」
- 位置：`docs/theories.md:68`、`:325`
- 站上寫法：「TAM 一開始是為了「公司內部系統」而設計的。這是它的隱藏假設：使用者沒有選擇不用的自由，重點在於接受度。把它直接套用到自願性、娛樂性、社群性的情境時，這個假設就不成立了。」
- 原始出處：Davis, Bagozzi & Warshaw (1989), Management Science 35(8)（摘要）；Venkatesh & Davis (2000), Management Science 46(2)（摘要）
  - 原文（Davis et al. 1989）："Computer systems cannot improve organizational performance if they aren't used. Unfortunately, resistance to end-user systems by managers and professionals is a widespread problem. To better predict, explain, and increase user acceptance, we need to better understand why people accept or reject computers."
  - 原文（Venkatesh & Davis 2000）："The extended model, referred to as TAM2, was tested using longitudinal data collected regarding four different systems at four organizations (N = 156), two involving voluntary usage and two involving mandatory usage."
- 判定：錯誤
- 說明：組織內系統這個情境沒錯；但 TAM 要解釋的正是使用者「接受或拒用」，前提是使用者可以不用（原文："resistance … is a widespread problem""accept or reject"）。強制使用與自願使用的區分，是到 TAM2 才另外處理的。站上說 TAM 假設「沒有選擇不用的自由」，和原始論文的問題設定相反。我第二次查核重讀了 Davis et al. 的摘要，結論一樣。
- 建議改法：「TAM 最初在組織內、以知識工作者自主決定是否使用的系統為情境發展。延伸到消費、娛樂或社群情境時，要考慮享樂動機、社會影響、價格等原模型沒有的前因（參見 UTAUT2）；強制使用情境則要另外處理（參見 TAM2 的自願性）。」

#### REF-66　ECM 的路徑圖少了「知覺有用性 → 持續使用意圖」
- 位置：`docs/theories.md:79-89`
- 站上寫法：圖示「確認 ─→ 知覺有用性 ┐ ├─→ 滿意度 ─→ 持續使用意圖」，確認另外一條箭頭指向滿意度
- 原始出處：Bhattacherjee (2001), MISQ 25(3)（摘要）
  - 原文："The results suggest that users' continuance intention is determined by their satisfaction with IS use and perceived usefulness of continued IS use. User satisfaction, in turn, is influenced by their confirmation of expectation from prior IS use and perceived usefulness. Post-acceptance perceived usefulness is influenced by users' confirmation level."
- 判定：不精確
- 說明：原模型有一條知覺有用性直接到持續使用意圖的路徑，站上的圖只畫到滿意度。
- 建議改法：圖上補一條「知覺有用性 ─→ 持續使用意圖」。

#### REF-67　ELM：「周邊路徑只能影響到注意，進而影響涉入的高低」
- 位置：`docs/theories.md:126`、`:327`
- 站上寫法：「3. 周邊路徑只能影響到「注意」，進而影響涉入的高低，不能直接產生穩固的態度。」；回顧「ELM 的關鍵是動機與能力同等重要；周邊路徑只能影響注意。」
- 原始出處：Petty, Cacioppo & Schumann (1983). Central and peripheral routes to advertising effectiveness: The moderating role of involvement. *Journal of Consumer Research*, 10(2), 135–146, doi:10.1086/208954（摘要）；Petty & Cacioppo (1986) 專書未取得全文
  - 原文："The manipulation of argument quality had a greater impact on attitudes under high than low involvement, but the manipulation of product endorser had a greater impact under low than high involvement. These results are consistent with the view that there are two relatively distinct routes to persuasion."
- 判定：錯誤
- 說明：周邊線索（代言人身分）在低涉入時會直接改變「態度」，不是只影響注意。涉入是決定走哪條路徑的前提條件（動機），不是周邊路徑造成的結果。「不能產生穩固的態度」這半句大致對（ELM 認為周邊路徑造成的態度改變比較短暫），本頁第 117–120 行的表格也寫了「短暫、易被推翻」，和第 126 行自相矛盾。第二次查核重讀了摘要，確認是指 attitudes。
- 建議改法：「3. 周邊路徑也會改變態度，但這種改變較短暫、較容易被反駁，也比較不能預測行為；涉入程度是決定走哪條路徑的條件，不是周邊路徑的結果。」回顧句改成「周邊路徑帶來的態度改變較不持久」。

#### REF-68　UTAUT 整合八個模型、四個核心前因與四個調節變數；UTAUT2 加三個構念
- 位置：`docs/theories.md:75-77`、`:237`
- 站上寫法：「整合八個既有模型，四個核心前因：績效期望、努力期望、社會影響、促成條件；並納入性別、年齡、經驗、自願性作為調節變數。UTAUT2 針對消費者情境加入享樂動機、價格價值、習慣。」
- 原始出處：Venkatesh et al. (2003)（摘要）；Venkatesh, Thong & Xu (2012)（摘要）
  - 原文（2003）："The eight models reviewed are the theory of reasoned action, the technology acceptance model, the motivational model, the theory of planned behavior, a model combining the technology acceptance model and the theory of planned behavior, the model of PC utilization, the innovation diffusion theory, and the social cognitive theory. … UTAUT … with four core determinants of intention and usage, and up to four moderators of key relationships."
  - 原文（2012）："Our proposed UTAUT2 incorporates three constructs into UTAUT: hedonic motivation, price value, and habit."
- 判定：正確
- 說明：數量和 UTAUT2 的三個構念，摘要都證實了。四個前因與四個調節變數的名稱，摘要沒有列出，我只在二手來源（多篇引用文）看到一致的名稱，沒有看到矛盾。
- 建議改法：不需修改

#### REF-69　TPB：知覺行為控制同時直接影響行為
- 位置：`docs/theories.md:44-54`、`:235`
- 站上寫法：「在 TRA 上加入第三個前因，也就是知覺行為控制…知覺行為控制同時直接影響行為」
- 原始出處：Ajzen (1991), OBHDP 50(2)（摘要）
  - 原文："Intentions to perform behaviors of different kinds can be predicted with high accuracy from attitudes toward the behavior, subjective norms, and perceived behavioral control; and these intentions, together with perceptions of behavioral control, account for considerable variance in actual behavior."
- 判定：正確
- 建議改法：不需修改

#### REF-70　RBV：Barney (1991) 的 VRIN 四特性
- 位置：`docs/theories.md:170`、`:277`、`:328`
- 站上寫法：「有價值（Valuable）、稀少（Rare）、難以模仿（Inimitable）、難以取代（Non-substitutable）」
- 原始出處：Barney (1991), JOM 17(1)（摘要）
  - 原文："Four empirical indicators of the potential of firm resources to generate sustained competitive advantage-value, rareness, imitability, and substitutability-are discussed."
- 判定：正確
- 建議改法：不需修改

#### REF-71　Moore & Benbasat (1991) 與 Oliver (1980) 的一句話描述
- 位置：`docs/theories.md:238-240`
- 站上寫法：「把 DOI 的創新特徵操作化成可用的量表」；「滿意度來自實際表現與事前期望的落差」
- 原始出處：兩篇的摘要
  - 原文（Moore & Benbasat）："The perceptions of adopting were initially based on the five characteristics of innovations derived by Rogers (1983) from the diffusion of innovations literature, plus two developed specifically within this study. … The result is a parsimonious, 38-item instrument comprising eight scales"
  - 原文（Oliver）："A model is proposed which expresses consumer satisfaction as a function of expectation and expectancy disconfirmation."
- 判定：正確
- 說明：Rogers 的五個創新特徵（theories.md:238），Moore & Benbasat 的摘要也證實了。
- 建議改法：不需修改

#### REF-72　Orlikowski & Iacono (2001) 盤點「IS 頂級期刊十年」，五種 IT 人工物觀點
- 位置：`docs/is-research.md:11-19`
- 站上寫法：「Orlikowski 與 Iacono（2001）盤點了 IS 頂級期刊十年的論文後發現，多數研究其實把「IT」當成一個沒有內容的黑盒子。他們整理出…五種觀點」
- 原始出處：Orlikowski & Iacono (2001), ISR 12(2)（摘要，IDEAS/RePEc 頁 <https://ideas.repec.org/a/inm/orisre/v12y2001i2p121-134.html>）
  - 原文："drawing on a review of the full set of articles published in Information Systems Research (ISR) over the past ten years, we argue that the field has not deeply engaged its core subject matter—the information technology (IT) artifact. … The IT artifact itself tends to disappear from view, be taken for granted, or is presumed to be unproblematic once it is built and installed."
- 判定：不精確
- 說明：盤點的範圍只有一本期刊 ISR，不是「IS 頂級期刊」（複數）。「把 IT 當黑盒子」大致符合摘要。五種觀點（tool、proxy、ensemble、computational、nominal）的名稱，我只在二手摘要看到；全文託管站 nissenbaum.tech.cornell.edu 憑證有問題又回 503，沒能讀到原文。
- 建議改法：「Orlikowski 與 Iacono（2001）盤點了 *Information Systems Research* 創刊後十年的全部論文…」

#### REF-73　Benbasat & Zmud (2003)：資管研究的核心是 IT 人工物及其緊鄰的因果網絡
- 位置：`docs/is-research.md:24`
- 站上寫法：「Benbasat 與 Zmud（2003）進一步主張：資管研究的核心應該是 IT 人工物及其緊鄰的因果網絡…離這個核心愈遠，愈難說服審查者」
- 原始出處：Benbasat & Zmud (2003), MISQ 27(2)（摘要）
  - 原文："We are concerned that the IS research community is making the discipline's central identity ambiguous by, all too frequently, under-investigating phenomena intimately associated with IT-based systems and over-investigating phenomena distantly associated with IT-based systems. … we discuss research by IS scholars that either fails to address this core set of properties (labeled as error of exclusion) or that addresses concepts/phenomena falling outside this core set (labeled as error of inclusion)."
- 判定：正確
- 說明：摘要支持「核心性質」與「離核心太遠是 error of inclusion」。「IT artifact and its immediate nomological net」這個片語我沒在原文核對到（全文被擋），二手資料的轉述一致。
- 建議改法：不需修改

#### REF-74　Berthon et al. (2002)：複製／擴充／創造三種策略與學術價值高低
- 位置：`docs/is-research.md:91-101`
- 站上寫法：「把研究空間切成三種操作」；表格「複製｜同樣的理論、同樣的方法，換一批樣本｜最低…」「擴充…中等」「創造…最高」；「Berthon 等人的關鍵論點是：這三者不是「等級」，而是一個研究空間裡的不同座標」
- 原始出處：Berthon et al. (2002), ISR 13(4)（摘要）
  - 原文："Our framework includes a conceptualization of the relationship among replication, extension, and generation in IS research. The concept of "research space" is defined and a framework is developed that delineates eight possible research strategies."
- 判定：不精確
- 說明：原框架定義的是「八種」研究策略；站上收斂成三類，表格又給了「最低／中等／最高」的價值排序，跟同一段「不是等級」的說法互相矛盾。價值排序和「換一批樣本」的定義，我沒能從原文核對（全文被擋，figshare 條目沒有檔案）。
- 建議改法：「Berthon 等人以研究空間的維度組合出八種研究策略，可歸成複製、擴充、創造三大類」；表格的「學術價值」一欄註明是本站的實務判斷，不是原文的排序。

#### REF-75　Straub, Boudreau & Gefen (2004) 驗證指引涵蓋的效度類型
- 位置：`docs/is-research.md:123`
- 站上寫法：「（內容效度、建構效度、信度、操弄檢核、統計結論效度該怎麼報告）。它是開放取用的。」
- 原始出處：Straub et al. (2004), CAIS 13（摘要）
  - 原文："this paper suggests heuristics for reinvigorating the quest for validation in IS research via content/construct validity, reliability, manipulation validity, and statistical conclusion validity."
- 判定：正確
- 說明：原文用 manipulation validity，站上寫「操弄檢核」，意思相近。Unpaywall 標示這篇在 AIS 是開放取用（BRONZE），但用程式抓 PDF 時被 Cloudflare 擋下（瀏覽器應該能開）。
- 建議改法：不需修改

#### REF-76　Palvia et al. 依方法分類統計 MIS 期刊論文
- 位置：`docs/is-research.md:131`
- 站上寫法：「Palvia 等人在 CAIS 上的系列盤點把 MIS 期刊論文依方法分類統計」
- 原始出處：Palvia et al. (2004), CAIS 14（摘要）
  - 原文："This article presents trends in published MIS research for an 11 year period, 1993-2003. It is an update of a previous article in CAIS (Volume 11, Article 16) that covered the period 1993-1997. All of the articles in seven mainstream MIS journals were examined in terms of subjects researched and methodologies employed to conduct research."
- 判定：正確
- 建議改法：不需修改（書目見 REF-51）

#### REF-77　Webster & Watson (2002)：concept-centric 引文與概念矩陣
- 位置：`docs/literature.md:216-218`、`:261`；`docs/sources.md:78`
- 站上寫法：「「概念決定一篇回顧的組織架構；相對地，有些作者採取以作者為中心的寫法，實際上只是把相關文章摘要一遍，這種做法無法整合文獻。」」；「以文獻為列、概念為欄，必要時再依分析層次（個人／團隊／組織）切分子欄」
- 原始出處：Webster & Watson (2002), MISQ 26(2)（全文 <https://ntnu.no/wiki/download/attachments/98080959/Webster%20%20Watson%20-%20Writing%20a%20literature%20review.pdf?api=v2>）
  - 原文："A literature review is concept-centric. Thus, concepts determine the organizing framework of a review. In contrast, some authors take an author-centric approach and essentially present a summary of the relevant articles. This method fails to synthesize the literature."
  - 原文："You might need to add a further dimension to the concept matrix to handle the unit of analysis (Table 3)."；Table 3 圖例："Legend: O (organizational), G (group), I (individual)"
- 判定：正確
- 說明：中譯忠實。原文的矩陣構想來自 Salipante et al. (1982)，站上沒提但沒有錯。
- 建議改法：不需修改

#### REF-78　彭明輝〈如何選研究的主題〉：問「有沒有見人所未見的能力」，不是問「有沒有興趣」
- 位置：`docs/finding-reading.md:266-268`
- 站上寫法：「他主張真正該問的不是「我對這個題目有沒有興趣」，而是「我在這個題目上有沒有『見人所未見』的能力」，因為學位論文的成敗關鍵在於原創性貢獻」
- 原始出處：彭明輝，〈如何選研究的主題〉，2022-11-01，<https://mhperng.blogspot.com/2022/11/blog-post.html>
  - 原文：「所以，選一個研究的主題或題目時，你該問自己的是：「我對這個主題有沒有『見人所未見』的能力」。而不是問：「我對這題目有沒有興趣」。」；「（2）對該主題的學術界有重要而可觀的貢獻（所謂的「原創性」…）…而（2）則通常是成敗的關鍵。」
- 判定：正確
- 建議改法：不需修改

#### REF-79　彭明輝部落格版權聲明的引文
- 位置：`docs/sources.md:54`
- 站上寫法：「明訂：「謝絕所有商業網站之轉載」「其他形式之轉載必須徵得本人同意」，僅「歡迎善意之引用，或客觀公允之評論」。」
- 原始出處：清大彭明輝的部落格「版權聲明」，<http://mhperng.blogspot.com/p/blog-page_78.html>
  - 原文：「自 2015 年 5 月 11 日 起，謝絕所有商業網站之轉載。其他形式之轉載必須徵得本人同意。…凡善意之引用，或客觀公允之評論，本人在此表示歡迎。」
- 判定：不精確
- 說明：前兩段引文是逐字的。第三段放在引號裡，但原文是「凡善意之引用，或客觀公允之評論，本人在此表示歡迎」，站上把語序改成「歡迎…」，又放在引號內。輕微，但引號裡應該逐字。
- 建議改法：「…，並表示「凡善意之引用，或客觀公允之評論，本人在此表示歡迎」。」
- 查核日期：2026-10-23

#### REF-80　《研究生完全求生手冊》各章導讀與章號
- 位置：`docs/sources.md:33`
- 站上寫法：「先讀第 1–2 章（研究所學什麼、學術著作的要件）…再讀第 6–7 章（期刊論文閱讀技巧、總覽式文獻回顧）…第 9–12 章（批判與創新、十倍速文獻回顧）…第 16 章（口試委員的期待）」；2.2 節「第 3–4 章（論文架構、構思與寫作次序）…第 9–10 章（結果與討論、比較基準與視覺化）…第 12 章（口試與簡報）」
- 原始出處：金石堂書頁目錄 <https://www.kingstone.com.tw/basic/2015250055579/>；聯經官方書店目次 <https://store.linkingbooks.com.tw/product/152138>
  - 原文（研究生）：「1 達摩面壁，慧可立雪──研究所學什麼 2 黃金與糞土──學術著作的要件與良瓢 … 6 告別大學時代──期刊論文的閱讀技巧 7 鳥瞰全局──總覽式文獻回顧與田野 … 9 青出於藍──批判與創新的要領（上）… 12 上窮碧落下黃泉──十倍速文獻回顧要訣 … 16 終戰秘笈──考古題與口試委員的期待」
  - 原文（論文寫作）：「3 精心擘畫，層次井然：論文的架構與主要內容 4 攻守兼備，成竹在胸（上）：論文的構思與寫作次序 … 9 結果與討論（上）… 10 結果與討論（下）：比較的基準與數據的視覺化 … 12 綱張目舉，進退有據：口試與簡報的要領」
- 判定：正確
- 建議改法：不需修改

#### REF-81　其他頁面歸給彭明輝書中的觀點（書的內容）
- 位置：`docs/research-basics.md:33`、`:92`、`:125-130`；`docs/problem-design.md:13`；`docs/literature.md:6`
- 站上寫法：「創意是用來走完最後一哩路的…這是彭明輝《研究生完全求生手冊》反覆強調的核心觀點」；「研究者的根本能力只有四項（這一組整理同時出現在彭明輝的書…）」；「《研究生完全求生手冊》提出的時程規劃…碩一寒假結束前…」；「彭明輝書中的比喻…把「海底潛水艇周邊之壓力分布」抽象成「有限長木棍在二維不可壓縮流體中之流場分析」」
- 原始出處：彭明輝《研究生完全求生手冊》（聯經，2017）。未取得全文，只看到書店頁的目錄與作者自序
  - 原文（自序，金石堂頁）：「從學術界的文獻找創意，以便「用前人的智慧，解決自己的問題」。只要學會這些方法，就可以產出夠資格拿碩士的創意；至於個人的才華與靈感，則是用來追求「更上層樓」的創意。」
  - 原文（目錄）：「3 山中無曆日，寒盡不知年──研究的歷程與時間表」
- 判定：查不到
- 說明：自序支持「先從文獻找創意，才華靈感是更上層樓」這個方向；目錄證實第 3 章有時間表。但時程表的各階段內容、四大能力、潛水艇比喻，都要看書的內文才能核對。我試過書店頁、WebSearch（潛水艇＋木棍＋彭明輝，找不到）、部落格搜尋。
- 建議改法：各處加章號（例如「見《研究生完全求生手冊》第 3 章」），方便讀者自己查；內容不需改。

---

### 小計

- 查了 79 條：
  - 書目 53 條（第一節表格的 REF-01～REF-49、REF-52～REF-55；REF-49 是七筆經典專書和論文的合併列）：正確 42、不精確 10、錯誤 1、查不到 0。第二節的 REF-50、REF-51 是書目問題的詳列，不另外計數。
  - 觀點 26 條（REF-56～REF-81）：正確 13、不精確 7、錯誤 2、查不到 4。
- 合計：正確 55、不精確 17、錯誤 3、查不到 4。
- 錯誤（3）：REF-53、REF-65、REF-67
- 不精確（17）：REF-04、REF-05、REF-07、REF-11、REF-16、REF-32、REF-33、REF-36、REF-37、REF-40（書目篇名、刊名或欄位不完整，詳見 REF-50／REF-51），REF-59、REF-63、REF-64、REF-66、REF-72、REF-74、REF-79
- 查不到（4）：REF-57、REF-58、REF-62、REF-81

附註：所有 DOI（13 個）都能從 doi.org 解析。兩個 AOM 的 10.5465 DOI 已改成 JSTOR 10.2307 DOI 的別名，仍可解析。pubsonline／journals.aom.org／sagepub／dl.acm.org／misq.umn.edu 的連結用程式抓都回 403，是機器人防護，不代表連結失效。

---

## 七、TOOL：研究工具

查核日期：2026-10-23。範圍：三頁中可查證的工具價格、方案、功能、數字、版本號與日期、網址、軟體操作步驟、書目。
方法說明：
- 網頁用 curl＋WebFetch 抓官方頁；GitHub 網頁與 API 被代理擋（403），改用 `git clone`／`git ls-remote` 直接讀官方 repo（Better BibTeX、zotero/utilities、zotero/zotero、obsidian-releases、各 Obsidian 外掛、winget-pkgs、Consensus MCP、thesis-notes-template）。
- Zotero 日期解析與 Better BibTeX 日期解析兩件事，除了讀原始碼，也把官方原始碼下載到查核環境實際執行（測試腳本未納入 repo）。
- Zotero 官方文件用 `?do=export_raw` 抓下來轉成純文字比對。
- 以下「原文」只貼我在來源上實際讀到的文字。

---

### 一、docs/tool-directory.md

#### TOOL-01　Semantic Scholar 由 AI2 維運、免費、索引超過 2 億篇
- 位置：`docs/tool-directory.md:71`；`docs/tool-directory.md:266`（最小組合）
- 站上寫法：「Allen Institute for AI（AI2）維運的免費學術搜尋引擎，索引超過 2 億篇論文」「提供 TLDR 摘要、引文脈絡、Semantic Reader、開放 API 與 S2ORC 語料庫」
- 原始出處：Semantic Scholar About，<https://www.semanticscholar.org/about>
  - 原文："a Research and Product Development team within Ai2"；"free, AI-driven search and discovery tools"；"over 200 million academic papers"；S2ORC 稱為 "Semantic Scholar Open Research Corpus"
- 判定：正確
- 說明：維運單位、免費、2 億篇、Semantic Reader、API、S2ORC 都對得上（About 頁沒寫 TLDR，但這是 Semantic Scholar 公開的功能，不影響判定）。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-02　OpenAlex「超過 2 億筆著作、資料完全開放且可查 API」
- 位置：`docs/tool-directory.md:72`
- 站上寫法：「免費開放的著作資料庫，收錄超過 2 億筆著作紀錄，資料完全開放且可查 API」
- 原始出處：OpenAlex Help（help.openalex.org 的 data/works 與 access/pricing 頁），<https://help.openalex.org/data/works/>、<https://help.openalex.org/access/pricing/>
  - 原文："There are over 320 million works in OpenAlex, with tens of thousands added every day."
  - 原文："The OpenAlex *data* is free — but serving it is not, so *usage* is what costs money. … every account gets **$1 of API usage per day for free**"
  - 原文："the data is a public good, released under a CC0 public-domain license"
  - 實測：不帶 API key 直接打 `api.openalex.org/works` 會被拒，回傳 "This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address"
- 判定：不精確
- 說明：資料本身確實是 CC0、免費開放，但數量已經超過 3.2 億，而且 API 現在是「免費帳號、每天 US$1 額度」，需要申請 key，超過要付費，已經不能算毫無限制的免費 API。
- 建議改法：「免費開放（CC0）的著作資料庫，收錄超過 3.2 億筆著作紀錄；API 需要免費申請 key，每天有 US$1 的免費用量，大量查詢要付費（2026-10 查詢）」
- 查核日期：2026-10-23

#### TOOL-03　Elicit 搜尋 1.38 億篇論文與 54.5 萬筆臨床試驗，以及核心功能
- 位置：`docs/tool-directory.md:82-83`；`docs/tool-directory.md:55`
- 站上寫法：「官網自述搜尋範圍超過 1.38 億篇學術論文與 54.5 萬筆臨床試驗」「核心功能：Research Agent（跨來源蒐證並產出帶引用的報告、表格、圖表）、論文搜尋、系統性回顧的自動化篩選與資料萃取」
- 原始出處：Elicit 首頁，<https://elicit.com/>
  - 原文："Search over 138 million academic papers and 545,000 clinical trials, with more data sources coming soon."
  - 原文："Gathers evidence across scientific databases, academic journals, public data sources, and internally uploaded documents. • Creates fully cited artifacts like reports, tables, figures, bioinformatics analyses, calculations, and slides"
- 判定：正確
- 說明：數字和功能描述都跟官網一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-04　Consensus 2021 年創立、「超過千萬名研究者、12,500 所以上大學使用」
- 位置：`docs/tool-directory.md:89`
- 站上寫法：「定位是『科學研究的 AI 工作區』，2021 年創立，官網宣稱超過千萬名研究者、12,500 所以上大學使用」
- 原始出處：Consensus About Us，<https://consensus.app/home/about-us/>；Consensus Pricing，<https://consensus.app/pricing/>
  - 原文（About）："Consensus is an AI workspace for scientific research."；"Consensus was founded in 2021 by Christian Salem and Eric Olson"；"10+ million Researchers, students, and clinicians choose Consensus 12,500+ Universities represented amongst our users"
  - 原文（Pricing）："Over 5 million researchers, students, and clinicians trust Consensus"
- 判定：不精確
- 說明：官網原文是「使用者來自 12,500 所以上的大學」，不是「12,500 所大學在用」；「千萬」包含學生與臨床人員，不只研究者。而且官網自己的兩個頁面數字就不一致（About 寫 10+ million，Pricing 寫 5 million）。
- 建議改法：「2021 年創立；About 頁宣稱有超過 1,000 萬名研究者、學生與臨床人員使用，使用者來自 12,500 所以上大學（同站 Pricing 頁寫 500 萬，數字以官網為準）」
- 查核日期：2026-10-23

#### TOOL-05　Consensus MCP：安裝指令、OAuth、不登入也能用、免費帳號每月 30 次 API／MCP 呼叫
- 位置：`docs/tool-directory.md:102`、`docs/tool-directory.md:104-105`、`docs/tool-directory.md:111`
- 站上寫法：「`claude mcp add --transport http consensus https://mcp.consensus.app/mcp`。用 OAuth 登入 Consensus 帳號……不登入也能試用，額度較低；免費帳號每月有 30 次 API 與 MCP 呼叫額度」
- 原始出處：Consensus 官方 MCP README（`Consensus-NLP/consensus-mcp`，最後 commit 2026-08-26），<https://github.com/Consensus-NLP/consensus-mcp>；Consensus Help Center〈Subscription Plans〉（2026-09-12 版，經 intercom.help 鏡像取得），<https://intercom.help/consensus-d118a252369c/en/articles/10087865-subscription-plans>；Claude Code 文件，<https://code.claude.com/docs/en/mcp>
  - 原文（README）："claude mcp add --transport http consensus https://mcp.consensus.app/mcp"
  - 原文（README）："Most clients use OAuth: you sign in with your Consensus account the first time you connect. Claude and ChatGPT also work without an account at reduced limits."
  - 原文（方案頁）："Free Tier Cost: $0 … 30 included API & MCP calls per month"；"Pro Subscription Cost: $20/month or $144/year … 500 included API & MCP calls per month"
  - 原文（Claude Code 文件）："claude mcp add --transport http <name> <url>"
- 判定：正確
- 說明：指令、OAuth、不登入有較低額度、免費 30 次都對得上。附註：站上連到的 `https://docs.consensus.app/consensus-mcp` 與 `help.consensus.app/...` 從這裡抓回 403（Cloudflare 擋機器人），無法確認網址是否仍有效；docs 站 llms.txt 目前列出的 MCP 頁是 `https://docs.consensus.app/core-features/mcp`。
- 建議改法：不需修改；可以考慮把 MCP 文件連結換成 `https://docs.consensus.app/core-features/mcp`
- 查核日期：2026-10-23

#### TOOL-06　Elicit MCP：安裝指令，以及 MCP／API 要 Pro 以上方案
- 位置：`docs/tool-directory.md:106-107`、`docs/tool-directory.md:111`
- 站上寫法：「`claude mcp add --transport http elicit https://elicit.com/api/mcp`。加入後輸入 `/mcp`，選 `elicit` 再按 Authenticate……MCP 與 API 都要 Pro 以上付費方案，Basic／Plus 不能用」
- 原始出處：Elicit API 文件，<https://docs.elicit.com/>；Elicit Pricing，<https://elicit.com/pricing>
  - 原文（文件）："claude mcp add --transport http elicit https: //elicit.com/api/mcp Then run /mcp , select the elicit server, and choose Authenticate to open a browser for login."
  - 原文（文件）："Use an Elicit account with API access (Pro or above)"；"The same plan, quota, and session-access rules as REST apply."；限額表："Basic No access Plus No access Pro 300 Scale 500 Enterprise 10,000"
  - 原文（價格頁）："Basic For casual exploration Free"；"Plus For deeper research $11 … Per user/month, billed as $132 annually"；"Pro For systematic reviews $39 … API access"
- 判定：正確
- 說明：指令、操作與方案限制都和官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-07　Perplexity MCP：網址、OAuth 要是 API 組織管理員、Search API 每 1,000 次 US$5
- 位置：`docs/tool-directory.md:108-109`
- 站上寫法：「`claude mcp add --transport http perplexity https://api.perplexity.ai/mcp`……帳號必須是能支付 API 費用的組織管理員……加上 `--header "Authorization: Bearer YOUR_API_KEY"`……標準 Search API 每 1,000 次請求 US$5」
- 原始出處：Perplexity Docs〈MCP Server〉，<https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server>；〈Pricing〉，<https://docs.perplexity.ai/docs/getting-started/pricing>
  - 原文："de mcp add --transport http perplexity https://api.perplexity.ai/mcp Run /mcp inside Claude Code and follow the sign-in prompt for perplexity . To use an API key instead, add --header "Authorization: Bearer YOUR_API_KEY" to the command."
  - 原文："Needs an API organization. You must be an admin of an API organization that can pay for usage."
  - 原文："Tool calls are billed at standard API pricing to the API key you connect with, or to the organization you chose when signing in."
  - 原文："Search API Pricing API Price per 1K requests Description Search API $5.00 Raw web search results with advanced filtering"
- 判定：正確
- 說明：全部對得上。三家都有免費網頁版（Elicit Basic、Consensus Free、Perplexity Standard (Free)），也跟官方方案頁一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-08　ResearchRabbit「官網稱可存取超過 3.1 億篇論文」
- 位置：`docs/tool-directory.md:122`
- 站上寫法：「官網稱可存取超過 3.1 億篇論文，可與參考文獻管理工具連動、追蹤新論文」
- 原始出處：ResearchRabbit 首頁，<https://www.researchrabbit.ai/>
  - 原文："Trusted by 1,000,000+ researchers worldwide Access over 320 million academic papers"；"Bring your reference library and ResearchRabbit together"
- 判定：不精確
- 說明：官網現在寫的是 3.2 億篇；其餘功能描述沒問題。
- 建議改法：「官網稱可存取超過 3.2 億篇論文（2026-10 查詢）」
- 查核日期：2026-10-23

#### TOOL-09　Inciteful 網址寫成 incitefulmed.com/academic
- 位置：`docs/tool-directory.md:124`
- 站上寫法：「**Inciteful**（[incitefulmed.com](https://incitefulmed.com/academic/)）」
- 原始出處：實測 `https://inciteful.xyz/` 回傳 `HTTP/2 301 location: https://incitefulmed.com/academic/`；該頁 `<title>`：
  - 原文："Inciteful Academic | Using Citations to Explore Academic Literature"
- 判定：正確
- 說明：這個網域乍看可疑，但 Inciteful 的舊網域 inciteful.xyz 確實轉址到這裡，是官方網址。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-10　scite 數據：16 億筆引用陳述、3.17 億篇全文、35 家以上出版商
- 位置：`docs/tool-directory.md:146`（三分類在 :141-145）
- 站上寫法：「官網數據：索引超過 16 億筆引用陳述、3.17 億篇全文文章，與 35 家以上出版商有直接授權」
- 原始出處：scite 首頁，<https://scite.ai/>
  - 原文："Reads across 323 M+ full-text scholarly articles"；"Scite has indexed 1.6B+ citations, partners with 44 + publishers, and serves 2M users worldwide."；"with agreements across 44+ publishers plus the full open access corpus"；"Built on direct agreements with Wiley, SAGE, and 42+ more publishers"
- 判定：不精確
- 說明：16 億仍然對；全文篇數現在是 3.23 億，出版商是 44 家以上，官網同一頁還有「42+ more」的寫法。Supporting／Contrasting／Mentioning 三分類沒有問題。
- 建議改法：「官網數據：索引超過 16 億筆引用、3.2 億篇以上全文文章，與 40 多家出版商有授權協議（2026-10 查詢）」
- 查核日期：2026-10-23

#### TOOL-11　NotebookLM 在 2026 年 7 月改名為 Gemini Notebook，網址 notebook.google
- 位置：`docs/tool-directory.md:161`、`:171`、`:269`
- 站上寫法：「**Gemini Notebook**（原 NotebookLM，Google 於 2026 年 7 月改名）（[notebook.google](https://notebook.google/)）」
- 原始出處：Google Workspace Updates，2026-07-16，<https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html>
  - 原文："We're renaming NotebookLM to Gemini Notebook."；"While it remains a standalone product focused on being your premier research tool"
  - 實測：`https://notebooklm.google/` 回 301 轉到 `https://notebook.google/`；notebook.google 頁面標題 "Gemini Notebook | AI Research Tool & Thinking Partner"
- 判定：正確
- 說明：改名日期與網址都對。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-12　Rayyan 的完整流程，以及「有免費方案」
- 位置：`docs/tool-directory.md:181`
- 站上寫法：「證據合成平台……匯入 → 協作者分工 → 去重 → 題目摘要篩選 → 全文篩選與衝突解決 → 資料萃取 → 偏誤風險評估 → 產出 PRISMA 流程圖；有免費方案」
- 原始出處：Rayyan 首頁，<https://www.rayyan.ai/>
  - 原文："evidence synthesis platform in active research use."；"No credit card required · Free forever for basic use"；"01. Import & Organize … 02. Invite Collaborators … 03. Deduplicate … 04. Title & Abstract Screening … 05. Fu[ll-text screen]ing Review full articles Confirm eligibility Resolve conflicts 06. Data Extraction … 07. Risk of Bias … 08. Reporting Export results Generate PRISMA flow"
- 判定：正確
- 說明：八個步驟的順序與名稱都一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-13　ASReview：開源、Utrecht 大學協調、可減少高達 95% 篩選工作量
- 位置：`docs/tool-directory.md:183`
- 站上寫法：「**開源**，由荷蘭 Utrecht 大學協調……官網稱可減少高達 95% 的篩選工作量，強調程式碼可驗證、使用者完全掌握資料與決策」
- 原始出處：ASReview 首頁，<https://asreview.nl/>
  - 原文："Coordinated at Utrecht University, The Netherlands"；"reduce your workload by 95%"；"Fully open-source Complete transparency with code you can trust and verify. You are in control Empowering you with full control over your data and decisions."
- 判定：正確
- 說明：官網原文是「減少 95%」，站上寫「高達 95%」，語氣反而比較保守，可以接受。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-14　Covidence 多半由機構訂閱
- 位置：`docs/tool-directory.md:182`
- 站上寫法：「同類商業平台｜醫學領域常見，多半由機構訂閱」
- 原始出處：Covidence 首頁，<https://www.covidence.org/>
  - 原文："Check if your institution already has access to Covidence"；"Start a free trial"；"One licence Every discipline. Every review type."
- 判定：正確
- 說明：官網以機構授權為主，個人另有試用。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-15　Jupyter 支援 40 多種語言
- 位置：`docs/tool-directory.md:207`
- 站上寫法：「官網說明支援 Python、R 等 40 多種語言」
- 原始出處：Jupyter 首頁，<https://jupyter.org/>
  - 原文："Jupyter supports over 40 programming languages, including Python, R, Julia, and Scala."
- 判定：正確
- 說明：跟官網一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-16　RStudio：開源版免費、Desktop Pro 差在商業授權與支援、Posit AI 讀取變數與資料框
- 位置：`docs/tool-directory.md:208`
- 站上寫法：「由 Posit（前身為 RStudio, PBC）開發。開源版免費；付費的 RStudio Desktop Pro 差在商業授權與技術支援。另可付費加購 Posit AI，它會讀取你載入的變數與資料框」
- 原始出處：Posit RStudio 產品頁，<https://posit.co/products/open-source/rstudio/>
  - 原文："Open Source Edition The premier IDE for R Free"；"AGPL v3 license RStudio Desktop Pro A commercial license and priority support $1204.00 per year"；"A commercial license for organizations that cannot use AGPL software Priority email support with 8-hour response during business hours (ET) Posit Professional Drivers for database connectivity"
  - 原文："Posit Assistant lives inside RStudio with access to your loaded packages, variables, and data frames. … Available for $20/month with a free trial."
- 判定：正確
- 說明：大方向正確；Pro 版另外附 Posit Professional Drivers，站上沒提但不影響判斷。
- 建議改法：不需修改（想寫完整可以補「及資料庫驅動程式」）
- 查核日期：2026-10-23

#### TOOL-17　Tableau Public：任何人都能檢視與下載活頁簿；Desktop Public Edition 不能商用；Cloud／Server 要付費授權
- 位置：`docs/tool-directory.md:209`
- 站上寫法：「發布到 Tableau Public 的作品與資料不是私人的，任何人都能檢視，也能下載活頁簿與資料來源……Tableau Desktop Public Edition 可把活頁簿存在本機，但它僅限非商業用途；要連線 Tableau Cloud／Server 發布與分享內容，則需付費授權」
- 原始出處：Tableau Public FAQ，<https://help.tableau.com/current/pro/desktop/en-us/public_faq.htm>；Desktop 版本比較，<https://help.tableau.com/current/pro/desktop/en-us/desktop_comparison.htm>
  - 原文："By default, any Tableau Public viz as well as the underlying data can be downloaded by clicking the Download link … You can toggle off the ability to download the workbook and the underlying data set in the viz settings."
  - 原文："Anyone who knows (or stumbles across) the URL for the viz can see it, so be sure not to use this service for data that isn't meant for sharing."
  - 原文："Important : Tableau Desktop Public Edition is not for commercial use."；"Activating Tableau Desktop Professional Edition with a paid Tableau license allows individuals or businesses to: Connect to Tableau Server or Tableau Cloud Share and publish data and content"
- 判定：不精確
- 說明：「任何人都能檢視」與授權部分都正確；但「能下載活頁簿與資料」只是預設值，作者可以關掉。不過不要放私密資料的結論仍然成立。
- 建議改法：「……任何知道網址的人都能檢視；而且預設任何人都能下載活頁簿與底層資料（可在設定關閉，但關閉下載不等於資料變私人）」
- 查核日期：2026-10-23

#### TOOL-18　QuillBot 免費版與付費版的字數與模式差異
- 位置：`docs/tool-directory.md:226`
- 站上寫法：「免費版每次可改寫的字數與可用模式有限，付費版放寬字數並開放更多模式（依官方說明中心……2026-09-25 查證）」
- 原始出處：QuillBot Help Center 文章（站上連結）<https://help.quillbot.com/hc/en-us/articles/35855733045143-...>
  - 未取得原文：curl、WebFetch 都回 403（quillbot.com 首頁同樣 403）。WebSearch 只找到第三方評測（Scribbr、casrai 等），寫法是免費版 125 字、Standard／Fluency 兩種模式，付費版不限字數，但這些都不是官方原文。
- 判定：查不到
- 說明：沒辦法讀到官方頁，不能確認；第三方資料方向一致。
- 建議改法：暫不修改；維護者用瀏覽器開官方頁確認
- 查核日期：2026-10-23

#### TOOL-19　「AIS Senior Scholars' Basket」名稱
- 位置：`docs/tool-directory.md:152`
- 站上寫法：「資管領域常參考 AIS Senior Scholars' Basket」
- 原始出處：AIS 官網選單與頁面名稱，<https://aisnet.org/page/SeniorScholarListofPremierJournals>
  - 原文："Ranking Services Senior Scholars' List of Premier Journals"
- 判定：不精確
- 說明：AIS 現在的正式名稱是「Senior Scholars' List of Premier Journals」，「Basket」是舊稱（學界口語仍常用）。
- 建議改法：「AIS Senior Scholars' List of Premier Journals（舊稱 Senior Scholars' Basket）」
- 查核日期：2026-10-23

#### TOOL-20　三頁所有外部網址是否仍有效
- 位置：三頁全部連結（共 100 個；逐一檢查的清單與結果未納入 repo）
- 站上寫法：各工具官網與文件連結
- 原始出處：2026-10-23 用 curl（`-L`，瀏覽器 UA）逐一請求
  - 結果：多數回 200。回 403 的有 clarivate.com（WoS）、endnote.com、mendeley.com、jasp-stats.org、quillbot.com、scholarcy.com、scopus.com、ssrn.com、help.consensus.app、docs.consensus.app/consensus-mcp、所有 github.com／api.github.com，原因是 bot 防護或本環境代理。github 那幾個 repo 我改用 git 確認都存在；endnote.com、mendeley.com 用 WebFetch 可以讀到內容。`mcp.consensus.app/mcp`、`api.perplexity.ai/mcp` 回 401、`elicit.com/api/mcp` 回 405，是 MCP 端點本來就該有的反應（端點存在，要授權或要用 POST）。gpower.hhu.de 轉到 hhu.de 的新路徑，scopus.com 轉到 /pages/home，都還能用。
- 判定：正確
- 說明：沒有發現失效（404 或網域不存在）的連結。403 那幾個只能說無法自動確認，不代表失效。
- 建議改法：不需修改
- 查核日期：2026-10-23

---

### 二、docs/tools-knowledge.md

#### TOOL-21　Zotero：開源免費，雲端同步免費額度有限，可接 WebDAV
- 位置：`docs/tools-knowledge.md:35`
- 站上寫法：「開放原始碼、免費……雲端同步空間免費額度有限，可自行接 WebDAV 或自架儲存」
- 原始出處：Zotero Documentation〈Syncing〉，<https://www.zotero.org/support/sync>
  - 原文："Data syncing is free and unlimited, and it can be used without file syncing."；"Each Zotero user is given 300 MB of free Zotero Storage for attached files, with larger storage plans available for purchase."；"WebDAV is a standard protocol … it can be used to sync files in your personal library. (Group libraries cannot use WebDAV.)"
- 判定：正確
- 說明：可以補具體數字：檔案同步免費 300 MB，書目資料同步免費不限量；WebDAV 只能同步個人文獻庫。
- 建議改法：不需修改（想補充的話：「檔案同步免費 300 MB（書目資料同步不限量）；WebDAV 只適用個人文獻庫，不支援群組」）
- 查核日期：2026-10-23

#### TOOL-22　Mendeley 免費、內建 PDF 註記
- 位置：`docs/tools-knowledge.md:36`
- 站上寫法：「免費（Elsevier）｜內建 PDF 註記與閱讀器」
- 原始出處：Mendeley 首頁（WebFetch 取得），<https://www.mendeley.com/>
  - 原文："The free all-in-one reference manager."；"Enjoy 2GB of free storage"；"read, highlight and annotate — all from one place."
- 判定：正確
- 說明：「免費」與「PDF 註記」有官網原文支持。Elsevier 擁有 Mendeley 是公開事實，但這次抓到的首頁內容沒有寫到，這一點我沒有從首頁取得原文。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-23　EndNote「期刊投稿的樣式檔最齊全」
- 位置：`docs/tools-knowledge.md:37`
- 站上寫法：「台灣許多大學圖書館有校園授權；期刊投稿的樣式檔最齊全」
- 原始出處：EndNote Output Styles 頁（WebFetch 取得），<https://endnote.com/downloads/styles/>；Zotero Style Repository 資料檔 <https://www.zotero.org/styles-files/styles.json>
  - 原文（EndNote）："EndNote offers more than 6,000 bibliographic styles."（同頁列表顯示 "7613 results found"）
  - Zotero：styles.json 實際計數 10,868 筆（包含 dependent styles）
- 判定：不精確
- 說明：用數量比，Zotero／CSL 樣式庫比 EndNote 多，「最齊全」沒有根據。EndNote 另可個人購買（Buy 頁："Full license: $275"、"Student license: $150"，標示 "One-time purchase"），不一定綁學校。
- 建議改法：「台灣許多大學圖書館有校園授權；內建與可下載的期刊樣式很多（官網稱 6,000 種以上）」，並刪掉「最齊全」
- 查核日期：2026-10-23

#### TOOL-24　Zotero Connector 自動偵測機構代理，並詢問要不要記住
- 位置：`docs/tools-knowledge.md:69`
- 站上寫法：「偵測到你正透過機構代理造訪某個網站時，會跳出提示問你要不要記住這個代理設定，同意之後之後造訪同一網域會自動幫你轉走代理登入流程」
- 原始出處：Zotero Documentation〈Zotero Connector Preferences〉（Last updated 2025-07-02），<https://www.zotero.org/support/connector_preferences>
  - 原文："When it detects that you are using an institutional proxy to access a particular site, it will ask if you want to remember it in the future. If you agree, Zotero will automatically use the proxy for matching URLs in the future."；"Zotero proxy redirection is not available in Safari."
- 判定：正確
- 說明：跟官方一致。可以補一句 Safari 不支援。
- 建議改法：不需修改（想補充的話：「Safari 不支援這項代理轉址」）
- 查核日期：2026-10-23

#### TOOL-25　DOI 自動找全文：VPN 抓得到訂閱 PDF，網頁代理只保證抓 OA
- 位置：`docs/tools-knowledge.md:71-72`
- 站上寫法：「用 Zotero 的『以識別碼新增項目』或『Find Available PDF』……如果你是 VPN 連線，能抓到有訂閱權限的全文；如果是網頁代理登入，這個自動抓取功能只保證抓得到公開取用（open access）的全文」
- 原始出處：Zotero Blog〈Improved PDF retrieval with Unpaywall integration〉（2018-10-09），<https://www.zotero.org/blog/improved-pdf-retrieval-with-unpaywall-integration/>
  - 原文："When you use "Add Item by Identifier" or "Find Available PDF","；"Zotero will load the page associated with the item's DOI or URL and try to find a PDF to download"；"This will work if you have direct or VPN-based access to the PDF."；"If you use a web-based proxy, only open-access PDFs will be automatically retrieved using this new functionality,"；"but you can continue to save items with gated PDFs from the browser using the Zotero Connector."
- 判定：正確
- 說明：跟官方部落格一致。（這段正好跟下面 TOOL-30 的警告框互相矛盾。）
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-26　Zotero Connector「點一下按鈕就把目前網站存進資料庫」
- 位置：`docs/tools-knowledge.md:86-88`
- 站上寫法：「官方文件的說法是『點一下按鈕就會把目前開啟的網站存進你的 Zotero 資料庫』」
- 原始出處：Zotero Documentation〈Zotero Connector〉，<https://www.zotero.org/support/connector>；〈Adding Items to Zotero〉
  - 原文："Clicking the button will save the currently open website into your Zotero library. The saving workflow has three steps: Select a collection in Zotero … Click the Connector button … The item is saved into your library"
  - 原文："The Save to Zotero button will usually save high-quality metadata and also automatically download the relevant PDF if you have access to it."
- 判定：正確
- 說明：引文翻譯正確。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-27　Better BibTeX 的「官方定位」與兩個核心價值
- 位置：`docs/tools-knowledge.md:93-96`；`docs/tools-knowledge.md:641`
- 站上寫法：「官方定位是『改善 BibTeX／biber 匯出功能』」「官方文件明講『Zotero 的 key 不一定適合 bibtex/biber 使用』」「資料庫更新時自動即時匯出一份 `.bib`」
- 原始出處：BBT 官方文件原始檔（repo `retorquere/zotero-better-bibtex`，commit 83e7f67，2026-10-22）`site/content/_index.md`、`installation/_index.md`、`exporting/auto.md`；<https://retorque.re/zotero-better-bibtex/>
  - 原文（首頁）："Better BibTeX (BBT) is an extension for Zotero and (in principle) Juris-M that makes it easier to manage bibliographic data, especially for people authoring documents using text-based toolchains (e.g. based on LaTeX / Markdown)."
  - 原文（安裝頁）："the default setting of BBT will generate different citekeys than Zotero would itself generate; the keys from Zotero are not always safe for use in bibtex/biber."
  - 原文（自動匯出）："checking the `Keep updated` option will register the export for automation. After you've completed the current export, any changes to the collection or library will trigger an automatic re-export to update the file."
- 判定：不精確
- 說明：「Zotero 的 key 不一定適合 bibtex/biber」引用正確；但「改善 BibTeX／biber 匯出功能」不是官方原文，官方說的是「讓用文字工具鏈（LaTeX／Markdown）寫作的人更容易管理書目資料」。另外自動匯出不是預設就有，匯出時要勾「Keep updated」。
- 建議改法：「官方自述是讓用 LaTeX／Markdown 等文字工具寫作的人更容易管理書目資料」；第二點改成「匯出時勾選 **Keep updated**，之後資料庫一有變動就會自動重新匯出 `.bib`……」
- 查核日期：2026-10-23

#### TOOL-28　Better BibTeX 安裝步驟
- 位置：`docs/tools-knowledge.md:98-103`；`docs/thesis-notes-template.md:118`、`:120`
- 站上寫法：「到 GitHub Releases 頁下載最新版的 `.xpi`（用 Firefox 時要用右鍵另存……）→ 工具 → 外掛程式 → 齒輪 →『從檔案安裝外掛程式（Install Plugin From File）』→ 選 `.xpi`，之後 BBT 會自動更新」
- 原始出處：BBT `site/content/installation/_index.md`；Zotero Documentation〈Plugins〉（Last updated 2026-05-05），<https://www.zotero.org/support/plugins>
  - 原文（BBT）："if you use Firefox, make sure to right-click and save the XPI file, not just clicking it"；"1. In the main menu go to Tools > Plugins … 3. Click on the gear in the top-right corner and choose 'Install Plugin From File...' 4. Choose .xpi that you've just downloaded, click 'Install'"；"After the initial installation, the plugin will auto-update to newer releases"
  - 原文（Zotero）："in Zotero, go to "Tools → Plugins" and drag the .xpi onto the Plugins window."
  - 版本資訊：GitHub 最新 release 是 v9.0.71（頁面顯示 "07 Oct"）；package.json 標示 `"minVersion": "8.0.1"`、`"maxVersion": "11.*"`；README："**Zotero 7 is no longer supported**. BBT 8.0.25 still works on 7.0.32, but will not receive further updates."；目前 Zotero 是 10.0.6（官方 changelog："Changes in 10.0.6 (October 7, 2026)"）
- 判定：正確
- 說明：步驟跟官方一致，目前的 Zotero 10 也適用。可以補提醒：最新版 BBT 需要 Zotero 8 以上，還在用 Zotero 7 的人要先升級。
- 建議改法：不需修改（想補充的話：「最新版 BBT 需 Zotero 8 以上」）
- 查核日期：2026-10-23

#### TOOL-29　「以識別碼新增項目」支援的識別碼與分隔方式
- 位置：`docs/tools-knowledge.md:107`
- 站上寫法：「支援的識別碼包括 DOI、ISBN、PubMed ID、arXiv ID、ADS Bibcode；要一次匯入多筆，識別碼之間用空格、逗號或換行分隔即可」
- 原始出處：Zotero Documentation〈Adding Items to Zotero〉，<https://www.zotero.org/support/adding_items_to_zotero>
  - 原文："You can quickly add items to your library if you already know their ISBN, DOI, PubMed ID, arXiv ID, or ADS Bibcode. … To add more than one item, separate identifiers by spaces, commas, or line breaks."
- 判定：正確
- 說明：完全一致。
- 建議改法：不需修改

#### TOOL-30　警告框：「以識別碼新增項目通常不會附全文 PDF，官方沒有把它跟自動下載 PDF 綁在一起」
- 位置：`docs/tools-knowledge.md:109-110`
- 站上寫法：「『以識別碼新增項目』查到的是書目資料庫……裡的中繼資料，不是期刊頁面本身，所以官方文件並沒有把它跟自動下載 PDF 綁在一起……用 DOI 打進書目之後，PDF 全文多半還是要……自己下載」
- 原始出處：Zotero Blog〈Improved PDF retrieval with Unpaywall integration〉，<https://www.zotero.org/blog/improved-pdf-retrieval-with-unpaywall-integration/>
  - 原文："When you use "Add Item by Identifier" or "Find Available PDF","；"Zotero will load the page associated with the item's DOI or URL and try to find a PDF to download"；"This will work if you have direct or VPN-based access to the PDF."
- 判定：錯誤
- 說明：Zotero 官方明白寫了「以識別碼新增項目」會去載入 DOI 對應的頁面並嘗試下載 PDF：在校內或 VPN 下可以抓到訂閱全文，用網頁代理時只抓得到 OA。站上「官方沒有綁在一起」的說法跟官方矛盾，也跟同頁 2.3.1 的 note 框（TOOL-25，寫法正確）互相打架。（我重讀過部落格原文，確認沒有看錯。）
- 建議改法：把警告框改成「**用網頁代理時，這樣匯入通常只附得到 OA 全文**」，內文寫：「以識別碼新增項目時，Zotero 會依 DOI 去找出版社頁面並嘗試下載 PDF，在校內網路或 VPN 下可以抓到有訂閱權限的全文；如果你是用圖書館網頁代理，只會自動抓到公開取用（OA）的版本，其他全文要回到已登入代理的期刊頁面用 Zotero Connector 存。」
- 查核日期：2026-10-23

#### TOOL-31　2.3.6 日期解析的機制：解析綁介面語言、英文介面不認得「年月日」、BBT 的 `year` 取 Zotero 解析好的值、年份會變空
- 位置：`docs/tools-knowledge.md:114-118`（修法在 :120）
- 站上寫法：「這個解析器認得的日期寫法，綁定在你目前 Zotero 介面設定的語言（locale）上……中文介面才認得『年』『月』『日』這種寫法」「介面設成英文卻打中文格式的日期（例如『2024年5月1日』）……Zotero 解析不出結構化的年份」「`year` 這個函式抓的是『出版年份』這個已經解析好的值，不是它自己重新去猜你輸入的原始字串……這裡年份那一段就是空的」
- 原始出處：
  1. Zotero 日期解析器原始碼 `zotero/utilities` 的 `date.js`（`strToDate`），<https://github.com/zotero/utilities/blob/master/date.js>
     - 原文（程式碼）：`var _slashRe = /^(.*?)\b([0-9]{1,4})(?:([\-\/\.年])([0-9]{1,2}))?(?:([\-\/\.月])([0-9]{1,4}))?((?:\b|[^0-9]).*?)$/`；`(m[3] == "年" && m[5] == "月")`；`if(m[2].length == 3 || m[2].length == 4 || m[3] == "年") { // ISO 8601 style date (big endian)`
     - （年＝「年」，月＝「月」：寫死在正規式裡，跟介面語言無關。）
     - 實測：把這支官方 date.js 拿到 node 跑，`Zotero.locale` 設 en-US 時，`strToDate("2024年5月1日")` 得到 `{"order":"ymd","year":"2024","month":4,"day":1}`，zh-TW 的結果一樣。
  2. Better BibTeX 原始碼（commit 83e7f67，2026-10-22）`content/key-manager/formatter.ts`
     - 原文（程式碼）：`this.date = parseDate(this.getField('date') as string, …)`；`/** The year of the publication */ public $year(): string { return this.padYear(this.format_date(this.item.date, '%-Y'), 2) }`
     - 原文（Zotero `item.js`）：`if (!unformatted) { // Multipart date fields … value = Zotero.Date.multipartToStr(value);`（也就是交給 BBT 的是使用者輸入的原始字串）
     - 實測：把 BBT 的 `content/dateparser.ts` 用 esbuild 打包後執行，`"2024年5月1日"`、`"2024年5月"`、`"2024年"` 都得到 `{"type":"verbatim","verbatim":"2024年5月1日"}` 這類結果；`"2024-05-01"` → `{"type":"date","year":2024,"month":5,"day":1}`；`"2024"` → `{"type":"date","year":2024}`。BBT 的解析器不讀介面語言。
     - 原文（程式碼，verbatim 的處理）：`case 'verbatim': Object.assign(parsed, { [`${prefix}Y`]: dp.verbatim, …`
- 判定：錯誤
- 說明：站上的三層機制都跟原始碼不符。(1) Zotero 自己的解析器在任何介面語言下都認得「2024年5月1日」，不是英文介面才失敗。(2) BBT 的 `year` 不用 Zotero 解析好的年份，而是自己重新解析原始字串。(3) BBT 解析器不認得「年／月／日」，會把整串當 verbatim；`year` 那一段因此塞進整串原文「2024年5月1日」，不是變成空的。改用中文介面也解決不了。結論「一律填 `YYYY-MM-DD` 或 `YYYY`」仍然正確，而且更有必要。（兩支解析器都重跑過一次確認。附註：Zotero 實測用的月份對照表是我自己做的簡化版，不影響「年月」分支的判定，那段邏輯不讀月份表。）另外「Zotero 論壇與官方說明一致建議」這句，我在 Zotero 官方文件裡沒找到相應原文。
- 建議改法：把三層原理改寫成：「Better BibTeX 產生 citekey 時，`year` 是 BBT 拿日期欄位的**原始文字**自己重新解析，跟 Zotero 介面語言無關。BBT 認得 `2024-05-01`、`2024`、`May 1, 2024`、`5/1/2024` 這類寫法，但**不認得『2024年5月1日』『民國113年』這種中文寫法**，會把整串原文直接塞進 key 的年份位置，key 就會亂掉。」修法段保留，刪掉「這也是 Zotero 論壇與官方說明一致建議的填法」，或改附可查的出處。
- 查核日期：2026-10-23（以當日 BBT 與 zotero/utilities 主線原始碼為準）

#### TOOL-32　BBT 預設公式、重複時加 a/b/c 字尾、右鍵「Refresh BibTeX Key」
- 位置：`docs/tools-knowledge.md:118`、`:120`；`docs/thesis-notes-template.md:74`
- 站上寫法：「官方文件所舉的預設公式範例是 `auth.lower + shorttitle(3,3) + year`」「偵測到 key 重複時會自動加字尾（a、b、c……）」「右鍵→Better BibTeX→**Refresh BibTeX Key**，重新產生 citekey」
- 原始出處：BBT `site/content/citing/_index.md`；BBT 介面字串 `locale/en-US/better-bibtex.ftl`（commit 83e7f67）
  - 原文："The default key pattern is `auth.lower + shorttitle(3,3) + year`"；"a letter postfix (a, b, c, etc) in case of a clash (this part is always added, you can't disable it, although you can change it to Zotero-style numeric)"
  - 原文："existing keys are not automatically regenerated when you change the pattern. If you want your keys to update after a pattern change you will have to select your items, right-click, and select `Refresh`."
  - 原文（介面字串）：`better-bibtex_zotero-pane_citekey_refresh = .label = Regenerate BibTeX key`
- 判定：不精確
- 說明：公式與字尾正確；但目前 BBT 9.x 右鍵選單的實際名稱是「Regenerate BibTeX key」，找不到「Refresh BibTeX Key」，照站上的字找會卡住。（官方文件內文還寫 `Refresh`，文件和介面不一致。）
- 建議改法：「右鍵 → Better BibTeX → **Regenerate BibTeX key**（舊版或官方文件稱 Refresh）」
- 查核日期：2026-10-23

#### TOOL-33　Word 外掛在首次啟動 Zotero 時自動安裝
- 位置：`docs/tools-knowledge.md:127`
- 站上寫法：「首次啟動 Zotero 時，應該會自動幫每個支援的文書處理器裝好外掛」
- 原始出處：Zotero Documentation〈Word Processor Plugin Installation〉（Last updated 2025-01-12），<https://www.zotero.org/support/word_processor_plugin_installation>
  - 原文："The word processor plugins are bundled with Zotero and should be installed automatically for each supported word processor on your computer when you first start Zotero."
- 判定：正確
- 說明：翻譯忠實。
- 建議改法：不需修改

#### TOOL-34　Word 的 Zotero 分頁：Add/Edit Citation、Add/Edit Bibliography、Document Preferences；書目自動更新；引用語言整份文件一起設定
- 位置：`docs/tools-knowledge.md:127-131`、`:150`
- 站上寫法：「Word 功能區會多一個『Zotero』分頁……Add/Edit Bibliography……之後每插入一筆新引用，這份清單會自動更新」「引用語言是整份文件一起設定」
- 原始出處：Zotero Documentation〈Using the Zotero Word Plugin〉，<https://www.zotero.org/support/word_processor_plugin_usage>
  - 原文："Installing the Zotero Word plugin adds a Zotero tab to Microsoft Word."；"Add/Edit Citation Add a new citation or edit an existing citation in your document at the cursor location."；"As you use the plugin, Zotero will automatically update the bibliography based on the citations in the document."；"The "Document Preferences" window lets you set the following document-specific preferences: The citation style . The language to use to format citations and bibliography."
- 判定：正確
- 說明：都對得上。「第一次使用會先跳出 Document Preferences」這點官方使用頁沒有明寫，但這是實際行為，不影響判定。
- 建議改法：不需修改

#### TOOL-35　Unlink Citations 不可逆，做之前先備份
- 位置：`docs/tools-knowledge.md:134`
- 站上寫法：「這個動作官方文件明講不可逆，做之前先另存一份備份（[官方說明](https://www.zotero.org/support/kb/unlinking_citations)）」
- 原始出處：〈Using the Zotero Word Plugin〉；〈How do I unlink all Zotero citations in a document?〉（Last updated 2023-05-27），<https://www.zotero.org/support/kb/unlinking_citations>
  - 原文（使用頁）："Note that removing field codes is irreversible , and should usually only be done in a final copy of your document."
  - 原文（kb 頁）："Always unlink citations in a copy of the document. Keep the original version of the document with active Zotero citations"
- 判定：正確
- 說明：內容正確。「不可逆」這句出自使用說明頁，站上連到的 kb 頁講的是「要在副本上做」；兩頁合起來支持站上寫法。
- 建議改法：不需修改（可以把「不可逆」的出處改成 word_processor_plugin_usage）

#### TOOL-36　作者欄：人名兩欄、機構單欄
- 位置：`docs/tools-knowledge.md:138`
- 站上寫法：「官方說明的建議是人名用兩欄、機構名用單欄，作者欄右側的按鈕可以切換」
- 原始出處：〈Adding Items to Zotero〉，<https://www.zotero.org/support/adding_items_to_zotero>
  - 原文："Each name field can be toggled between single and two field mode by clicking the "Switch to single field" / "Switch to two fields" buttons at the end of the creator field. Single field mode should be used to institutions … while two field mode (last name, first name) should be used for personal names."
- 判定：正確
- 說明：一致。
- 建議改法：不需修改

#### TOOL-37　中文作者兩欄／單欄的 APA 7 輸出、et al.／「等」
- 位置：`docs/tools-knowledge.md:140-150`
- 站上寫法：表格「兩欄 → (王, 2022)／王小明. (2022).；單欄 → (王小明, 2022)／王小明. (2022).」；「三位以上的中文作者也會印成『et al.』，例如『(王小明 et al., 2024)』。引用語言改成繁體中文會印『等』……英文文獻也會跟著印成『(Smith等, 2021)』」
- 原始出處：自行重跑。citeproc-js 2.4.63（npm `citeproc`）＋官方 CSL repo 的 `apa.csl`（"APA Style 7th edition"，updated 2026-02-07）＋ `locales-en-US.xml`、`locales-zh-TW.xml`
  - 實際輸出（en-US）：`(王, 2022)`、`(王小明, 2022)`、`(王小明 et al., 2024)`；書目：`王小明. (2022). 測試. 期刊.`
  - 實際輸出（zh-TW）：`(王小明等, 2024)`、`(Smith等, 2021)`
- 判定：正確
- 說明：結果跟站上表格完全一致。附註：Zotero 內建的 citeproc-js 版本可能和 npm 版略有不同，但這部分邏輯沒有差異。
- 建議改法：不需修改

#### TOOL-38　語言欄填 `zh-TW`，影響標題大小寫轉換
- 位置：`docs/tools-knowledge.md:152`
- 站上寫法：「中文文獻填 `zh-TW`。官方說明建議填 ISO 語言碼，這一欄會決定引用樣式要不要把標題轉成英文的大小寫規則」
- 原始出處：〈Item Types and Fields〉，<https://www.zotero.org/support/kb/item_types_and_fields>
  - 原文："We recommend storing these as two letter ISO language codes followed by two letter ISO country codes (e.g., en-US for American English, or de-DE for German)."；"The Language field is used to determine whether English Title Casing rules should be applied when formatting item titles."
- 判定：正確
- 說明：一致。
- 建議改法：不需修改

#### TOOL-39　Webster & Watson (2002) 書目
- 位置：`docs/tools-knowledge.md:183`
- 站上寫法：「Webster, J., & Watson, R. T. (2002). Analyzing the Past to Prepare for the Future: Writing a Literature Review. *MIS Quarterly*, 26(2), xiii–xxiii. <https://aisel.aisnet.org/misq/vol26/iss2/3/>」
- 原始出處：Crossref `10.2307/4132319`；AIS eLibrary 頁
  - Crossref 回傳：title "Analyzing the Past to Prepare for the Future: Writing a Literature Review"；container "MIS Quarterly"；volume 26；issue 2；page "xiii-xxiii"；2002；authors Webster, Watson
  - `https://doi.org/10.2307/4132319` → 302 到 misq.umn.edu 的文章頁
- 判定：不精確
- 說明：作者、年份、篇名、刊名、卷期、頁碼全部正確，AIS 網址也有效；但這篇有 DOI，APA 7 規定有 DOI 時要列 DOI。另外 APA 7 期刊文章篇名用句首大寫（sentence case），站上用的是標題式大寫。
- 建議改法：「Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare for the future: Writing a literature review. *MIS Quarterly*, *26*(2), xiii–xxiii. https://doi.org/10.2307/4132319」

#### TOOL-40　Logseq「本機的 Markdown／Org 檔」
- 位置：`docs/tools-knowledge.md:165`
- 站上寫法：「**Logseq**｜本機的 Markdown／Org 檔」
- 原始出處：Logseq 官方 GitHub tags（`git ls-remote`：目前有 `2.0.1`、`2.0.2`）；Logseq 官方論壇公告〈What's New with Logseq DB - May 16th 2026〉，<https://discuss.logseq.com/t/whats-new-with-logseq-db-may-16th-2026/35020>
  - 原文："Logseq's DB graphs live in SQLite."；"Logseq writes a plain markdown projection of your blocks to a folder on disk"；"It's opt-in per graph."；"Logseq is splitting into two versions"
- 判定：不精確
- 說明：Logseq 2.0 的 DB 版把資料存在 SQLite，Markdown 只是選用的單向鏡像；舊的檔案版（Markdown／Org）仍然存在。站上這句只描述了舊版，用在「資料能不能拿得出來」的判準上會誤導。
- 建議改法：「本機 Markdown／Org 檔（舊版檔案圖譜）；2.0 起的 DB 版改存 SQLite，Markdown 匯出是選用的單向鏡像」
- 查核日期：2026-10-23

#### TOOL-41　方法筆記範例門檻：HTMT < 0.85、VIF < 3
- 位置：`docs/tools-knowledge.md:590`
- 站上寫法：「（例如：區別效度 HTMT < 0.85、共線性 VIF < 3；**門檻依領域與期刊而異，引用前查最新來源**）」
- 原始出處：Henseler, Ringle, & Sarstedt (2015), *Journal of the Academy of Marketing Science*, 43(1), 115–135, <https://doi.org/10.1007/s11747-014-0403-8>（全文，CC BY 4.0；彙整時由 STAT 節改從 link.springer.com 取得 PDF）；SmartPLS 官方門檻頁 <https://smartpls.com/documentation/functionalities/thresholds/>
  - 原文（Henseler et al., 2015）："Some authors suggest a threshold of 0.85 (Clark and Watson 1995; Kline 2011), whereas others propose a value of 0.90 (Gold et al. 2001; Teo et al. 2008)."
  - 原文（SmartPLS）："VIF values of 3.00 or lower indicate that collinearity among indicators or predictor constructs is not a critical issue; values above 5.00 indicate critical collinearity problems."
- 判定：正確
- 說明：TOOL 節查核時因 Springer 擋爬蟲判「查不到」；彙整時以 STAT-06、STAT-08 取得的原文補查。範例取的是較嚴格的門檻，加上站上自己的但書，作為筆記範例沒有問題。0.85 與 0.90 的選擇條件見 STAT-06。
- 建議改法：可補出處「（Henseler et al., 2015；Hair et al., 2019）」。

---

### 三、docs/thesis-notes-template.md

#### TOOL-42　範本的文獻矩陣用核心外掛 Bases，Obsidian 太舊會打不開
- 位置：`docs/thesis-notes-template.md:35`
- 站上寫法：「範本不需要裝任何 Obsidian 外掛。文獻矩陣用的是核心外掛 Bases，Obsidian 版本太舊會打不開」
- 原始出處：Obsidian Changelog 1.9.0（2025-05-21），<https://obsidian.md/changelog/2025-05-21-desktop-v1.9.0/>；範本 repo `.obsidian/core-plugins.json`
  - 原文："1.9.0 Desktop catalyst Introducing Bases , a new core plugin that lets you turn any set of notes into a powerful database."；"To support Bases, we're introducing the .base file format"
  - repo：`"bases": true`；`.gitignore` 排除 `.obsidian/community-plugins.json` 與 `.obsidian/plugins/`
- 判定：正確
- 說明：Bases 是 1.9.0 起的核心外掛；目前 Obsidian 正式版是 1.14.5（obsidian-releases `desktop-releases.json`）。
- 建議改法：不需修改（想寫具體的話：「需 Obsidian 1.9 以上」）
- 查核日期：2026-10-23

#### TOOL-43　Zotero Integration：最新版 3.2.1 停在 2024-08，repo 已轉到 `community-archive`
- 位置：`docs/thesis-notes-template.md:39`
- 站上寫法：「最新版 3.2.1 停在 2024-08，原作者的 repo 已轉到 `community-archive` 組織」
- 原始出處：GitHub repo `community-archive/obsidian-zotero-integration`（從 mgmeyers/ 和 obsidian-community/ 進去都指到同一個 HEAD 2043211）
  - 原文（git tags）：`3.2.1 2024-08-11`、`3.2.0 2024-08-10`；commit log："Sun Aug 11 08:47:30 2024 -0700 3.2.1"，之後只有 "Fri Mar 6 09:39:35 2026 -0800 Remove funding"
  - WebFetch：repo 頁標示 "community-archive/obsidian-zotero-integration"；Obsidian 外掛登錄檔 `community-plugins.json` 的 author 是 "Obsidian Community Archive"
- 判定：正確
- 說明：版本、日期、移轉都對。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-44　Citations 外掛：最新版 0.4.5 停在 2022-09
- 位置：`docs/thesis-notes-template.md:40`
- 站上寫法：「Citations：最新版 0.4.5 停在 2022-09」
- 原始出處：GitHub repo `hans/obsidian-citation-plugin`
  - 原文（git tags）：`0.4.5 2022-09-24`；HEAD 日期 "Sat Sep 24 11:20:13 2022 -0400"
- 判定：正確
- 說明：一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-45　ZotLit：2.1.4（2026-09）、需要另裝 Zotero companion 外掛、AGPL-3.0
- 位置：`docs/thesis-notes-template.md:41`
- 站上寫法：「ZotLit：還在更新（2.1.4，2026-09），需要另外在 Zotero 裝它的 companion 外掛；授權是 AGPL-3.0」
- 原始出處：GitHub repo `aidenlx/zotlit`（README、manifest.json、LICENSE、tags）
  - 原文（tags）：`2.1.4 2026-09-12`；另有 beta `2.2.0-beta.4 2026-10-20`
  - 原文（LICENSE）："GNU AFFERO GENERAL PUBLIC LICENSE Version 3"
  - 原文（README）："**Live updates** | Push changes from Zotero to Obsidian as they happen. *Requires the companion.*"；"ZotLit reads your Zotero database directly … It reads only and does not write to your Zotero database."；"ZotLit needs Obsidian 1.13.4 or newer, and the **installer version** must also be 1.13.4 or newer."
- 判定：不精確
- 說明：版本、日期、授權都對；但 v2 的 companion 只有「Live updates」才需要，建筆記、插引用、讀註記都是直接讀 Zotero 資料庫，不需要 companion。另外 v2 要求 Obsidian 安裝程式本身也是 1.13.4 以上，這是常見的載入失敗原因，值得一提。
- 建議改法：「ZotLit：還在更新（2.1.4，2026-09），直接讀 Zotero 資料庫；想要 Zotero 變動即時推送才需要另裝它的 companion 外掛。需 Obsidian 1.13.4 以上（安裝程式版本也要）；授權是 AGPL-3.0」
- 查核日期：2026-10-23

#### TOOL-46　安裝提示詞裡的 winget／brew 套件名稱與 PyMuPDF
- 位置：`docs/thesis-notes-template.md:113-116`
- 站上寫法：「Zotero（winget：DigitalScholar.Zotero；brew：--cask zotero）」「Obsidian（winget：Obsidian.Obsidian；brew：--cask obsidian）」「Python 3（已經有 3.9 以上就跳過；winget：Python.Python.3.12；brew：python）」「python -m pip install pymupdf」
- 原始出處：microsoft/winget-pkgs（HEAD 2026-10-23）目錄；Homebrew API <https://formulae.brew.sh/api/>；PyPI <https://pypi.org/pypi/pymupdf/json>
  - winget：`manifests/d/DigitalScholar/Zotero/10.0.6`、`manifests/o/Obsidian/Obsidian/1.14.4`、`manifests/p/Python/Python/3/12/…` 都存在
  - Homebrew：cask `zotero` 10.0.6、cask `obsidian` 1.14.5；`python` 是 `python@3.15` 的 alias（"aliases": ['python', 'python3', 'python@3']）
  - PyPI：`pymupdf` 最新版 2.0（2026-10-19），requires_python `>=3.11`；1.26.5 是最後一版支援 `>=3.9`，1.26.6 起是 `>=3.10`
- 判定：正確
- 說明：套件 ID 都有效。小提醒：PyMuPDF 最新版要 Python 3.11 以上；用 3.9／3.10 的人，pip 會自動退回裝舊版，仍然能用，但 3.9 已經停止維護。
- 建議改法：不需修改（可以考慮把「3.9 以上」改成「3.11 以上」，讓使用者裝到最新版 PyMuPDF）
- 查核日期：2026-10-23

#### TOOL-47　Zotero 設定位置、BBT 的 Citation keys 分頁與「Citation key formula」、Connector 下載網址
- 位置：`docs/thesis-notes-template.md:120-122`
- 站上寫法：「選『工具 → 外掛程式』，點右上角齒輪的『從檔案安裝外掛程式』」「開 Zotero 的設定（Windows 在『編輯 → 設定』，Mac 在『Zotero → 設定』），到 Better BibTeX 的 Citation keys 分頁，把 Citation key formula 改成 auth.capitalize + year」「https://www.zotero.org/download/connectors」
- 原始出處：Zotero Documentation〈Preferences〉，<https://www.zotero.org/support/preferences>；BBT `locale/en-US/better-bibtex.ftl`；網址實測
  - 原文："Open the preferences by clicking "Edit → Settings" (Windows/Linux) or "Zotero → Settings" (Mac)."
  - 原文（介面字串）：`better-bibtex_preferences_tab_citekey = Citation keys`；`better-bibtex_preferences_citekey_format = Citation key formula`
  - `https://www.zotero.org/download/connectors` → 200
- 判定：正確
- 說明：選單路徑與介面名稱一致。
- 建議改法：不需修改

#### TOOL-48　BBT JSON-RPC：`http://127.0.0.1:23119/better-bibtex/json-rpc`、`api.ready` 回傳版本、`item.search`、`item.attachments` 的 `path`
- 位置：`docs/thesis-notes-template.md:124`、`:188-191`、`:101`
- 站上寫法：「用 Python 的 urllib 對 http://127.0.0.1:23119/better-bibtex/json-rpc 送 POST，內容是 {"jsonrpc":"2.0","method":"api.ready","params":[]}。回傳裡有 betterbibtex 的版本號」「送 {"jsonrpc":"2.0","method":"item.search","params":[""]}」「送 {"jsonrpc":"2.0","method":"item.attachments","params":["{citekey}"]}，回傳裡副檔名是 .pdf 的 path 就是 Zotero 裡的 PDF」
- 原始出處：BBT 文件〈JSON-RPC〉，<https://retorque.re/zotero-better-bibtex/exporting/json-rpc/>；BBT 原始碼 `content/json-rpc.ts`（commit 83e7f67）
  - 原文（文件）："on the URL http://localhost:23119/better-bibtex/json-rpc"；"**api.ready**() … returns: { betterbibtex: string; zotero: string } … Returns the Zotero and BetterBibTeX version to show the JSON-RPC API is ready."；"**item.attachments**(citekey: string, library?: string | number) … List attachments for an item with the given citekey"
  - 原文（程式碼）：`const data: Record<string, any> = { open: `zotero://open-pdf/…`, path: att.getFilePath(), }`
  - 原文（程式碼，item.search）：`if (!terms.length) { // empty string or empty array }` 之後才有 `else if (typeof terms === 'string') { … // Do not list attachments search.addCondition('itemType', 'isNot', 'attachment')`
- 判定：正確
- 說明：端點、方法名與回傳欄位都對（127.0.0.1 跟 localhost 等價）；`path` 欄位官方文件沒寫，是從原始碼確認的。小細節：`item.search` 傳空字串時會跳過「排除附件」與「排除 feed」的條件，回傳結果可能包含附件或筆記項目，AI 列清單時要依 citekey 篩過；站上實測寫「通過」，可以不改。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-49　範本 repo 的結構描述（八個資料夾、7 份模板、`_text/` 在 .gitignore、頁面提示詞與 repo 內容相同）
- 位置：`docs/thesis-notes-template.md:47-58`、`:99`、`:101`、`:129`
- 站上寫法：「`07_模板`｜理論、變數、文獻筆記三型、假說推演、方法，共 7 份」「`_text/`，這個資料夾已經寫進 `.gitignore`」「下面跟 repo 裡的 `00_總覽/prompt.md` 內容相同」「`00_總覽` 到 `07_模板` 八個資料夾」
- 原始出處：`git clone https://github.com/wayhong0928/thesis-notes-template`（HEAD 9cf3783，2026-10-15）
  - 目錄：00_總覽、01_理論、02_變數、03_文獻筆記、04_論文草稿、05_假設推演、06_方法、07_模板；07_模板 內有 01_理論、02_變數、03_文獻筆記_實證型／方法型／理論型、05_假設推演、06_方法，共 7 個檔
  - `.gitignore` 原文："_text/"
  - 用腳本比對頁面上 11 個 ```text 區塊與 repo 的 `prompt.md`：完全相同
- 判定：正確
- 說明：結構描述與實際 repo 一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### TOOL-50　試跑結果：Davis（1989）原文同一相關係數摘要／表 8 寫 .59、討論段寫 .69
- 位置：`docs/thesis-notes-template.md:312`
- 站上寫法：「同一個相關係數，摘要和表 8 寫 .59、討論段寫 .69；另一個相關係數，內文標 p<.001、表 8 標 **」
- 原始出處：Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319–340. https://doi.org/10.2307/249008
  - 未取得全文：MISQ／JSTOR 要付費，沒取得 PDF，無法核對表 8 與討論段的數字。
- 判定：查不到
- 說明：這是站上對原論文內容的具體宣稱，需要有原文 PDF 的人核對。
- 建議改法：暫不修改；建議站主在頁面上補頁碼（例如「摘要 p. 319、表 8 p. XXX、討論 p. XXX」），讓讀者能自己查

---

### 小計

- 查核條數：50
- 正確：34（TOOL-01、03、05、06、07、09、11、12、13、14、15、16、20、21、22、24、25、26、28、29、33、34、35、36、37、38、41、42、43、44、46、47、48、49）
- 不精確：12
- 錯誤：2
- 查不到：2（TOOL-18、TOOL-50）（TOOL-41 原判查不到，彙整時以 STAT 節取得的 Henseler 2015 全文改判正確）

- 「錯誤」代號：TOOL-30、TOOL-31
- 「不精確」代號：TOOL-02、TOOL-04、TOOL-08、TOOL-10、TOOL-17、TOOL-19、TOOL-23、TOOL-27、TOOL-32、TOOL-39、TOOL-40、TOOL-45

---

## 八、AI：AI 工具與流程

查核範圍：docs/ai-tools.md、ai-workflow.md、ai-workflow-map.md、ai-quickstart.md、ai-quickstart-agent.md、ai-case-study.md、prompts.md、claude-tools-overview.md、ai-agents.md、harness.md、skill-build.md。
其中 claude-tools-overview.md、ai-agents.md、harness.md、skill-build.md 都是遷移後的導引頁，可查證的主張只有 claude-tools-overview.md 的「Pro／Max 內含 Claude Code」一條（併入 AI-20）。ai-quickstart.md 第七節的「示範研究 A/B/C」是虛構練習，沒有查。

取得原文的方式：
- code.claude.com、learn.chatgpt.com、claude.com/docs、github.com 的 README：用 WebFetch 讀取，引文是工具從頁面擷取的原句。
- support.claude.com、support.google.com、workspaceupdates.googleblog.com、prisma-statement.org、arxiv.org、raw.githubusercontent.com：用 curl 直接下載 HTML 再轉純文字，引文是逐字原文。
- help.openai.com 直接連線回 403（Cloudflare 擋），改透過 r.jina.ai 的網頁轉文字服務取得同一頁全文（頁首有 `URL Source: https://help.openai.com/en/articles/10169521-projects-in-chatgpt`、`Updated: 19 hours ago`）。
- openai.com 部落格、cell.com 全文、web.archive.org 都連不上（403／連線被重設），相關條目有另外註明。

---

#### AI-01　OpenAI 因準確率過低下架自家的 AI Classifier
- 位置：`docs/ai-tools.md:95`
- 站上寫法：「OpenAI 曾因準確率過低而下架自己的 AI Classifier。」
- 原始出處：OpenAI（2023）〈New AI classifier for indicating AI-written text〉，<https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/>
  - 原文：未取得原頁（openai.com 對 curl 和 WebFetch 都回 403，web.archive.org 連線被重設）。以下是二手報導轉述 OpenAI 補在原文章上的說明：Decrypt（<https://decrypt.co/149826/openai-quietly-shutters-its-ai-text-classifier-due-to-low-accuracy>）寫 OpenAI 在原部落格文章加註，理由是 "its low rate of accuracy"。WebSearch 摘要另指出該分類器 2023-01-31 上線、2023-07-20 下架。
- 判定：正確
- 說明：多家報導轉述的 OpenAI 說明都一致指向「準確率低」，跟站上寫法相符。只是 OpenAI 原頁本次拿不到。
- 建議改法：不需修改。想更完整可以補時間與出處：「OpenAI 在 2023 年 7 月以準確率過低（low rate of accuracy）為由，停止提供自己 1 月推出的 AI Classifier。」

#### AI-02　AI 偵測器對非母語寫作者有系統性誤判
- 位置：`docs/ai-tools.md:95`
- 站上寫法：「市面上的偵測工具至今仍存在對非母語寫作者的系統性誤判傾向。」
- 原始出處：Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J.（2023）. GPT detectors are biased against non-native English writers. *Patterns, 4*(7), 100779. https://doi.org/10.1016/j.patter.2023.100779（書目已用 Crossref 核對）
  - 原文（arXiv:2304.02819 摘要，期刊全文頁回 403）："Our findings reveal that these detectors consistently misclassify non-native English writing samples as AI-generated, whereas native writing samples are accurately identified."
- 判定：不精確
- 說明：誤判現象有原始研究支持，但站上沒有附出處。證據是 2023 年針對當時幾款偵測器做的研究，「市面上的偵測工具至今仍」把它擴大到現在所有工具，這點沒有找到原始出處。
- 建議改法：「已有研究發現，多款 GPT 偵測器會把非英語母語者的寫作誤判為 AI 生成（Liang et al., 2023）。」
- 查核日期：2026-10-23

#### AI-03　即使用改寫工具，各檢測平台的檢出率仍然很高
- 位置：`docs/ai-tools.md:97-100`（第 178 行的重點回顧「規避沒有用」也是同一主張）
- 站上寫法：「真相二：降低機器味不等於能規避檢測。社群實測顯示，即使套用專門的改寫工具，各檢測平台的檢出率仍然很高。」「偵測不可靠 → 你可能被誤判；規避不管用 → 你也躲不掉。」
- 原始出處：
  - Krishna et al.（2023）, Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense, arXiv:2303.13408
    - 原文（摘要）："Using DIPPER to paraphrase text generated by three large language models (including GPT3.5-davinci-003) successfully evades several detectors, including watermarking, GPTZero, DetectGPT, and OpenAI's text classifier. For example, DIPPER drops detection accuracy of DetectGPT from 70.3% to 4.6% (at a constant false positive rate of 1%)"
  - Sadasivan et al.（2023）, Can AI-Generated Text be Reliably Detected?, arXiv:2303.11156
    - 原文（摘要）："our recursive paraphrasing method can significantly reduce detection rates, it only slightly degrades text quality in many cases"
  - Liang et al.（2023），同 AI-02
    - 原文（摘要）："simple prompting strategies can not only mitigate this bias but also effectively bypass GPT detectors"
- 判定：不精確
- 說明：「社群實測」沒有附出處，查不到。已發表的研究反而一再顯示，改寫可以大幅降低偵測率。這段的結論（不要靠規避偵測）沒有問題，但「規避不管用」這個事實理由跟研究相反，也跟同一段「偵測器不可靠」互相矛盾。
- 建議改法：把理由從「躲不掉」改成誠信層面。例如：「真相二：就算改寫工具真的能騙過偵測器，也不會讓這件事變得正當。研究顯示改寫可以大幅降低偵測率（Krishna et al., 2023），但規避偵測本身就違反多數學校的 AI 使用揭露規定，而且工具紀錄、提示詞紀錄與修改軌跡都可能被追溯。」重點回顧那一條（第 178 行）也要一起改。

#### AI-04　LangChain Open Deep Research 已封存
- 位置：`docs/ai-tools.md:38`
- 站上寫法：「repo 已封存（archived），不再維護（2026-09-26 查證）」
- 原始出處：GitHub langchain-ai/open_deep_research，<https://github.com/langchain-ai/open_deep_research>
  - 原文："This repository was archived by the owner on Aug 21, 2026. It is now read-only."
- 判定：正確
- 說明：GitHub 頁面上有封存公告。
- 建議改法：不需修改（可以順便補上封存日期 2026-08-21）。
- 查核日期：2026-10-23

#### AI-05　STORM 的兩階段流程，以及 Co-STORM 可以人工介入
- 位置：`docs/ai-tools.md:37`
- 站上寫法：「視角引導提問 + 兩階段（先寫大綱再產出長文）」「Co-STORM 可人工介入」
- 原始出處：GitHub stanford-oval/storm README，<https://github.com/stanford-oval/storm>
  - 原文："The system conducts Internet-based research to collect references and generates an outline." "The system uses the outline and references to generate the full-length article with citations." "STORM discovers different perspectives by surveying existing articles from similar topics" Co-STORM："actively engage in the conversation by injecting utterances to steer the discussion focus."
- 判定：正確
- 說明：README 對兩階段、視角探索和使用者介入的描述都跟站上一致。repo 由 Stanford OVAL 維護。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-06　DeerFlow（字節跳動）是結合搜尋、程式碼執行與沙箱的長時程 agent 框架
- 位置：`docs/ai-tools.md:39`
- 站上寫法：「長時程的研究型 agent 框架，結合網路搜尋、程式碼執行與沙箱」
- 原始出處：GitHub bytedance/deer-flow，<https://github.com/bytedance/deer-flow>
  - 原文（About）："An open-source long-horizon SuperAgent harness that researches, codes, and creates."；README："is an open-source super agent harness that orchestrates sub-agents, memory, and sandboxes to do almost anything"
- 判定：正確
- 說明：跟官方描述一致，repo 放在 bytedance 組織底下。官方現在的定位是通用的「SuperAgent harness」，不只用在研究，但站上的說法不算錯。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-07　PaperQA2 主要是為生醫與自然科學設計
- 位置：`docs/ai-tools.md:41`
- 站上寫法：「科學 PDF 的 RAG 問答，精確引用原文段落」；限制欄：「主要為生醫與自然科學設計」
- 原始出處：GitHub Future-House/paper-qa README，<https://github.com/Future-House/paper-qa>
  - 原文："PaperQA2 is a package for doing high-accuracy retrieval augmented generation (RAG) on PDFs, text files, Microsoft Office documents, and source code files, with a focus on the scientific literature."（About："High accuracy RAG for answering questions from scientific documents with citations"）
- 判定：不精確
- 說明：README 只寫「focus on the scientific literature」，沒有限定在生醫或自然科學。站上把它寫成這款工具本身的設計限制，README 不支持這個說法。
- 建議改法：「主要針對科學文獻設計，用在社會科學文獻的效果需要自行測試」
- 查核日期：2026-10-23

#### AI-08　Webster & Watson (2002) 的書目與篇幅，以及 2020 年的更新版
- 位置：`docs/ai-workflow.md:145-146`、`docs/ai-workflow.md:181`、`docs/ai-workflow.md:400`
- 站上寫法：「Webster & Watson (2002), *MIS Quarterly* 26(2)」「Webster & Watson (2002) 只有十來頁……2020 年有更新版（Watson & Webster, *Journal of Decision Systems*）」
- 原始出處：Crossref API
  - 10.2307/4132319："Analyzing the Past to Prepare for the Future: Writing a Literature Review", MIS Quarterly, 26(2), xiii-xxiii, 2002-06
  - 10.1080/12460125.2020.1798591："Analysing the past to prepare for the future: Writing a literature review a roadmap for release 2.0", Journal of Decision Systems, 29(3), 129-147, 2020（作者 Watson, Webster）
  - 「concept-centric vs author-centric」的內容：未取得全文（JSTOR 付費），本次只核對了書目。
- 判定：正確
- 說明：年份、刊名、卷期都對。頁碼 xiii–xxiii 共 11 頁，符合「十來頁」。2020 年更新版的作者順序、刊名和年份也都對。
- 建議改法：不需修改（可以補上頁碼與 DOI：*MIS Quarterly, 26*(2), xiii–xxiii；*Journal of Decision Systems, 29*(3), 129–147, https://doi.org/10.1080/12460125.2020.1798591）

#### AI-09　PRISMA 流程圖記錄每一階段篩掉多少篇
- 位置：`docs/ai-workflow.md:115`
- 站上寫法：「並記錄每一階段篩掉多少篇。這正是 PRISMA 流程圖在做的事。」
- 原始出處：PRISMA statement，PRISMA 2020 flow diagram，<https://www.prisma-statement.org/prisma-2020-flow-diagram>
  - 原文："The flow diagram depicts the flow of information through the different phases of a systematic review. It maps out the number of records identified, included and excluded, and the reasons for exclusions."
- 判定：正確
- 說明：流程圖記錄的就是各階段的篇數和排除理由。（事先寫下納入排除準則這件事屬於研究計畫書與 PRISMA 清單的範圍，不是流程圖本身，但站上這句只把「記錄篇數」歸給流程圖。）
- 建議改法：不需修改

#### AI-10　NotebookLM 的名稱已經改了；答案以上傳的原文為準
- 位置：`docs/ai-workflow.md:345`、`docs/ai-workflow.md:375`、`docs/ai-workflow.md:378`、`docs/ai-case-study.md:33`
- 站上寫法：「用 NotebookLM 這類『以文件為準』的工具建立筆記本，把 PDF 丟進去問問題（答案錨定在你上傳的原文，比一般對話工具更不容易編造內容）」
- 原始出處：
  - Google Workspace Updates（2026-07-16）〈NotebookLM is now Gemini Notebook〉，<https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html>
    - 原文："We’re renaming NotebookLM to Gemini Notebook . While it remains a standalone product focused on being your premier research tool, the new name reflects how it will evolve to do more across the Google ecosystem."
  - Gemini Notebook Help〈Learn about Gemini Notebook〉（原本的 support.google.com/notebooklm/answer/16164461 已經轉址到 <https://support.google.com/gemininotebook/answer/16164461?hl=en>）
    - 原文："Chat with your notebook to get grounded information based on your sources with clear in-line citations for accuracy, transparency, and trust." "Gemini Notebook is designed to answer questions based on the information provided in your uploaded sources." "Gemini Notebook can make mistakes"
- 判定：不精確
- 說明：「答案以上傳的原文為準」有官方說法支持，但產品從 2026-07-16 起已經改名為 Gemini Notebook，站上還在用舊名。讀者照舊名去找，會找到已經轉址的頁面。ai-case-study.md:33 寫的是站主過去用過的工具，維持舊名可以接受，但最好加註新名稱。
- 建議改法：ai-workflow.md:345 改成「用 Gemini Notebook（2026 年 7 月前叫 NotebookLM）這類『以文件為準』的工具……」，第 375、378 行一起改。官方自己也寫「can make mistakes」，括號裡「比一般對話工具更不容易編造內容」建議加上「仍可能出錯，要回原文核對」。
- 查核日期：2026-10-23

#### AI-11　ChatGPT Projects：建立專案與專案指示的步驟
- 位置：`docs/ai-quickstart.md:32-33`
- 站上寫法：「在左側欄選『New project』，輸入專案名稱，可以順便選圖示和顏色。」「點更多選項選單（•••），選『Project settings』……專案指示只在這個專案裡有效，會蓋過你在帳號層級設定的自訂指示」
- 原始出處：OpenAI Help Center〈Projects in ChatGPT〉，<https://help.openai.com/en/articles/10169521-projects-in-chatgpt>
  - 原文："Select **New project** in the sidebar." "Enter a project name, then select an icon and color." "Select the more options menu (•••), then select **Project settings** to add instructions for the project." "Project instructions apply only within that project and override your global custom instructions."
- 判定：正確
- 說明：步驟和覆蓋規則都跟官方說明一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-12　ChatGPT 專案的檔案上限依方案而定
- 位置：`docs/ai-quickstart.md:34`
- 站上寫法：「Free 5 個，Go、Plus 25 個，Edu、Pro、Business、Enterprise 40 個，一次最多上傳 10 個。……可以從專案的來源清單開啟、下載或刪除。」
- 原始出處：同 AI-11（Plans and limits 段落）
  - 原文："Note that only 10 files can be uploaded at the same time." "**Free:** 5 files per project" "**Go, Plus:** 25 files per project" "**Edu, Pro, Business, Enterprise:** 40 files per project"；"you can open it from the project sources list to preview, download, or delete it."
- 判定：正確
- 說明：每個數字都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-13　ChatGPT 專案的記憶設定（project-only memory）
- 位置：`docs/ai-quickstart.md:35`
- 站上寫法：「建立專案時就能選，之後也能從 •••『Project settings』的『Memory』更改。改成後者，這個專案的內容就不會被專案外的對話拿去參考。」
- 原始出處：同 AI-11（Memory in projects 段落）
  - 原文："You can select a memory setting when you create a project and change it later from the project’s settings." "Select the more options menu (•••), then select **Project settings**." "Under **Memory**, select **Default memory** or **Project-only memory**." "Chats outside the project cannot reference conversations from the project."
- 判定：正確
- 說明：跟官方說明一致。官方另外提到「Changes may take a few hours to take effect.」，也提到共享專案一律是 project-only memory，站上沒寫這兩點，但不影響正確性。
- 建議改法：不需修改（可以補一句「改設定後可能要幾小時才生效」）
- 查核日期：2026-10-23

#### AI-14　ChatGPT 的「Improve the model for everyone」開著時，Free、Plus、Pro 的專案內容可能被拿去訓練模型
- 位置：`docs/ai-quickstart.md:117`
- 站上寫法：「例如 ChatGPT 的『Improve the model for everyone』開著時，Free、Plus、Pro 的專案內容可能被用來訓練模型」
- 原始出處：同 AI-11（Projects FAQ）
  - 原文："For ChatGPT Free, Plus, and Pro users, we may use information accessed from projects to train our models if your “**Improve the model for everyone**” setting is on."
- 判定：正確
- 說明：方案範圍和條件都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-15　Claude Projects：建立步驟，以及 Claude 讀不到名稱和說明
- 位置：`docs/ai-quickstart.md:41-44`
- 站上寫法：「點右上角的『+ New Project』，輸入專案名稱和說明。官方說明提醒，Claude 讀不到名稱和說明的內容」「點『Set project instructions』……再點『Save instructions』」「點『+』上傳文件」
- 原始出處：Claude Help Center〈How can I create and manage projects?〉，<https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects>
  - 原文："Click "+ New Project" in the upper right corner." "Give your project a name and description (note that Claude will not have access to these details)." "Click on "Set project instructions."" "Add instructions for how you'd like Claude to behave and respond and click "Save instructions."" "Click on the "+" button to add content to the project."
- 判定：正確
- 說明：步驟和提醒都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-16　Claude 免費帳號最多建立五個專案
- 位置：`docs/ai-quickstart.md:46`
- 站上寫法：「免費帳號也能用 Projects，但最多只能建立五個專案。」
- 原始出處：同 AI-15
  - 原文："Projects are available to all users, including those with free Claude accounts. Free users can create a maximum of five projects."
- 判定：正確
- 說明：跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-17　Gemini Gems 的建立步驟與年齡門檻
- 位置：`docs/ai-quickstart.md:52-57`
- 站上寫法：「打開側邊欄（Open sidebar），點『Gems』，再點『New Gem』。如果從沒建過 Gem，要先點『Settings and help』，再點『Gems』。」「在『Knowledge』下面點『Add files』。從電腦上傳點『Upload files』，從 Google 雲端硬碟加入點『Add from Drive』。」「個人帳號要年滿 13 歲（或所在國家規定的年齡）」
- 原始出處：Gemini Apps Help〈Use Gems in Gemini Apps〉，<https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop>
  - 原文："Click Open Sidebar" "Click Gems" "If you’ve never made a Gem before, first click Settings and help Gems" "Click New Gem" "(Optional) To add sources, under "Knowledge," click Add files" "To upload a file from your device: click Upload files" "To add a file from your Google Drive: click Add from Drive" "To create and use Gems with a personal Google Account, you must also be 13 (or the applicable age in your country) or over."
- 判定：正確
- 說明：跟官方一致。官方另外寫了：從 Drive 加檔案要開啟 Keep Activity 並連結 Google Workspace，站上沒寫。
- 建議改法：不需修改（可以補「從雲端硬碟加入要先開啟 Keep Activity」）
- 查核日期：2026-10-23

#### AI-18　Gems 轉成技能（skills）的時程，以及哪些檔案格式不會轉移
- 位置：`docs/ai-quickstart.md:60-62`（第 5 行和 `docs/prompts.md:671` 也建議用 Gem 當專案）
- 站上寫法：「個人帳號的 Gems 從 2026 年 11 月起會移除……Workspace 的商務、企業與非營利帳號是 2027 年 3 月，教育帳號是 2027 年 6 月。」「Knowledge 裡的檔案只會轉移技能支援的格式，.docx、.doc、.xlsx 不在其中。」
- 原始出處：
  - Gemini Apps Help〈About the transition from Gems to skills〉，<https://support.google.com/gemini/answer/18560919?hl=en>
    - 原文："November 2026: Personal Google accounts." "March 2027: Workspace business, enterprise, and non-profit accounts." "June 2027: Workspace education accounts." "We’ll automatically transition your Gems, along with any supported files, to skills for you when Gems go away."
  - Gemini Apps Help〈Create and manage skills for Gemini Apps〉，<https://support.google.com/gemini/answer/17094296?hl=en>
    - 原文："Not supported: Binary: .docx , .doc , .xlsx , or any other non-plain-text formats."
- 判定：正確
- 說明：時程和格式限制都跟官方一致。要提醒的是，查核日（2026-10-23）離個人帳號移除 Gems 只剩幾天，第 5 行「Gemini 叫 Gems」和 prompts.md:671「Gemini 用 Gem」很快就會過時。
- 建議改法：不需修改。11 月以後建議把第 5 行和 prompts.md:671 的「Gems」改成「技能（skills）」。
- 查核日期：2026-10-23

#### AI-19　Gemini 技能（skills）的使用條件與建立路徑
- 位置：`docs/ai-quickstart.md:62`
- 站上寫法：「條件是年滿 18 歲、用個人 Google 帳號登入、開啟『Keep Activity』。建立方式是在 gemini.google.com 點『Settings』→『Skills』→『Create manually』，填入名稱、說明和指示後點『Create』；在對話裡輸入『/』就能選用。」
- 原始出處：
  - Gemini Apps Help〈Create and manage skills for Gemini Apps〉，<https://support.google.com/gemini/answer/17094296?hl=en>
    - 原文："Be 18 or over." "Sign in to the Gemini app." "Have Keep Activity on." "On the sidebar, click Customize . If you don’t find “Customize,” first click More . At the top, click Skills ." "At the top of the Skills page, click Create Create manually ." "In the chat or task thread, enter / (or @ , if you have the updated shortcut), then select the skill."
  - 〈About the transition from Gems to skills〉（同 AI-18）
    - 原文："Skills are now available in Gemini chat to individuals over 18 signed in to a personal Google Account." "On the sidebar, click Settings Skills ."
- 判定：不精確
- 說明：條件正確。站上引用的那一頁（17094296）現在的路徑是側邊欄「Customize」→「Skills」→「Create」→「Create manually」，已經沒有「Settings」；只有轉移說明頁還寫 Settings。另外「/」之外，官方現在也提到新版快捷鍵「@」。
- 建議改法：「建立方式是在 gemini.google.com 側邊欄點『Customize』（找不到就先點『More』）→ 上方『Skills』→『Create』→『Create manually』……在對話裡輸入『/』（新版快捷鍵為『@』）就能選用。」
- 查核日期：2026-10-23

#### AI-20　Claude Code 需要的方案（Pro、Max 方案本身就內含 Claude Code）
- 位置：`docs/ai-quickstart-agent.md:14`、`docs/claude-tools-overview.md:13`
- 站上寫法：「Claude Code 要 Claude 的 Pro、Max、Team、Enterprise 方案，或 Claude Console 帳號」；「Pro／Max 方案本身就內含 Claude Code」
- 原始出處：Claude Code Docs〈Quickstart〉，<https://code.claude.com/docs/en/quickstart>
  - 原文："A [Claude subscription] (Pro, Max, Team, or Enterprise), [Claude Console] account, or access through a [supported cloud provider]"
- 判定：正確
- 說明：跟官方一致。官方另外列了雲端供應商這條路，站上沒寫，但不影響研究生的情境。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-21　Codex CLI 要 Plus 以上方案，Free 和 Go 只有桌面 app；也可以用 API key 依用量計費
- 位置：`docs/ai-quickstart-agent.md:14`
- 站上寫法：「Codex 的官方方案頁把終端機版本（Codex CLI）列在 ChatGPT Plus 以上的方案，Free 和 Go 只寫到桌面 app（Pricing）。兩者也都可以改用 API key 登入，依 API 用量另外計費。」
- 原始出處：Codex Pricing，<https://learn.chatgpt.com/docs/pricing>
  - 原文（WebFetch 擷取）：Free／Go："GPT-6 Luna at Standard speed in the desktop app, subject to rollout."；Plus："Codex on the web, in the CLI, in the IDE extension, and on iOS."；Pro："Everything in Plus and:"；API Key："Codex in the CLI, SDK, or IDE extension" "Pay for Codex usage based on API pricing."
- 判定：正確
- 說明：Free 和 Go 只列桌面 app，CLI 從 Plus 才開始列，跟站上一致。（Business 那一欄寫的是「desktop and mobile apps」，沒有明寫 CLI，所以「Plus 以上」嚴格來說是指 Plus 和 Pro。）Claude Code 用 Console 帳號，就是依 API 用量計費。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-22　Claude Code 的安裝、驗證與登入
- 位置：`docs/ai-quickstart-agent.md:36-38`、`docs/ai-quickstart-agent.md:15`
- 站上寫法：「Windows 的 PowerShell 和 CMD 用的指令不同，貼錯會出現錯誤訊息，官方頁面上寫了怎麼分辨。官方也建議 Windows 先裝 Git for Windows。」「輸入 `claude --version`，有印出版本號就是裝好了。」「第一次會要你在瀏覽器登入。之後要換帳號，在 Claude Code 裡輸入 `/login`。」
- 原始出處：Claude Code Docs〈Quickstart〉，<https://code.claude.com/docs/en/quickstart>
  - 原文："If you see `The token '&&' is not a valid statement separator`, you're in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you're in CMD, not PowerShell." "[Git for Windows] is recommended on native Windows so Claude Code can use the Bash tool." "When the installer finishes, open a new terminal window and run `claude --version`. A working installation prints a version number." "Claude Code prompts you to log in on first use." "To switch accounts later or re-authenticate, type `/login` inside the running session."
- 判定：正確
- 說明：每一步都跟官方一致，終端機入門頁（terminal-guide）也存在。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-23　Codex CLI 的四種安裝方式，以及第一次登入
- 位置：`docs/ai-quickstart-agent.md:42-43`
- 站上寫法：「macOS／Linux、Windows（PowerShell）、npm、Homebrew 四種方式擇一。」「第一次執行時選『Sign in with ChatGPT』」
- 原始出處：Codex CLI，<https://learn.chatgpt.com/docs/codex/cli>
  - 原文（頁面資料）："Install the Codex CLI with the standalone installer for Windows.\nStart these from a new PowerShell window." "You can also install the Codex CLI with npm." "You can also install the Codex CLI with Homebrew."；登入（WebFetch 擷取）："The first time you run Codex, choose **Sign in with ChatGPT** or another available sign-in method."
- 判定：正確
- 說明：四個安裝分頁和登入選項都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-24　Claude Code 從 v2.1.283 起預設 auto 模式；Manual 模式的開法、Shift+Tab 與狀態列
- 位置：`docs/ai-quickstart-agent.md:49`、`docs/ai-quickstart-agent.md:180`
- 站上寫法：「v2.1.283 起，終端機的互動 session 預設是 auto 模式，背景有分類器先審過動作……啟動時輸入 `claude --permission-mode manual`，或在 session 裡按 `Shift+Tab` 切換，下方狀態列顯示 `manual mode on` 就對了。」
- 原始出處：Claude Code Docs〈Permission modes〉，<https://code.claude.com/docs/en/permission-modes>
  - 原文："With Claude Code v2.1.283 or later, auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions." "A separate classifier model reviews actions before they run" "The CLI accepts `manual` as an alias wherever you type the value, for example `claude --permission-mode manual`" "The status bar shows the active mode as a gray `⏸ manual mode on` for `default`" "From `auto`, the first press switches to `default`"
- 判定：正確
- 說明：版本號、模式名稱、切換方式和狀態列字樣都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-25　Codex 的預設沙箱、Auto 模式與 read-only 建議
- 位置：`docs/ai-quickstart-agent.md:50`、`docs/ai-quickstart-agent.md:73`
- 站上寫法：「預設會把寫入限制在目前的工作資料夾，也不能連網。常用的 Auto 設定下……要改資料夾以外的檔案或要連網時才會問你。官方建議沒有版本控制的資料夾用 read-only，在 Codex 裡輸入 `/permissions` 就能切換」「Codex 可能先以唯讀模式啟動，等你確認信任這個資料夾」
- 原始出處：Codex〈Agent approvals & security〉，<https://learn.chatgpt.com/docs/agent-approvals-security>
  - 原文（WebFetch 擷取）："Defaults include no network access and write permissions limited to the active workspace." "Codex asks for approval to edit files outside the workspace or to run commands that require network access." "Version-controlled folders: `Auto` (workspace write + on-request approvals)" "Non-version-controlled folders: `read-only`" "switch to `read-only` mode with the `/permissions` command" "Depending on your setup, Codex may also start in `read-only` until you explicitly trust the working directory."
- 判定：正確
- 說明：每一點都跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-26　指示檔的檔名與位置：Claude Code 讀 CLAUDE.md、Codex 讀 AGENTS.md；確認有沒有讀到的方法
- 位置：`docs/ai-workflow-map.md:29`、`docs/ai-quickstart-agent.md:81-82`、`docs/ai-quickstart-agent.md:97`、`docs/ai-case-study.md:178`
- 站上寫法：「Claude Code 讀資料夾根目錄的 `CLAUDE.md`」「Codex 讀資料夾根目錄的 `AGENTS.md`」「Claude Code：在 session 裡輸入 `/context`，看『Memory files』底下有沒有你的 `CLAUDE.md`。Codex：請它『Summarize the current instructions.』」
- 原始出處：
  - Claude Code Docs〈How Claude remembers your project〉，<https://code.claude.com/docs/en/memory>
    - 原文："A project CLAUDE.md can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`." "To confirm the file loaded, run `/context` in a session and check the list under **Memory files**."
  - Codex〈AGENTS.md〉，<https://learn.chatgpt.com/docs/agent-configuration/agents-md>
    - 原文（WebFetch 擷取）："Starting at the project root (typically the Git root), Codex walks down to your current working directory." 驗證範例：`codex --ask-for-approval never "Summarize the current instructions."`
- 判定：正確
- 說明：檔名、位置和驗證方法都跟官方一致。Claude Code 也接受 `./.claude/CLAUDE.md`；Codex 另外會讀 `~/.codex/AGENTS.md` 和子資料夾裡的 AGENTS.md。站上寫的是最常見的情況，沒有錯。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-27　Claude Code v2.1.277 起，沒有 CLAUDE.md 時會改讀 AGENTS.md
- 位置：`docs/ai-quickstart-agent.md:83`
- 站上寫法：「Claude Code 從 v2.1.277 起，在資料夾裡和上層資料夾都沒有 `CLAUDE.md`、`.claude/CLAUDE.md`、`CLAUDE.local.md` 時，會改讀 `AGENTS.md`。剛從舊版升級後的第一個 session 可能還讀不到」
- 原始出處：Claude Code Docs〈How Claude remembers your project〉，<https://code.claude.com/docs/en/memory>
  - 原文："Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later." "**Count, so Claude reads them instead of `AGENTS.md`**: a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your working directory or any directory above it" "In some cases, it's your [first session after you upgrade] from v2.1.276 or earlier. Claude reads `AGENTS.md` from your next session on"
- 判定：正確
- 說明：版本號、條件和升級後的例外都跟官方一致。（官方另外提到：v2.1.281 以前，在 Amazon Bedrock 或關閉遙測的 session 只讀 CLAUDE.md。研究生一般用不到。）
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-28　thesis-toolkit 的 plugin 安裝指令，以及安裝範圍（scope）的選擇
- 位置：`docs/ai-quickstart-agent.md:111-116`、`docs/ai-case-study.md:204-207`、`docs/prompts.md:10`、`docs/ai-workflow-map.md:30`
- 站上寫法：「/plugin marketplace add wayhong0928/mis-thesis-skills」「/plugin install thesis-toolkit@mis-thesis-skills」「第二行不會直接安裝，會先打開這個 plugin 的說明畫面，讓你選安裝範圍（scope）。選 user……選 local，只有目前這個資料夾能用」
- 原始出處：
  - Claude Code Docs〈Install and manage plugins〉，<https://code.claude.com/docs/en/discover-plugins>
    - 原文："In a session, this command doesn't install right away: it opens the `/plugin` panel on that plugin's details so you can review it and choose a scope first." "**Install for you (user scope)**: you get the plugin in every project on this machine" "**Install for all collaborators on this repository (project scope)**" "**Install for you, in this repo only (local scope)**: you get it in this repository only"；GitHub 來源格式："`owner/repo`"
  - mis-thesis-skills 的 `.claude-plugin/marketplace.json`（raw.githubusercontent.com）：`"name": "mis-thesis-skills"`、plugins 裡有 `"name": "thesis-toolkit"`
- 判定：正確
- 說明：指令格式、marketplace 名稱和 plugin 名稱都對得上。官方提供 user、project、local 三個選項，站上只說明了 user 和 local，沒有寫錯。
- 建議改法：不需修改（可以補一句「另有 project，會寫進資料夾的設定檔、讓共用這個資料夾的人都啟用，一個人用不需要選」）
- 查核日期：2026-10-23

#### AI-29　plugin 的 SKILL 用 `/plugin名稱:skill名稱` 指定，也會依任務自動啟用
- 位置：`docs/ai-quickstart-agent.md:118`
- 站上寫法：「你提到相關任務時 Claude 會自己啟用對應的 SKILL。也可以直接指定，例如輸入 `/thesis-toolkit:research-question-audit`」
- 原始出處：Claude Code Docs〈Extend Claude with skills〉，<https://code.claude.com/docs/en/skills>
  - 原文（WebFetch 擷取）："Plugin skills are namespaced as `/plugin-name:skill-name`." "Claude uses skills when relevant, or you can invoke one directly with `/skill-name`"
- 判定：正確
- 說明：跟官方一致。repo 裡確實有 `research-question-audit` 這個資料夾。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-30　從第三方市集裝的 plugin 預設不會自動更新
- 位置：`docs/ai-quickstart-agent.md:129`
- 站上寫法：「Claude Code 從第三方市集裝的 plugin 預設不會自動更新，要在 `/plugin` 的 Marketplaces 分頁選這個市集，開啟自動更新」
- 原始出處：Claude Code Docs〈Install and manage plugins〉，<https://code.claude.com/docs/en/discover-plugins>
  - 原文："**Off by default**: every other marketplace, including the community marketplace, third-party marketplaces, and local development marketplaces." "In a Claude Code session, run `/plugin` and go to the **Marketplaces** tab. Select the marketplace, then select **Enable auto-update** or **Disable auto-update**."
- 判定：正確
- 說明：跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-31　Codex 讀同樣格式的 SKILL，放在 `.agents/skills/`
- 位置：`docs/ai-quickstart-agent.md:122-127`、`docs/ai-workflow-map.md:30`
- 站上寫法：「Codex 讀得懂同樣格式的 SKILL」「把……四個資料夾，整個複製到 `我的論文/.agents/skills/`。想讓每個資料夾都能用，改放到家目錄底下的 `.agents/skills/`。」「Codex 會自動偵測新的 SKILL，沒出現就重開 Codex。輸入 `/skills` 可以看清單，輸入 `$research-question-audit` 就能指定使用。」
- 原始出處：Codex〈Build skills〉，<https://learn.chatgpt.com/docs/build-skills>
  - 原文（WebFetch 擷取）："Skills build on the open agent skills standard." 存放位置：repo 的 `.agents/skills`（從工作資料夾往上到 repo 根目錄）、使用者層級 `$HOME/.agents/skills`。"run `/skills` or type `$` to mention a skill." "Codex detects skill changes automatically."（沒出現時重開 Codex）
- 判定：正確
- 說明：路徑和指令都跟官方一致。repo 裡確實有四個 SKILL 資料夾（academic-writing-discipline、research-direction-finding、research-question-audit、thesis-roadmap）。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-32　Consensus 的官方 MCP：網址、加入指令與登入規則
- 位置：`docs/ai-quickstart-agent.md:135-140`、`docs/ai-workflow-map.md:63`
- 站上寫法：「多數用戶端第一次連線時會要你用 Consensus 帳號登入，Claude 與 ChatGPT 不登入也能用，但額度較低；每月能搜尋幾次依方案而定。」「`claude mcp add --transport http consensus https://mcp.consensus.app/mcp`」「`codex mcp add consensus --url https://mcp.consensus.app/mcp`……`codex mcp login consensus`」
- 原始出處：GitHub Consensus-NLP/consensus-mcp，<https://github.com/Consensus-NLP/consensus-mcp>
  - 原文（WebFetch 擷取）："claude mcp add --transport http consensus https://mcp.consensus.app/mcp" "codex mcp add consensus --url https://mcp.consensus.app/mcp" "codex mcp login consensus" "you sign in with your Consensus account the first time you connect." "also work without an account at reduced limits." "Paper counts and monthly search limits vary by plan."
- 判定：正確
- 說明：指令和規則都跟官方說明一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-33　Elicit 的 MCP 要 Pro 以上方案；官方沒寫 Codex 的步驟
- 位置：`docs/ai-quickstart-agent.md:142-145`
- 站上寫法：「要 Elicit 的 Pro 以上方案才能用 MCP。」「`claude mcp add --transport http elicit https://elicit.com/api/mcp`，再到 Claude Code 裡輸入 `/mcp`，選 `elicit`，按『Authenticate』」「Elicit 的官方說明沒有寫 Codex 的步驟。」
- 原始出處：GitHub elicit/api-examples（integrations/mcp），<https://github.com/elicit/api-examples/tree/main/integrations/mcp>
  - 原文（WebFetch 擷取）："An Elicit account on Pro plan or above" "https://elicit.com/api/mcp" "claude mcp add --transport http elicit https://elicit.com/api/mcp"；說明裡寫的是在 Claude Code 的 MCP 選單選 elicit、點「Authenticate」，會開瀏覽器做 OAuth 登入。頁面沒有提到 Codex。
- 判定：正確
- 說明：跟官方一致。
- 建議改法：不需修改
- 查核日期：2026-10-23

#### AI-34　Claude 網頁版上傳 SKILL 時，description 上限是 200 字元
- 位置：`docs/prompts.md:666`
- 站上寫法：「Claude 網頁版也能手動上傳 SKILL，但其中兩個的說明欄（description）超過網頁版 200 字元的上限。」
- 原始出處：
  - Claude Help Center〈How to create custom skills〉，<https://support.claude.com/en/articles/12512198-how-to-create-custom-skills>
    - 原文："This is critical—Claude uses this to determine when to invoke your skill (200 characters maximum)."
  - Claude Docs〈Create custom skills〉，<https://claude.com/docs/skills/how-to>（這頁講的就是打包 ZIP、上傳到 Claude）
    - 原文："`description` | string | What the skill does and when to use it. Claude reads this to decide when to load the skill. Up to 1,024 characters, the limit in the [Agent Skills specification]"
- 判定：不精確
- 說明：Anthropic 自己的兩份官方文件現在說法不一樣：Help Center 寫 200 字元，較新的 claude.com/docs 寫 1,024 字元，沒有另外替 claude.ai 設 200 的限制。站上把 200 寫成確定的上限，可能已經過時。我另外量了 repo 目前的 description 長度：academic-writing-discipline 307、research-direction-finding 212、research-question-audit 183，所以「三個裡有兩個超過 200」這個數字本身對。
- 建議改法：「Claude 網頁版也能手動上傳 SKILL。官方說明對 description 的長度上限寫法不一（Help Center 寫 200 字元，Claude Docs 寫 1,024 字元），其中兩個 SKILL 超過 200 字元，上傳失敗時改用這一節的簡版。」
- 查核日期：2026-10-23

#### AI-35　「SKILL 是 Claude 的機制，ChatGPT、Gemini 用不了」
- 位置：`docs/prompts.md:658`
- 站上寫法：「skill 是 Claude Code 或其他明確支援 skill 的 Claude 介面所用的機制。如果你平常使用 ChatGPT、Gemini，或不支援 skill 的純網頁對話，本頁的靜態提示詞仍是最泛用的做法」
- 原始出處：
  - Codex〈Build skills〉（同 AI-31）："Skills build on the open agent skills standard."
  - Gemini Apps Help〈Create and manage skills for Gemini Apps〉（同 AI-19）："upload a skill file or a folder with a SKILL.md file and optional supported reference files."
- 判定：不精確
- 說明：SKILL.md 現在是開放格式，OpenAI 的 Codex 和 Google 的 Gemini 網頁版都能讀。站上其他頁面也寫了 Codex 能用 SKILL（ai-quickstart-agent.md:122）、Gemini 有技能功能（ai-quickstart.md:62），這句跟它們互相矛盾。（ChatGPT 對話介面是否支援上傳 SKILL，本次沒有找到官方說明頁，不下判斷。）
- 建議改法：「SKILL（SKILL.md）是開放格式，Claude Code、Claude 網頁版、Codex 和 Gemini 網頁版的技能（skills）都能使用。如果你用的介面不支援，本頁的靜態提示詞仍是最泛用的做法，不必勉強轉換。」
- 查核日期：2026-10-23

#### AI-36　網頁簡版提示詞對照 thesis-toolkit 0.4.3 版（2026-10-06）
- 位置：`docs/prompts.md:666`
- 站上寫法：「對照的是 thesis-toolkit 0.4.3 版（2026-10-06）。SKILL 改版時，這一節會跟著更新」
- 原始出處：mis-thesis-skills repo（2026-10-23 clone），`plugins/thesis-toolkit/CHANGELOG.md` 與 `.claude-plugin/plugin.json`
  - 原文："## 0.4.3（2026-10-05）"；最新一筆："## 0.5.4（2026-10-17）"；plugin.json：`"version": "0.5.4"`
- 判定：不精確
- 說明：CHANGELOG 記的 0.4.3 日期是 2026-10-05，不是 10-06。之後已經改版到 0.5.4（0.5.0 到 0.5.4 改了 academic-writing-discipline 等規則），但這一節還寫對照 0.4.3，跟「改版時會跟著更新」的承諾對不上。
- 建議改法：日期改成 2026-10-05；如果簡版還沒照 0.5.x 更新，就寫「對照 0.4.3（2026-10-05）；目前最新為 0.5.4，差異見 CHANGELOG」，或者照 0.5.4 更新三段簡版之後再改版本號。
- 查核日期：2026-10-23

---

### 小計

- 查核條數：36 條
- 正確：28 條（AI-01、AI-04 到 AI-06、AI-08、AI-09、AI-11 到 AI-18、AI-20 到 AI-33）
- 不精確：8 條
- 錯誤：0 條
- 查不到：0 條（AI-03 的「社群實測」本身查不到出處，但因為有原始研究跟它矛盾，判為不精確）

「錯誤」清單：無

「不精確」清單：AI-02、AI-03、AI-07、AI-10、AI-19、AI-34、AI-35、AI-36

附註：AI-01 的 OpenAI 原頁和 AI-08 的 Webster & Watson 全文這次沒拿到，判定分別根據二手報導和 Crossref 書目資料，各條裡已經註明。

---

## 九、ETH／VEN：倫理法規、期刊政策與期刊研討會清單

查核日期：2026-10-23。只查核、未修改 repo。

範圍說明：任務提示列出的 Belmont Report、Springer Nature／ACM／AIS／MISQ 的 AI 政策、國科會 AI 指引、《專科以上學校學術倫理案件處理原則》等，**這三頁實際上都沒有寫**（用 grep 確認過），所以沒有列成條目。三頁實際寫到的法規是《學位授予法》（只是隱含）、《人體研究法》、《個人資料保護法》、《人工智慧基本法》和行政院生成式 AI 參考指引。

存取限制：publicationethics.org（COPE）、aisnet.org、多數出版社頁面（Wiley、T&F、Sage、ScienceDirect）對 curl 和 WebFetch 回 403／Cloudflare。遇到這種情況時，下面會寫明改用哪一層來源。aisconferences.org 換成 Firefox UA 後可以用 curl 正常讀取。有兩個台灣站台（nkust、ntunhs）的伺服器沒有送出中繼憑證。我從憑證的 AIA 欄位抓官方中繼憑證，加進信任清單再驗證，**沒有關閉 TLS 驗證**。

---

### 第一部分：ethics.md、research-ethics-data.md（ETH）

#### ETH-01　四條紅線與「可以嚴重到撤銷學位」
- 位置：`docs/ethics.md:14-21`、`docs/ethics.md:228`
- 站上寫法：「抄襲……代寫……造假……變造……在台灣，違反這些規定的後果可以嚴重到**撤銷學位**。」
- 原始出處：《學位授予法》第 17 條（民國 107 年 11 月 28 日修正），全國法規資料庫，<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0030010>
  - 原文：「學校授予之學位，有下列情事之一者，應予撤銷，並公告註銷其已頒給之學位證書；……二、論文、作品、成就證明、書面報告、技術報告或專業實務報告有造假、變造、抄襲、由他人代寫或其他舞弊情事。」
- 判定：正確
- 說明：四條紅線和第 17 條第 1 項第 2 款的用語完全一致。不過法條寫的是「應予撤銷」，屬於強制效果，比站上的「可以嚴重到」更重。
- 建議改法：可以補上法源，例如「依《學位授予法》第 17 條，學位論文有造假、變造、抄襲、由他人代寫等情事者，學校『應予撤銷』學位並註銷證書。」
- 查核日期：2026-10-23

#### ETH-02　生成式 AI 產出「不屬於著作權法保護的著作」
- 位置：`docs/ethics.md:27`、`docs/ethics.md:51`
- 站上寫法：「生成式 AI 產出的內容**不屬於著作權法保護的著作**，無法享有著作權保障，而直接使用恐違反抄襲規定，可能導致學位撤銷。」；「生成內容不屬著作權法保護的著作」
- 原始出處：教育部學術倫理電子報第 13 期（2023-08）主題文章〈大學校園因應生成式AI之指引及教學建議〉，<https://ethics.moe.edu.tw/resource/epaper/html/21/>
  - 原文：「依據著作權法的規定，非由自然人或法人創作的成果，不屬著作權法保護的著作，原則上無法享有著作權（經濟部智慧財產局，2018）。……研究者如果直接使用其生成內容，也可能產生抄襲、違反他人著作權之疑慮；依據教育部《學位授予法》（2018）規定，若學位論文有抄襲情事，應予撤銷學位」
- 判定：不精確
- 說明：原文的前提是「非由自然人或法人創作」，並且用「原則上」保留空間。站上改寫成所有 AI 產出一律不受保護，等於拿掉了條件。有人類創作性投入的成果，未必適用這個說法。
- 建議改法：「依智慧局見解，非由自然人或法人創作的成果原則上不受著作權法保護；完全由 AI 生成、缺乏人類創作投入的內容，原則上無法享有著作權。」
- 查核日期：2026-10-23

#### ETH-03　教育部電子報彙整七校指引，不是教育部正式指引
- 位置：`docs/ethics.md:39`、`docs/ethics.md:241`
- 站上寫法：「教育部學術倫理電子報的主題文章，彙整臺大、臺師大、陽明交大、中央、北科、高大、逢甲七校的校內指引。**不是教育部發布的正式指引**」
- 原始出處：同 ETH-02
  - 原文：「2023-08　第13期」；「筆者根據國立中央大學、國立高雄大學、國立陽明交通大學、國立臺北科技大學、國立臺灣大學、國立臺灣師範大學，以及逢甲大學等校於2023年所制定之生成式AI相關文件後，整理出五項較常見的議題」
- 判定：正確
- 說明：七校名單和時間都相符。原文是「筆者」整理的主題文章，站上說它不是正式指引，這個說法成立。
- 建議改法：不需修改（可以補上「第 13 期」）。

#### ETH-04　國內大學指引的共同要求（驗證、著作權、資安、揭露）
- 位置：`docs/ethics.md:43-61`、`docs/ethics.md:230`
- 站上寫法：「對 AI 產出之內容『保持一定程度之質疑』……禁止輸入個人資訊、未公開文件、機密資料……應先了解經費補助機關或期刊等單位對生成式 AI 的政策……於著作中『適度公開相關訊息』」
- 原始出處：同 ETH-02
  - 原文：「必須對於其產出之內容保持一定程度之質疑，並親自驗證相關內容的正確性與時效性」；「不要將個人資訊、未公開文件、機密資料等內容輸入到生成式AI的對話框中」；「建議研究者應先瞭解經費補助機關（構）或期刊等單位對於生成式AI之政策，並於著作或報告中適度公開相關訊息」
- 判定：正確
- 說明：引號裡的文字逐字相符。原文共有五項議題，站上省略了第四項「依賴科技而缺乏自我意識」，不影響正確性。另外，原文說的是「研究者應留意，不要……」，站上寫成「禁止」，語氣稍強。
- 建議改法：不需修改（「禁止輸入」可以改成「不應輸入」，更貼近原文語氣）。

#### ETH-05　《人工智慧基本法》三讀、公布日期、主管機關、七大原則
- 位置：`docs/ethics.md:37`、`docs/ethics.md:229`
- 站上寫法：「立法院於 2025 年 12 月 23 日三讀通過，2026 年 1 月 14 日公布施行｜明定主管機關為國科會，揭示政府推動 AI 應遵循的七大治理原則（含資安與安全）」
- 原始出處：全國法規資料庫《人工智慧基本法》，<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093>；數位發展部新聞稿 <https://moda.gov.tw/press/press-releases/18316>
  - 原文（法規資料庫）：「公布日期：民國 115 年 01 月 14 日」；第 2 條「本法所稱主管機關：在中央為國家科學及技術委員會」；第 4 條列「一、永續發展與福祉……四、資安與安全……七、問責」；第 20 條「本法自公布之日起施行。」
  - 原文（數發部）：「立法院114年12月23日三讀通過《人工智慧基本法》」
- 判定：正確
- 說明：日期、主管機關、七項原則（第 4 條）和施行日（第 20 條）都相符。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-06　行政院生成式 AI 參考指引「2023 年 8 月，由國科會公告，無強制性、無罰則」
- 位置：`docs/ethics.md:38`
- 站上寫法：「2023 年 8 月｜由國科會公告，**無強制性、無罰則**，但常被各機關與學校援引為原則」
- 原始出處：行政院院會議案頁（112-08-31）<https://www.ey.gov.tw/Page/448DE008087A1971/40c1a925-121d-4b6b-8f40-7e9e1a5401f2>；行政院新聞稿 <https://www.ey.gov.tw/Page/9277F759E41CCD91/e63572a7-fb79-4c02-9ea3-b731e7c06a56> 及其附件〈國科會新聞稿〉PDF（含指引草案全文）
  - 原文（院會議案頁）：「國科會研擬本指引……提出本指引草案，續將依程序簽核函頒各機關參考」
  - 原文（行政院新聞稿）：「行政院長陳建仁今（31）日在行政院會聽取國家科學及技術委員會『行政院及所屬機關（構）使用生成式AI參考指引（草案）』報告後表示……並函頒各機關參考」
  - 原文（指引總說明）：「研訂『行政院及所屬機關（構）使用生成式 AI 參考指引』，供各機關依循。各機關得視使用生成式 AI 之業務需求，參酌本參考指引另訂使用規範或內控管理措施。」；第九點「公營事業機構、公立學校、行政法人及政府捐助之財團法人使用生成式 AI，得準用本參考指引。」
- 判定：不精確
- 說明：程序上是國科會研擬，行政院會在 2023-08-31 通過，再由國科會「函頒」，不是單純「由國科會公告」。指引全文確實沒有罰則，但「無強制性」是站上的詮釋，原文寫的是「供各機關依循」。另外，公立學校適用的是「得準用」，站上沒有交代。
- 建議改法：「國科會研擬，2023 年 8 月 31 日行政院會通過後由國科會函頒各機關參考；性質為參考指引，條文未設罰則；公立學校『得準用』。」
- 查核日期：2026-10-23

#### ETH-07　行政院參考指引的原則清單
- 位置：`docs/ethics.md:65-70`
- 站上寫法：「須由**承辦人最終判斷，不可完全信任**／禁止向生成式 AI 提供未公開資訊或機密／應揭露使用程度與範圍／須查驗產出內容的正確性／遵守著作權、個人資料保護等規定／生成式 AI 為輔助工具，**使用者應自負其責**」
- 原始出處：同 ETH-06，指引草案十點全文（行政院附件 PDF）
  - 原文：「二、生成式 AI 產出之資訊，須由業務承辦人就其風險進行客觀且專業之最終判斷」；「四、業務承辧人不得向生成式 AI 提供涉及公務應保密、個人及未經機關（構）同意公開之資訊……但封閉式地端部署之生成式 AI 模型，須確認系統環境安全性後，方得依機密等級分級使用。」；「五、各機關不可完全信任生成式 AI 產出之資訊，亦不得以未經確認之產出內容直接作成行政行為或作為公務決策之唯一依據。」；「六、各機關使用生成式 AI 作為執行業務或提供服務輔助工具時，應適當揭露。」；「七、使用生成式 AI 應遵守資通安全、個人資料保護、著作權與相關資訊使用規定」
- 判定：不精確
- 說明：前四項大致可以對應原文。但第六點只寫「應適當揭露」，沒有「使用程度與範圍」。「使用者應自負其責」在十點條文裡找不到，最接近的是總說明的「問責」原則。第四點的「封閉式地端部署」例外，站上也沒有交代。
- 建議改法：把「應揭露使用程度與範圍」改成「作為業務輔助工具時應適當揭露（第六點）」；刪除「使用者應自負其責」，或改成「秉持負責任及可信賴之態度與問責原則（總說明）」。
- 查核日期：2026-10-23

#### ETH-08　COPE：AI 不能成為作者
- 位置：`docs/ethics.md:78-79`、`docs/ethics.md:231`
- 站上寫法：「根據出版倫理委員會（COPE）的立場，AI 工具無法為提交的研究負起責任，也無法承擔法律與專業責任。」
- 原始出處：COPE Position Statement "Authorship and AI tools"（2023-02-13），<https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools>；交叉參照 ICMJE Recommendations, "Use of AI by Authors"，<https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html>
  - 原文：COPE 官方頁對 curl 和 WebFetch 都回 Cloudflare 403，**未直接讀到全文**。搜尋引擎索引確認官方頁有這句："AI tools cannot meet the requirements for authorship as they cannot take responsibility for the submitted work."（此句不是我親自在原頁讀到的）。
  - ICMJE 原文（親自讀取）："Chatbots (such as ChatGPT) and other AI-assisted tools should not be listed as authors because they cannot be responsible for the accuracy, integrity, and originality of the work, and these responsibilities are required for authorship"
- 判定：正確（附存取限制說明）
- 說明：核心主張「AI 不能是作者，因為無法負責」，有 ICMJE 的原文支持，也和 COPE 官方頁的索引句一致。站上說的「法律責任」，對應的是 COPE 所說 AI 不是法律實體，因此不能聲明利益衝突、也不能管理著作權與授權。這部分我只取得二手摘要，沒有讀到原句。
- 建議改法：不需修改；可以在參考來源補上 COPE 與 ICMJE 的連結（目前頁尾都沒有列）。
- 查核日期：2026-10-23

#### ETH-09　最終責任在人類作者，必須驗證含引用在內的 AI 內容
- 位置：`docs/ethics.md:81-82`
- 站上寫法：「所有的學術錯誤……均由全體人類作者共同承擔。研究人員必須驗證所有 AI 生成內容，**包括文獻引用的準確性**。」
- 原始出處：Elsevier, "Generative AI policies for journals"，<https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals>；ICMJE（同 ETH-08）
  - 原文（Elsevier）："Carefully reviewing and verifying the accuracy, comprehensiveness, and impartiality of all AI-generated output (including checking the sources, as AI-generated references can be incorrect or fabricated)."
  - 原文（ICMJE）："Therefore, humans are responsible for any submitted material that included the use of AI-assisted technologies."
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-10　IEEE：在致謝說明工具與章節
- 位置：`docs/ethics.md:88`
- 站上寫法：「IEEE｜在致謝部分說明工具名稱與具體使用章節」
- 原始出處：IEEE Author Center, "Submission and Peer Review Policies"，<https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/>
  - 原文："The use of content generated by artificial intelligence (AI) in an article (including but not limited to text, figures, images, and code) shall be disclosed in the acknowledgments section of any article submitted to an IEEE publication. The AI system used shall be identified, and specific sections of the article that use AI-generated content shall be identified and accompanied by a brief explanation regarding the level at which the AI system was used to generate the content." ／ "The use of AI systems for editing and grammar enhancement is common practice and, as such, is generally outside the intent of the above policy. In this case, disclosure as noted above is not required, but recommended."
- 判定：正確
- 建議改法：不需修改（可以補一句「純語法潤飾不強制、但建議揭露」）。
- 查核日期：2026-10-23

#### ETH-11　Elsevier：參考文獻前獨立聲明段落與建議標題
- 位置：`docs/ethics.md:89`
- 站上寫法：「需在參考文獻前加獨立聲明段落，建議標題為『稿件準備過程中使用生成式 AI 與 AI 輔助技術的聲明』」
- 原始出處：Elsevier（同 ETH-09）
  - 原文："you must include a separate declaration section at the end of your manuscript, immediately before the references, titled for instance: 'Declaration of generative AI and AI-assisted technologies in the manuscript preparation process.'" ／ "Please note: Basic checks of grammar, spelling and punctuation do not need a declaration statement."
- 判定：正確
- 說明：標題譯法對應的是現行版本的 "manuscript preparation process"。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-12　ACS：致謝說明，較大範圍用在方法等章節
- 位置：`docs/ethics.md:90`
- 站上寫法：「ACS｜在致謝部分說明；使用範圍較大時在方法論等章節詳述」
- 原始出處：ACS Researcher Resources, AI policy，<https://researcher-resources.acs.org/publish/aipolicy>
  - 原文（經 WebFetch 讀取該頁引述的期刊作者須知）："The use of AI tools for text or image generation should be disclosed in the manuscript within the Acknowledgment section" ／ "For more substantial use cases or descriptions of AI tool use, authors should provide full details" "within the Methods or other appropriate section of the manuscript."
- 判定：正確
- 說明：curl 無法直接下載這頁，引文是 WebFetch 從頁面擷取的片段。另外，個別 ACS 期刊可能另有規定（例如有二手來源指出 ACS Catalysis 要求寫在 Methods），投稿時以該刊作者須知為準，這一點站上已經提醒。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-13　AIP：潤飾可讀性不需揭露；影響結論的用途寫在方法
- 位置：`docs/ethics.md:91`
- 站上寫法：「僅用於潤飾可讀性不需揭露；可能影響研究發現或結論的使用，須在方法論部分詳述」
- 原始出處：AIP Publishing, AI Policy，<https://publishing.aip.org/resources/researchers/policies-and-ethics/ai-policy/>
  - 原文（curl 回 403，改由 WebFetch 擷取）："improve the readability of original content created by the authors is permitted and does not require disclosure." ／ "AI use should be disclosed when it has the potential to affect the findings or conclusions of an article" ／ "Such uses of AI should be described in detail in the Methods section."
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-14　語法、拼寫檢查要不要揭露，依投稿單位而異
- 位置：`docs/ethics.md:93`、`docs/ethics.md:198`
- 站上寫法：「語法檢查、拼寫修正等是否需要揭露，依投稿單位政策而異」
- 原始出處：Elsevier（ETH-11）、IEEE（ETH-10）、AIP（ETH-13）
  - 原文：Elsevier "Basic checks of grammar, spelling and punctuation do not need a declaration statement."；IEEE "disclosure as noted above is not required, but recommended."
- 判定：正確
- 說明：三家的做法確實不同：Elsevier 不需要揭露，IEEE 建議揭露，AIP 對可讀性潤飾不需要揭露。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-15　「涉及人類受試者就要走 IRB」
- 位置：`docs/ethics.md:233`（另見 `docs/ethics.md:169`）
- 站上寫法：「涉及人類受試者就要走 IRB；資料進 AI 前先確認去識別化與同意範圍。」
- 原始出處：《人體研究法》第 5 條，<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020176>
  - 原文：「研究主持人實施研究前，應擬定計畫，經倫理審查委員會（以下簡稱審查會）審查通過，始得為之。但研究計畫屬主管機關公告得免審查之研究案件範圍者，不在此限。」
- 判定：不精確
- 說明：法律本身設有免審查的範圍。同站的 research-ethics-data.md 已經寫明「免審不等於自己判定不用送」，但重點回顧這句說成一律要走審查，和法條、和同站另一頁的細緻寫法都不一致。第 169 行的寫法（「都需留意所屬機構的倫理審查規定」）沒有問題。
- 建議改法：「涉及人或其資料的研究，先依所屬機構程序送 IRB／REC 判定（含是否屬免審範圍），不要自行認定免送。」

#### ETH-16　「《人體研究法》列有得免審查的案件」
- 位置：`docs/research-ethics-data.md:32`
- 站上寫法：「《人體研究法》列有得免審查的案件，但各機構如何確認、要不要申請證明，須看其程序。」
- 原始出處：《人體研究法》第 5 條第 1 項但書（原文見 ETH-15）
- 判定：不精確
- 說明：法律本身沒有列出案件，只授權主管機關（衛福部）「公告」得免審查的研究案件範圍。實際範圍在衛福部（前衛生署）的公告裡。臺大醫院 REC 頁面列的排除對象（未成年人、收容人、原住民、孕婦等），就是依據那份公告。
- 建議改法：「《人體研究法》第 5 條授權主管機關公告『得免審查之研究案件範圍』；是否符合免審，各機構多要求由審查會判定。」

#### ETH-17　臺大醫院 REC：是否免審由委員會判定
- 位置：`docs/research-ethics-data.md:32`、`docs/research-ethics-data.md:183`
- 站上寫法：「以臺大醫院研究倫理委員會為例，是否符合免審由委員會判定」
- 原始出處：臺大醫院研究倫理委員會「免審案」，<https://www.ntuh.gov.tw/RECO/Fpage.action?fid=5536>
  - 原文：「一、擬執行之人體研究是否符合免審條件，須送交研究倫理委員會判定。」
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-18　審查通過後才能實施；變更須經原審查會同意；審查分一般與簡易程序
- 位置：`docs/research-ethics-data.md:6`、`docs/research-ethics-data.md:17`、`docs/research-ethics-data.md:50`、`docs/research-ethics-data.md:194`
- 站上寫法：「需要審查的計畫，必須在核准後才招募或蒐集資料」；「可能是一般審查、簡易審查、免予審查的申請」；「若要改招募對象、題目、同意方式……先確認是否須提出變更」
- 原始出處：《人體研究法》第 5、8 條
  - 原文：第 5 條第 3 項「研究計畫內容變更時，應經原審查通過之審查會同意後，始得實施。」；第 8 條「研究計畫之審查，依其風險程度，分為一般程序及簡易程序。」
- 判定：正確
- 建議改法：不需修改（第 50 行可以補上法源「第 5 條第 3 項」）。

#### ETH-19　《人體研究法》第 14 條告知事項
- 位置：`docs/research-ethics-data.md:58`
- 站上寫法：「《人體研究法》第十四條列出的告知內容包括研究目的與方法、權益與個資保護、撤回方式、可預見風險、救濟措施，以及研究材料的保存期限與運用規劃。」
- 原始出處：《人體研究法》第 14 條
  - 原文：「二、研究目的及方法。……五、研究對象之權益及個人資料保護機制。六、研究對象得隨時撤回同意之權利及撤回之方式。七、可預見之風險及造成損害時之救濟措施。八、研究材料之保存期限及運用規劃。九、研究可能衍生之商業利益及其應用之約定。」
- 判定：正確
- 說明：站上用「包括」列出九款中的六項，沒有扭曲。沒列的是機構名稱與經費來源、主持人資料、聯絡人和商業利益。另外第 2 項規定「不得以強制、利誘或其他不正當方式為之」，和站上酬謝不宜過高的段落呼應。
- 建議改法：不需修改（可以補上「研究機構與經費來源、可能衍生之商業利益」）。

#### ETH-20　免除同意須由有權單位判定
- 位置：`docs/research-ethics-data.md:73`
- 站上寫法：「若研究擬免除部分或全部同意程序，應提出理由並由有權單位判定，不由研究者自行決定。」
- 原始出處：《人體研究法》第 12 條第 2 項
  - 原文：「研究計畫應依審查會審查通過之同意方式及內容，取得前項研究對象之同意。但屬主管機關公告得免取得同意之研究案件範圍者，不在此限。」
- 判定：正確
- 建議改法：不需修改。

#### ETH-21　未成年人、受拘禁者、原住民族另有更嚴格規定
- 位置：`docs/research-ethics-data.md:90`
- 站上寫法：「若招募未成年人、受拘禁者、原住民族或其他可能受不當脅迫的群體，另有更嚴格的法規與程序」
- 原始出處：《人體研究法》第 12、15 條；臺大醫院 REC 免審頁（ETH-17）
  - 原文：第 12 條「研究對象除胎兒或屍體外，以有意思能力之成年人為限。」；第 15 條「以研究原住民族為目的者，除依第十二條至第十四條規定外，並應諮詢、取得各該原住民族之同意；其研究結果之發表，亦同。」；臺大醫院 REC「研究案件非以未成年人、收容人、原住民、孕婦、身心障礙、精神病患、判斷受不當脅迫或無法以自由意願做決定者為研究對象……得免本會審查」
- 判定：正確
- 建議改法：不需修改。

#### ETH-22　「去連結」的法定定義
- 位置：`docs/research-ethics-data.md:147`
- 站上寫法：「去連結｜……依《人體研究法》定義，永久不能以任何方式連結、比對」
- 原始出處：《人體研究法》第 4 條第 3 款
  - 原文：「去連結：指將研究對象之人體檢體、自然人資料及其他有關之資料、資訊（以下簡稱研究材料）編碼或以其他方式處理後，使其與可供辨識研究對象之個人資料、資訊，永久不能以任何方式連結、比對之作業。」
- 判定：正確
- 建議改法：不需修改。

#### ETH-23　代碼化／假名化資料仍是個人資料；間接識別資訊
- 位置：`docs/research-ethics-data.md:136-146`
- 站上寫法：「代碼化／假名化｜持有對照表者仍可連回｜對照表分開保管，仍按個人資料保護」；「間接識別資訊：稀有職稱、精確地點……」
- 原始出處：《個人資料保護法》第 2 條第 1 款（民國 114 年 11 月 11 日修正版），<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021>
  - 原文：「個人資料：指自然人之姓名、出生年月日……社會活動及其他得以直接或間接方式識別該個人之資料。」
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### ETH-24　個資法連結的說明（蒐集告知、特定目的、利用、安全維護）與查證日期
- 位置：`docs/research-ethics-data.md:182`、`docs/research-ethics-data.md:187`
- 站上寫法：「《個人資料保護法》：蒐集告知、特定目的、利用與安全維護」；「法規與機構頁面查證日期：2026-09-04。」
- 原始出處：同 ETH-23
  - 原文：第 5 條「不得逾越特定目的之必要範圍」；第 8 條「……向當事人蒐集個人資料時，應明確告知當事人下列事項」；法規頁沿革附註「一百十四年十一月十一日修正第 1-1、12、18、21、22～26、41、47～49、52、53、55 條條文；增訂第 1-2、20-1、21-1～21-5、51-1、53-1 條條文……；刪除第 27 條條文，施行日期，由行政院定之。」；現行第 1-1 條「本法之主管機關為個人資料保護委員會。」
- 判定：正確
- 說明：說明文字沒錯。但讀者要留意，個資法在 2025-11-11 大修過：非公務機關安全維護義務原本在第 27 條，已刪除並改列他條，主管機關也改成個資會，部分條文的施行日期還沒定。如果讀者照舊資料找「第 27 條」，會找不到。
- 建議改法：可以補一句「本法於 2025 年 11 月修正，部分條文施行日期由行政院另定，引用條號前請查現行版本。」
- 查核日期：2026-10-23

---

### 第二部分：venues.md（VEN）

#### VEN-01　AIS Senior Scholars' List 擴編為 11 本（2023 年新增 DSS、I&M、I&O）
- 位置：`docs/venues.md:21-23`、`docs/venues.md:57`、`docs/venues.md:116`
- 站上寫法：「2023 年擴編後的『Senior Scholars' List of Premier Journals』，**共 11 本**……2023 年新增了 3 本：*Decision Support Systems*……*Information & Management*、*Information and Organization*」
- 原始出處：AIS College of Senior Scholars 公告，AISWorld 郵件論壇（2023-02-16），<https://lists.aisnet.org/pipermail/aisworld_lists.aisnet.org/20230216/047571.html>（aisnet.org 官方頁對 curl 和 WebFetch 回 403，改讀 AIS 自己的郵件論壇公告）
  - 原文："the task force recommended to the College of Senior Scholars that the following three journals should be added to the basket: Decision Support Systems (DSS), Information & Management (I&M), Information and Organization (I&O)" ／ "The CSS resolved to rename the SSB as the Senior Scholars List of Premier Journals." ／ "Thus, the new composition of the AIS CSS List of Premier Journals, with immediate effect, is:"（下列 11 本）
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-02　ICIS 2026 官方 track「共 12 個」
- 位置：`docs/venues.md:40`、`docs/venues.md:65`
- 站上寫法：「以 ICIS 2026 官方 tracks（共 12 個）為骨架」；「12 個 track，如 Cybersecurity and Privacy、Data Management and Analytics、Blockchain-DLT-Fintech 等」
- 原始出處：ICIS 2026 Track Descriptions，<https://icis2026.aisconferences.org/submissions/track-descriptions/>
  - 原文（頁面列出的 track 名稱，依序）："Conference theme: Digital collaboration and coexistence"、"General topics"、"Future of Work"、"Sustainability and environmental issues"、"Responsibility and Ethics"、"Societal impacts"、"Data management and analytics"、"Cybersecurity and privacy"、"Blockchain, DLT, and Fintech"、"Computational Design and Evaluation"、"Design, Development, and Project Management"、"Implementation and organizing"、"Human technology interaction"、"User behavior and engagement"、"Innovation and entrepreneurship"、"Organizational strategy, governance, and transformation"、"Platforms, sharing economy, and crowds"、"IoT, public IS, and infrastructures"、"Healthcare and wellbeing"、"Economics of digital, social, and mobile commerce"、"Policy and Regulations"、"Digital learning and pedagogy"、"Research methods, theories, and philosophy"、"Social media"
- 判定：錯誤
- 說明：官方頁有 24 個 track（含主題 track 與 General topics），每個 track 各有一段 "Track Chairs:"，共 24 段。我數了兩次都是 24，不是 12。
- 建議改法：把「共 12 個」「12 個 track」改成「共 24 個（含大會主題 track 與 General topics）」。
- 查核日期：2026-10-23

#### VEN-03　電子商務、人機互動、醫療資訊、數位學習是「ICIS track 沒單獨列出」的子領域
- 位置：`docs/venues.md:40`
- 站上寫法：「再補上幾個 ICIS track 沒單獨列出、但學界公認很活躍的子領域（電子商務、人機互動、醫療資訊、知識管理、數位學習）。」
- 原始出處：同 VEN-02
  - 原文：ICIS 2026 有 "Human technology interaction"、"Healthcare and wellbeing"、"Digital learning and pedagogy"、"Economics of digital, social, and mobile commerce" 四個 track。
- 判定：錯誤
- 說明：五個子領域裡有四個，ICIS 2026 其實都有對應的獨立 track，只有知識管理沒有。
- 建議改法：「再補上 ICIS 沒有獨立 track 的知識管理，並把電子商務、人機互動、醫療資訊、數位學習對應到 ICIS 2026 的 Economics of digital, social, and mobile commerce、Human technology interaction、Healthcare and wellbeing、Digital learning and pedagogy。」
- 查核日期：2026-10-23

#### VEN-04　ICIS 2026 投稿時程
- 位置：`docs/venues.md:65`
- 站上寫法：「投稿截止 2026/5/1（Lisbon 場），2026/2/11 開放投稿，2026/7/27 通知結果」
- 原始出處：ICIS 2026 Call for Papers & Important Dates，<https://icis2026.aisconferences.org/submissions/call-for-papers/>
  - 原文："Submission Opens: February 11, 2026" ／ "Submission Deadline: May 1 (Fri.), 2026, by 23:59 WEST (UTC +1) – Lisbon" ／ "Acceptance Notification: July 27, 2026" ／ "Please join us in Lisbon, Portugal for ICIS 2026"
- 判定：正確
- 說明：「Lisbon」在原文裡是指截止時間的時區（WEST），會議地點也在里斯本。7/27 是第一次錄取通知，9/25 還有一次 Final Acceptance Notification。
- 建議改法：不需修改（可以改成「2026/5/1 23:59 里斯本時間（WEST）」，比較清楚）。
- 查核日期：2026-10-23

#### VEN-05　ECIS 2026：26 個 track、2026/6/15–17 米蘭
- 位置：`docs/venues.md:66`
- 站上寫法：「26 個 track，含 Cybersecurity and Privacy、Digital Transformation、Blockchain & Fintech 等｜會議日期 2026/6/15–17（Milan）」
- 原始出處：ECIS 2026 Track Descriptions，<https://ecis2026.it/track-descriptions/>（curl 回 429，改由 WebFetch 讀取）
  - 原文："Track 01 | Conference Theme" 至 "Track 26 | Competences and Competence Management in an Augmented Digital World"；"Track 08 | Cybersecurity and Privacy"、"Track 09 | Digital Transformation"、"Track 21 | Blockchain & Fintech – Reimagining Financial Services through Decentralized Technologies"；"June 15–17, 2026: ECIS Main Conference"；地點為 Milan（Bocconi University）
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-06　PACIS 2026：22 個 track；投稿截止 3/8（延長）；7/4–8 雅加達
- 位置：`docs/venues.md:67`
- 站上寫法：「（22 個 track）｜投稿截止 2026/3/8（延長後），會議 2026/7/4–8（Jakarta）」
- 原始出處：PACIS 2026 Track Descriptions <https://pacis2026.aisconferences.org/submissions/track-descriptions/>；Call for Papers <https://pacis2026.aisconferences.org/submissions/call-for-papers/>
  - 原文（track 頁）："Track 1: Artificial Intelligence and Machine Learning" …… "Track 17: General Topics and the Future of IT"（頁面上最後一個 track 是 17）
  - 原文（CFP 頁）："encapsulated through eighteen tracks"；"March 1 March 8, 2026 (Extended): Submission deadline"；"in-person discussion from July 4th to 8th, 2026, in Jakarta, Indonesia"
- 判定：錯誤
- 說明：日期和地點都正確，但 track 數錯了。官方 track 頁列 17 個，CFP 文字寫 18 個，兩者都不是 22。我重新 grep 過整頁，沒有 Track 18 以上。
- 建議改法：把「22 個 track」改成「17 個 track（CFP 文字寫 18 個，以 track 頁為準）」，或直接刪掉數字。
- 查核日期：2026-10-23

#### VEN-07　AMCIS 2026：截止 3/1 17:00 PST，8/20–22 雷諾
- 位置：`docs/venues.md:68`
- 站上寫法：「投稿截止 2026/3/1 17:00 PST，會議 2026/8/20–22（Reno）」
- 原始出處：AMCIS 2026 Call for Papers，<https://amcis2026.aisconferences.org/submissions/call-for-papers/>
  - 原文："to the 32nd Americas Conference on Information Systems (AMCIS) in Reno, Nevada. From August 20-22, 2026" ／ "March 1, 2026 | 17:00 PST (Reno/Los Angeles)"
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-08　HICSS 2027（第 60 屆）：截止 6/15 23:59 HST，2027/1/5–8 大島
- 位置：`docs/venues.md:69`
- 站上寫法：「投稿截止 2026/6/15 23:59 HST，會議 2027/1/5–8（Big Island）」
- 原始出處：HICSS 首頁 <https://hicss.hawaii.edu/>；Authors 頁 <https://hicss.hawaii.edu/authors/>
  - 原文："The 60th Hawaii International Conference on System Sciences (HICSS) will take place at Hilton Waikoloa Village, Big Island on January 5-8, 2027." ／ "authors shall submit a full paper by June 15, 11:59pm HST."
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-09　Computers & Security 自 2024 年起暫停收 AI/ML 為主的投稿
- 位置：`docs/venues.md:46`、`docs/venues.md:119`
- 站上寫法：「該刊 2024 年起暫停收『以 AI/ML 為主要成分』的投稿，投稿前先確認現況」
- 原始出處：Elsevier, Computers & Security 期刊頁，<https://shop.elsevier.com/journals/computers-and-security/0167-4048>
  - 原文："AI and ML: As of early 2024, we have instituted a moratorium on consideration of submissions that feature AI or ML as significant components. Thus, submissions about applying an AI/ML technique to system security and privacy topics will not be considered. Also, items directed to the security of AI/ML systems themselves (such as LLM and federated learning) are out of scope" ／ "Cryptology: …submissions with some aspect of cryptology (including blockchains, watermarking, and steganography) as a principal component will not be considered for review."
- 判定：正確
- 說明：另外補充：該刊也不收以密碼學、**區塊鏈**為主要成分的稿件，對資管生同樣實用。
- 建議改法：不需修改；可以補「也不收以密碼學／區塊鏈為主要成分的稿件」。
- 查核日期：2026-10-23

#### VEN-10　JAIS：對主題、分析單位、理論、方法、哲學取向都開放；發展式審稿
- 位置：`docs/venues.md:30`
- 站上寫法：「對主題、分析單位、理論、方法、哲學取向都開放，走『發展式審稿』」
- 原始出處：JAIS About，<https://aisel.aisnet.org/jais/about.html>
  - 原文："It is inclusive in topics, level and unit of analysis, theory, method and philosophical and research approach" ／ "Developmental reviewing approach"
- 判定：正確
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-11　資訊管理學報：TSSCI、季刊（1、4、7、10 月）、雙匿名、第一輪約 4 個月
- 位置：`docs/venues.md:83`
- 站上寫法：「TSSCI 收錄，每年 1、4、7、10 月出刊（季刊），雙匿名審查，第一輪約 4 個月」
- 原始出處：國科會人社中心〈2024 年「臺灣人文及社會科學期刊評比暨核心期刊收錄」期刊名單〉，<https://www.hss.ntu.edu.tw/Files/WebPartsFile/960/>（2024年評比結果暨核心期刊名單_11502.pdf）；JIM 官網投稿說明 PDF（由 <https://jim-tw.com/> 連到 jim-tw.com/api/files/download/6fbe2f45-…）
  - 原文（人社中心）：「2024 年名單適用期間：2025 年 1 月 1 日至 2027 年 12 月 31 日止。」；表一「資訊管理學報……中華民國資訊管理學會……TSSCI」；表二分級結果「第二級」
  - 原文（JIM）："The JIM is published quarterly at the end of January, April, July, and October each year." ／ "the first round of reviews would be completed within four months after receiving submissions in the correct format." ／ "Submitted papers will undergo double-blind peer review by two scholars."
- 判定：正確
- 建議改法：不需修改（可以補「TSSCI 第二級，2024 年評比，適用至 2027 年底」）。
- 查核日期：2026-10-23

#### VEN-12　資訊管理學報投稿信箱、編輯部網址與投稿說明 PDF
- 位置：`docs/venues.md:83`
- 站上寫法：「編輯部：<https://eclab.nkust.edu.tw/>（國立高雄科技大學）；[投稿說明 PDF](https://eclab.nkust.edu.tw/submitjim/JIM_Call_for_Paper.pdf)……投稿信箱 submit.jim@gmail.com｜編輯部網站憑證鏈較舊，瀏覽器可能顯示『不安全』警告」
- 原始出處：JIM 官網投稿說明（同 VEN-11）；直接連 eclab.nkust.edu.tw 的實測結果
  - 原文（JIM）："The online submission system (https://jim-tw.com/jim) is the sole channel through which the Editorial Office receives manuscripts. All manuscripts must be submitted through the system; submissions by email are no longer accepted." ／ "If you do not receive a notification by then, please contact submit.jim@gmail.com"
  - 實測：<https://eclab.nkust.edu.tw/> 的內容只剩 `<meta http-equiv="refresh" content="0;url=https://jim-tw.com" />`；投稿說明 PDF 網址回 "404 Not Found"。憑證本身有效（*.nkust.edu.tw，TWCA，有效至 2027-03-25），但伺服器沒有送出中繼憑證（"unable to get local issuer certificate"）。
- 判定：錯誤
- 說明：官方明文寫「submissions by email are no longer accepted」，現在只能走線上系統，gmail 信箱只用來詢問審查進度，站上把它寫成「投稿信箱」會誤導讀者。編輯部網址已轉到 jim-tw.com，投稿說明 PDF 已失效。另外，問題是缺少中繼憑證，不是「憑證鏈較舊」。我第二次查核時把官方中繼憑證加進信任清單重新抓取，結果相同。
- 建議改法：「投稿：一律經線上系統 <https://jim-tw.com/jim>（官方已不受理 email 投稿）；進度詢問 submit.jim@gmail.com；投稿說明見 jim-tw.com 官網。」刪除 eclab 編輯部網址、舊 PDF 連結和憑證鏈的說明。
- 查核日期：2026-10-23

#### VEN-13　資訊管理學報「2025 年五年影響係數 0.333」
- 位置：`docs/venues.md:83`
- 站上寫法：「（2025 年五年影響係數 0.333，TSSCI 收錄）」
- 原始出處：查不到
  - 原文：未取得。
- 判定：查不到
- 說明：試過的地方：JIM 官網 jim-tw.com（含前端程式和 API 的公告、卷期資料，裡面沒有影響係數）、人社中心 2024 年評比名單（只有分級，沒有係數）、WebSearch 搜 TCI-HSS「資訊管理學報 五年影響係數」（沒有結果）。TCI-HSS 引用報告需要進資料庫查詢，這次沒有取得。
- 建議改法：補上出處和年度，例如「（TCI-HSS 20XX 年版期刊引用報告）」；無法提供出處就刪掉這個數字。
- 查核日期：2026-10-23

#### VEN-14　資訊管理學報「確實仍在正常發行」
- 位置：`docs/venues.md:83`
- 站上寫法：「期刊確實仍在正常發行」
- 原始出處：JIM 官網卷期 API（jim-tw.com/api/issues/volumes）和公告（jim-tw.com/api/official_website/posts）
  - 原文（API 回傳的最新卷）：`{"volume":32,"issues":[{"volume":32,"issue":3,"articleCount":4,"date":"2025-07"},{"volume":32,"issue":2,...,"date":"2025-04"},{"volume":32,"issue":1,...,"date":"2025-01"}]}`；最新公告標題「資訊管理學報32-3期(2025年7月號)出刊通知」（建立時間 2026/01/12）
- 判定：不精確
- 說明：照季刊時程，到 2026-10 應該已經出到 33 卷 3 期（2026-07），但官網目前列出的最新一期是 32(3)（2025-07 號），而且 2026 年 1 月才補公告。可能是網站搬遷後資料還沒補齊，也可能真的有出刊延遲。目前證據無法支持「正常發行」這個肯定說法。
- 建議改法：「期刊仍在發行（官網最新列出 32 卷 3 期，2025 年 7 月號；查核日 2026-10-23），投稿前請查官網最新卷期。」
- 查核日期：2026-10-23

#### VEN-15　電子商務學報：中華企業資源規劃學會、TSSCI「自 2006 年起」
- 位置：`docs/venues.md:84`
- 站上寫法：「中華企業資源規劃學會（CERPS）……TSSCI 收錄（自 2006 年起）」
- 原始出處：國科會人社中心「歷年資訊（2015年以前）」〈2005 年 TSSCI 資料庫收錄期刊名單〉（hss.ntu.edu.tw/Files/WebPartsFile/50/2005年（審查資料範圍：2002-2004）.PDF）；〈2024 年評比結果暨核心期刊名單〉
  - 原文（2005 年名單）：「2005 年期刊收錄名單如下表，新增期刊以『★』標示」，表中列「電子商務學報 ★」；名單說明寫明是「2005 年 12 月 26 日召開期刊評審委員會聯席會議」決議的。
  - 原文（2024 年名單）：「電子商務學報……中華企業資源規劃學會……TSSCI」，分級「第二級」
- 判定：不精確
- 說明：官方名單顯示，電子商務學報是在「2005 年」名單首次以新增期刊（★）收錄，之後 2006–2015 年各年名單都有，2024 年評比仍是 TSSCI 第二級。站上寫「2006 年」差了一年（可能是把 2005 年底開會、隔年適用混在一起）。出版單位正確。
- 建議改法：「TSSCI 收錄（2005 年名單起；2024 年評比為第二級，適用至 2027 年底）」。
- 查核日期：2026-10-23

#### VEN-16　電子商務學報舊網址轉到華藝 iPress
- 位置：`docs/venues.md:84`
- 站上寫法：「<https://www.ipress.tw/J0284>（華藝 iPress 投稿平台，舊網址 jeb.cerps.org.tw 已轉到這裡）」
- 原始出處：<http://jeb.cerps.org.tw/> 實測；中華企業資源規劃學會官網 <https://www.cerps.org.tw/zh-TW>
  - 原文：jeb.cerps.org.tw 回傳 `http-equiv="refresh" content="0; url=http://www.ipress.tw/j0284"`；學會官網的「電子商務學報」連結指向 `http://jeb.cerps.org.tw/`
- 判定：正確
- 說明：補充：iPress J0284 頁面的 ISSN 欄位顯示成 "10.6941/JCHC"，出版者欄位是空的，看起來是平台資料缺漏，讀者可能會困惑。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-17　電子商務學報：半年刊（6 月底、12 月底）、中英文皆可投
- 位置：`docs/venues.md:84`
- 站上寫法：「每年 6 月底、12 月底出刊（半年刊），中英文皆可投」
- 原始出處：查不到
- 判定：查不到
- 說明：試過的地方：iPress J0284（用 curl 和 WebFetch，頁面內容由前端動態載入，沒有刊期資訊）、CERPS 官網（只有連結）、WebSearch（只找到另一本《電子商務研究》〔國立臺北大學〕「每年六月、十二月各出版一期」，**名稱相近，不是同一本**）、Crossref journals 查詢（沒有收錄）。
- 建議改法：附上投稿須知的出處；如果找不到，就改成「出刊頻率以 iPress 期刊頁為準」。也請確認沒有和《電子商務研究》混淆。
- 查核日期：2026-10-23

#### VEN-18　ICIM 2026（第 37 屆）主題與時程
- 位置：`docs/venues.md:90`
- 站上寫法：「2026 年徵稿主題『數位轉型驅動跨域整合與協作治理創新』，徵稿 2026/3/8 起、截稿延長至 2026/4/10，會議 2026/5/16（國立臺北科技大學）」
- 原始出處：ICIM 2026 官網，<https://icim2026.com/>
  - 原文：「第37屆國際資訊管理學術研討會」「國立臺北科技大學 2026/05/16」「會議主題 AI Agent 領航，從對話到行動 數位轉型驅動跨域整合與協作治理創新」「線上投稿開始 2026年03月08日(日) 論文截稿日期（最後延長期限）2026年04月10日(五)」「主辦單位 中華民國資訊管理學會 國立臺北科技大學」
- 判定：不精確
- 說明：屆次、日期、地點和主辦單位都正確。但官網的「會議主題」有兩行，第一行是「AI Agent 領航，從對話到行動」，站上只引了第二行，等於漏掉主標。
- 建議改法：「會議主題『AI Agent 領航，從對話到行動——數位轉型驅動跨域整合與協作治理創新』」。
- 查核日期：2026-10-23

#### VEN-19　中華民國資訊管理學會官網「SSL 憑證已過期」
- 位置：`docs/venues.md:94-95`、`docs/venues.md:119`
- 站上寫法：「csim.org.tw 打開時顯示『不安全』，是真的｜中華民國資訊管理學會官網的 SSL 憑證已過期，瀏覽器會跳出警告。」；「CSIM 官網 SSL 憑證過期（研討會沒停辦）」
- 原始出處：對 <https://www.csim.org.tw/> 實測（curl -v）
  - 原文（憑證資訊）："subject: CN=csim.org.tw" ／ "start date: Oct 22 07:47:59 2026 GMT" ／ "expire date: Jan 20 07:47:58 2027 GMT" ／ "issuer: C=US; O=Let's Encrypt; CN=YE2"；HTTP 狀態 503，頁面標題「網站正在進行維護 | 中華民國資訊管理學會」
- 判定：錯誤
- 說明：查核當天，憑證是有效的 Let's Encrypt 憑證（2026-10-22 才換發），TLS 驗證正常，所以「憑證已過期，瀏覽器會跳出警告」不成立。網站目前的問題是維護中（503）。我重新連線確認過一次，結果相同。不過這類狀態會變，站上 2026-09 整理時可能確實過期過。
- 彙整補查（憑證透明度紀錄，<https://crt.sh/?q=csim.org.tw>）：www.csim.org.tw 前一張 GoDaddy 憑證效期為 2025-09-04 至 2026-09-03；之後的 Let's Encrypt 憑證 2026-09-21 才簽發（另一張 2026-10-22 簽發，即上面實測到的那張）。所以站上 2026-09-07 寫「憑證已過期」在當時是對的，只是到查核日已經過時。判定維持「錯誤」，指的是現在的狀態，不是當初寫錯。
- 建議改法：刪掉「SSL 憑證已過期」的警告框，改成「學會官網偶有維護或連線問題（2026-10-23 顯示維護中），打不開時改查本屆網站（如 icim2026.com）」；重點回顧那一條也一併修改。
- 查核日期：2026-10-23

#### VEN-20　TANET 2026 暨 ICS：北護主辦、9 大主題、時程
- 位置：`docs/venues.md:91`
- 站上寫法：「2026 年為國立臺北護理健康大學｜列出 9 大研究方向……｜投稿系統 2026/6/30 開放；徵稿截止分兩階段，第一階段 2026/9/20、第二階段 2026/10/9……；會議 2026/10/29–31」
- 原始出處：TANET 2026 官網，<https://tanet2026.ntunhs.edu.tw/>（伺服器沒有送中繼憑證，我從 AIA 取得 Sectigo 官方中繼憑證加入信任清單後驗證）
  - 原文：「2026年臺灣網際網路研討會(Taiwan Academic Network Conference)暨國際計算機會議(International Computer Symposium)由國立臺北護理健康大學主辦，謹訂於2026年10月29日(週四)至31日(週六)」；「本屆大會依研究主軸規劃為九大主題領域，涵蓋四十一個子領域」；「投稿系統開放 2026/06/30」「徵稿截止日 2026/09/20 (第一階段) 2026/10/09 (第二階段)」
- 判定：正確
- 說明：括號裡舉的例子（AI 與應用、生成式 AI……）其實是子領域，不是九大主題本身的名稱。九大主題是「全世代人工智慧」「數位創新與永續發展」等，但這不影響正確性。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### VEN-21　NCS 在 2021、2023、2025 年與 TANET 合辦；2026 年官網沒提到 NCS
- 位置：`docs/venues.md:92`、`docs/venues.md:119`
- 站上寫法：「2021、2023、2025 年都與 TANET 合辦為『TANET 暨 NCS』，**沒有單獨徵稿**。2026 年 TANET 改與國際計算機會議（ICS）合辦，官網沒有提到 NCS。」
- 原始出處：TANET2021 CFP（tanet2021.thu.edu.tw）、TANET 2023 會議手冊（tanet2023.nccu.edu.tw）、TANET 2025 官網（tanet2025.niu.edu.tw）、TANET 2026 官網
  - 原文：2021「2021 年臺灣網際網路研討會(TANET)暨全國計算機會議(NCS)的主題為『5G+AI 迎向新時代』」；2023「誠摰歡迎大家蒞臨 2023 臺灣網際網路研討會 TANET &全國計算機會議 NCS」「全國計算機會議（National Computer Symposium, NCS）每 2 年舉辦一次」；2025 官網選單有「NCS 論文」「NCS專門研討會(Workshop)」；2026 官網的協辦單位列了「中華民國電腦學會」，大會名稱是「暨國際計算機會議(International Computer Symposium)」
- 判定：正確
- 說明：補充：站上 NCS 的官方網址 <http://www.csroc.org.tw/ncs.php> 現在會 302 轉到學會首頁 /index.jsp，已經不是 NCS 專頁。
- 建議改法：不需修改；NCS 連結可以改成學會首頁 <http://www.csroc.org.tw/>，或加註「已轉址」。
- 查核日期：2026-10-23

---

### 小計

- 查核條數：45 條（ETH 24 條、VEN 21 條）
- 正確：30 條（ETH 19、VEN 11）
- 不精確：8 條（ETH 5、VEN 3）
- 錯誤：5 條（全部在 VEN）
- 查不到：2 條（全部在 VEN）

- 「錯誤」代號：VEN-02、VEN-03、VEN-06、VEN-12、VEN-19
- 「不精確」代號：ETH-02、ETH-06、ETH-07、ETH-15、ETH-16、VEN-14、VEN-15、VEN-18
- 「查不到」代號：VEN-13、VEN-17
- 判正確但附補充建議的條目：ETH-01（法條是「應予撤銷」）、ETH-08（COPE 原頁 403）、ETH-24（個資法 2025-11 修正）、VEN-09（另外也不收區塊鏈為主的稿件）、VEN-21（NCS 連結已轉址）

---

## 十、MTH：方法學

範圍：`docs/methodology.md`、`docs/method-dsr.md`、`docs/method-data.md`、`docs/method-secondary-data.md`、`docs/method-qualitative.md`、`docs/method-experiment.md`、`docs/systematic-review.md`、`docs/quant-analysis-basics.md`
查核日期：2026-10-23。

先說明：常見的 Peffers et al. (2007) DSRM、Gregor & Hevner (2013)、Arksey & O'Malley 五階段、Cohen 效果量門檻、Glaser & Strauss (1967)、precision／recall／F1 的定義公式，**這 8 頁都沒有出現**（已 grep 全部 8 頁，沒有這些作者名，也沒有這些定義或門檻），所以沒有列條目。PRISMA 2020 的「27 條」、PRISMA-ScR 的條目數，站上也都沒寫，只說它們是報告指引，見 MTH-25。

---

#### MTH-01　因果關係的三個條件：共變、時間先後、排除替代解釋
- 位置：`docs/methodology.md:59-61`、`docs/methodology.md:185`、`docs/method-experiment.md:19`
- 站上寫法：「1. **相關性**：X 與 Y 確實共變　2. **時間先後**：X 發生在 Y 之前　3. **排除其他解釋**：排除干擾因子（confounding factor）的替代解釋」
- 原始出處：Shadish, Cook & Campbell (2002), *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*, Houghton Mifflin, ch. 1（公開 PDF：https://iaes.cgiar.org/sites/default/files/pdf/147.pdf ）
  - 原文（PDF 文字層的字間空白遺失，以下只補回空格）："In a classic analysis formalized by the 19th-century philosopher John Stuart Mill, a causal relationship exists if (1) the cause preceded the effect, (2) the cause was related to the effect, and (3) we can find no plausible alternative explanation for the effect other than the cause."
- 判定：正確
- 說明：三條件與 SCC 的寫法一致。SCC 把它溯源到 Mill。
- 建議改法：不需修改。若要附出處，可加「（Shadish, Cook, & Campbell, 2002，承 J. S. Mill）」。

#### MTH-02　Nunamaker et al.（1990）的引句「沒有系統發展，研究沒有用；沒有研究，系統發展沒有根基」，以及「概念框架、架構設計與嚴謹評估」
- 位置：`docs/method-dsr.md:16-20`
- 站上寫法：「Nunamaker 等人（1990）因此提出強烈的主張：> 沒有系統發展，研究沒有用；沒有研究，系統發展沒有根基。他們確立了系統發展法的正當性，證明只要具備**概念框架、架構設計與嚴謹評估**，系統開發本身就是一種合法的研究方法。」
- 原始出處：Nunamaker, Chen & Purdin (1990), "Systems Development in Information Systems Research," *JMIS* 7(3), 89–106。JMIS 官網文章頁：https://jmis-web.org/articles/731
  - 未取得全文（Taylor & Francis 付費牆，OpenAlex 標為 closed）。以下是 JMIS 官網的摘要原文："It is the authors' belief that systems development and other research methodologies are complementary and that an integrated multi-dimensional and multimethodological approach will generate fruitful is research results."；"Progress in several application domains is reviewed to provide a basis upon which to argue that systems development is a valid research methodology."
- 判定：查不到
- 說明：摘要支持「系統發展是正當的研究方法、和其他方法互補」這個大方向。但站上用引言區塊呈現的那句話，在摘要裡找不到；WebSearch 找英文對應句也沒有結果，可能是轉述或二手中文教材的說法。「概念框架、架構設計」大概對應原文的研究流程，但沒有全文可以核對。
- 建議改法：拿掉引言格式，改成轉述，例如「Nunamaker 等人（1990）主張系統發展與其他研究方法互補，系統發展本身可以是正當的 IS 研究方法」。若要保留引句，須找到原文頁碼並附英文原句。

#### MTH-03　Nunamaker et al. 的參考文獻資訊不完整
- 位置：`docs/method-dsr.md:213`
- 站上寫法：「**參考文獻**：Nunamaker, Chen & Purdin (1990)；March & Smith (1995), *Decision Support Systems* 15(4)；…」
- 原始出處：Crossref `10.1080/07421222.1990.11517898`；JMIS 官網 https://jmis-web.org/articles/731
  - 原文（Crossref）：title "Systems Development in Information Systems Research"；container "Journal of Management Information Systems"；vol 7、issue 3、pages 89-106、issued 1990-12。JMIS 官網："Volume 7 Number 3 1990 pp. 89-106"。Hevner et al. (2004) 的參考文獻則寫成 "(7:3), Winter 1991a, pp. 89-106"。
- 判定：不精確
- 說明：作者和年份沒錯，但同一列的另外兩筆都附了刊名與卷期，這筆卻沒有，讀者無從查找。另外這期是 1990–91 冬季號，有些文獻寫成 1991，最好附 DOI 避免混淆。
- 建議改法：「Nunamaker, J. F., Jr., Chen, M., & Purdin, T. D. M. (1990). Systems development in information systems research. *Journal of Management Information Systems, 7*(3), 89–106. https://doi.org/10.1080/07421222.1990.11517898」

#### MTH-04　March & Smith (1995)：四種研究產出（構念、模型、方法、實例）與建置／評估兩種設計活動
- 位置：`docs/method-dsr.md:24-42`、`docs/method-dsr.md:204`
- 站上寫法：「四大研究產出 … 構念（Constructs）… 模型（Models）… 方法（Methods）… 實例（Instantiations）」；「建置（Build）：示範可行性 … 評估（Evaluate）：發展指標並測量績效」
- 原始出處：March & Smith (1995) 原文未取得（ScienceDirect 擋機器人，OpenAlex 標為 closed）。改用 March 本人也是共同作者的 Hevner, March, Park & Ram (2004), *MISQ* 28(1), p. 78 的轉述，全文 PDF：https://www.in.th-nuernberg.de/professors/Holl/Personal/Hevner_DesignScience_ISRes.pdf
  - 原文（Hevner et al., 2004）："March and Smith (1995) identify two design processes and four design artifacts produced by design-science research in IS. The two processes are build and evaluate. The artifacts are constructs, models, methods, and instantiations."；"Constructs provide the language in which problems and solutions are defined and communicated (Schön 1983). Models use constructs to represent a real world situation—the design problem and its solution space"
- 判定：正確
- 說明：四種產出、build/evaluate 的名稱與意涵都和 March 共同署名的 2004 文章一致。核對層級是同一作者群後來的轉述，不是 1995 年原文。
- 建議改法：不需修改。

#### MTH-05　March & Smith (1995)：理論化（Theorize）／驗證（Justify）屬於「自然科學範疇（用以輔助設計科學）」
- 位置：`docs/method-dsr.md:44-47`、`docs/method-dsr.md:62-68`（圖）、`docs/method-dsr.md:92`（圖說）
- 站上寫法：「**自然科學範疇（用以輔助設計科學）** - **理論化（Theorize）**：提出因果理論，解釋「為什麼有效？」 - **驗證（Justify）**：以科學證據測試理論是否成立」
- 原始出處：March & Smith (1995), *Decision Support Systems* 15(4), 251–266, https://doi.org/10.1016/0167-9236(94)00041-2
  - 未取得全文，也沒取得出版社摘要（ScienceDirect 與 BibSonomy 都有機器人驗證；Crossref 沒有摘要；OpenAlex 沒有摘要索引）。WebSearch 摘要提到的二手引句 "both design science and natural science activities are needed to insure that IT research is both relevant and effective" 我沒有在原文頁面讀到，不能當作逐字原文。
- 判定：查不到
- 說明：四種活動 build／evaluate／theorize／justify 的名稱是常見說法，但我沒拿到原文可以核對。站上把自然科學活動定位成「用以輔助設計科學」，這是站方的詮釋，原作可能是把兩者並列互補；沒有全文無法確定。
- 建議改法：把「（用以輔助設計科學）」改成「（與設計科學互補）」，等取得原文再決定。

#### MTH-06　Hevner et al. (2004) 七項指引的名稱與要求
- 位置：`docs/method-dsr.md:99-109`、`docs/method-dsr.md:155-182`（章節骨架對應）
- 站上寫法：「1 研究產出（Design as an Artifact）… 2 問題關聯性（Problem Relevance）… 3 研究評估（Design Evaluation）…（觀察、分析、實驗、測試或描述性論證）… 4 研究貢獻（Research Contributions）… 5 研究嚴謹性（Research Rigor）… 6 搜尋過程（Design as a Search Process）… 惡性問題（wicked problems）… 夠好（satisficing）… 7 研究溝通（Communication of Research）」
- 原始出處：Hevner et al. (2004), *MISQ* 28(1), Table 1 (p. 83)、Table 2 (p. 86)、pp. 80, 88–90。PDF 同 MTH-04。
  - 原文（Table 1）："Guideline 1: Design as an Artifact — Design-science research must produce a viable artifact in the form of a construct, a model, a method, or an instantiation." / "Guideline 2: Problem Relevance — The objective of design-science research is to develop technology-based solutions to important and relevant business problems." / "Guideline 3: Design Evaluation — The utility, quality, and efficacy of a design artifact must be rigorously demonstrated via well-executed evaluation methods." / "Guideline 4: Research Contributions — Effective design-science research must provide clear and verifiable contributions in the areas of the design artifact, design foundations, and/or design methodologies." / "Guideline 5: Research Rigor — Design-science research relies upon the application of rigorous methods in both the construction and evaluation of the design artifact." / "Guideline 6: Design as a Search Process — The search for an effective artifact requires utilizing available means to reach desired ends while satisfying laws in the problem environment." / "Guideline 7: Communication of Research — Design-science research must be presented effectively both to technology-oriented as well as management-oriented audiences."
  - Table 2 評估方法："1. Observational … 2. Analytical … 3. Experimental … 4. Testing … 5. Descriptive"
  - p. 89："In such situations, the search is for satisfactory solutions, i.e., satisficing (Simon 1996)"；p. 80："Design-science research in IS addresses what are considered to be wicked problems"
  - p. 88（G5）："We argue, along with behavioral IS researchers (Applegate 1999), that it is possible and necessary for all IS research paradigms to be both rigorous and relevant."
- 判定：正確
- 說明：七項名稱、順序、評估方法五類、wicked problems 與 satisficing 都和原文相符。有兩處小加工：G2 多了「而非純學術假設」，原文沒有；G5 寫「在嚴謹與實務相關性之間取得平衡」，原文的意思是兩者「都要做到」，不是取捨。這兩處不影響主體。
- 建議改法：主體不需修改。G5 可改為「建置與評估都要運用知識庫中的理論與方法；研究要同時兼顧嚴謹與實務相關」。

#### MTH-07　Hevner 七大規範是「公認」的、論文「必須明確回應這七點」、是「評審的檢查表」
- 位置：`docs/method-dsr.md:99`、`docs/method-dsr.md:111-112`、`docs/method-dsr.md:205`
- 站上寫法：「提出目前 IS 學界公認的七大規範。**一篇合格的系統發展研究論文，必須明確回應這七點：**」；「把七大規範當成論文的檢查表」；「Hevner 七大規範是評審的檢查表，逐條對照著寫。」
- 原始出處：Hevner et al. (2004), pp. 81–82（PDF 同 MTH-04）
  - 原文："Following Klein and Myers (1999), we advise against mandatory or rote use of the guidelines. Researchers, reviewers, and editors must use their creative skills and judgment to determine when, where, and how to apply each of the guidelines in a specific research project. However, we contend that each of these guidelines should be addressed in some manner for design-science research to be complete. How well the research satisfies the intent of each of the guidelines is then a matter for the reviewers, editors, and readers to determine."
- 判定：不精確
- 說明：原作確實主張每項指引都應「以某種方式」回應，但明確反對把它當成強制、機械式的清單。站上的「必須明確回應」「評審的檢查表」「公認」，口氣比原作強，也和作者的提醒相反。
- 建議改法：「Hevner 等人主張，完整的設計科學研究應以某種方式回應這七項指引；但他們也提醒不要強制、機械式地套用（advise against mandatory or rote use），要依專案判斷每項指引怎麼落實。」tip 標題可改為「把七大規範當成自我檢視的參考」。

#### MTH-08　Hevner (2004) 與 March & Smith (1995) 的書目
- 位置：`docs/method-dsr.md:99`、`docs/method-dsr.md:213`
- 站上寫法：「Hevner, March, Park & Ram (2004), *MIS Quarterly* 28(1), 75–105.」；「March & Smith (1995), *Decision Support Systems* 15(4)」
- 原始出處：Crossref `10.2307/25148625`、`10.1016/0167-9236(94)00041-2`；Hevner 原文 PDF 首頁頁尾
  - 原文：Hevner PDF 首頁頁尾 "MIS Quarterly Vol. 28 No. 1, pp. 75-105/March 2004"；Crossref 記為 pages "75-106"。March & Smith 在 Crossref 是 Decision Support Systems vol 15、issue 4、pages 251-266、issued 1995-12。
- 判定：正確
- 說明：作者、年份、刊名、卷期都對。Hevner 頁碼 75–105 和文章自己印的頁碼一致；Crossref 記成 75-106，可能把最後一頁也算進去。
- 建議改法：不需修改。可替 March & Smith 補上頁碼 251–266 和 DOI。

#### MTH-09　Boosting 的機制是「提高錯誤樣本的權重」（含 XGBoost），而且「可能過度擬合」
- 位置：`docs/method-data.md:49-53`、`docs/method-data.md:207`
- 站上寫法：「Boosting（如 AdaBoost、XGBoost）｜**提高錯誤樣本的權重**，讓後續模型專注學習困難資料，序列式訓練｜降低偏誤，**可能過度擬合**」
- 原始出處：Chen & Guestrin (2016), "XGBoost: A Scalable Tree Boosting System," KDD 2016, arXiv:1603.02754v3 §2.2–2.3, https://arxiv.org/abs/1603.02754
  - 原文："We review gradient tree boosting algorithms in this section."；"where g_i = ∂ŷ(t−1) l(yi, ŷ(t−1)) and h_i = ∂²ŷ(t−1) l(yi, ŷ(t−1)) are first and second order gradient statistics on the loss function."；"Besides the regularized objective mentioned in Sec. 2.1, two additional techniques are used to further prevent overfitting. The first technique is shrinkage … The second technique is column (feature) subsampling."
- 判定：不精確
- 說明：「提高錯誤樣本權重」描述的是 AdaBoost。XGBoost 是梯度提升：每一步擬合損失函數的一階／二階梯度，不是對錯分樣本重新加權，而且內建正則化、shrinkage 與欄位抽樣來防止過擬合。把兩者放在同一格，會讓讀者誤會 XGBoost 的原理。
- 建議改法：「Boosting：序列式訓練，後續模型針對前面模型的錯誤修正。AdaBoost 會提高錯分樣本的權重；梯度提升（如 XGBoost）則沿損失函數的梯度擬合殘差，並用正則化、學習率縮減與抽樣控制過擬合」。

#### MTH-10　Adam「收斂速度與訓練穩定性明顯優於基本梯度下降」
- 位置：`docs/method-data.md:103`
- 站上寫法：「**Adam（自適應動量估計法）**：根據歷史梯度資訊自動調整每個參數的學習率，收斂速度與訓練穩定性明顯優於基本梯度下降，是目前深度學習最廣泛使用的最佳化器之一。」
- 原始出處：Kingma & Ba (2015), "Adam: A Method for Stochastic Optimization," ICLR, arXiv:1412.6980v9；Wilson et al. (2017), "The Marginal Value of Adaptive Gradient Methods in Machine Learning," NeurIPS, arXiv:1705.08292
  - 原文（Kingma & Ba）："The method computes individual adaptive learning rates for different parameters from estimates of first and second moments of the gradients; the name Adam is derived from adaptive moment estimation."；"Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods."
  - 原文（Wilson et al.）："We observe that the solutions found by adaptive methods generalize worse (often significantly worse) than SGD, even when these solutions have better training performance. These results suggest that practitioners should reconsider the use of adaptive methods to train neural networks."
- 判定：不精確
- 說明：名稱與「每個參數各有自適應學習率」都正確。但「明顯優於」是過度概括：原作只說 "compares favorably"，後續研究也發現 Adam 的泛化有時明顯比 SGD 差。
- 建議改法：「…自動調整每個參數的學習率，通常收斂較快、對學習率較不敏感，是深度學習常用的最佳化器之一；但它的泛化表現不一定勝過 SGD，論文中應交代選擇理由與超參數。」

#### MTH-11　「詞袋模型效果通常較差，分散式向量表示效果明顯較好」是「一個穩定的實證結論」
- 位置：`docs/method-data.md:88`、`docs/method-data.md:91`
- 站上寫法：「一個穩定的實證結論：**詞袋模型效果通常較差，分散式向量表示（如 Word2Vec 以上）效果明顯較好。**」
- 原始出處：Wang & Manning (2012), "Baselines and Bigrams: Simple, Good Sentiment and Topic Classification," ACL 2012 (Short Papers), 90–94, https://aclanthology.org/P12-2018/ ；Joulin et al. (2016), "Bag of Tricks for Efficient Text Classification," arXiv:1607.01759
  - 原文（Wang & Manning）："Contrary to claims in the literature, we show that bag of features models are still strong performers on snippet sentiment classification tasks, with NB models generally outperforming the sophisticated, structure-sensitive models explored in recent work."
  - 原文（Joulin et al.）："Our experiments show that our fast text classifier fastText is often on par with deep learning classifiers in terms of accuracy, and many orders of magnitude faster for training and evaluation."
- 判定：不精確
- 說明：站上沒附出處，而且已有文獻直接指出詞袋加 n-gram 的線性模型在不少分類任務上很強，和深度方法不相上下。哪種表示較好要看任務、資料量與模型，稱為「穩定的實證結論」言過其實。站上建議「把詞袋當基準線一起報告」則是合理的。
- 建議改法：「分散式向量與預訓練模型在許多語意任務上表現較好，但詞袋／TF-IDF 加 n-gram 的線性模型在不少文本分類任務上仍是強基準（Wang & Manning, 2012），哪一種較好須以實驗比較，並把詞袋當基準線一起報告。」表格中「效果通常明顯優於詞袋」也一併改為「在許多任務上優於詞袋」。

#### MTH-12　類別不平衡時「應以 AUC 或 F1 作為主要判準」
- 附註：`docs/glossary.md:102` 的同類問題另見 STAT-18。
- 位置：`docs/method-data.md:159-161`、`docs/method-data.md:210`
- 站上寫法：「這種情況下應以 **AUC 或 F1** 作為主要判準，並同時報告 Precision 與 Recall」；「類別不平衡時用 AUC／F1，不要用 Accuracy。」
- 原始出處：Saito & Rehmsmeier (2015), "The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets," *PLoS ONE* 10(3): e0118432, https://doi.org/10.1371/journal.pone.0118432
  - 原文："We show here that the visual interpretability of ROC plots in the context of imbalanced datasets can be deceptive with respect to conclusions about the reliability of classification performance, owing to an intuitive but wrong interpretation of specificity. PRC plots, on the other hand, can provide the viewer with an accurate prediction of future classification performance due to the fact that they evaluate the fraction of true positives among positive predictions."
- 判定：不精確
- 說明：「Accuracy 在不平衡時會誤導」與 5%／95% 的算例都正確。但沒說明是哪一種 AUC 時，一般讀者會理解成 ROC-AUC；而 ROC 在嚴重不平衡時本身也可能讓人高估表現，PR 曲線／PR-AUC 較能反映少數類別。
- 建議改法：「…應以 PR-AUC（Precision-Recall 曲線下面積）或 F1 等聚焦少數類別的指標為主要判準；ROC-AUC 可以一併報告，但在嚴重不平衡時可能高估表現（Saito & Rehmsmeier, 2015）。」

#### MTH-13　PSM 只能平衡觀察得到的共變數
- 位置：`docs/method-data.md:182-186`
- 站上寫法：「依據觀察到的共變數估計每個個體『進入處理組』的傾向分數 … PSM 只能平衡**觀察得到**的共變數，無法處理未觀察到的干擾因子。」
- 原始出處：Rosenbaum & Rubin (1983), "The central role of the propensity score in observational studies for causal effects," *Biometrika* 70(1), 41–55, https://doi.org/10.1093/biomet/70.1.41
  - 摘要（經 OpenAlex 摘要索引取得，未讀全文）："The propensity score is the conditional probability of assignment to a particular treatment given a vector of observed covariates. Both large and small sample theory show that adjustment for the scalar propensity score is sufficient to remove bias due to all observed covariates."
- 判定：正確
- 說明：定義與限制都和原作一致。原作的保證只涵蓋「觀察到的共變數」。
- 建議改法：不需修改。

#### MTH-14　「授權資料」與 End User Licence；資料分公開／授權／受限
- 位置：`docs/method-secondary-data.md:52-57`
- 站上寫法：「**授權資料**｜註冊後使用、資料庫訂閱、API 或 End User Licence｜閱讀使用條款…」；「**受限資料**｜含敏感欄位，只能在安全環境或經申請使用」
- 原始出處：UK Data Service, "Access conditions", https://ukdataservice.ac.uk/find-data/access-conditions/
  - 原文："Safeguarded data: Safeguarded data collection can be downloaded by registering and accepting our End User Licence Agreement (PDF). Use of these data are subject to the terms and conditions of the End User Licence Agreement."；"Controlled data: Data that are very detailed, sensitive or confidential are accessed through the UKDS SecureLab, the UK Data Service Trusted Research Environment."
- 判定：正確
- 說明：「End User Licence」是 UK Data Service 的實際用語（英式拼法，全名 End User Licence Agreement）。站上公開／授權／受限的分法，大致對應 UKDS 的 open／safeguarded／controlled。
- 建議改法：不需修改。可寫成「End User Licence Agreement（如 UK Data Service）」，讓讀者知道出處。
- 查核日期：2026-10-23

#### MTH-15　著作權只保護表達，不保護觀念、方法、程序與事實
- 位置：`docs/method-secondary-data.md:59`、`docs/method-secondary-data.md:181`
- 站上寫法：「著作權保護具體表達，不保護觀念、方法、程序與事實」
- 原始出處：著作權法第 10 條之 1、第 9 條（全國法規資料庫，修正日期民國 111 年 06 月 15 日），https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=J0070017&flno=10-1
  - 原文（第 10-1 條）："依本法取得之著作權，其保護僅及於該著作之表達，而不及於其所表達之思想、程序、製程、系統、操作方法、概念、原理、發現。"
  - 原文（第 9 條第 1 項第 4 款）："單純為傳達事實之新聞報導所作成之語文著作。"
- 判定：正確
- 說明：思想／概念、程序、操作方法都在第 10-1 條明文排除。「事實」條文沒有直接寫，但「發現」以及第 9 條對單純事實報導的排除支持這個說法。
- 建議改法：不需修改。可補上「（著作權法第 10 條之 1）」。
- 查核日期：2026-10-23

#### MTH-16　檔案研究的來源原則（provenance）與原始秩序（original order）
- 位置：`docs/method-secondary-data.md:105-106`
- 站上寫法：「**來源原則（provenance）**：確認檔案由誰建立、保管與移轉，不把不同產生者的紀錄混成同一來源。**原始秩序（original order）**：盡量保留建立者原有的分類與排列…」
- 原始出處：Society of American Archivists, *Dictionary of Archives Terminology*，"provenance"、"original order"，https://dictionary.archivists.org/entry/provenance.html 、https://dictionary.archivists.org/entry/original-order.html
  - 原文："original order n. … the organization and sequence of records established by the creator of the records"；provenance 條目所引 Gilliland-Swetland 2000a："The principle of provenance has two components: records of the same provenance should not be mixed with those of a different provenance, and the archivist should maintain the original order in which the records were created and kept."
- 判定：正確
- 說明：兩個原則的定義都和 SAA 辭典一致。
- 建議改法：不需修改。

#### MTH-17　Kember 反思思考模型的四個層次是「描述 → 理解 → 反思 → 批判性反思」
- 位置：`docs/method-qualitative.md:169-173`、`docs/method-qualitative.md:282`
- 站上寫法：「可結合 **Kember 反思思考模型**的四個層次做分層編碼：描述（describing） → 理解（understanding） → 反思（reflection） → 批判性反思（critical reflection）」
- 原始出處：Kember, McKay, Sinclair & Wong (2008), "A four-category scheme for coding and assessing the level of reflection in written work," *Assessment & Evaluation in Higher Education* 33(4), 369–379, https://doi.org/10.1080/02602930701293355 ；Kember et al. (2000), "Development of a Questionnaire to Measure the Level of Reflective Thinking," *AEHE* 25(4), 381–395, https://doi.org/10.1080/713611442
  - 摘要（經 OpenAlex 摘要索引取得；Taylor & Francis 頁面被機器人驗證擋下，未讀全文）：2008 年："This article presents a protocol that can be used to guide the allocation of work to four categories, namely: habitual action/non‐reflection, understanding, reflection, and critical reflection."；2000 年："…led to the development of a four-scale instrument measuring four constructs; habitual action, understanding, reflection and critical reflection."
- 判定：錯誤
- 說明：Kember 的第一層是「習慣性行動／非反思」（habitual action/non-reflection），不是「描述（describing）」。兩篇摘要的寫法一致，已兩次查證。後三層正確。另外站上沒附 Kember 的年份與出處。
- 建議改法：「習慣性行動／非反思（habitual action / non-reflection）→ 理解（understanding）→ 反思（reflection）→ 批判性反思（critical reflection）（Kember et al., 2008）」，參考文獻補上 Kember, D., McKay, J., Sinclair, K., & Wong, F. K. Y. (2008). *Assessment & Evaluation in Higher Education, 33*(4), 369–379.

#### MTH-18　Lincoln & Guba (1985) 信實度四準則及對應的量化概念
- 位置：`docs/method-qualitative.md:183-190`、`docs/method-qualitative.md:274`、`docs/method-qualitative.md:282`
- 站上寫法：「Lincoln 與 Guba（1985）提出的四個對應判準：可信性（credibility）｜內部效度；可轉移性（transferability）｜外部效度；可靠性（dependability）｜信度；可確認性（confirmability）｜客觀性」
- 原始出處：1985 年原書（*Naturalistic Inquiry*, Sage）未取得全文。改用兩位原作者自己的 AERA 1988 會議論文 Lincoln & Guba (1988), "Criteria for Assessing Naturalistic Inquiries as Reports," ERIC ED297007，https://archive.org/download/ERIC_ED297007/ERIC_ED297007.pdf ，文中直接引用了 1985 原書 p. 301。
  - 原文："The four terms credibility, transferability, dependability and confirmability were established as the naturalist's equivalents for the more conventional rigor criteria of internal validity, external validity, reliablity and objectivity. The terms were adopted for the single purpose of making clear 'the inappropriateness of the conventional terms when applied to naturalistism and to provide a more logical and derivative relation to the naturalistic axioms' (Lincoln and Guba, 1985, p.301)."（"reliablity"、"naturalistism" 是原文的拼法）
- 判定：正確
- 說明：四個名稱與一對一的對應關係有原作者文字支持。「常見作法」一欄沒有核到原文：1985 原書把稽核（audit）同時用在 dependability 與 confirmability，站上把 audit trail 只放在可靠性，屬於簡化，但不構成錯誤。
- 建議改法：不需修改。若要更精確，可在可確認性一欄也加上「稽核軌跡」。

#### MTH-19　把「開放／主軸／選擇性」三層編碼當成紮根理論的通用程序
- 位置：`docs/method-qualitative.md:39`、`docs/method-qualitative.md:91-95`、`docs/method-qualitative.md:150-160`、`docs/method-qualitative.md:271`
- 站上寫法：「分析卻悄悄套用了紮根理論的三層編碼」；「4.1 紮根理論的三層編碼｜開放編碼…｜主軸編碼…｜選擇性編碼…」；「三層編碼是紮根理論的分析程序」；方法論來源列「Strauss 與 Corbin（1998）、Charmaz（2014）」
- 原始出處：Strauss & Corbin、Glaser、Charmaz 的原書都未取得全文。改用同儕審查的方法論文章 Chun Tie, Birks & Francis (2019), "Grounded theory research: A design framework for novice researchers," *SAGE Open Medicine* 7, https://doi.org/10.1177/2050312118822927 （Europe PMC 全文 PMC6318722）
  - 原文（Table 1，改編自 Birks & Mills）："Traditional: Open coding / Selective coding / Theoretical coding; Evolved: Open coding / Axial coding / Selective coding; Constructivist: Initial coding / Focused coding / Theoretical coding"；"Coding terminology in evolved GT refers to open (a procedure for developing categories of information), axial (an advanced procedure for interconnecting the categories) and selective coding (procedure for building a storyline from core codes that connects the categories)"
- 判定：不精確
- 說明：三層的內容描述大致符合 Strauss & Corbin 的版本。但「開放／主軸／選擇性」只是 Strauss & Corbin（evolved GT）的術語：Glaser 的古典紮根理論沒有主軸編碼，用的是 substantive（open, selective）＋ theoretical coding；站上同列為來源的 Charmaz（2014）用的則是 initial／focused／theoretical coding。寫成「紮根理論的三層編碼」，等於把一個流派當成整個方法。
- 建議改法：表頭改為「紮根理論的編碼（以 Strauss & Corbin 版本為例）」，並加一句：「不同流派用語不同：Glaser 採實質編碼（開放、選擇性）與理論編碼，Charmaz 採初始、聚焦與理論編碼。方法章應說明採用哪一個流派。」

#### MTH-20　Yin 個案研究：複現邏輯（相似結果／可預期的相反結果），不是抽樣邏輯
- 位置：`docs/method-qualitative.md:79-87`
- 站上寫法：「多重個案設計採『複現邏輯』（replication logic），不是抽樣邏輯——選第二、第三個案的理由是『預期會得到類似結果』或『預期會因為某個已知差異得到不同結果』」；「單一個案要說明其**代表性或極端性**」
- 原始出處：Yin (2018), *Case Study Research and Applications: Design and Methods* (6th ed.), Sage
  - 未取得全文。試過 WebSearch 找原句（"predicts similar results (a literal replication)"、"each case must be carefully selected so that it either"），只找到二手教材與摘要，沒有 Yin 書本身可讀的頁面。Hak & Dul (2009, ERIM ERS-2009-035-ORG) 只轉述 "Robert Yin states that replication is the attempt to find support for a proposition in a number of single case studies"，沒有逐字列出兩種複現。
- 判定：查不到
- 說明：多份二手來源和站上寫法一致：literal replication 是預期得到相似結果，theoretical replication 是因可預期的理由得到相反結果。但我沒有讀到 Yin 原文。另外，Yin 列的單一個案理由不只代表性（common）與極端性（unusual），還有 critical、revelatory、longitudinal，站上只列兩種，偏簡化。
- 建議改法：主體暫不修改。單一個案理由可改為「說明選它的理由（例如關鍵、極端或不尋常、常見、揭露性、縱貫）」，並請持有原書的人核對頁碼。

#### MTH-21　質性方法專書的書目（作者、年份、書名）
- 位置：`docs/method-qualitative.md:51`、`:63`、`:75`、`:87`、`:95`、`:107`、`:119`、`:282`
- 站上寫法：「Kvale & Brinkmann (2009), *InterViews*；Patton (2002), *Qualitative Research & Evaluation Methods*；Moustakas (1994)…；van Manen (1990)…；Clandinin & Connelly (2000)…；Riessman (2008)…；Yin (2018), *Case Study Research and Applications*；Strauss & Corbin (1998)…；Charmaz (2014)…；Hammersley & Atkinson (2007)…；Van Maanen (2011)…；Krippendorff (2018)…；Lincoln & Guba (1985), *Naturalistic Inquiry*」
- 原始出處：Open Library 書目 API（https://openlibrary.org/search.json ）；Crossref 書目查詢
  - 書目資料（Open Library 回傳）：Naturalistic inquiry—Lincoln, Guba, 1985, Sage；Qualitative research & evaluation methods—Patton, 2002；Phenomenological research methods—Moustakas, 1994；Researching lived experience—van Manen, 1990, SUNY Press；Narrative inquiry—Clandinin, Connelly, 2000, Jossey-Bass；Narrative methods for the human sciences—Riessman, 2007/2008, Sage；Case Study Research and Applications—Yin, 2017（第 6 版版權年 2018）, Sage；Basics of qualitative research—Strauss, 1990, 1998；Constructing grounded theory—Charmaz, 2006, 2014；Ethnography—Hammersley, Atkinson, 2007；Tales of the field—Van Maanen, 1988, 2011, University of Chicago Press；Content Analysis—Krippendorff, 2018；InterViews—Kvale, 2009 版
- 判定：正確
- 說明：作者、書名、年份都對得上實際版本（多為第 2 到第 6 版）。Hammersley & Atkinson 已有 2019 年第 4 版，Corbin & Strauss 有 2008 年起的新版，但站上引用的舊版年份本身沒錯。
- 建議改法：不需修改。若要更完整，可補版次與出版社。

#### MTH-22　Eisenhardt (1989) 與 Bowen (2009) 的期刊書目
- 位置：`docs/method-qualitative.md:87`、`docs/method-qualitative.md:119`、`docs/method-qualitative.md:282`
- 站上寫法：「Eisenhardt (1989), "Building Theories from Case Study Research"」；「Bowen (2009), "Document Analysis as a Qualitative Research Method"」
- 原始出處：Crossref `10.5465/amr.1989.4308385`（轉到 10.2307/258557）、`10.3316/QRJ0902027`
  - Crossref 回傳：Eisenhardt, "Building Theories from Case Study Research," The Academy of Management Review, vol 14, issue 4, page 532, issued 1989-10；Bowen, "Document Analysis as a Qualitative Research Method," Qualitative Research Journal, vol 9, issue 2, pages 27-40, issued 2009-08。
- 判定：正確
- 說明：作者、年份、篇名都正確。站上沒寫刊名卷期，但沒有寫錯。
- 建議改法：不需修改。可補成 *Academy of Management Review, 14*(4), 532–550 與 *Qualitative Research Journal, 9*(2), 27–40。

#### MTH-23　內部效度威脅表（含「需求特徵」）
- 位置：`docs/method-experiment.md:124-134`
- 站上寫法：「### 4.1 內部效度…｜歷史（history）｜成熟（maturation）｜測驗（testing）｜…Solomon 四組設計｜工具（instrumentation）｜選擇（selection）｜流失（mortality）｜迴歸假象｜需求特徵｜受試者猜到假設而配合｜掩飾研究目的、使用填充任務」
- 原始出處：Campbell & Stanley (1963), *Experimental and Quasi-Experimental Designs for Research*, pp. 5–6，https://jwilson.coe.uga.edu/emat7050/articles/CampbellStanley.pdf
  - 原文："Relevant to internal validity, eight different classes of extraneous variables will be presented … 1. History … 2. Maturation … 3. Testing … 4. Instrumentation … 5. Statistical regression … 6. Biases resulting in differential selection of respondents for the comparison groups. 7. Experimental mortality … 8. Selection-maturation interaction"；"The factors jeopardizing external validity or representativeness which will be discussed are: … 11. Reactive effects of experimental arrangements, which would preclude generalization about the effect of the experimental variable upon persons being exposed to it in nonexperimental settings."；設計名稱："5. The Solomon Four-Group Design"、"6. The Posttest-Only Control Group Design"
- 判定：不精確
- 說明：前七項和 Campbell & Stanley 的內部效度清單一致，Solomon 四組設計作為測驗效應的對策也正確。但「需求特徵／受試者猜到假設而配合」屬於實驗安排的反應性效應：Campbell & Stanley 把它列在外部效度（第 11 項），Shadish, Cook & Campbell (2002) 一般把它歸到建構效度（這點沒取得 2002 年該章全文逐字核對）。放在內部效度表，歸類不當。另外原清單第 8 項「選擇與成熟交互作用」沒有列入。
- 建議改法：把「需求特徵」移到 4.3 建構效度，或另寫一句「受試者猜測研究假設而配合（需求特徵）屬於實驗情境的反應性，傳統上歸在外部或建構效度」。內部效度表可補一列「選擇與其他因素的交互作用」。

#### MTH-24　彭明輝書中對實驗設計的三點歸納
- 位置：`docs/method-experiment.md:107-111`
- 站上寫法：「彭明輝書中對實驗設計的三點歸納…：1. 選擇最有利的實驗條件… 2. 設法隔離或排除其他干擾因素或雜訊的影響… 3. 當前兩項目標衝突時…」
- 原始出處：彭明輝《研究生完全求生手冊》（聯經）
  - 未取得原書。WebSearch 搜「彭明輝 實驗設計 選擇最有利的實驗條件」只找到書評與新聞，沒有原書段落；也沒找到彭明輝部落格的對應文章。
- 判定：查不到
- 說明：無法確認這三點是不是書中原有的歸納、用語是否忠於原書。
- 建議改法：請持有原書的人補上章節或頁碼。若是站方轉述，可改成「參考彭明輝《研究生完全求生手冊》第 X 章的觀點整理」。

#### MTH-25　PRISMA 2020 是報告指引（檢核表＋流程圖），PRISMA-ScR 供範疇回顧使用；不能當作研究方法或品質保證
- 位置：`docs/systematic-review.md:100-101`、`docs/systematic-review.md:254`、`docs/systematic-review.md:267`、`docs/systematic-review.md:279`
- 站上寫法：「PRISMA 2020 提供系統性回顧的報告檢核表與流程圖，PRISMA-ScR 則供範疇回顧使用。遵循清單有助於透明報告，但清單本身不會替你設計研究，也不能保證回顧品質。」
- 原始出處：Page et al. (2021), "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews," *BMJ* 372:n71, https://doi.org/10.1136/bmj.n71 （Europe PMC 全文 PMC8005924）；PRISMA 官網 https://www.prisma-statement.org/prisma-2020 、https://www.prisma-statement.org/scoping
  - 原文（Page et al.）："The PRISMA 2020 statement consists of a 27-item checklist, an expanded checklist that details reporting recommendations for each item, the PRISMA 2020 abstract checklist, and revised flow diagrams for original and updated reviews"；"PRISMA 2020 is not intended to guide systematic review conduct, for which comprehensive resources are available. … PRISMA 2020 should not be used to assess the conduct or methodological quality of systematic reviews; other tools exist for this purpose."
  - 原文（官網 scoping 頁）："The PRISMA extension for scoping reviews (PRISMA-ScR) was published in 2018. The checklist contains 20 essential reporting items and 2 optional items to include when completing a scoping review."
- 判定：正確
- 說明：和 PRISMA 2020 原文與官網說法一致。站上沒寫條目數，沒有出錯的地方。站上四個「正式資源」連結（PRISMA 2020、PRISMA-ScR、JBI Manual 10. Scoping reviews、Cochrane Handbook current）都回應 HTTP 200。
- 建議改法：不需修改。若要補數字：「PRISMA 2020 含 27 項檢核表；PRISMA-ScR 含 20 項必要與 2 項選擇性條目」。
- 查核日期：2026-10-23

#### MTH-26　統合分析是統計綜整技術，不是系統性回顧的同義詞
- 位置：`docs/systematic-review.md:19`、`docs/systematic-review.md:275`
- 站上寫法：「**統合分析（meta-analysis）是統計綜整技術，不是系統性回顧的同義詞。**」
- 原始出處：Page et al. (2021), *BMJ* 372:n71, Box 1 Glossary（Europe PMC PMC8005924）
  - 原文："Systematic review—A review that uses explicit, systematic methods to collate and synthesise findings of studies that address a clearly formulated question"；"Meta-analysis of effect estimates—A statistical technique used to synthesise results when study effect estimates and their variances are available, yielding a quantitative summary of results"
- 判定：正確
- 說明：PRISMA 2020 的詞彙表把兩者分開定義，統合分析是統計綜整的一種技術。
- 建議改法：不需修改。

#### MTH-27　範疇回顧的品質評讀「是否進行依目的而定」
- 位置：`docs/systematic-review.md:16`、`docs/systematic-review.md:211`、`docs/systematic-review.md:278`
- 站上寫法：「品質評讀｜…｜是否進行依目的而定；做或不做都要說明理由」；「範疇回顧若目的只是描繪證據分布，可以不做正式品質評讀」
- 原始出處：PRISMA-ScR Checklist（Tricco et al., 2018, *Ann Intern Med* 169(7), 467–473；官網 PDF https://www.prisma-statement.org/s/PRISMA-ScR-Fillable-Checklist_11Sept2019.pdf ）
  - 原文（Item 12）："Critical appraisal of individual sources of evidence§ — If done, provide a rationale for conducting a critical appraisal of included sources of evidence; describe the methods used and how this information was used in any data synthesis (if appropriate)."
- 判定：正確
- 說明：PRISMA-ScR 把品質評讀列為選擇性（"If done"），和站上說法一致。PRISMA-ScR 只要求「做了」要說明理由，「不做也要說明」是站方更嚴格的建議，不衝突。
- 建議改法：不需修改。
- 查核日期：2026-10-23

#### MTH-28　p 值的定義與它不代表的東西
- 位置：`docs/quant-analysis-basics.md:186`
- 站上寫法：「p 值只回答在特定模型與虛無假設下，觀察到目前或更極端資料的相容程度。它不表示效果大小、理論重要性、結果可重現的機率，也不能單獨判斷研究價值。」
- 原始出處：Wasserstein & Lazar (2016), "The ASA Statement on p-Values: Context, Process, and Purpose," *The American Statistician* 70(2), 129–133, https://doi.org/10.1080/00031305.2016.1154108 。逐字原文取自 ASA 新聞稿 PDF https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf ；期刊全文頁回 403，沒有讀到。
  - 原文："1. P-values can indicate how incompatible the data are with a specified statistical model. 2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone. 3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold. … 5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result. 6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis."
- 判定：正確
- 說明：「相容程度」「不表示效果大小與重要性」「不能單獨判斷」都和 ASA 六原則一致。「不表示結果可重現的機率」ASA 原則沒有明文，但屬於標準統計常識，不構成錯誤。
- 建議改法：不需修改。可附「（ASA, Wasserstein & Lazar, 2016）」。

---

### 小計

- 查核條目：28 條
- 正確：15 條（MTH-01、04、06、08、13、14、15、16、18、21、22、25、26、27、28）
- 不精確：8 條（MTH-03、07、09、10、11、12、19、23）
- 錯誤：1 條（MTH-17）
- 查不到：4 條（MTH-02、05、20、24）
- 合計：15 + 8 + 1 + 4 = 28

**錯誤**：MTH-17
**不精確**：MTH-03、MTH-07、MTH-09、MTH-10、MTH-11、MTH-12、MTH-19、MTH-23
