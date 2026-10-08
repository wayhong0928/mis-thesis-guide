# 維護說明

這份寫給要修改內容、新增頁面，或想自己架一份網站的人。只是要讀內容的話，直接看[網站](https://wayhong0928.github.io/mis-thesis-guide/)就好。

## 檔案配置

```
docs/      內容來源（Markdown，可以直接在 Obsidian 開啟閱讀）
pages/     由 build.py 產生的 HTML，不要手動編輯
assets/    共用樣式與網頁腳本
build.py   從 docs/ 產生 pages/ 與 index.html
```

**`docs/` 是唯一的內容來源（single source of truth）。** `pages/` 底下的 HTML 全部由 `build.py` 產生，手動改了下次重建就會被覆蓋。

逐頁清單以 `build.py` 的 `NAV` 為準，這裡不另外列，免得兩邊不同步。

---

## 怎麼修改內容

1. 編輯 `docs/` 底下對應的 `.md` 檔（可以直接在 Obsidian 裡改）
2. 重新產生 HTML：

```bash
pip install markdown        # 只需要一次
python3 build.py
```

> **Windows 使用者注意**：主控台預設編碼（cp950）下直接執行可能在印出進度訊息時噴 `UnicodeEncodeError` 而中斷——檔案通常已經正確寫完，只是腳本印訊息時掛掉，不代表資料流失。建議先設定環境變數再執行：`set PYTHONIOENCODING=utf-8`（cmd）或 `$env:PYTHONIOENCODING="utf-8"`（PowerShell）。

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

推送前建議跑一次檢查腳本（只用 Python 標準函式庫，Windows 與 Linux 皆可執行）：

```bash
python scripts/precheck.py                 # 檢查 docs/ 底下所有 .md
python scripts/precheck.py docs/style.md   # 指定其他檔案或目錄
python scripts/precheck.py --warn-only     # 只列出命中，不讓結束碼變成 1
```

腳本會依「個資」與「大陸用語」兩組列出命中的 `路徑:行號: 命中的詞 | 該行內容`，最後印出各組筆數。沒有命中時結束碼為 0，有命中為 1（加 `--warn-only` 則一律為 0），路徑不存在或檔案無法以 UTF-8 讀取時為 2。關鍵字清單放在 `scripts/precheck.py` 開頭的常數，依自己的需要增減；「演算法」不會被當成「算法」命中。

`style.md`、`glossary.md`、`checklists.md`、`prompts.md` 本來就列了這些詞當反例，所以結束碼現在一定是 1。看的方法是逐筆確認命中處是刻意寫的反例，不是要把結束碼壓到 0；要接進 pre-push hook，得先把這幾頁排除或改成 `--warn-only`。

沒有 Python 時，可以改用以下兩道 grep 手動檢查，結果與腳本相同：

```bash
# 檢查有沒有殘留的個人研究資訊（依自己的關鍵字調整）
grep -rniE "我的論文|本研究的構念|學號|真實姓名" docs/

# 檢查大陸用語
grep -rnE "被試|數據收集|信息|回歸分析|結果表明|人工智能|用戶|(^|[^演])算法|數據庫|優化|場景|默認|受眾" docs/
```
