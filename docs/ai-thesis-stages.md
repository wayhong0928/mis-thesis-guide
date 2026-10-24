# 論文各階段用什麼：整合入口

> 這頁把本站、thesis-toolkit、論文筆記庫範本和 Claude Code 工作流程設定串起來，依論文的階段列出每一步可以用哪個資源。想從找文獻開始，照著重現整套流程，從這頁出發。每一站在網頁版和 Claude Code／Codex 兩條路線各用什麼，見[論文 AI 工作流全圖](ai-workflow-map.md)；這頁是用階段找資源的索引。

---

## 一、先讀這段：文獻最好自己讀過

這套流程能幫你找文獻、整理筆記、核對數字、檢查邏輯和文字，但每篇要寫進論文的文獻，最好自己讀過。AI 寫的筆記照樣會漏東西，也會把原文沒有的話寫進去；你沒讀過原文，就看不出哪裡漏了、哪裡錯了。論文裡每一句話由你負責，口試時被問到的也是你。

後面每個階段都有「回原文核對」這一欄，意思是 AI 給的東西要回 PDF 或原始資料對過，才算數。學術倫理與 AI 揭露怎麼寫，見[學術倫理與 AI 揭露](ethics.md)。

---

## 二、四個資源與說明網址

| 資源 | 做什麼用 | 說明網址 |
|---|---|---|
| mis-thesis-guide | 研究方法與論文寫作的知識庫，查觀念、查判準，也有提示詞範本 | <https://wayhong0928.github.io/mis-thesis-guide/> |
| mis-thesis-skills（內含 plugin `thesis-toolkit`） | 讓 Claude Code 照固定判準稽核研究題目與寫作，另有流程導覽 SKILL | <https://github.com/wayhong0928/mis-thesis-skills>，沒有獨立介紹網站 |
| thesis-notes-template | 下載就能用的 Obsidian 論文筆記庫：五種筆記模板、填寫規則、文獻矩陣、給 AI 的提示詞 | 介紹頁 <https://wayhong0928.github.io/thesis-notes-template/>，說明頁見[論文筆記庫範本](thesis-notes-template.md) |
| claude-workflow-template | Claude Code 的工作流程設定：接續進度、派工模板、獨立驗收。制度怎麼運作寫在它自己的網站，這裡不重寫 | <https://wayhong0928.github.io/claude-workflow-template/> |

---

## 三、階段表：每一步用什麼

骨架是 thesis-toolkit 的 `thesis-roadmap` 判斷的三個階段（找方向、稽核題目、稽核寫法），再加上它列為「thesis-toolkit 不管」的幾項。第 4、5、9 列在 `thesis-roadmap` 沒有對應的 SKILL，這裡依本站的頁面和筆記庫範本補上可用的資源，補上的部分不屬於 thesis-toolkit。

節號有兩套。「提示詞範本」指[AI 提示詞範本](prompts.md)的節；「範本 6.x」指[論文筆記庫範本](thesis-notes-template.md)第六節的小節。

