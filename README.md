# 研究方法與論文寫作知識網絡

社會科學／資訊管理取向的研究方法知識庫。把學習筆記、方法論書籍、公開規範與 AI 輔助研究的實務，整理成一個可以反覆查閱的靜態網站與一組 Markdown 文件。

**線上入口**：`index.html`（GitHub Pages 啟用後即為站台首頁）

---

## 預設讀者

本站以**社會科學取向的資訊管理研究**為預設情境，主要讀者是研究所學生。統計判準、章節慣例與寫作規範都有領域限定，其他領域請以自身系所規範為準。

## AI 使用揭露

本站內容由作者規劃、篩選與審定，撰寫過程使用 AI 工具協助蒐集資料、查證出處與草擬文字。

站內引用的卷期、DOI 與連結均經工具查證並標明查證日期，但作者**尚未逐篇取得原文核對**。因此：

> **請勿直接引用本站的整理。** 需要引用時，一律回到 `docs/sources.md` 列出的原始文獻，自行取得原文、確認內容後再引用。

作者對本站公開的內容負責：發現錯誤請回報，作者會更正或撤下。

## 免責聲明

本站不是官方規範。實際要求一律以下列順序為準：

> 系所規定 → 指導教授意見 → 研究倫理審查委員會 → 投稿單位作者須知

站內的判準門檻（信效度、統計指標、格式慣例）會因領域與期刊而異，引用前請自行查證最新版本。

---

## 這是什麼

一份個人學習筆記的彙整，涵蓋五個區塊：

| 區塊 | 內容 |
|---|---|
| 研究的基礎 | 從零開始的第一個月、研究的本質與時程、怎麼找／怎麼讀／怎麼選題目、資訊管理研究的範疇、研究問題與假說、文獻回顧與批判性思考、理論的構成與評估、常用理論家族 |
| 研究方法 | 方法選擇地圖、問卷調查法、實驗法、系統發展法／DSR、演算法與資料分析、質性研究 |
| 論文寫作 | 論文架構與各章要領、學術中文寫作紀律、計畫書與口試簡報 |
| AI 輔助研究 | 工作流與三層架構、AI 學術研究工具指南、AI 代理工具懶人包（Claude Code／Skill／Plugin／Codex）、工具生態與風險、學術倫理與 AI 揭露 |
| 工具箱 | 文獻管理與知識庫、檢查清單、AI 提示詞範本、名詞與用語對照、延伸閱讀與資源指南 |

## 這不是什麼

- **不是官方規範**（見上方免責聲明）。
- **不包含任何特定研究的題目、架構或構念。** 所有寫作範例都是通用的教科書級範例。
- **不包含他人論文報告的內容摘要**，也**不重製參考書籍或講座的內容**——只列書目、連結與導讀評價。詳見 `docs/sources.md`。

---

## 目錄結構

```
.
├── index.html            首頁（知識地圖入口，由 build.py 產生）
├── build.py              從 docs/*.md 產生 pages/*.html 與 index.html
├── assets/
│   ├── style.css         共用樣式（含深色模式與列印樣式）
│   ├── site.js           導覽開合、篩選、目錄標示、檢查清單狀態
│   └── index.json        頁面索引（由 build.py 產生）
├── docs/                 ★ 內容來源，可直接在 Obsidian 開啟閱讀
│   ├── getting-started.md
│   ├── research-basics.md
│   ├── finding-reading.md
│   ├── is-research.md
│   ├── problem-design.md
│   ├── literature.md
│   ├── theory-building.md
│   ├── theories.md
│   ├── methodology.md
│   ├── method-survey.md
│   ├── method-experiment.md
│   ├── method-dsr.md
│   ├── method-data.md
│   ├── method-qualitative.md
│   ├── writing.md
│   ├── style.md
│   ├── defense.md
│   ├── ai-workflow.md
│   ├── tool-directory.md
│   ├── ai-agents.md
│   ├── ai-tools.md
│   ├── ethics.md
│   ├── tools-knowledge.md
│   ├── checklists.md
│   ├── prompts.md
│   ├── glossary.md
│   └── sources.md        延伸閱讀與資源指南
└── pages/                產生出來的 HTML（不要手動編輯）
```

