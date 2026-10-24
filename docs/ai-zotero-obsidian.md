# 用 Claude Code＋Zotero＋Obsidian 管理文獻與文獻筆記

> 這頁說明[論文筆記庫範本](thesis-notes-template.md)怎麼和 Zotero、Claude Code 接在一起。Zotero 管文獻和 PDF，Obsidian 放筆記，Claude Code 讀 Zotero 裡的 PDF，再寫進 Obsidian 的筆記庫。這頁只講順序和每一步該看哪裡，原步驟和 prompt 都在範本說明頁與各 repo 的 README，這裡不改寫，只連過去。整體階段表見[論文各階段用什麼](ai-thesis-stages.md)。

---

## 一、分工與順序

| 工具 | 管什麼 |
|---|---|
| Zotero 加 Better BibTeX | 文獻清單、PDF、每篇文獻的 citekey（例如 `Davis1989`） |
| Obsidian | 筆記庫。文獻筆記的檔名就是 citekey，筆記之間用連結串起來 |
| Claude Code | 用 citekey 向 Better BibTeX 查出 PDF 在哪裡，讀完全文，照填寫規則寫進 `03_文獻筆記/` |

筆記庫和 Zotero 靠 citekey 對上，所以 citekey 公式要在寫第一份筆記之前設好，定了就不改。

整體順序是先裝工具，再設 citekey，接著寫筆記、換一個新對話核對，最後把核對過的筆記收進構念卡。下面五節各指到原本的段落。

文獻最好自己讀過。AI 寫的筆記可以拿來加速整理，但寫進論文之前，數字和頁碼要回 PDF 對過。

---

## 二、第一步：裝工具、下載範本

範本說明頁第六節 6.0 有一段貼給 Claude Code 或 Codex 的安裝 prompt，會裝好 Zotero、Obsidian、Python 和 PyMuPDF，下載範本，再一步一步帶你點完 Better BibTeX 和 Obsidian 的設定。見[論文筆記庫範本 6.0 安裝與匯入](thesis-notes-template.md#60-安裝與匯入只有-cli-版)。範本 repo 的 README 也有同樣的「用 AI 安裝」和「自己來」兩種做法，見 [thesis-notes-template README 的下載與開啟](https://github.com/wayhong0928/thesis-notes-template#下載與開啟)。

如果還要一起裝 thesis-toolkit 和 Claude Code 的工作流程設定，改用[整套安裝](ai-full-install.md)那一頁的 prompt。

安裝 prompt 的測試範圍寫在範本說明頁第七節。在 Zotero、Obsidian、Python 都已裝好的 Windows 電腦上，用 Claude Code 跑過；從零安裝和 Mac 都還沒測。

---

## 三、第二步：設好 citekey

Zotero 這邊要先做的事，在範本 README 的「第一週清單」和「Zotero 怎麼接」兩節，包括 Better BibTeX 的 citekey 公式、日期欄位格式、中文作者姓名單欄還是兩欄。見 [thesis-notes-template README](https://github.com/wayhong0928/thesis-notes-template#第一週清單)。

Zotero、Better BibTeX、校外連線和 Word 引用的細節，見[文獻管理與知識庫](tools-knowledge.md)。

---

## 四、第三步：寫文獻筆記，再開新對話核對

寫筆記和核對筆記的 prompt 在範本說明頁第六節，網頁版和 CLI 版各一份：

- [6.2 寫文獻筆記](thesis-notes-template.md#62-寫文獻筆記)
- [6.3 核對文獻筆記（一定要開新對話）](thesis-notes-template.md#63-核對文獻筆記一定要開新對話)

CLI 版會讀寫你電腦上的檔案，第一次用之前先看[Claude Code／Codex 一小時上手](ai-quickstart-agent.md)第三節的權限設定。填寫規則的重點見[論文筆記庫範本第五節](thesis-notes-template.md#五文獻筆記填寫規則重點)，完整規則在 repo 的 `00_總覽/文獻筆記填寫規則.md`。

寫的那個對話看不出自己的錯，所以核對一定換新對話。核對完，自己再回 PDF 看過，才把 `verified` 填上日期。

---

## 五、第四步：用狀態欄追蹤讀到哪

每份文獻筆記的 `status` 欄是 🌱、🌿、🌳 三種狀態，`00_總覽/文獻矩陣.base` 會把它排成一張表。這個追蹤方式和下一篇怎麼挑，寫在[論文各階段用什麼](ai-thesis-stages.md)第三節的「第 4 列的閱讀追蹤」。

---

## 六、第五步：收進構念卡、推演卡

累積幾張文獻筆記之後，用範本的兩段 prompt 往上整理：

- [6.4 收料進構念卡](thesis-notes-template.md#64-收料進構念卡)
- [6.5 推演卡健檢](thesis-notes-template.md#65-推演卡健檢)

這兩段在範本說明頁第七節寫明還沒實測。用的時候，每個 `[[citekey]]` 都回筆記確認那句話真的在裡面。

---

## 七、要更新的時候

範本更新時只換 `07_模板/`、`00_總覽/文獻筆記填寫規則.md` 和 `00_總覽/prompt.md`，不要整包覆蓋。細節見[論文各階段用什麼](ai-thesis-stages.md)第五節。
