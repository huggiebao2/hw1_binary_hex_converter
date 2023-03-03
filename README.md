# Decimal to Binary/Hexadecimal Converter

## How to Use
![](https://i.imgur.com/MeNTx8E.gif)

1. Run Binary_Hexadecimal_Converter.py .
2. Input a decimal number between 0 to 255.


### Example
For example, if you input the decimal number "10", the program will output:
```
You entered: 10
Binary representation: 1010
Hexadecimal representation: A
```

## Conversion Principle

> #### Info
> - Draft and explanation can be found in **Notes.ipynb**。
> - Conversion methods are defined as `Convert_2_Bin()` and `Convert_2_Hex()` in **Binary_Hexadecimal_Converter.py** and **Binary_Hexadecimal_Converter_GUI.py** .

In the decimal system, when a number exceeds ten, it will carry over to the next digit. For example, when the number is 9, the next number is ten, so 1 is carried over to the "tens" digit, and the "ones" digit returns to 0.

$$9+1 = 1 \times 10^1 + 0 \times 10^0 = 10$$

When a number exceeds 10 in the decimal system, we divide it by 10 to obtain a quotient ($\textbf{Q}$) and a remainder ($\underline{r}$). The quotient is then added to the next digit, and the remainder remains in the current digit.

$$a \div b = Q ... r$$

$$a = (Q \times b) + r$$

For example：

$$10 \div 10 = \textbf{1} ... \underline{0}$$

$$10 = (\textbf{1} \times 10) + \underline{0}$$

This process is repeated until the entire number has been converted.

$$\begin{align*}
\underline{42310} 
&= 42310\times 1\\
&= \textbf{4231} \times 10 + \underline{0}\times 1\\
&= \Big(\textbf{423} \times 10 + \underline{1}\Big) \times 10 + \underline{0}\times 1\\
&= \bigg(\Big(\textbf{42} \times 10 + \underline{3}\Big) \times 10 + \underline{1}\bigg) \times 10 + \underline{0}\times 1\\
&=\ ...\\
&= \underline{4} \times 10^4 + \underline{2} \times 10^3 + \underline{3} \times 10^2 + \underline{1} \times 10^1 + \underline{0} \times 10^0
\end{align*}$$

The process of dividing by the base and taking the quotient and remainder is a fundamental principle of positional notation, which is used in all numbering systems. Therefore, the same conversion principle applies to binary, hexadecimal, octal, and other numbering systems as well.

## Representation of Binary and Hexadecimal

- In binary notation, as mentioned earlier, each digit represents a remainder obtained by dividing the number by 2, and therefore, there are only two possible values: `0` and `1`.
    | Decimal | $r \times 2^n$ | Binary |
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
- In hexadecimal notation, each digit can have a value from 0 to 15. To represent the values greater than 9, letters `A` through `F` are used.
    | Decimal | Hexadecimal | Decimal | Hexadecimal |
    | --- | --- | --- | --- |
    | 0 | `0` | 8 | `8` |
    | 1 | `1` | 9 | `9` |
    | 2 | `2` | 10 | `A` |
    | 3 | `3` | 11 | `B` |
    | 4 | `4` | 12 | `C` |
    | 5 | `5` | 13 | `D` |
    | 6 | `6` | 14 | `E` |
    | 7 | `7` | 15 | `F` |
    
## Bonus：GUI version (Experimental)

### How to Use
1. Run Binary_Hexadecimal_Converter_GUI.py.
2. Enter an integer within the range of 0 to 255 in the text box.
3. Click the `Convert` button and the output will be displayed below.

    ```
    Binary representation: <bin_num>
    Hexadecimal representation: <hex_num>
    ```