**`docs/` 是唯一的內容來源（single source of truth）。** `pages/` 底下的 HTML 全部由 `build.py` 產生，手動改了下次重建就會被覆蓋。

---

## 怎麼修改內容

1. 編輯 `docs/` 底下對應的 `.md` 檔（可以直接在 Obsidian 裡改）
2. 重新產生 HTML：

```bash
pip install markdown        # 只需要一次
python3 build.py
```

3. commit 並 push

### 新增一頁

1. 在 `docs/` 建立 `新頁面.md`
2. 在 `build.py` 的 `NAV` 清單中，找到對應的區塊加入一列：
   `("新頁面", "頁面標題", "一句話說明")`
3. 執行 `python3 build.py`

導覽列、首頁卡片、上一頁／下一頁都會自動更新。

---

## Markdown 慣例

`build.py` 使用 Python-Markdown 的 `extra`、`toc`、`sane_lists`、`admonition` 擴充。

**提示框**：

```markdown
!!! warning "標題"
    內容需縮排四個空格。

!!! tip "標題"
!!! note "標題"
!!! danger "標題"
```

**可勾選的清單**：

```markdown
- [ ] 這一項會變成網頁上可以勾選的核取方塊
- [x] 預設打勾
```

勾選狀態存在瀏覽器的 `localStorage`，只在該裝置的該瀏覽器有效，清除網站資料就會消失。

**頁面之間的連結**：直接寫 `.md` 的相對連結，建置時會自動轉成 `.html`。

```markdown
見[文獻回顧](literature.md)
```

**每頁的 H1 會被移除**，標題統一由 `build.py` 的 `NAV` 提供，所以 `.md` 開頭的 `# 標題` 只是給 Obsidian 看的。

---

## 在本機預覽

直接用瀏覽器開 `index.html` 就可以（沒有用到任何需要伺服器的功能）。若想用本機伺服器：

```bash
python3 -m http.server 8000
# 然後開 http://localhost:8000
```

---

## 部署到 GitHub Pages

1. 把整個資料夾推到 GitHub repo
2. Repository → **Settings** → **Pages**
3. Source 選 **Deploy from a branch**，branch 選 `main`、資料夾選 `/ (root)`
4. 等待部署完成後即可透過 Pages 網址存取

> **關於公開範圍**：GitHub Pages 在免費方案下，即使 repo 是 private，發布出去的站台仍是**公開可存取**的。若需要限制存取，需使用付費方案的 private Pages，或改用其他有存取控制的靜態站台服務。**部署前請確認站內沒有不該公開的內容。**

repo 內已放置 `.nojekyll`，讓 GitHub Pages 直接輸出檔案，不經過 Jekyll 處理。

---

## 隱私與內容檢查

推送前建議跑一次：

```bash
# 檢查有沒有殘留的個人研究資訊（依自己的關鍵字調整）
grep -rniE "我的論文|本研究的構念|學號|真實姓名" docs/

# 檢查大陸用語
grep -rnE "被試|數據收集|信息|回歸分析|結果表明|人工智能|用戶|算法|數據庫|優化|場景|默認|受眾" docs/
```

---

## 授權與引用

本站採**雙授權**：

| 範圍 | 授權 |
|---|---|
| `docs/*.md` 內容與 `pages/*.html` 呈現的文字 | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)（姓名標示－非商業性－相同方式分享） |
| `build.py`、`assets/site.js`、`assets/style.css` 等程式碼 | [MIT License](LICENSE) |

- 本站是個人學習筆記，供自己與同儕參考。
- 引用自書籍、論文與官方文件的部分，著作權屬於原作者與原出版單位，不受本站授權條款影響。
- 若要引用站內整理的觀念，請追溯到 `docs/sources.md` 列出的原始出處引用。

---

## 待辦

- [ ] 依系所的最新論文格式規定，核對「台灣碩論章節慣例」一節
- [ ] 投稿目標期刊確定後，補上該期刊的 AI 使用政策
- [ ] 定期回頭確認法規與期刊政策是否更新（建議每學期一次）
