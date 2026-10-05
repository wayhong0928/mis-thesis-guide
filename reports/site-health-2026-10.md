# 全站健檢報告（2026-10）

- 範圍與日期：index.html 與 docs/*.md 產生的 38 個 pages/*.html，共 39 頁；2026-10-05 檢查。重跑：`python scripts/site_health.py`
- 連結：內部 2836 個（含錨點與資源檔）、外部 236 個不重複網址；發現 68、修 1、確認不需修改 2、留給人工 65
- 手機版（375×812）：39 頁；溢出 2 頁、修 2、留給人工 0；修正後 0 頁溢出
- 無障礙：39 頁；發現 244、修 22、留給人工 222
- build：無錯誤、無輸出警告；產物與 commit 只差 `data-updated` 時間戳（沒有人手改 HTML）；發現 2、修 0、留給人工 2
- 外部連結數量核對：docs 內出現 326 次、236 個不重複網址；直接用正規式數 docs/*.md 原文也是 326 次、236 個，與腳本實際請求的網址一致
- 本次只動連結、標題層級、Markdown 跳脫與 CSS，沒有改文章文字；pages/*.html 全部由 build.py 重新產生

## 檢查方式

- 腳本：`scripts/site_health.py`。它把整個 repo 複製到暫存目錄再跑 build.py，工作目錄不會被改到；所有檢查都對暫存目錄的產出進行。
- 內部連結：解析每頁 HTML 的 `href`／`src`，確認檔案存在、`#錨點` 對得到目標頁的 `id`。另外檢查 Markdown 表格有沒有某一列欄數多於表頭（多出的欄會被 Python-Markdown 直接丟掉）。
- 外部連結：先 HEAD，失敗再 GET；逾時 15 秒；User-Agent 用一般 Chrome 的字串。分類為正常、404/410、跳到別的網域、逾時、403/429（需人工確認）、連線錯誤，以及「執行環境擋住」（見下）。`doi.org` 本來就是轉址服務，轉到出版社網域算正常。
- 手機版：Playwright（Chromium）以 375×812 開每一頁，比較 `document.documentElement.scrollWidth` 與 `window.innerWidth`，再找出右緣超出畫面、而且不在可捲動容器裡的最內層元素。
- 無障礙：同樣用 Playwright 開頁（1280×900），在亮色與暗色兩種 `prefers-color-scheme` 下檢查 html lang、img alt、標題跳級、連結文字、表單控制項名稱，以及每個有文字的元素實際算出來的文字色與背景色對比（一般文字 4.5:1，大字 3:1；背景由下往上合成，漸層底色也算）。
- build：一般執行 `python build.py` 看輸出；另外用 `python -W default build.py` 打開 Python 警告再跑一次；最後逐檔比對產物與 repo 裡的版本。

## 一、連結

內部連結：2836 個，全部指得到存在的檔案與標題，沒有需要修的。另有 584 個連結指向的錨點是 Python-Markdown 依標題順序自動編的（`#_5`、`#42` 這類，中文標題沒有英數字可用時產生），目前都對得上，但前面增刪標題就會指錯，列在「留給人工」。

外部連結數量：docs 內出現 326 次、236 個不重複網址；直接用正規式數 docs/*.md 原文也是 326 次、236 個；樣板沒有外部連結。腳本實際請求 236 個不重複網址。
- 修正前兩個數字不一致（產出頁 325 次／235 個，原文 326 次／236 個），差的那一個就是 about.md:150 被表格吃掉的連結；修正後一致。

本次結果：403/429（需人工確認） 43、404/410 2、執行環境擋住 16、正常 169、跳到別的網域 2、連線錯誤 3、逾時 1（「跳到別的網域」等數字是修正後的重跑結果，已替換的連結不在其中）。

下表列出所有不是「正常」的連結，加上已修正的項目：

| 頁面（來源） | 連結 | 狀態 | 處置 |
|---|---|---|---|
| pages/about.html（docs/about.md:150） | https://code.claude.com/docs/en/artifacts | 連結沒有出現在網頁上：表格儲存格裡的「Plan \| Pro, …」有一個沒跳脫的直線符號，Python-Markdown 把它當成欄分隔，這一列從「Plan」之後的文字連同連結都被丟掉 | **已修正**：在那個直線符號前面加一個反斜線跳脫（網頁上顯示的文字不變）。重建後這一列完整顯示，連結檢查正常（200） |
| docs/style.md:448 | https://language.chinadaily.com.cn/2015-09/01/content_21765083.htm | 404/410：404 | 沒有替換，留給人工。查不到這篇轉載文章的新網址 |
| docs/venues.md:84 | http://jeb.cerps.org.tw/readme.php | 404/410：404 | 沒有替換，留給人工。期刊網站首頁還在，但只剩一個連到 ipress.tw/j0284 的連結；無法確認投稿須知搬到哪裡、是否為同一份文件 |
| docs/style.md:61 | https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf | 跳到別的網域：302 暫時轉址 → static1.squarespace.com 的同名 PDF | 不需修改。作者網站把檔案放在 Squarespace 的檔案主機，原網址就是正式入口，且是暫時轉址 |
| docs/tool-directory.md:206 | https://www.gpower.hhu.de/ | 跳到別的網域：302 暫時轉址 → www.psychologie.hhu.de/…/gpower | 不需修改。轉址由杜塞道夫大學（hhu.de）自己發出，而且是 302 暫時轉址，原網址仍是官方入口 |
| docs/venues.md:83 | https://eclab.nkust.edu.tw/ | 連線錯誤：TLS 憑證已過期（openssl 回報 certificate has expired） | 沒有修改，留給人工。對方網站問題，一般瀏覽器也會跳安全警告；是否改連其他頁面需人工判斷 |
| docs/venues.md:83 | https://eclab.nkust.edu.tw/submitjim/JIM_Call_for_Paper.pdf | 連線錯誤：TLS 憑證已過期 | 同上 |
| docs/venues.md:91 | https://tanet2026.ntunhs.edu.tw/ | 連線錯誤：TLS 憑證鏈缺中繼憑證（openssl：unable to verify the first certificate） | 沒有修改，留給人工。多數瀏覽器會自動補中繼憑證而能正常開啟，請用瀏覽器確認 |
| docs/research-ethics-data.md:183、docs/sources.md:208 | https://www.ntuh.gov.tw/RECO/Fpage.action?fid=5536 | 逾時：逾時（15 秒）；curl 重測也逾時 | 沒有修改，留給人工。2026-09 的政策查核報告也記錄此站會重設自動化連線 |
| docs/about.md:45、docs/theory-building.md:72 | https://journals.aom.org/doi/10.5465/AMR.1989.4308374 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:48、docs/is-research.md:103 | https://doi.org/10.1287/isre.13.4.416.71 | 403/429（需人工確認）：GET 403（轉址到 https://pubsonline.informs.org/doi/10.1287/isre.13.4.416.71） | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:53、docs/theories.md:252 | https://misq.umn.edu/misq/article/19/2/189/1161/Computer-Self-Efficacy-Development-of-a-Measure | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:54、docs/theories.md:263 | https://pubsonline.informs.org/doi/10.1287/mnsc.32.5.554 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:56、docs/theories.md:288 | https://pubsonline.informs.org/doi/10.1287/isre.3.1.60 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:58、docs/theories.md:279 | https://pubsonline.informs.org/doi/10.1287/orsc.5.2.121 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:66、docs/theory-building.md:157 | https://doi.org/10.1287/isre.14.3.221.16560 | 403/429（需人工確認）：GET 403（轉址到 https://pubsonline.informs.org/doi/10.1287/isre.14.3.221.16560） | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:69、docs/finding-reading.md:194、docs/sources.md:82 | https://dl.acm.org/doi/10.1145/1273445.1273458 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:70、docs/is-research.md:67 | https://journals.sagepub.com/doi/10.1177/000276428102500205 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:72、docs/theories.md:239 | https://pubsonline.informs.org/doi/10.1287/isre.2.3.192 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:85、docs/is-research.md:87 | https://journals.aom.org/doi/10.5465/amr.1989.4308371 | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/finding-reading.md:354、docs/sources.md:142 | https://www.dcard.tw/f/graduate_school | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/sources.md:211 | https://www.icpsr.umich.edu/sites/ICPSR/manage-data/prepare-deposit/guide | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/theories.md:277 | https://doi.org/10.1177/014920639101700108 | 403/429（需人工確認）：GET 403（轉址到 https://journals.sagepub.com/doi/10.1177/014920639101700108） | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/theories.md:299 | https://is.theorizeit.org/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:105 | https://docs.consensus.app/consensus-mcp | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:105、docs/tool-directory.md:111 | https://help.consensus.app/en/articles/10087865-subscription-plans | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:111 | https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:164 | https://www.scholarcy.com/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:226 | https://help.quillbot.com/hc/en-us/articles/35855733045143-What-is-the-difference-between-free-and-Premium-in-the-Quillbot-Paraphraser | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:226 | https://quillbot.com/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:53 | https://www.perplexity.ai/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:73 | https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:73 | https://www.scopus.com/ | 403/429（需人工確認）：GET 403（轉址到 https://www.scopus.com/pages/home） | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tool-directory.md:74 | https://www.ssrn.com/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tools-knowledge.md:36 | https://www.mendeley.com/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/tools-knowledge.md:37 | https://endnote.com/ | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:27 | https://misq.umn.edu/pages/Overview | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:28 | https://pubsonline.informs.org/page/isre/editorial-statement | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:29 | https://www.tandfonline.com/journals/mmis20/about-this-journal | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:31 | https://www.tandfonline.com/journals/tjis20/about-this-journal | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:32 | https://onlinelibrary.wiley.com/page/journal/13652575/homepage/productinformation.html | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:33 | https://journals.sagepub.com/aims-scope/jin | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:34 | https://www.sciencedirect.com/journal/the-journal-of-strategic-information-systems | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:46 | https://www.sciencedirect.com/journal/computers-and-security | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:47 | https://www.sciencedirect.com/journal/decision-support-systems | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:47 | https://www.sciencedirect.com/journal/international-journal-of-information-management | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:50 | https://www.sciencedirect.com/journal/electronic-commerce-research-and-applications | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:51 | https://www.sciencedirect.com/journal/international-journal-of-human-computer-studies | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:52 | https://www.sciencedirect.com/journal/computers-in-human-behavior | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:53 | https://academic.oup.com/jamia/pages/About | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:54 | https://www.sciencedirect.com/journal/computers-and-education | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/venues.md:55 | https://www.emerald.com/jkm | 403/429（需人工確認）：GET 403 | 沒有修改，需人工確認。網站擋自動化請求（多為 Cloudflare 等防護），不算壞連結；請用瀏覽器開啟確認 |
| docs/about.md:147、docs/about.md:151、docs/ai-case-study.md:209、docs/finding-reading.md:302、docs/getting-started.md:14、docs/problem-design.md:114、docs/prompts.md:10、docs/skill-build.md:16、docs/sources.md:165、docs/style.md:5、docs/writing.md:203 | https://github.com/wayhong0928/mis-thesis-skills | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:36、docs/sources.md:183 | https://github.com/assafelovic/gpt-researcher | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:37、docs/sources.md:184 | https://github.com/stanford-oval/storm | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:38 | https://github.com/langchain-ai/open_deep_research | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:39 | https://github.com/bytedance/deer-flow | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:40 | https://github.com/LearningCircuit/local-deep-research | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:41、docs/sources.md:185 | https://github.com/Future-House/paper-qa | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:42 | https://github.com/SakanaAI/AI-Scientist | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/ai-tools.md:42 | https://github.com/SamuelSchmidgall/AgentLaboratory | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/prompts.md:10 | https://github.com/wayhong0928/mis-thesis-skills#安裝方式 | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/sources.md:162 | https://github.com/pedrohcgs/claude-code-my-workflow | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/sources.md:163 | https://github.com/Imbad0202/academic-research-skills | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/sources.md:164 | https://github.com/ammosu/awesome-claude-skills-zh-TW | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/tool-directory.md:105 | https://github.com/Consensus-NLP/consensus-mcp | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/tool-directory.md:107 | https://github.com/elicit/api-examples/tree/main/integrations/mcp | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |
| docs/tools-knowledge.md:100 | https://github.com/retorquere/zotero-better-bibtex/releases/latest | 執行環境擋住（github.com 回 403） | 沒有修改，需人工確認。這個雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址一律回 403，腳本無法判斷連結是否有效；請在一般網路環境重跑腳本 |


## 二、手機版溢出（375×812）

修正前 2 頁溢出，修正後 0 頁。

| 頁面 | 元素 | 處置 |
|---|---|---|
| pages/is-research.html（docs/is-research.md） | 行內 `<a>`：`https://ideas.repec.org/a/inm/orisre/v12y2001i2p121-134.html`（scrollWidth 484px，元素右緣 404px） | **已修**：assets/style.css 加 `.doc { overflow-wrap: break-word; }`，沒有空白可斷的長字串改成在字中換行；重測 scrollWidth = 375 |
| pages/is-research.html（docs/is-research.md） | 行內 `<a>`：`https://journals.sagepub.com/doi/10.1177/000276428102500205`（scrollWidth 484px，元素右緣 484px） | **已修**：assets/style.css 加 `.doc { overflow-wrap: break-word; }`，沒有空白可斷的長字串改成在字中換行；重測 scrollWidth = 375 |
| pages/is-research.html（docs/is-research.md） | 行內 `<a>`：`https://journals.aom.org/doi/10.5465/amr.1989.4308371`（scrollWidth 484px，元素右緣 423px） | **已修**：assets/style.css 加 `.doc { overflow-wrap: break-word; }`，沒有空白可斷的長字串改成在字中換行；重測 scrollWidth = 375 |
| pages/theory-building.html（docs/theory-building.md） | 行內 `<a>`：`https://journals.aom.org/doi/10.5465/AMR.1989.4308374`（scrollWidth 432px，元素右緣 432px） | **已修**：assets/style.css 加 `.doc { overflow-wrap: break-word; }`，沒有空白可斷的長字串改成在字中換行；重測 scrollWidth = 375 |

## 三、無障礙

| 頁面 | 問題 | 處置 |
|---|---|---|
| 全部 39 頁 | html lang、img alt、連結文字 | 沒有問題：每頁都有 `lang="zh-Hant"`；沒有缺 alt 的圖片；沒有「這裡」「點此」之類的連結文字 |
| 全部 39 頁 | 標題跳級 | 沒有問題 |
| 全站（側欄分區標題、站名小字、麵包屑、頁尾、本頁目錄標題、首頁分區說明與編號） | 對比不足：亮色：`--ink-faint` #8b857a 在 #fbfaf7／#f3f1eb／#ffffff 上只有 3.24–3.66:1 | **已修**：`--ink-faint` 改 #706b62（同色相調暗），對比 4.61–5.29:1 |
| 全站（同上） | 對比不足：暗色：`--ink-faint` #857f74 在側欄 #1e1d1a 上 4.24:1、在面板 #1c1b18 上 4.33:1 | **已修**：暗色 `--ink-faint` 改 #8f8a7f，對比 4.62–5.31:1 |
| 有提示框的頁面 | 對比不足：提示框標題（warning／danger）用框線色 `--warn-rule` 當文字色：亮色 #d9a45b 對 #fdf3e7 只有 2.03:1；暗色 #a8763a 對 #2c231a 3.9:1 | **已修**：新增文字專用的 `--warn-ink`（亮 #916222、暗 #b98240，對比 4.82／4.65:1），框線仍用 `--warn-rule` |
| 有提示框的頁面 | 對比不足：提示框標題（tip／note）用 `--ok-rule`：亮色 #7fa06f 對 #eef5ec 2.64:1；暗色 #5f7a52 對 #1e2a1e 3.13:1 | **已修**：新增 `--ok-ink`（亮 #58734c、暗 #779866，對比 4.76／4.6:1），框線不變 |
| 全站 | 對比不足：「跳到主要內容」連結（鍵盤 Tab 時出現）：暗色是白字 #fff 配 `--accent` #d9a173，2.26:1 | **已修**：文字色改 `var(--panel)`，亮色仍是白字（7.39:1），暗色變深色字（7.62:1） |
| pages/ai-workflow.html、literature.html、writing.html | 對比不足：暗色：`<em>` 的螢光筆底色 `--mark` #5a4c1e 配 `--ink-soft` 色的文字只有 3.78:1 | **已修**：暗色 `--mark` 改 #4b3f19，對比 4.65:1（一般內文 `--ink` 也同時 ≥ 4.6:1） |
| pages/checklists.html（133）、pages/post-defense.html（16）、pages/defense.html（13）、pages/finding-reading.html（13）、pages/quant-analysis-basics.html（12）、pages/tools-knowledge.html（11）、pages/research-ethics-data.html（10）、pages/is-research.html（5）、pages/problem-design.html（5）、pages/tool-directory.html（4） | 檢查清單的 checkbox 沒有可讀出的名稱，共 222 個：build.py 把 `- [ ]` 換成 `<input type="checkbox">`，後面的文字沒有用 `<label>` 綁定，螢幕報讀器只會念「核取方塊，未勾選」 | 沒有修改，留給人工（理由見「留給人工」） |

修正後重跑：對比不足 0 組、標題跳級 0、缺 alt 0、缺 lang 0。

## 四、build

| 項目 | 結果 | 處置 |
|---|---|---|
| `python build.py` | 結束碼 0，沒有警告或錯誤訊息 | — |
| `python -W default build.py` | 每讀一個來源檔出現一次 `ResourceWarning: unclosed file`：build.py 第 282 行的 `open(...).read()` 沒有關檔 | 不影響產物。沒有修改，留給人工 |
| 產物與 commit 比對 | 修正前：39 個檔只差 `data-updated="…"` 時間戳，其餘內容逐位元相同，沒有手改過的 HTML | 這次重新 build，時間戳已同步；成因在 build.py，留給人工（見下） |
| 修正後比對 | 40 個產物與工作目錄完全相同 | — |

## 留給人工

1. **外部連結：65 筆**（明細與各自的理由見第一節表格「處置」欄）。共通原則：找不到能確認是同一份文件的官方新網址就不替換；403/429 是網站擋機器人，不算壞連結，需要用瀏覽器確認。
2. **github.com 連結無法在這個環境檢查**：雲端執行環境的 GitHub 代理只開放本次作業的 repo，其餘 github.com 網址都回 403。這不是 GitHub 的回應，所以不能判定壞掉，也不能判定正常；請在一般網路環境執行 `python scripts/site_health.py --skip-browser` 重測。
3. **指向自動編號錨點的連結（584 個）**：目前都有效，但 `#_5` 這種 id 依標題出現順序產生，前面多一個或少一個中文標題就會整批位移、指到錯的段落。根治要在 build.py 設定 toc 的 `slugify`（例如保留中文字），屬於建置邏輯變更，而且會改掉所有現有錨點，需要人工決定。腳本的 JSON 輸出（`--json`）有完整清單。
4. **`data-updated` 時間戳每次提交都會落後**：build.py 用「來源檔最後一次 git 提交時間」當時間戳，但 HTML 是在提交前產生的，所以 commit 裡的 HTML 永遠記著上一次的時間，下一次任何人重建都會出現一批只有時間戳的變動。要改得改 build.py 的設計（例如改用檔案內容的雜湊判斷、或提交後再重建一次），超出這次可以自動修的範圍。腳本比對時已把這種差異和真正的內容差異分開。
5. **build.py 的 `ResourceWarning`**：改成 `with open(...) as f:` 即可，但這是建置程式碼，不在這次允許修改的範圍。
6. **檢查清單的 checkbox 沒有名稱（222 個）**：修法是讓 build.py 第 291 行附近產生的 `<input>` 用 `<label>` 包住後面的文字（或加 `aria-labelledby`）。這要改 build.py 的輸出結構，`assets/site.js` 記憶勾選狀態的選擇器也要一起確認，不屬於這次列出的機械性修正，也需要確認版面不受影響。

## 這次沒有檢查的部分

- 「soft 404」：網站回 200 但內容已經換成別的頁面，自動檢查看不出來。
- 滑鼠移過（hover）與鍵盤焦點狀態的對比只檢查了「跳到主要內容」連結；其他 hover 樣式沒有算。
- 手機版是在容器裡的 Chromium 跑的，系統中文字型是文泉驛正黑，不是 style.css 指定的思源黑體；字寬略有差異，所以溢出的修法用 `overflow-wrap`，不依賴特定字寬。
- 錯字與文章觀點不在本次範圍。
