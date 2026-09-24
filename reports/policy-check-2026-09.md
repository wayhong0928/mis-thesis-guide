# 會隨時間變動的事實：2026 年 9 月例行查核

- 查證日期：2026-09-24（全部條目同一天查證）
- 範圍：`docs/` 全部 37 頁中，法規、政府與教育部指引、學校規定、研究倫理（IRB／REC）、期刊與出版社的 AI 政策、APA 與報告準則版本，以及期刊與研討會的現況與時程
- 行號：依本次修改前的 `main`（commit `ad60a9b`）
- 狀態：**仍正確**／**已更新**（本次已修改 docs/）／**查不到官方來源**（只列在這裡，沒有修改）

## 查證方式與限制

- 這個環境的 WebFetch 工具被網路政策擋住，所以改用終端機的 `curl` 直接讀官方頁面，並用 WebSearch 找官方網址。
- 部分官方網站會擋自動化連線，包括 apastyle.apa.org／apa.org（Incapsula）、publicationethics.org（Cloudflare）、aisnet.org 與 aisconferences.org（captcha）、sciencedirect.com。另有幾個網站連線逾時或被重設：ntuh.gov.tw、tanet2026.ntunhs.edu.tw、jeb.cerps.org.tw、csroc.org.tw。
- 上述網站的條目，只能用 WebSearch 限定官方網域取得的標題與摘要來比對，表中「依據」欄標為「官方網域搜尋摘要」。這類證據比直接讀頁面弱，所以只用來判定「仍正確」，不拿來修改內容。
- 不在這次範圍內：工具功能與數字（GitHub 星數、OpenAlex 收錄數、ASReview 減少工作量比例等）、SmartPLS 統計門檻、理論文獻的書目資料。

## 統計

| 狀態 | 條數 |
|---|---|
| 仍正確 | 37 |
| 已更新 | 4 |
| 查不到官方來源 | 7 |
| **合計** | **48** |

## 一、法規

| # | 檔案:行號 | 原文摘要 | 目前引用的來源或日期 | 狀態 | 查證結果與官方來源 | 依據 |
|---|---|---|---|---|---|---|
| 1 | ethics.md:21 | 違反學術誠信紅線，後果可以嚴重到撤銷學位 | 未標來源 | 仍正確 | 《學位授予法》第 17 條：論文有造假、變造、抄襲、由他人代寫等情事，應撤銷學位（107-11-28 修正）。<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0030010> | 直接讀取 |
| 2 | ethics.md:37、ethics.md:226、sources.md:199 | 《人工智慧基本法》2025-12-23 三讀通過，主管機關國科會，揭示七大治理原則 | 中央社、數位發展部新聞稿 | **已更新** | 已於 2026-01-14（民國 115 年 1 月 14 日）公布，且「自公布之日起施行」；主管機關仍為國科會，第 4 條列七項原則。原文三讀日期正確，但少了已公布施行這件事。<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093>；三讀日期見 <https://moda.gov.tw/press/press-releases/18316> | 直接讀取 |
| 3 | research-ethics-data.md:32 | 《人體研究法》列有得免審查的案件，但各機構如何確認依其程序 | 全國法規資料庫，查證日 2026-09-04 | 仍正確 | 第 5 條第 1 項但書：「屬主管機關公告得免審查之研究案件範圍者」，免審範圍是由主管機關公告，法條本身沒有逐項列舉。原文大意正確，但措辭可以更精確（沒有修改）。<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020176> | 直接讀取 |
| 4 | research-ethics-data.md:58 | 第十四條告知事項：目的與方法、權益與個資保護、撤回方式、可預見風險、救濟措施、研究材料保存期限與運用規劃 | 同上 | 仍正確 | 第 14 條共九款，原文列的各項都在其中（另外還有機構名稱與經費來源、主持人、聯絡人、商業利益約定）。同上網址 | 直接讀取 |
| 5 | research-ethics-data.md:147、glossary.md:220 | 「去連結」依《人體研究法》定義，永久不能以任何方式連結、比對 | 同上 | 仍正確 | 第 4 條第 3 款定義相符。同上網址 | 直接讀取 |
| 6 | research-ethics-data.md:181、sources.md:206 | 《人體研究法》為審查、同意與研究材料管理的法規基礎（連結） | 查證日 2026-09-04 | 仍正確 | 最新修正日期為民國 108-01-02，之後沒有新修正；連結有效。同上網址 | 直接讀取 |
| 7 | research-ethics-data.md:182、sources.md:207 | 《個人資料保護法》：蒐集告知、特定目的、利用與安全維護（連結） | 查證日 2026-09-04 | 仍正確 | 原文的用途描述仍正確。補充：最新修正為民國 114-11-11，主管機關改為「個人資料保護委員會」，且部分條文尚未生效（全國法規資料庫標示「最後生效日期：未定」）。站內沒有提到主管機關，所以不必修改。<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021> | 直接讀取 |
| 8 | post-defense.md:124、sources.md:212 | 依 2026 年 1 月修正的〈大專校院學位論文送存國家圖書館典藏作業要點〉：學校送存、電子檔附授權書、個資抽出或隱蔽，延後公開限於機密、專利或依法不得提供，須經學校認定 | 教育部主管法規共用系統，查證日 2026-09-04 | 仍正確 | 修正日期為民國 115-01-14；第四點第（六）款規定個資抽出或隱蔽，第六點規定延後公開，第八點規定授權書，內容都相符。<https://edu.law.moe.gov.tw/LawContent.aspx?id=GL001869> | 直接讀取 |
| 9 | post-defense.md:186、sources.md:213 | 國家圖書館作業要點與申請表單頁（連結） | 查證日 2026-09-04 | 仍正確 | 連結有效，頁面標題與內容相符。<https://www.ncl.edu.tw/form-downloads/0Q099526045144197574> | 直接讀取 |

