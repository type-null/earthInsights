# 10 Google Sheets Formulas
Source: [link](https://codingisforlosers.com/google-sheets-formulas/).
[Tutorial](https://docs.google.com/spreadsheets/d/1aOAoqOcZ7JigNJ9UqqJKzP-S0-cQh3MW47bU5tUQ_IQ/copy).

## 1 `ARRAYFORMULA`
- Apply formula to an entire row or column
- Pass cell 'A2' as array: `=ARRAYFORMULA( VLOOKUP( A2:A, data!$A:$C, 3, 0))`
- Example:

|A    	    |B         |A - B
|:---------:|:--------:|:-------:
|174,193	|58,028    |`=ARRAYFORMULA(A1:A5-B1:B5)`
|109,189	|44,409    |
|32,454	    |1,720     |
|1,845	    |893       |
|2,115	    |1,041     |

## 2 `SPLIT`
- `=SPLIT(B3," ")` converts sentence in 'B3' into words in separated cells

## 3 `INDEX`
- `=INDEX(B3:C4, 2, 1)` returns cell in row 2, col 1


