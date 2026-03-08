library(data.table)
setwd("/Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/Data")

files <- list(
  "panel_capital_accounts.csv",
  "panel_labour_accounts.csv",
  "panel_national_accounts.csv",
  "panel_growth_accounts.csv"
)

dts <- lapply(files, fread)

panel <- Reduce(
  function(x, y) merge(x, y, by = c("year", "nace_r2_code"), all = TRUE),
  dts
)
fwrite(panel, "final_panel.csv")
