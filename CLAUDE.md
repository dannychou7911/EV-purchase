# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ford Focus Wagon vs Tesla Model Y RWD 換車經濟效益評估報告。這是一個純靜態的單頁網頁專案，透過 GitHub Pages 部署，無任何 build 工具或套件管理器。

## Architecture

- **`index.html`** — 整個報告的唯一頁面，包含所有 HTML、CSS（`<style>` 內嵌）、JavaScript（`<script>` 內嵌）。使用 Chart.js（CDN 載入）繪製 6 張圖表（保養費用、年度營運成本、累計支出、TCO 結構、節省來源、油價敏感度分析）。
- **`docs/`** — Markdown 分析文件與原始資料（Excel），包含用車報告、保養費用明細、貸款方案、評估報告等。這些是研究資料，非程式碼的一部分。
- **`imgs/`** — 原廠定保費用表與消耗性零件費用截圖。

## Development

無 build、lint、test 流程。直接編輯 `index.html` 後用瀏覽器開啟即可預覽。

```bash
# 本機預覽
open index.html
```

## Deployment

透過 GitHub Pages 部署（推送到 `main` 即部署）。

## Key Context

- 所有金額單位為新台幣（NT$）
- 評估期間為 10 年（2026 ~ 2036），基準里程每月 1,661 km
- Chart.js 圖表數據直接寫在 `<script>` 中，修改數據需同步更新 HTML 表格與 JS 圖表資料
- CSS 使用 CSS custom properties（`--focus-color`, `--tesla-color` 等）統一配色
