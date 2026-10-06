# 一小時上手：用 Claude Code 或 Codex 建立你的論文助手

> 這頁寫給做過[網頁版一小時上手](ai-quickstart.md)、願意打開終端機的研究生。照著做一小時，你會有一個放文獻和草稿的研究資料夾、一份 AI 每次都會先讀的指示檔，裝好站主整理的 thesis-toolkit 三個 SKILL，再用其中一個檢查自己的題目。Claude Code（Anthropic）和 Codex（OpenAI）的步驟大部分相同，相同的地方只寫一次，不同的地方分開寫，手上有哪一個就用哪一個。
>
> 這頁沒有提供「整段貼給 AI，讓它自己裝好設好」的提示詞，每一步都要你自己動手。自己做過一次，你才知道每個檔案是做什麼的，之後 AI 出錯時也看得懂問題在哪。

下面的工具事實都對照官方說明，查證日期是 2026-10-06。這兩個工具更新很快，畫面或指令跟這頁不一樣時，以官方說明為準。

---

## 一、開始之前

- 先做完[網頁版一小時上手](ai-quickstart.md)。這頁的指示檔沿用那頁第三節的範本，回原文核對的練習也在那頁。
- 兩個工具都要付費方案。Claude Code 要 Claude 的 Pro、Max、Team、Enterprise 方案，或 Claude Console 帳號（[Quickstart](https://code.claude.com/docs/en/quickstart)）。Codex 的官方方案頁把終端機版本（Codex CLI）列在 ChatGPT Plus 以上的方案，Free 和 Go 只寫到桌面 app（[Pricing](https://learn.chatgpt.com/docs/pricing)）。兩者也都可以改用 API key 登入，依 API 用量另外計費。
- 沒用過終端機的話，Claude Code 官方有一頁[終端機入門](https://code.claude.com/docs/en/terminal-guide)，教你怎麼打開終端機、怎麼貼上指令。

## 二、一小時時間表

| 時間 | 做什麼 | 對應本頁 |
|---|---|---|
| 0 到 10 分鐘 | 安裝、登入，先看懂權限設定 | 第三節 |
| 10 到 20 分鐘 | 建研究資料夾，放進文獻和草稿 | 第四節 |
| 20 到 30 分鐘 | 寫指示檔，確認 AI 有讀到 | 第五節 |
| 30 到 40 分鐘 | 安裝 thesis-toolkit | 第六節 |
| 40 到 55 分鐘 | 用研究問題稽核檢查自己的題目，回原文核對 | 第八節 |
| 55 到 60 分鐘 | 對照第九節，確認資料夾裡沒有不該放的東西 | 第九節 |

第七節接 Consensus、Elicit 是選用的，有付費帳號或想多試的人再做。

---

## 三、安裝、登入、看懂權限

### 3.1 Claude Code

1. 照官方 [Quickstart](https://code.claude.com/docs/en/quickstart) 的 Step 1，依作業系統複製那一行安裝指令到終端機執行。Windows 的 PowerShell 和 CMD 用的指令不同，貼錯會出現錯誤訊息，官方頁面上寫了怎麼分辨。官方也建議 Windows 先裝 [Git for Windows](https://git-scm.com/downloads/win)。
2. 裝完開一個新的終端機視窗，輸入 `claude --version`，有印出版本號就是裝好了。
3. 輸入 `claude`，第一次會要你在瀏覽器登入。之後要換帳號，在 Claude Code 裡輸入 `/login`。

### 3.2 Codex

1. 照官方 [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) 的「Install Codex」段落，macOS／Linux、Windows（PowerShell）、npm、Homebrew 四種方式擇一。
2. 在資料夾裡輸入 `codex`，第一次執行時選「Sign in with ChatGPT」，用你的 ChatGPT 帳號登入。

### 3.3 權限：第一次先看懂再按

這類工具會直接讀你的檔案、改你的檔案、在你的電腦上跑指令。剛開始用，先讓它每一步都問過你。

- Claude Code：v2.1.283 起，終端機的互動 session 預設是 auto 模式，背景有分類器先審過動作，大部分動作不會再問你（[Permission modes](https://code.claude.com/docs/en/permission-modes)）。剛開始建議改用 Manual 模式，每個動作都先問你：啟動時輸入 `claude --permission-mode manual`，或在 session 裡按 `Shift+Tab` 切換，下方狀態列顯示 `manual mode on` 就對了。
- Codex：預設會把寫入限制在目前的工作資料夾，也不能連網。常用的 Auto 設定下，它可以在工作資料夾裡讀檔、改檔、跑指令，要改資料夾以外的檔案或要連網時才會問你。官方建議沒有版本控制的資料夾用 read-only，在 Codex 裡輸入 `/permissions` 就能切換（[Agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security)）。

不管用哪一個，跳出確認時先看清楚它要讀哪個檔、改哪個檔、跑什麼指令。看不懂就先拒絕，再問它這一步要做什麼、為什麼要做。

---

## 四、建研究資料夾

在電腦上開一個資料夾，例如叫 `我的論文`，裡面再開三個子資料夾：

```text
我的論文/
├── 文獻/      放核心文獻的 PDF
├── 筆記/      AI 寫的文獻筆記初稿，你核對過的版本也放這裡
└── 草稿/      你的研究計畫和各章草稿
```

先放的東西跟網頁版第四節一樣：三篇核心文獻、系所格式規範、自己的研究計畫草稿。受試者的原始資料不要放進這個資料夾，原因見第九節。

之後每次使用，都先在終端機用 `cd` 進到這個資料夾，再輸入 `claude` 或 `codex`。AI 能讀寫的範圍以這個資料夾為主，從別的地方啟動，它讀到的就是別的資料夾。

會用 Git 的話，可以在這個資料夾執行 `git init`，每次請 AI 改檔前後各 commit 一次，改壞了可以還原。不會用 Git 也沒關係，改檔前自己先複製一份備份就好。

用 Codex 的人要多注意一件事：官方建議有版本控制的資料夾用 Auto，沒有的用 read-only，而且 Codex 可能先以唯讀模式啟動，等你確認信任這個資料夾。如果 Codex 寫不進 `筆記/`，先看 `/permissions` 目前是哪一種；想讓它寫檔，建議先 `git init`，再用 `/permissions` 切換。

---

## 五、寫指示檔

指示檔的作用跟網頁版的專案指示一樣：每次開新 session，AI 都會先讀它。

- Claude Code 讀資料夾根目錄的 `CLAUDE.md`（[Memory](https://code.claude.com/docs/en/memory)）。
- Codex 讀資料夾根目錄的 `AGENTS.md`（[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)）。
- 兩個工具都會用的話，可以只寫一份 `AGENTS.md`。Claude Code 從 v2.1.277 起，在資料夾裡和上層資料夾都沒有 `CLAUDE.md`、`.claude/CLAUDE.md`、`CLAUDE.local.md` 時，會改讀 `AGENTS.md`。剛從舊版升級後的第一個 session 可能還讀不到，用 `/context` 確認一次就知道。

做法：

1. 在 `我的論文/` 建一個純文字檔，檔名照上面取。用記事本或任何文字編輯器都可以，存檔時確認副檔名是 `.md`，不是 `.md.txt`。
2. 把網頁版[第三節的專案指示範本](ai-quickstart.md#_3)整段貼進去，`⟨⟩` 換成你的內容。
3. 紅線第 1 條的「上傳到這個專案的文獻」改成「`文獻/` 資料夾裡的 PDF」，再在紅線最後加上下面三條：

```text
8. 不要修改、搬移或刪除 文獻/ 資料夾裡的任何檔案。
9. 要修改 草稿/ 裡的檔案以前，先告訴我要改哪個檔、改哪一段、為什麼改，等我同意。
10. 不要讀取 我的論文/ 以外的檔案。需要其他資料時，先問我。
```

4. 確認 AI 有讀到。Claude Code：在 session 裡輸入 `/context`，看「Memory files」底下有沒有你的 `CLAUDE.md`。Codex：請它「Summarize the current instructions.」，回答裡應該會列出你寫的規則。

第 8 到 10 條 AI 不一定每次都照做。能確實攔下動作的是第 3.3 節的權限設定，所以跳出確認時還是要自己看。

---

## 六、安裝 thesis-toolkit

thesis-toolkit 是站主整理的三個 SKILL：研究方向收斂（`research-direction-finding`）、研究問題稽核（`research-question-audit`）、學術寫作檢查（`academic-writing-discipline`）。原始檔在 [mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills)。

### 6.1 Claude Code：用 plugin 安裝

在 Claude Code 裡依序輸入下面兩行：

```text
/plugin marketplace add wayhong0928/mis-thesis-skills
/plugin install thesis-toolkit@mis-thesis-skills
```

第二行不會直接安裝，會先打開這個 plugin 的說明畫面，讓你選安裝範圍（scope）。選 user，你在這台電腦的每個資料夾都能用；選 local，只有目前這個資料夾能用（[Discover plugins](https://code.claude.com/docs/en/discover-plugins)）。

裝好以後，你提到相關任務時 Claude 會自己啟用對應的 SKILL。也可以直接指定，例如輸入 `/thesis-toolkit:research-question-audit`（[Skills](https://code.claude.com/docs/en/skills)）。

### 6.2 Codex：把 SKILL 資料夾複製進去

thesis-toolkit 是照 Claude Code 的 plugin 格式打包的，Codex 這邊改成直接放 SKILL 資料夾，Codex 讀得懂同樣格式的 SKILL（[Build skills](https://learn.chatgpt.com/docs/build-skills)）。

1. 打開 [mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills)，點綠色的「Code」按鈕，選「Download ZIP」，下載後解壓縮。會用 Git 的話，用 `git clone` 也可以。
2. 在 `我的論文/` 裡建一個 `.agents` 資料夾，裡面再建一個 `skills` 資料夾。資料夾名稱開頭有一個點，有些系統預設會把它隱藏起來。
3. 把解壓縮後 `plugins/thesis-toolkit/skills/` 底下的三個資料夾，整個複製到 `我的論文/.agents/skills/`。想讓每個資料夾都能用，改放到家目錄底下的 `.agents/skills/`。
4. Codex 會自動偵測新的 SKILL，沒出現就重開 Codex。輸入 `/skills` 可以看清單，輸入 `$research-question-audit` 就能指定使用。

SKILL 之後會改版。Claude Code 從第三方市集裝的 plugin 預設不會自動更新，要在 `/plugin` 的 Marketplaces 分頁選這個市集，開啟自動更新；Codex 要自己重新下載，再覆蓋那三個資料夾。各版改了什麼，寫在 repo 的 CHANGELOG。

---

## 七、選用：接上 Consensus、Elicit

Consensus 和 Elicit 都有官方的 MCP 伺服器。MCP 是讓 AI 工具連上外部服務的標準做法，接上以後，可以在 Claude Code 或 Codex 的對話裡直接搜尋文獻。不接也沒關係，兩者的免費網頁版就能做基本搜尋，兩者的差別和方案見[工具指南 3.2 節](tool-directory.md#32-ai)。

**Consensus**（[官方說明](https://github.com/Consensus-NLP/consensus-mcp)）：官方說明寫，多數用戶端第一次連線時會要你用 Consensus 帳號登入，Claude 與 ChatGPT 不登入也能用，但額度較低；每月能搜尋幾次依方案而定。

- Claude Code：在終端機執行 `claude mcp add --transport http consensus https://mcp.consensus.app/mcp`。
- Codex：先執行 `codex mcp add consensus --url https://mcp.consensus.app/mcp`，再執行 `codex mcp login consensus` 登入。

**Elicit**（[官方說明](https://github.com/elicit/api-examples/tree/main/integrations/mcp)）：要 Elicit 的 Pro 以上方案才能用 MCP。

- Claude Code：在終端機執行 `claude mcp add --transport http elicit https://elicit.com/api/mcp`，再到 Claude Code 裡輸入 `/mcp`，選 `elicit`，按「Authenticate」，在瀏覽器登入。
- Codex：Elicit 的官方說明沒有寫 Codex 的步驟。要用的話，照 [Codex 的 MCP 說明](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)加入 HTTP 伺服器，網址跟上面相同。

搜尋結果裡的摘要不能當原文引用。看起來相關的論文，一樣要下載原文，放進 `文獻/` 再讀。

---

## 八、第一個任務：稽核自己的題目

在 `我的論文/` 啟動工具，輸入下面這段。Codex 的話，把開頭換成 `$research-question-audit`。

```text
請用 research-question-audit 稽核我的研究想法：
⟨一句話研究想法或研究問題；有的話也附上研究目的、假說、研究設計⟩

涉及文獻的判斷，只根據 文獻/ 資料夾裡的 PDF，並標出是哪一篇、哪個章節。
文獻裡查不到的，寫「文獻裡查不到」，不要用你記得的內容補。
這次只輸出報告，不要建立或修改任何檔案。
```

拿到報告以後：

1. 有引用文獻的判斷，打開那篇 PDF，確認作者真的這樣寫。
2. 「預期質詢清單」裡每一題，先自己試著回答。答不出來的，就是下次跟指導教授討論的題目。
3. 判「通過」的項目也要看理由寫得對不對，口試委員的標準可能比 AI 嚴。

報告的格式和七個檢查點，跟網頁簡版（[提示詞範本 10.2 節](prompts.md#skill-lite-audit)）一樣。兩者差在完整版會參考 references 裡的詳細判準，也能直接讀你資料夾裡的文獻。

時間還夠的話，可以再挑 `草稿/` 裡的一段文字，用 `academic-writing-discipline` 檢查一次。

---

## 九、資料安全

- 工具讀到的檔案內容，會送到 Anthropic 或 OpenAI 的模型處理，跟網頁版上傳檔案一樣，所以網頁版[第四節](ai-quickstart.md#_4)的規則照樣適用。
- 受試者的原始資料（問卷回覆、訪談逐字稿、錄音）不要放進研究資料夾，就算刪掉姓名也一樣，見[研究倫理與資料管理](research-ethics-data.md)第七節。要分析這類資料時，先對照倫理審查核准的計畫書，再問指導教授。
- 指示檔的紅線靠 AI 自己遵守，權限設定才會在動作執行前攔下來。auto 模式和 `bypassPermissions` 這類跳過確認的設定，等你熟悉工具、知道它平常會做哪些事以後再考慮。

---

## 十、下一步

1. [論文 AI 工作流全圖](ai-workflow-map.md)：從找方向到口試，每一站在 Claude Code／Codex 這條路線用什麼。
2. [實例：一個碩士生的 AI 研究流程](ai-case-study.md)：站主自己的 Claude Code 設定在[第五節](ai-case-study.md#claude-code)。
3. [ai-agent-notes](https://wayhong0928.github.io/ai-agent-notes/)：工具本身的設定，包括權限、MCP、SKILL、plugin，整理在那個站。
