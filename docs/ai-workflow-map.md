# 論文 AI 工作流全圖

> 這張圖先打地基，再把論文從找方向到口試分成六站，每一步都列出兩條路線各用什麼。只用網頁版 AI 的人，用專案功能（Projects、Gems）加提示詞；願意開終端機的人，用 Claude Code 或 Codex，再裝上站主整理的 thesis-toolkit SKILL。每站最右欄是要回原文核對的地方，這一欄兩條路線都一樣。圖裡的項目都連到本站對應的節次。

---

## 一、全圖

<div class="wfmap">
<p class="wf-legend"><span><i class="wf-tag live">已上線</i>點進去就是那一節</span><span><i class="wf-tag soon">尚未上線</i>正在寫，寫好會換成連結</span></p>
<ol class="wf-strip" aria-label="地基加六站流程">
<li><a href="#wf-s0"><b>0</b>地基</a></li>
<li><a href="#wf-s1"><b>1</b>找方向</a></li>
<li><a href="#wf-s2"><b>2</b>找文獻</a></li>
<li><a href="#wf-s3"><b>3</b>讀與筆記</a></li>
<li><a href="#wf-s4"><b>4</b>缺口與研究問題</a></li>
<li><a href="#wf-s5"><b>5</b>寫作</a></li>
<li><a href="#wf-s6"><b>6</b>送審與口試</a></li>
</ol>
<section class="wf-stage wf-base" id="wf-s0">
<h3 class="wf-title"><small>第 0 站・一次設定</small>地基</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>開專案，貼上專案指示：研究背景、構念中英對照、七條紅線（<a href="ai-quickstart.md#二建立專案">一小時上手第二、三節</a>）<i class="wf-tag live">已上線</i></li>
<li>上傳三篇核心文獻、系所格式規範、計畫草稿（<a href="ai-quickstart.md#四該上傳和不該上傳的">第四節</a>）<i class="wf-tag live">已上線</i></li>
<li>三個 SKILL 的網頁簡版提示詞，ChatGPT、Claude、Gemini 都能用（<a href="prompts.md#skill-lite">提示詞範本第十節</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li>指示檔：Claude Code 讀 <code>CLAUDE.md</code>，Codex 讀 <code>AGENTS.md</code>，紅線跟網頁版同一套。站主的設定見<a href="ai-case-study.md#五進階claude-code-設定">實例第五節</a> <i class="wf-tag live">已上線</i></li>
<li>安裝 thesis-toolkit：Claude Code 用 plugin，Codex 把 SKILL 資料夾複製到 <code>.agents/skills/</code>（<a href="https://github.com/wayhong0928/mis-thesis-skills#安裝方式">安裝說明</a>）<i class="wf-tag live">已上線</i></li>
<li>一步一步自己設定的 <a href="ai-quickstart-agent.md">Claude Code／Codex 一小時上手</a> <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>指示檔裡的紅線就是後面每一站的核對標準：只依上傳的文獻回答、數字附出處、橫斷面資料不寫因果、不捏造引用。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s1">
<h3 class="wf-title"><small>第 1 站</small>找方向</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>可以直接貼給 AI 的提示詞（<a href="getting-started.md#九完全沒有頭緒把這段貼給-ai">從零開始最後一節</a>）<i class="wf-tag live">已上線</i></li>
<li>環境掃描（<a href="prompts.md#11-環境掃描">提示詞範本 1.1</a>）<i class="wf-tag live">已上線</i></li>
<li>研究方向收斂的簡版提示詞（<a href="prompts.md#skill-lite-direction">提示詞範本 10.1</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li><a href="https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/research-direction-finding"><code>research-direction-finding</code></a>：把模糊的興趣收成一句話的研究想法 <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>AI 提的方向要能指到真實存在的文獻。帶著那幾篇去跟指導教授談。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s2">
<h3 class="wf-title"><small>第 2 站</small>找文獻</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>Consensus、Elicit 這類 AI 輔助檢索（<a href="tool-directory.md#32-ai-輔助檢索">工具指南 3.2</a>）<i class="wf-tag live">已上線</i></li>
<li>資料庫的檢索管道與關鍵字（<a href="finding-reading.md#二怎麼找-paper">怎麼找 paper</a>）<i class="wf-tag live">已上線</i></li>
<li>納入排除準則與檢索式（<a href="prompts.md#21-把模糊方向收斂成納入排除準則">提示詞範本 2.1</a>、<a href="prompts.md#22-檢索式產生與搜尋結果接力">2.2</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li>Consensus、Elicit 的官方 MCP，接上以後在 Claude Code 裡直接搜尋。加入指令和方案條件見<a href="tool-directory.md#32-ai-輔助檢索">工具指南 3.2</a> <i class="wf-tag live">已上線</i></li>
<li>資料庫檢索的方法跟網頁版相同 <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>每篇先確認文獻存在（<a href="prompts.md#31-文獻事實查核三步查核的第二步">提示詞範本 3.1</a>），再下載原文。搜尋工具給的摘要不能當原文引用。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s3">
<h3 class="wf-title"><small>第 3 站</small>讀與筆記</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>筆記模板，請 AI 寫初稿（<a href="ai-quickstart.md#五文獻筆記模板">一小時上手第五節</a>）<i class="wf-tag live">已上線</i></li>
<li>構念定義表（<a href="ai-quickstart.md#61-用三篇核心文獻整理構念定義表">一小時上手 6.1</a>）、文獻矩陣（<a href="prompts.md#32-文獻矩陣">提示詞範本 3.2</a>）、單篇導讀（<a href="prompts.md#34-單篇論文導讀先自己讀再讓-ai-考你">3.4</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li>筆記軟體與欄位設計（<a href="tools-knowledge.md">文獻管理與知識庫</a>）<i class="wf-tag live">已上線</i></li>
<li>Zotero 加 Obsidian 的筆記庫範本，讓 AI 直接讀寫筆記資料夾 <i class="wf-tag soon">尚未上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>數字、樣本數、構念名稱逐項回 PDF 打勾。「跟我的研究有什麼關係」那一欄自己寫。<a href="ai-quickstart.md#七練習找出-ai-寫錯的地方">一小時上手第七節</a>的練習就是在練這一步。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s4">
<h3 class="wf-title"><small>第 4 站</small>缺口與研究問題</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>找研究缺口（<a href="ai-quickstart.md#63-請-ai-找研究缺口再自己回原文確認">一小時上手 6.3</a>）、口試委員式反駁（<a href="ai-quickstart.md#62-請-ai-對你的研究問題提出反駁">6.2</a>）<i class="wf-tag live">已上線</i></li>
<li>邏輯斷鏈與理論縫合（<a href="prompts.md#41-邏輯斷鏈檢查研究教練角色">提示詞範本 4.1</a>、<a href="prompts.md#43-理論縫合診斷">4.3</a>）<i class="wf-tag live">已上線</i></li>
<li>研究問題稽核的簡版提示詞（<a href="prompts.md#skill-lite-audit">提示詞範本 10.2</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li><a href="https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/research-question-audit"><code>research-question-audit</code></a>：七個檢查點，其中一項看研究問題、假說、架構圖、分析方法彼此對不對得上 <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>缺口一律寫成「在這幾篇裡沒看到」，再到資料庫搜一次。標了〔推論〕的反駁當成待查清單。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s5">
<h3 class="wf-title"><small>第 5 站</small>寫作</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>去 AI 感自檢、送達測試（<a href="prompts.md#61-去-ai-感自檢">提示詞範本 6.1</a>、<a href="prompts.md#62-送達測試">6.2</a>）<i class="wf-tag live">已上線</i></li>
<li>學術寫作紀律的簡版提示詞（<a href="prompts.md#skill-lite-writing">提示詞範本 10.3</a>）<i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li><a href="https://github.com/wayhong0928/mis-thesis-skills/tree/main/plugins/thesis-toolkit/skills/academic-writing-discipline"><code>academic-writing-discipline</code></a>：因果動詞、構句、APA 7、台灣學術用語 <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>橫斷面資料不寫「導致」這類動詞（<a href="style.md#一因果動詞紀律">學術中文寫作紀律第一節</a>）。每個引用都回原文確認作者真的這樣說。</p>
</div>
</div>
</section>
<section class="wf-stage" id="wf-s6">
<h3 class="wf-title"><small>第 6 站</small>送審與口試</h3>
<div class="wf-cells">
<div class="wf-cell web"><p class="wf-lane">網頁版</p><ul>
<li>摘要要素檢核、簡報結構檢查（<a href="prompts.md#63-摘要要素檢核">提示詞範本 6.3</a>、<a href="prompts.md#64-簡報結構檢查">6.4</a>）<i class="wf-tag live">已上線</i></li>
<li><a href="defense.md">計畫書、口試與簡報</a>、<a href="ethics.md">學術倫理與 AI 揭露</a> <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell cli"><p class="wf-lane">Claude Code／Codex</p><ul>
<li><code>research-question-audit</code> 的對抗式審查，產出預期質詢清單 <i class="wf-tag live">已上線</i></li>
</ul></div>
<div class="wf-cell chk"><p class="wf-lane">回原文核對</p>
<p>AI 揭露照系所和指導教授的規定寫。質詢清單裡的每一題，都要能指回論文或文獻裡的位置。</p>
</div>
</div>
</section>
</div>

## 二、從哪裡開始

- 第一次用 AI 做研究：先做[一小時上手](ai-quickstart.md)，做完照它第八節的順序往下讀。
- 願意開終端機：做 [Claude Code／Codex 版的一小時上手](ai-quickstart-agent.md)，裡面有 thesis-toolkit 的安裝步驟。站主自己的設定在[實例第五節](ai-case-study.md#五進階claude-code-設定)。工具本身怎麼設定，看 [ai-agent-notes](https://wayhong0928.github.io/ai-agent-notes/)。

第 2 到第 4 站實際上會來回跑好幾輪：讀到新文獻就回頭改研究問題，問題改了再補文獻。不確定自己卡在哪一站，用[AI 輔助研究工作流第十節](ai-workflow.md#十卡關診斷你站在哪個階段)的卡關診斷先定位。
