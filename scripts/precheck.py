#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
推送前的隱私與用語檢查，對應 README「隱私與內容檢查」的兩道 grep。
用法：python scripts/precheck.py [路徑 ...] [--warn-only]
  路徑：要檢查的檔案或目錄，目錄會遞迴找 .md；省略時檢查 docs/
  --warn-only：有命中也回傳 0
結束碼：0 沒有命中，1 有命中，2 路徑不存在或檔案無法以 UTF-8 讀取
只用 Python 標準函式庫。
"""
import os
import re
import sys
import argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PATHS = [os.path.join(ROOT, "docs")]
MAX_LINE = 80

# 殘留的個人研究資訊（依自己的關鍵字調整），不分大小寫
PRIVACY_TERMS = ["我的論文", "本研究的構念", "學號", "真實姓名"]

# 大陸用語
MAINLAND_TERMS = [
    "被試", "數據收集", "信息", "回歸分析", "結果表明", "人工智能",
    "用戶", "算法", "數據庫", "優化", "場景", "默認", "受眾",
]

# 前面接這個字時不算命中：「演算法」是台灣用法
SKIP_PREFIX = {"算法": "演"}

# (組名, 關鍵字, re 旗標)
RULES = [
    ("個資", PRIVACY_TERMS, re.IGNORECASE),
    ("大陸用語", MAINLAND_TERMS, 0),
]


def collect_files(paths):
    """展開參數：檔案直接收，目錄遞迴找 .md。"""
    files, missing = [], []
    for p in paths:
        if os.path.isfile(p):
            files.append(p)
        elif os.path.isdir(p):
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames.sort()
                for name in sorted(filenames):
                    if name.lower().endswith(".md"):
                        files.append(os.path.join(dirpath, name))
        else:
            missing.append(p)
    return files, missing


def display_path(path):
    """repo 內的檔案顯示相對路徑，其餘顯示原路徑；一律用 / 分隔。"""
    full = os.path.abspath(path)
    try:
        rel = os.path.relpath(full, ROOT)
    except ValueError:  # Windows 上不同磁碟機
        rel = None
    shown = path if rel is None or rel.startswith("..") else rel
    return shown.replace(os.sep, "/")


def shorten(text):
    text = text.strip()
    return text if len(text) <= MAX_LINE else text[:MAX_LINE] + "…"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="推送前的隱私與大陸用語檢查")
    parser.add_argument("paths", nargs="*", help="要檢查的檔案或目錄（預設 docs/）")
    parser.add_argument("--warn-only", action="store_true", help="有命中也回傳 0")
    args = parser.parse_args()

    files, missing = collect_files(args.paths or DEFAULT_PATHS)
    errors = len(missing)
    for p in missing:
        print(f"找不到路徑：{p}", file=sys.stderr)

    def term_regex(term):
        prefix = SKIP_PREFIX.get(term)
        return (f"(?<!{re.escape(prefix)})" if prefix else "") + re.escape(term)

    patterns = [(name, re.compile("|".join(map(term_regex, terms)), flags))
                for name, terms, flags in RULES]
    hits = {name: [] for name, _ in patterns}

    for path in files:
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except (OSError, UnicodeDecodeError) as e:
            print(f"無法讀取 {path}：{e}", file=sys.stderr)
            errors += 1
            continue
        # 和 grep 一樣只以 \n 分行，行號才會一致
        for lineno, line in enumerate(text.split("\n"), 1):
            line = line.rstrip("\r")
            for name, pattern in patterns:
                words = []
                for m in pattern.findall(line):
                    if m.lower() not in (w.lower() for w in words):
                        words.append(m)
                if words:
                    hits[name].append(
                        f"{display_path(path)}:{lineno}: {'、'.join(words)} | {shorten(line)}")

    for name, _ in patterns:
        print(f"== {name} ==")
        print("\n".join(hits[name]) if hits[name] else "（無）")
        print()

    print(f"檢查 {len(files)} 個檔案")
    for name, _ in patterns:
        print(f"{name}：{len(hits[name])} 筆")

    if errors:
        return 2
    if any(hits.values()) and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
