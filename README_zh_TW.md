# 十進位至二進位/十六進位轉換器

## 使用方式
1. 運行 Binary_Hexadecimal_Converter.py。
2. 輸入在 0 ~ 255 範圍內的整數。

## 轉換原理

> #### 說明
> - 草稿與說明可見 Notes.ipynb。
> - 在 Binary_Hexadecimal_Converter.py 及 Binary_Hexadecimal_Converter_GUI.py 中，定義成 `Convert_2_Bin()` 及 `Convert_2_Hex()`

十進位制中，當一個數字超過十，就會進位到下一個位數。舉例來說，9 的下一個數字就是十，因此會將 1 進位到十位數，個位數回到 0。

$$9+1 = 1 \times 10^1 + 0 \times 10^0 = 10$$

我們可以將其視為，只要超過 10，就把除以 10 拿到的數字（商數），進位到下一位數，再把餘數放回去。

$$a \div b = Q ... r$$

$$a = (Q \times b) + r$$

例如：

$$10 \div 10 = \textbf{1} ... \underline{0}$$

$$10 = (\textbf{1} \times 10) + \underline{0}$$

我們可以把超過十位數（例如百位數或更高）的視為一連串的商數 $\textbf{Q}$ 與餘數 $\underline{r}$：

$$\begin{align*}
\underline{42310} 
&= 42310\times 1\\
&= \textbf{4231} \times 10 + \underline{0}\times 1\\
&= \Big(\textbf{423} \times 10 + \underline{1}\Big) \times 10 + \underline{0}\times 1\\
&= \bigg(\Big(\textbf{42} \times 10 + \underline{3}\Big) \times 10 + \underline{1}\bigg) \times 10 + \underline{0}\times 1\\
&=\ ...\\
&= \underline{4} \times 10^4 + \underline{2} \times 10^3 + \underline{3} \times 10^2 + \underline{1} \times 10^1 + \underline{0} \times 10^0
\end{align*}$$

這在其他進位制中也同理。

## 二進位與十六進位的表示方式

- 在二進位中，誠如上述，每個位數都是除以二的餘數，因此只有兩個可能數值：`0` 和 `1`。
    | 十進位 | $r \times 2^n$ | 二進位 |
    | ---: | ---: | ---: |
    | 0 | $0 \times 2^0$ | 0 |
    | 1 | $1 \times 2^0$ | 1 |
    | 2 | $1 \times 2^1 + 0 \times 2^0$ | 10 |
    | 3 | $1 \times 2^1 + 1 \times 2^0$ | 11 |
    | 4 | $1 \times 2^2 + 0 \times 2^1 + 0 \times 2^0$ | 100 |
    | 5 | $1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$ | 101 |
    | 6 | $1 \times 2^2 + 1 \times 2^1 + 0 \times 2^0$ | 110 |
    | 7 | $1 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$ | 111 |
    | 8 | $1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 0 \times 2^0$ | 1000 |
- 在十六進位中，單一位數的範圍是 0 到 15，在表示上使用 `A` 至 `F` 來擴充。
    | 十進位 | 十六進位 | 十進位 | 十六進位 |
    | --- | --- | --- | --- |
    | 0 | `0` | 8 | `8` |
    | 1 | `1` | 9 | `9` |
    | 2 | `2` | 10 | `A` |
    | 3 | `3` | 11 | `B` |
    | 4 | `4` | 12 | `C` |
    | 5 | `5` | 13 | `D` |
    | 6 | `6` | 14 | `E` |
    | 7 | `7` | 15 | `F` |
    
## 附加：圖形介面版本 (實驗性)
> 最近稍微接觸 `tkinter`，就想要試看看。

### 使用方式
1. 運行 Binary_Hexadecimal_Converter_GUI.py。
2. 在文字框輸入 0 ~ 255 範圍內的整數。
3. 點擊 `Convert` 按鈕，輸出結果將顯示在下方。

    ```
    Binary representation: <二進位數值>
    Hexadecimal representation: <十六進位數值>
    ```