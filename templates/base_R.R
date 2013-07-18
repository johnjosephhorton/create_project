#! /usr/bin/Rscript --vanilla

###############################################
# Author: {{ author }} 
# Created Date: {{ creation_date }} 
# Project: {{ project_name }} 
###################################################

library(ggplot2)
library(scales)
library(testthat)

N <- 1000
df.raw <- data.frame(x = runif(N), y = runif(N))

pdf("../../writeup/plots/hist.pdf")
 qplot(x, y, data = df.raw)
dev.off() 
