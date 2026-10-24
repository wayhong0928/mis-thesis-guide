# 整套安裝：一段 prompt 裝好論文工作環境

> 這頁給一段貼給你自己的 AI（Claude Code）的安裝 prompt，把論文筆記庫範本、Zotero、Obsidian 和 thesis-toolkit 一次裝好，最後帶你接上 Claude Code 的工作流程設定。prompt 的內容取自各 repo 原本的安裝段落，Claude Code 工作流程怎麼運作，寫在 claude-workflow-template 自己的網站，這頁只連過去。整體階段表見[論文各階段用什麼](ai-thesis-stages.md)。

---

## 一、會裝什麼

| 項目 | 用途 | 原本的說明 |
|---|---|---|
| Zotero、Better BibTeX、Obsidian、Python 和 PyMuPDF，加上論文筆記庫範本 | 管文獻、放筆記、讓 AI 讀 PDF 寫筆記 | [論文筆記庫範本 6.0](thesis-notes-template.md#60-安裝與匯入只有-cli-版)，repo 的 `00_總覽/prompt.md` 第 0 段 |
| thesis-toolkit（Claude Code plugin） | 稽核研究題目與學術寫作 | [mis-thesis-skills README](https://github.com/wayhong0928/mis-thesis-skills#安裝方式) |
| claude-workflow-template（Claude Code 工作流程設定，選用） | 接續進度、派工模板、獨立驗收 | [claude-workflow-template 網站](https://wayhong0928.github.io/claude-workflow-template/) |

需要 Claude Code 登入，官方列的帳號類型是 Pro、Max、Team、Enterprise 付費方案，或 Claude Console。沒有付費方案的話，用[網頁版一小時上手](ai-quickstart.md)。安裝只在 Windows 實機測過一部分，Mac 和從零安裝沒測過，細節見[論文筆記庫範本第七節](thesis-notes-template.md#七這些提示詞測過哪些)。

文獻最好自己讀過。裝好的工具是加速整理，寫進論文的每一篇，自己要讀過原文。

---

## 二、怎麼用

1. 在終端機進到你想放論文資料的上層資料夾，打 `claude` 開 Claude Code。
2. 把下面整段貼給它。每一步它會先說要跑什麼，等你同意才做。
3. 它會在畫面上一步一步請你點 Zotero 和 Obsidian 的設定，你說「好了」才進下一步。
4. 做完照第三節檢查。

```text
請幫我裝論文工作環境。每一步先說你要做什麼、要跑什麼指令，等我同意再做；已經裝好的就跳過。不要修改 Zotero 或 Obsidian 的設定檔，設定都由我在畫面上操作。

第一部分，論文筆記庫、Zotero、Obsidian：
1. 讀 https://raw.githubusercontent.com/wayhong0928/thesis-notes-template/main/00_總覽/prompt.md ，找到標題「0. 安裝與匯入（只有 CLI 版）」下面的 prompt，照裡面的第 1 到 8 步做。讀不到這個檔案就停下來告訴我，不要自己編步驟。

第二部分，thesis-toolkit：
2. 跑 claude plugin marketplace add wayhong0928/mis-thesis-skills
3. 跑 claude plugin install thesis-toolkit@mis-thesis-skills
4. 告訴我要關掉 Claude Code 重開，新的 session 才會載入。

第三部分，Claude Code 工作流程設定（選用，先問我要不要裝）：
5. 我說要裝的話，請我關掉 Claude Code，在第一部分下載的筆記庫資料夾重新打 claude。
6. 在那個資料夾，請我打開 https://wayhong0928.github.io/claude-workflow-template/ ，照網站上的安裝說明做。裝法、版本需求和更新方式以那個網站與它的 README 為準，這裡不重複。

最後回報：哪些是這次裝的、哪些原本就有、哪一步失敗或被我跳過。
```

---

## 三、AI 做完後你要檢查

- 在 Zotero 的文獻清單上按右鍵，選單裡有 Better BibTeX。
- Obsidian 左側看得到 `00_總覽` 到 `07_模板` 八個資料夾。
- 重開 `claude` 後輸入 `/plugin`，已安裝清單裡有 `thesis-toolkit`。
- 有裝工作流程設定的話，輸入 `/hooks`，檢查項目見 [claude-workflow-template 的 README](https://github.com/wayhong0928/claude-workflow-template#readme) 安裝一節。

裝好之後接著做什麼，見[用 Claude Code＋Zotero＋Obsidian 管理文獻與文獻筆記](ai-zotero-obsidian.md)。

---

## 四、只想裝其中一部分

- 只要筆記庫和 Zotero、Obsidian：用[論文筆記庫範本 6.0](thesis-notes-template.md#60-安裝與匯入只有-cli-版)那一段就好。
- 只要 thesis-toolkit：照 [mis-thesis-skills README 的安裝方式](https://github.com/wayhong0928/mis-thesis-skills#安裝方式)。Codex、Claude.ai 網頁版的裝法也在那裡。
- 只要 Claude Code 工作流程設定：看 [claude-workflow-template 網站](https://wayhong0928.github.io/claude-workflow-template/)。

更新方式見[論文各階段用什麼](ai-thesis-stages.md)第五節。
