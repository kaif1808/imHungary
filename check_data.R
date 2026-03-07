library(readxl)
library(tidyverse)
path <- "Data/HU_labour_accounts.xlsx"

ga <- read_csv("Data/HU_growth_accounts.csv", show_col_types=FALSE)
cat("Growth accounts columns:", paste(names(ga), collapse=", "), "\n")

broad_sectors <- c("TOT","A","B","C","D-E","F","G","H","I","J","K","L","M-N","O-Q","R-S")
labqi_check <- ga |> filter(nace_r2_code %in% broad_sectors) |> select(nace_r2_code, year, LAB_QI)

cat("\nLABQI per sector - year range:\n")
labqi_nn <- labqi_check[!is.na(labqi_check$LAB_QI), ]
agg_yr <- aggregate(year ~ nace_r2_code, labqi_nn, function(x) c(min=min(x), max=max(x), n=length(x)))
print(agg_yr)

sh_e <- read_excel(path, sheet="Share_E")
long_e <- pivot_longer(sh_e, cols=matches("^[0-9]{4}$"), names_to="year", values_to="val")
long_e$year <- as.integer(long_e$year)
cat("\nShare_E obs per year:\n")
tab_e <- long_e |> group_by(year) |> summarise(n_obs = sum(!is.na(val)), .groups="drop")
print(tab_e, n=30)

sh_w <- read_excel(path, sheet="Share_W")
long_w <- pivot_longer(sh_w, cols=matches("^[0-9]{4}$"), names_to="year", values_to="val")
long_w$year <- as.integer(long_w$year)
cat("\nShare_W obs per year:\n")
tab_w <- long_w |> group_by(year) |> summarise(n_obs = sum(!is.na(val)), .groups="drop")
print(tab_w, n=30)

cat("\nUnique codes in Share_E:", paste(unique(sh_e$code), collapse=", "), "\n")
cat("Education levels:", paste(unique(sh_e$education), collapse=", "), "\n")
cat("Age groups:", paste(unique(sh_e$age), collapse=", "), "\n")
cat("Genders:", paste(unique(sh_e$gender), collapse=", "), "\n")
