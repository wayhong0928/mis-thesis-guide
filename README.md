# 研究方法與論文寫作知識網絡

社會科學／資訊管理取向的研究方法知識庫。把學習筆記、方法論書籍、公開規範與 AI 輔助研究的實務，整理成一個可以反覆查閱的靜態網站與一組 Markdown 文件。

**網站**：<https://wayhong0928.github.io/mis-thesis-guide/>

本站是個人學習筆記，撰寫時使用 AI 工具協助蒐集資料與草擬文字，內容由作者審定。不是官方規範，實際要求以系所規定與指導教授為準；需要引用時請回到原始文獻。

## 預設讀者

本站以**社會科學取向的資訊管理研究**為預設情境，主要讀者是研究所學生。統計判準、章節慣例與寫作規範都有領域限定，其他領域請以自身系所規範為準。

## 從哪裡開始

| 資源 | 適合誰 |
|---|---|
| [一小時上手](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart.html) | 只用 ChatGPT、Claude、Gemini 網頁版，想在一小時內建好論文助手（另有 [Claude Code、Codex 版](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart-agent.html)） |
| [thesis-notes-template](https://github.com/wayhong0928/thesis-notes-template) | 想用 Obsidian 做文獻筆記，要現成的模板和填寫規則 |
| [mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills) | 用 Claude Code 或 Codex，想讓 AI 照固定判準檢查題目與寫作 |

## 這是什麼

一份個人學習筆記的彙整，涵蓋六個區塊：

| 區塊 | 內容 |
|---|---|
| 研究的基礎 | 從零開始的第一個月、研究的本質與時程、怎麼找／怎麼讀／怎麼選題目、期刊與研討會清單、資訊管理研究的範疇、研究問題與假說、文獻回顧與批判性思考、理論的構成與評估、常用理論家族 |
| 研究方法 | 方法選擇地圖、研究倫理與資料管理、系統性／範疇回顧、量化分析規劃與資料處理、問卷調查法、實驗法、系統發展法／DSR、演算法與資料分析、次級資料／檔案研究、質性研究 |
| 論文寫作 | 論文架構與各章要領、學術中文寫作紀律、計畫書與口試簡報、口試後修訂／典藏／結案 |
| AI 輔助研究 | 工作流與三層架構、AI 工具生態與風險、學術倫理與 AI 揭露——放方法論判斷與紅線 |
| AI 工具與技術環境 | AI 工具本身怎麼設定、怎麼選，放在 [ai-agent-notes](https://wayhong0928.github.io/ai-agent-notes/)，本站只留導引頁 |
| 工具箱 | 文獻管理與知識庫、AI 學術研究工具指南、檢查清單、AI 提示詞範本、名詞與用語對照、延伸閱讀與資源指南、關於本站 |

## 這不是什麼

- **不是官方規範**（見開頭的聲明）。
- **不包含任何特定研究的題目、架構或構念。** 所有寫作範例都是通用的教科書級範例。
- **不包含他人論文報告的內容摘要**，也**不重製參考書籍或講座的內容**——只列書目、連結與導讀評價。詳見 `docs/about.md`。

## 檔案配置

```
docs/      內容來源（Markdown，可以直接在 Obsidian 開啟閱讀）
pages/     由 build.py 產生的 HTML，不要手動編輯
assets/    共用樣式與網頁腳本
build.py   從 docs/ 產生 pages/ 與 index.html
```

想修改內容、新增頁面或自己架一份，見 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 回報問題與更新

內容有錯請到 [Issues](https://github.com/wayhong0928/mis-thesis-guide/issues) 回報，作者會更正或撤下。法規與期刊政策每學期查核一次（上一輪是 2026-09）；各頁改了什麼，見[關於本站](https://wayhong0928.github.io/mis-thesis-guide/pages/about.html)的更新紀錄。

## 授權與引用

本站採**雙授權**：

| 範圍 | 授權 |
|---|---|
| `docs/*.md` 內容與 `pages/*.html` 呈現的文字 | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)（姓名標示－非商業性－相同方式分享） |
| `build.py`、`assets/site.js`、`assets/style.css` 等程式碼 | [MIT License](LICENSE) |

- 本站是個人學習筆記，供自己與同儕參考。
- 引用自書籍、論文與官方文件的部分，著作權屬於原作者與原出版單位，不受本站授權條款影響。
- 若要引用站內整理的觀念，請追溯到 `docs/about.md` 列出的原始出處引用。