## 二、政府與教育部的 AI 指引、學校規定

| # | 檔案:行號 | 原文摘要 | 目前引用的來源或日期 | 狀態 | 查證結果與官方來源 | 依據 |
|---|---|---|---|---|---|---|
| 10 | ethics.md:27、39、41–61；sources.md:197 | 教育部〈大學校園因應生成式 AI 之指引及教學建議〉：保持質疑、親自驗證；生成內容不屬著作權法保護的著作；直接使用恐構成抄襲，可導致撤銷學位；不輸入個資與機密；適度揭露 | ethics.moe.edu.tw 電子報連結；表格時間欄為「—」 | 仍正確 | 各點與原文相符（著作權一點原文是「原則上」無法享有著作權）。**疑義**：這份文件是臺灣學術倫理教育資源中心電子報第 13 期（2023-08）彙整各校規範的文章，不是教育部以公文發布的指引，「教育部指引」這個稱呼需要斟酌；時間欄可以補上 2023 年 8 月。以上都沒有修改。<https://ethics.moe.edu.tw/resource/epaper/html/21/> | 直接讀取 |
| 11 | ethics.md:38、63–70 | 《行政院及所屬機關（構）使用生成式 AI 參考指引》2023 年 8 月，由國科會公告，無強制性、無罰則 | 未單獨標來源 | 仍正確 | 行政院網站刊登日期為 112-08-31，由國科會研擬，並表示會「滾動修正」；目前沒有查到修正版。「不具強制性亦無明定罰則」出自國科會常見問答，臺灣學術倫理教育資源中心頁面有轉述。<https://www.ey.gov.tw/Page/448DE008087A1971/40c1a925-121d-4b6b-8f40-7e9e1a5401f2>；<https://ethics-s.moe.edu.tw/static/ethics/u03/p14.html> | 直接讀取 |
| 12 | getting-started.md:85、sources.md:198 | 多數學校要求修習臺灣學術倫理教育資源中心的課程並取得證書，通常是提口試計畫書的前提 | 資源中心連結 | 查不到官方來源 | 沒有全國統一的規定，各校要求不一：有的學校寫「取得修課證明始得申請學位考試」，有的寫「始能正式撰寫學位論文」。「多數學校」和「提計畫書前提」都沒有官方的全國性來源。沒有修改。 | 官方網域搜尋摘要（臺大、陽明交大、北大等校教務處頁面） |
| 13 | ai-tools.md:110 | 多數大學的原創性聲明與 AIGC 使用規範要求誠實揭露 AI 輔助範圍 | 未標來源 | 仍正確 | 臺灣學術倫理教育資源中心綜整各校規範時指出「若於研究中使用生成式 AI 工具，應適當揭露使用程度與範圍」，並列出臺大、成大、清大、陽明交大等校的規範。<https://ethics-s.moe.edu.tw/static/ethics/u03/p14.html> | 直接讀取 |
| 14 | method-experiment.md:125 | 不把受試者可辨識資料送到外部服務，這在多數學校的研究倫理與資安規定中都有明確要求 | 未標來源 | 查不到官方來源 | 找不到全國性的統整來源可以支持「多數學校」這個說法。沒有修改。 | — |
| 15 | research-ethics-data.md:32、183；sources.md:208 | 臺大醫院研究倫理委員會：是否符合免審由委員會判定（機構實例） | 查證日 2026-09-04 | 仍正確 | 官方頁面寫明「擬執行之人體研究是否符合免審條件，須送交研究倫理委員會判定」。直接連線被重設，所以用搜尋摘要比對。<https://www.ntuh.gov.tw/RECO/Fpage.action?muid=5018&fid=5536> | 官方網域搜尋摘要 |

