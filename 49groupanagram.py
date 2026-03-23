{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red70\green137\blue204;\red30\green30\blue30;\red202\green202\blue202;
\red67\green192\blue160;\red212\green214\blue154;\red140\green211\blue254;\red183\green111\blue179;\red194\green126\blue101;
}
{\*\expandedcolortbl;;\cssrgb\c33725\c61176\c83922;\cssrgb\c15686\c15686\c15686;\cssrgb\c83137\c83137\c83137;
\cssrgb\c30588\c78824\c69020;\cssrgb\c86275\c86275\c66667;\cssrgb\c61176\c86275\c99608;\cssrgb\c77255\c52549\c75294;\cssrgb\c80784\c56863\c47059;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class\cf4 \strokec4  \cf5 \strokec5 Solution\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 def\cf4 \strokec4  \cf6 \strokec6 groupAnagrams\cf4 \strokec4 (\cf7 \strokec7 self\cf4 \strokec4 , \cf7 \strokec7 strs\cf4 \strokec4 : List[\cf5 \strokec5 str\cf4 \strokec4 ]) -> List[List[\cf5 \strokec5 str\cf4 \strokec4 ]]:\cb1 \
\cb3         n = \cf6 \strokec6 len\cf4 \strokec4 (strs)\cb1 \
\cb3         a = \{\}\cb1 \
\
\cb3         \cf8 \strokec8 for\cf4 \strokec4  i \cf8 \strokec8 in\cf4 \strokec4  \cf6 \strokec6 range\cf4 \strokec4 (n):\cb1 \
\cb3             temp = \cf5 \strokec5 list\cf4 \strokec4 (strs[i])\cb1 \
\cb3             temp.sort()\cb1 \
\cb3             temp2 = \cf9 \strokec9 ""\cf4 \strokec4 .join(temp)\cb1 \
\
\cb3             \cf8 \strokec8 if\cf4 \strokec4  temp2 \cf2 \strokec2 in\cf4 \strokec4  a:\cb1 \
\cb3                 a[temp2].append(strs[i])\cb1 \
\cb3             \cf8 \strokec8 else\cf4 \strokec4 :\cb1 \
\cb3                 a[temp2] = [strs[i]]\cb1 \
\
\cb3         \cf8 \strokec8 return\cf4 \strokec4  \cf5 \strokec5 list\cf4 \strokec4 (a.values())\
\
\
\
Sorting a words in a list :\
\
Step 1: for loop\
Step 2: breaking the words into list( eg ate----> "a", "t" ,"e")  temp=s[i])\
Step 3: now sorting  temp.sort()\
Step 4: "".join(temp)\
\
\
Creating a list \
a=\{\}\
\
returning a list\
return list(a.values())\
\
Adding the list in correct index:\
 if temp2 in a:---> checking \
             a[temp2].append(strs[i])    --> adding the elelmt in correct index\
         else:\
              a[temp2] = [strs[i]]  --> creating anew array list nested array\cb1 \
}