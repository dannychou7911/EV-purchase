---
name: xlsx-to-md
description: 將 BUZ-7000 車輛記帳 App 匯出的 xlsx 檔案轉換為 Markdown 表格，方便 Claude 讀取車輛使用紀錄資料。當使用者提到「讀取 xlsx」、「轉換 Excel」、「車輛紀錄」、「用車紀錄」、「BUZ-7000」、「匯入紀錄」時觸發。適用於 docs/ 目錄下的 *-BUZ-7000.xlsx 檔案。
---

# xlsx-to-md

將 BUZ-7000 匯出的 xlsx 車輛使用紀錄轉為 Markdown 表格。

## 欄位格式

xlsx 固定五欄：`日期` | `里程數 (公里)` | `總額` | `抬頭` | `備註`

## 使用方式

執行轉換腳本（需 `openpyxl`）：

```bash
python3 .claude/skills/xlsx-to-md/scripts/xlsx_to_md.py <input.xlsx> [output.md]
```

- 省略 output 參數時輸出至 stdout
- 輸出包含標題、紀錄數量、完整 Markdown 表格

## 典型流程

1. 確認 docs/ 下的目標 xlsx 檔案
2. 執行腳本轉換為 Markdown
3. 讀取轉換後的 Markdown 內容進行分析

## 檔案命名慣例

檔名格式：`YYMMDD-BUZ-7000.xlsx`，日期為匯出日期。較新的檔案包含較舊檔案的所有紀錄加上新增部分，取最新檔案即可。
