---
layout: thesis_checklist
title: "Thesis writing checklist"
---

# Overall advice
If you want to use Microsoft Word to write your thesis, you had better know how to operate Word's styles settings, which can help save you adjusting sentences one by one.

If you use LaTeX to render your thesis, the benefit is that most formats are well defined and you can focus on the content. However, you need to spend effort on learning LaTeX syntax and being familiar with used packages.

# 1 Inconsistency

## 1.1 Inconsistent indentation
<img src="Indentation.png" height="400">

Advice: Paragraphs at the same level should have the same indentation.

## 1.2 Inconsistent font size
<img src="fontsize.png" height="120">

The (Luo et al., 2020) is smaller than other words.

## 1.3 Inconsistent fullwidth and halfwidth characters
<img src="halfwidth_fullwidth1.png" height="60">

This is a Chinese sentence and every character is fullwidth, but the ending period becomes halfwidth.

<img src="halfwidth_fullwidth2.png" height="60">

The first pair of parentheses is fullwidth, but the second is halfwidth.

## 1.4 Inconsistent language
<img src="Language1.png" height="60">

The table of content is in Chinese, but the term References is in English.

Advice: Change Reference to 參考資料.

<img src="Language2.png" height="240">

The thesis is written in Chinese, but the flow chart is written in English.

Advice: Redraw the flow chart.

## 1.5 Inconsistent reading direction
<img src="ReadingDirection1.png" height="360">

The bottom-right region needs to be read from right to left, which is inconsistent with the other three regions in this figure.

Revised:

<img src="ReadingDirection2.png" height="360">

## 1.6 Inconsistent blank
<img src="blank.png" height="90">

There is a missing blank between 3.8 and 倫理.

## 1.7 Inconsistent fonts
<img src="Font.png" height="210">

The fonts of 2.5 and 1. 2. are different. 

Advice: Unless you want to emphasize something different, use the same font.

## 1.8 Inconsistent numbering formats
<img src="Numbering1.png" height="210">
<img src="Numbering2.png" height="210">

The two paragraphs are consecutive, but their numbering formats are different.

Advice: Make them consistent.

<img src="Numbering3.png" height="120">
<img src="Numbering4.png" height="30">

It is inconsistent for GOLD 1 2 3 4 and GOLD II III.

## 1.9 Inconsistent case
<img src="Case.png" height="240">

"Feature Importance" is each word capitalized, but "loss reduction" is in lowercase.

# 2 Format

## 2.1 Wrong alignment settings
<img src="Alignment1.png" height="400">
<img src="Alignment2.png" height="400">
<img src="Alignment4.png" height="400">
<img src="Alignment3.png" height="400">

Advice: Use justified rather than align left.
## 2.2 Improper indentation
<img src="InsufficientIndentation.png" height="90">

The indentation here is too small. A proper indentation is 2 characters for Chinese sentences.

## 2.3 Forget to explain an acronym
<img src="Acronym.png" height="90">

Here DALYs and DALY are used, but its full name is missing.

Advice: Change to (DALY: Disability-Adjusted Life Year)

## 2.4 Unreasonable bold type
<img src="Bold.png" height="360">

I have no idea why some characters are suddenly in the bold type.

Advice: Remove their bold setting.

## 2.5 Unreasonable large number of decimal places
<img src="Table1.png" height="200">

Advice: Make them shorter and consistent.

# 3 References

## 3.1 Wrong expression of the author names
<img src="AuthorName1.png" height="60"> <br/>
<img src="AuthorName2.png" height="60"> <br/>
<img src="AuthorName3.png" height="60">

All author names are wrong. 

## 3.2 Double periods
<img src="AuthorName1.png" height="60">

It is impossible to have double periods at the end.

## 3.3 Good references example
This is an example of a well formatted references. Extracted from Luo L, Li J, Lian S, Zeng X, Sun L, Li C, Huang D, Zhang W. Using machine learning approaches to predict high-cost chronic obstructive pulmonary disease patients in China. Health Informatics J. 2020 Sep;26(3):1577-1598. doi: 10.1177/1460458219881335.
<img src="GoodReferences1.png" width="1000"> <br/>
<img src="GoodReferences2.png" width="1000">

# 4 acronym 

## 4.1 Incorrect case 
<img src="Acronym1.png" height="30">

It should be DOSE.

## 4.2 Incorrect full name location
<img src="Acronym2.png" height="120">

The full name of GOLD should be shown when the acronym is first used in the thesis. 

# 5 Figure
## 5.1 Resolution too low
<img src="Resolution.png" height="480">

The resolution is too low to clearly show characters.

Advice: Redraw this figure.

## 5.2 Inadequate caption
<img src="Caption.png" height="90">

The correct format should be 圖一：AI模型建構邏輯與流程圖。It is incorrect to use a subsection number to index the caption.

# 6 Grammar
## 6.1 Ambiguous relative pronoun which
<p> Otsu’s method [24] is a widely used automatic threshold selection method for image binarization in computer vision applications, <span class="highlight">which</span> determines the optimal threshold by maximizing the inter-class variance of pixel intensities. </p>

The author uses the which to infer to the main clause, but the which occurs after the noun "computer vision applications" and confuses readers.

## 6.2 Incorrect colon
<img src="Colon.png" height="90">

The equation is part of the sentence. We need to treat as a sentence so there should be no colon.

# 7 Table
## 7.1 Use an image
<img src="Table1.png" height="200">

This is wrong. The newline symbols should not appear. You should create a real table rather than using an image instead.
A real table can be rendered elegantly, but an image will look burry when a large zooming factor is used.

# 8 Poor translation
"Global healthcare systems are increasingly challenged by workforce shortages, burnout, and excessive workloads. Socially Assistive Robots (SARs) have emerged as a potential solution. Although SARs have demonstrated potential in pediatric care, existing research has largely concentrated on technological development or patient-centered perspectives, with insufficient focus on the experiences and professional insights of frontline healthcare providers."

This English abstract is translated from its Chinese version using a translation tool.

"隨著全球醫療體系面臨人力短缺、職業倦怠與工作負荷過重等挑戰，社交輔助機器人（Socially Assistive Robots, SARs）在臨床照護中的應用逐漸受到關注。雖然 SARs 在兒科醫療中展現潛力，但現有研究多聚焦於機器人發展的技術面或病患觀點，缺乏對第一線醫護人員經驗與專業角色看法的深入探討，並且多數研究缺乏理論依據以及實際使用的經驗。"

However, the translated English sentences become very difficult to read.

Advice: Find a native speaker to rewrite those sentences.

# 9 Irrelevant content
<img src="IrrelevantContent1.png" height="400" alt="IrrelevantContent">

The icon at the bottom right corner <img src="IrrelevantContent2.png" height="40" alt="IrrelevantContent">is irrelevant.

Advice: Remove it.