## 三、期刊與出版社的 AI 政策

| # | 檔案:行號 | 原文摘要 | 目前引用的來源或日期 | 狀態 | 查證結果與官方來源 | 依據 |
|---|---|---|---|---|---|---|
| 16 | ethics.md:79 | COPE 立場：AI 工具無法為研究負責，不能成為作者 | 未標連結 | 仍正確 | COPE〈Authorship and AI tools〉立場聲明相符。官網被 Cloudflare 擋住。<https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools> | 官方網域搜尋摘要 |
| 17 | ethics.md:88 | IEEE：在致謝說明工具名稱與使用章節 | 未標連結 | 仍正確 | 相符；另外寫明用於編修與文法時「不要求但建議」揭露。<https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/> | 直接讀取 |
| 18 | ethics.md:89 | Elsevier：獨立段落，標題為「撰寫過程中使用生成式 AI 的聲明」 | 未標連結 | **已更新** | 期刊政策已在 2026 年 6 月改版（頁尾標示「Policy updated June 2026」）。現在要求在參考文獻前加獨立聲明段落，建議標題改為「Declaration of generative AI and AI-assisted technologies in the manuscript preparation process」（原為「…in the writing process」，現在只有書籍政策還用舊標題）。<https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals> | 直接讀取 |
| 19 | ethics.md:90 | ACS：在致謝或方法論部分詳述 | 未標連結 | 仍正確 | 用於文字或圖像生成時在致謝說明，使用範圍較大時在方法等章節詳述。<https://researcher-resources.acs.org/publish/aipolicy> | 直接讀取 |
| 20 | ethics.md:90 | AIP：在致謝或方法論部分詳述（和 ACS 同一列） | 未標連結 | **已更新** | AIP 現行政策：只用於準備稿件或提升可讀性時「允許且不需揭露」；可能影響研究發現或結論的使用，須在 Methods 詳述，並寫出工具名稱、版本、廠商與用途。沒有提到致謝。<https://publishing.aip.org/resources/researchers/policies-and-ethics/ai-policy/> | 直接讀取 |
| 21 | ethics.md:92、195；tool-directory.md:205 | 語法、拼字檢查與翻譯是否需要揭露，依投稿單位政策而異 | — | 仍正確 | Elsevier 和 AIP 對基本語法檢查不要求揭露，IEEE 是「建議」揭露，各家確實不同。見第 17、18、20 條網址 | 直接讀取 |
| 22 | ethics.md:242、sources.md:200 | 陽明交大圖書館〈搞懂「AI 貢獻聲明」〉：各大出版社 AI 揭露規定整理 | 連結 | 查不到官方來源 | 這是圖書館的二手整理，不是出版社的一手政策，所以沒有逐項比對。它寫的 Elsevier 和 AIP 規定可能已經過時（見第 18、20 條）。沒有修改。 | — |
| 23 | venues.md:46、119 | Computers & Security 自 2024 年起暫停收以 AI／ML 為主要成分的投稿 | 無查證日 | 仍正確 | 期刊頁仍寫著自 2024 年初起暫停審理以 AI／ML 為重要成分的投稿；另外寫明 AI／ML 系統本身的安全也不在收稿範圍。<https://www.sciencedirect.com/journal/computers-and-security> | 官方網域搜尋摘要 |
| 24 | venues.md:22、57、116；theories.md:301 | AIS Senior Scholars' List 共 11 本，2023 年新增 DSS、I&M、I&O | 2026 年 9 月整理 | 仍正確 | AIS 公告〈New in 2023: Senior Scholars' List of Premier Journals〉與清單頁都是 11 本，新增的 3 本相符。<https://aisnet.org/research/seniorscholarsbasket/> | 官方網域搜尋摘要 |

## 四、APA 格式與報告準則