| # | 階段 | thesis-toolkit 的 SKILL | 提示詞 | 筆記庫範本 | 本站頁面 | 回原文核對 |
|---|---|---|---|---|---|---|
| 1 | 找方向 | `research-direction-finding` | [提示詞範本](prompts.md) 10.1、1.1 | 無 | [從零開始](getting-started.md)第九節 | AI 提的方向要能指到真實存在的文獻，帶著那幾篇去跟指導教授談 |
| 2 | 稽核題目 | `research-question-audit` | [提示詞範本](prompts.md) 10.2、4.1、4.3、1.3 | `00_總覽/研究設計速查.md` | [研究問題、假說與研究架構](problem-design.md) | 缺口寫成「在這幾篇裡沒看到」，再到資料庫搜一次 |
| 3 | 找文獻 | 無 | [提示詞範本](prompts.md) 2.1、2.2、3.1 | 無 | [怎麼找、怎麼讀、怎麼選題目](finding-reading.md)、[AI 學術研究工具指南](tool-directory.md) | 每篇先確認文獻存在，再下載原文；搜尋工具給的摘要不能當原文引用 |
| 4 | 讀文獻與寫筆記（補） | 無 | [提示詞範本](prompts.md) 3.2、3.4；範本 6.1 到 6.3 | 三種文獻筆記模板、`文獻筆記填寫規則.md`、`prompt.md`、`文獻矩陣.base` | [文獻回顧與批判性思考](literature.md)、[文獻管理與知識庫](tools-knowledge.md)、[論文筆記庫範本](thesis-notes-template.md) | 數字、頁碼、構念名稱回 PDF 逐項打勾；範本 6.3 的核對要開新對話 |
| 5 | 構念整理與假說推演（補） | 無 | 範本 6.4 收料進構念卡、範本 6.5 推演卡健檢 | `07_模板/02_變數.md`、`07_模板/05_假設推演.md` | [論文筆記庫範本](thesis-notes-template.md)第六節、[研究問題、假說與研究架構](problem-design.md) | 隨機點幾個 `[[citekey]]` 回筆記，看那句話是不是真的在裡面 |
| 6 | 選方法、設計問卷 | 無 | [提示詞範本](prompts.md) 5.1、5.2 | `07_模板/06_方法.md` | [方法論選擇地圖](methodology.md)、[問卷調查法](method-survey.md) | 操作型定義和量表題項回原始論文核對，不用 AI 轉述的版本 |
| 7 | 統計分析 | 無 | [提示詞範本](prompts.md) 5.3 | 無 | [量化分析規劃與資料處理基礎](quant-analysis-basics.md) | AI 對結果的解讀，回你自己的輸出表逐項對 |
| 8 | 寫章節 | `academic-writing-discipline` | [提示詞範本](prompts.md) 10.3、6.1、6.2 | `04_論文草稿`（只有說明檔） | [論文架構與各章寫作要領](writing.md)、[學術中文寫作紀律](style.md) | 橫斷面資料不寫「導致」這類動詞；每個引用回原文確認作者真的這樣說 |
| 9 | 計畫書、口試、簡報（補） | `research-question-audit` 的對抗式審查 | [提示詞範本](prompts.md) 6.3、6.4 | 無 | [計畫書、口試與簡報](defense.md)、[學術倫理與 AI 揭露](ethics.md) | AI 揭露照系所和指導教授的規定寫；質詢清單的每一題都要能指回論文或文獻裡的位置 |
| 跨 | 長專案接力、派工、獨立驗收 | 無 | 無 | 無 | 只連 [claude-workflow-template 介紹頁](https://wayhong0928.github.io/claude-workflow-template/)，這裡不重寫 | 做的人不驗自己的活，細節見該站 |

不確定自己在哪個階段，可以直接對 Claude Code 說「我論文卡住了，不知道下一步」，thesis-toolkit 的 `thesis-roadmap` 會判斷階段並指出下一步。它只管前面三個稽核 SKILL 對應的階段，其餘的看上面這張表。

### 第 4 列的閱讀追蹤

筆記範本的每份文獻筆記，frontmatter 都有 `status` 欄（🌱 剛建立、🌿 充實中、🌳 可直接寫進論文），`文獻矩陣.base` 把它顯示成「狀態」欄。所以讀文獻時可以這樣追蹤進度：

1. 建筆記時先標 🌱，讀完全文、筆記能撐起論文某一句話時才改成 🌳。
2. 在 `文獻矩陣.base` 依狀態排序，看哪些還沒讀完。
3. 下一篇讀哪篇，從已讀筆記的第九節「值得追讀的參考文獻」挑，回原文核對過就填 `verified` 日期（這是建議做法）。

前兩點是範本本來就有的欄位和表格。第 3 點是站主的建議，範本沒有把它寫成固定流程。

---

## 四、兩個附加頁

- [用 Claude Code＋Zotero＋Obsidian 管理文獻與文獻筆記](ai-zotero-obsidian.md)：這套筆記庫怎麼接上 Zotero 和 Claude Code，從裝工具到寫筆記、核對、收料的順序，每一步指到範本和各 README 原本的段落。
- [整套安裝：一段 prompt 裝好論文工作環境](ai-full-install.md)：一段貼給你自己的 AI 的安裝 prompt，把筆記庫範本、Zotero、Obsidian 和 thesis-toolkit 裝好，Claude Code 的工作流程設定接到它自己的網站。

---

## 五、怎麼取得新版

| 資源 | 更新方式 |
|---|---|
| 本站 | 沒有訂閱機制，各頁改了什麼寫在[關於本站](about.md)的更新紀錄，需要時回來看 |
| thesis-toolkit | 在終端機跑 `claude plugin marketplace update mis-thesis-skills` 和 `claude plugin update thesis-toolkit@mis-thesis-skills`；或在 Claude Code 輸入 `/plugin`，到 Marketplaces 分頁選 `mis-thesis-skills`，開啟 Enable auto-update。更新後開新 session，或在正在用的 session 輸入 `/reload-plugins`。Codex 是把 SKILL 資料夾複製到 `.agents/skills/` 或建 symlink，複製的要下載新版再複製一次，symlink 的更新它指向的那份就好。各版改了什麼見該 repo 的 [CHANGELOG](https://github.com/wayhong0928/mis-thesis-skills/blob/main/plugins/thesis-toolkit/CHANGELOG.md) |
| thesis-notes-template | 只換 `07_模板/`、`00_總覽/文獻筆記填寫規則.md`、`00_總覽/prompt.md`。`00_總覽/術語表.md` 和 `00_總覽/研究設計速查.md` 是你填過的，不要覆蓋；`01_理論` 到 `06_方法` 放的是你的筆記，也不要動。不要把整包新版蓋過去 |
| claude-workflow-template | 照它 README 寫的更新方式 |

換 `07_模板/` 之前，如果你自己改過模板，先把改過的檔案另存一份再換，換完再把想留的改動補回去。舊筆記不用重寫，缺的欄位照新模板補上就好。
