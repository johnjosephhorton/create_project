#!/bin/bash

echo "Important Claims" > .summary.md
echo "-----------------" >> .summary.md
sed -n '/^\\important{/ s/\\important{//p' {{ project_name }}.tex | sed 's/}//g' | sed 's/.*/1. &/' | sed  G >> .summary.md


echo "Quantitative Claims" >> .summary.md
echo "--------------------" >> .summary.md
sed -n '/^\\quantclaim{/ s/\\quantclaim{//p' {{ project_name }}.tex | sed 's/}//g' | sed 's/.*/1. &/' | sed  G >> .summary.md
echo "" >> .summary.md


echo "TK Sentences" >> .summary.md
echo "------------" >> .summary.md
sed -n '/TK/p' {{ project_name }}.tex | sed 's/.*/1. &/' | sed  G >> .summary.md 

echo "Abstract Stats" >> .summary.md 
echo "--------------" >> .summary.md

echo "lines, words and characters:" >> .summary.md
awk '/\\begin{abstract}/,/\\end{abstract}/' {{ project_name }}.tex | wc >> .summary.md

cat .summary.md > summary.md