| # | 檔案:行號 | 原文摘要 | 目前引用的來源或日期 | 狀態 | 查證結果與官方來源 | 依據 |
|---|---|---|---|---|---|---|
| 25 | style.md:3、220、265；writing.md:103；tools-knowledge.md:29、129；checklists.md:155 | 現行版本為 APA 第 7 版 | — | 仍正確 | APA 官方產品頁仍是 Publication Manual Seventh Edition（2020），沒有查到第 8 版的公告。<https://apastyle.apa.org/products/publication-manual-7th-edition> | 官方網域搜尋摘要 |
| 26 | style.md:267–272 | APA 6→7 差異：三位以上作者首次即用等人、DOI 改為 https://doi.org/、不列出版地、不用 "Retrieved from" | — | 仍正確 | 與 APA Style〈What's new in the seventh edition〉、〈DOIs and URLs〉、〈Book references: No location required〉相符。<https://apastyle.apa.org/blog/whats-new-7e> | 官方網域搜尋摘要 |
| 27 | style.md:273 | 期刊卷期：APA 6「卷號粗體」、APA 7「卷號斜體」 | — | 查不到官方來源 | **疑義**：就我所知，APA 6 的期刊卷號也是斜體，不是粗體，這一列可能有誤。但 APA 官網擋自動連線，也沒有找到可讀取的 APA 6 官方頁面可以佐證，所以沒有修改，建議人工用 APA 6 手冊核對。 | — |
| 28 | tools-knowledge.md:56 | APA 7 對超過 20 位作者的規則 | — | 仍正確 | 20 位以內全部列出；21 位以上列前 19 位、刪節號、最後一位。<https://apastyle.apa.org/blog/more-than-20-authors> | 官方網域搜尋摘要 |
| 29 | sources.md:223、writing.md:220、228 | APA JARS（量化、質性、混合研究報告準則） | 連結 apa.org/pubs/journals/resources/apa-style-jars.html | 仍正確 | 內容相符（2018 年修訂，納入質性與混合研究）。官方主頁現為 <https://apastyle.apa.org/jars>；舊連結是否仍會轉址，因網站擋自動連線無法確認。 | 官方網域搜尋摘要 |
| 30 | sources.md:219、systematic-review.md:101 | PRISMA 2020 為系統性回顧報告準則 | 連結 | 仍正確 | 官網現行版仍是 PRISMA 2020。<https://www.prisma-statement.org/prisma-2020> | 直接讀取 |
| 31 | sources.md:220、systematic-review.md:101 | PRISMA-ScR 供範疇回顧使用 | 連結 | 仍正確 | 2018 年發表，官網仍列為現行延伸準則。<https://www.prisma-statement.org/scoping> | 直接讀取 |
| 32 | sources.md:221 | JBI Manual for Evidence Synthesis（連結） | 連結 | 仍正確 | 連結有效。<https://jbi-global-wiki.refined.site/space/MANUAL/> | 直接讀取 |
| 33 | sources.md:222 | Cochrane Handbook（current 連結） | 連結 | 仍正確 | current 頁面指向 Version 6.5（2024）。站內沒有寫版本號，不必修改。<https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current> | 直接讀取 |
| 34 | sources.md:224 | ASA p 值聲明（連結） | 連結 | 仍正確 | PDF 連結有效。<https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf> | 直接讀取 |
| 35 | sources.md:211 | ICPSR 社會科學資料準備與典藏指南（連結） | 連結 | 查不到官方來源 | 網站對自動連線回應 403，無法確認內容與連結現況。沒有修改。 | — |
| 36 | research-ethics-data.md:184、sources.md:209 | UK Data Service 研究資料管理基礎（連結） | 查證日 2026-09-04 | 仍正確 | 連結有效。<https://ukdataservice.ac.uk/learning-hub/data-producer-support/foundations-of-research-data-management/> | 直接讀取 |
| 37 | research-ethics-data.md:185、sources.md:210 | ICO 匿名化有效性指引（連結） | 查證日 2026-09-04 | 仍正確 | 連結有效。<https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/> | 直接讀取 |

## 五、研討會與台灣期刊

