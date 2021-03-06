dim(H1B_project)
unique(H1B_project$job)
unique(H1B_project$employer)
unique(H1B_project$job_title)
unique(H1B_project$status)
head(H1B_project)
H1B_project1=H1B_project[,-1]
head(H1B_project1)
sum(is.na(H1B_project1))
H1B_project1=na.omit(H1B_project1)
head(H1B_project1)
sum(is.na(H1B_project1))
dim(H1B_project1)
dim(H1B_project)
names(H1B_project)
names(H1B_project1)
library(tidyr)
library(dplyr)
library(ggplot2)
library(lubridate)
H1B_project1=H1B_project1 %>% mutate(., Start.Year=year(as.Date(start_date, format="%m/%d/%y")))
H1B_project1=H1B_project1 %>% mutate(., Submit.Year=year(as.Date(submit_date, format="%m/%d/%y")))
names(H1B_project1)
unique(H1B_project1$Start.Year)
H1B_project1=H1B_project1 %>% mutate(., Submit.Month=month(as.Date(submit_date, format="%m/%d/%y")))
H1B_project1=H1B_project1 %>% mutate(., Start.Month=month(as.Date(start_date, format="%m/%d/%y")))
names(H1B_project1)

Y =H1B_project1 %>% separate(., location1, into= c('CITY','STATE'), sep = ',')

x=H1B_project1 %>% group_by(., )