| # | 檔案:行號 | 原文摘要 | 目前引用的來源或日期 | 狀態 | 查證結果與官方來源 | 依據 |
|---|---|---|---|---|---|---|
| 38 | venues.md:40、65 | ICIS 2026（Lisbon）：12 個 track，2026/5/1 截止，7/27 通知 | 2026 年 9 月整理 | 仍正確 | 截止 5/1 23:59 WEST、7/27 前通知相符；會議 2026/12/13–16 尚未舉行。track 數與 2/11 開放投稿沒有逐一核對。<https://icis2026.aisconferences.org/submissions/call-for-papers/> | 官方網域搜尋摘要 |
| 39 | venues.md:66 | ECIS 2026：Milan，2026/6/15–17，26 個 track | 同上 | 仍正確 | 會議日期與 26 個 track 相符（會議已結束）。<https://ecis2026.it/track-descriptions/> | 直接讀取 |
| 40 | venues.md:67 | PACIS 2026：投稿截止 2026/3/8（延長後），Jakarta 7/4–8 | 同上 | 仍正確 | 截止日與會議日期相符；「延長後」這個註記無法確認（會議已結束）。<https://pacis2026.aisconferences.org/> | 官方網域搜尋摘要 |
| 41 | venues.md:68 | AMCIS 2026：3/1 17:00 PST 截止，Reno 8/20–22 | 同上 | 仍正確 | 相符（會議已結束）。<https://amcis2026.aisconferences.org/submissions/call-for-papers/> | 官方網域搜尋摘要 |
| 42 | venues.md:69 | HICSS 2027（第 60 屆）：6/15 截止，2027/1/5–8，Big Island | 同上 | 仍正確 | 相符（Hilton Waikoloa Village）。<https://hicss.hawaii.edu/> | 直接讀取 |
| 43 | venues.md:83 | 資訊管理學報：TSSCI、季刊（1、4、7、10 月出刊）、雙匿名審查、第一輪約 4 個月、2025 年五年影響係數 0.333 | 同上 | 仍正確 | 官網寫明「TSSCI 收錄，1994 年創刊，每年一、四、七、十月出刊」。雙匿名、審查時間與影響係數在官網首頁找不到，沒有逐項核對。<https://jim-tw.com/> | 直接讀取（部分） |
| 44 | venues.md:84 | 電子商務學報：TSSCI（自 2006 年）、6 月與 12 月底出刊、中英文皆可 | 同上 | 仍正確 | 相符。直接連線逾時，所以用搜尋摘要比對。<https://jeb.cerps.org.tw/> | 官方網域搜尋摘要 |
| 45 | venues.md:90 | ICIM 2026 第 37 屆：徵稿 2026/3/8–3/31，會議 2026/5/16（北科大） | 同上 | **已更新** | 官網寫明線上投稿 2026/3/8 開始，論文截稿「最後延長期限」為 2026/4/10；會議日期與地點相符。另外官網首頁在「數位轉型驅動跨域整合與協作治理創新」之上還有一行「AI Agent 領航，從對話到行動」，兩者哪一個才是正式主題無法判斷，所以主題沒有修改。<https://icim2026.com/> | 直接讀取 |
| 46 | venues.md:91 | TANET 暨全國計算機會議 2026：國北護主辦，投稿截止 2026/9/7，會議 10/29–31 | 同上 | 查不到官方來源 | 會議日期與主辦學校相符（搜尋摘要）；投稿截止與優惠截止日無法確認，因為官網連線逾時。**疑義**：官網標題是「TANET 2026 臺灣網際網路研討會暨 ICS」，不是「暨全國計算機會議」。沒有修改。<https://tanet2026.ntunhs.edu.tw/> | 官方網域搜尋摘要（部分） |
| 47 | venues.md:92、119 | NCS 已與 TANET 合併，不再單獨徵稿 | 同上 | 仍正確 | 2021、2023、2025 年的官網都是「TANET 暨 NCS」，合併舉辦屬實。**疑義**：2026 年改為「TANET 暨 ICS」（ICS 也是中華民國電腦學會的會議），「不再單獨徵稿」這句在 csroc.org.tw 無法連線、無法確認。沒有修改。<https://tanet2023.nccu.edu.tw/>、<https://tanet2025.niu.edu.tw/> | 官方網域搜尋摘要 |
| 48 | venues.md:94–95、119 | csim.org.tw 的 SSL 憑證已過期 | 同上 | 查不到官方來源 | 這個環境的連線經過代理，看到的是代理重簽的憑證，無法檢查網站原本的憑證。這條需要用一般瀏覽器確認。沒有修改。 | — |

## 本次同時處理的使用者指示（不屬於查核條目）

- `writing.md` 開頭新增提醒：學位論文格式以中華民國教育部相關規定與學校、系所規定為第一優先。同一頁第十節「實際格式一律以所屬系所的規定為準」也改成一致的說法。
- 查證時沒有找到教育部層級統一的「論文格式指引」。教育部層級可以查到的是《學位授予法》與〈大專校院學位論文送存國家圖書館典藏作業要點〉（處理送存、授權、個資隱蔽、延後公開）；封面、字型、邊界等版面格式由各校自訂，例如臺大、政大、成大的學位論文格式規範。提醒的文字依照這個現況撰寫。
