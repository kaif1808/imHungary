#!/usr/bin/env Rscript
# Generate Finance sector (K) 3-factor decomposition figure
# Uses panel_with_labqi_backcast.csv (must run backcast_labqi.ipynb first)

library(tidyverse)
library(data.table)

dir.create("output/figures", showWarnings = FALSE, recursive = TRUE)

fp <- fread("/Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/Data/panel_with_labqi_backcast.csv")
broad_sectors <- c("A", "B", "C", "D-E", "F", "G", "H", "I", "J", "K", "L", "M-N", "O-Q", "R-S")

decomp_df <- fp |>
  filter(nace_r2_code %in% broad_sectors, year >= 1995, year <= 2011) |>
  mutate(
    total_hours = valH_EMP * (valEMP / valEMPE),
    LAB_QI = valueLAB_QI
  )

alpha <- 1/3
decomp_df <- decomp_df |>
  group_by(nace_r2_code) |>
  arrange(year) |>
  mutate(
    base_va = valVA_CP[year == min(year[!is.na(valVA_CP)])][1],
    VA_real = (valVA_Q / 100) * base_va,
    y = VA_real / total_hours,
    g_y = (log(y) - log(dplyr::lag(y))) * 100,
    g_K = (log(valKq_GFCF) - log(dplyr::lag(valKq_GFCF))) * 100,
    g_L = (log(total_hours) - log(dplyr::lag(total_hours))) * 100,
    cap_contrib = (alpha / (1 - alpha)) * (g_K - g_L),
    g_h = (log(LAB_QI) - log(dplyr::lag(LAB_QI))) * 100,
    hc_contrib = g_h,
    tfp_contrib = g_y - cap_contrib - hc_contrib
  ) |>
  ungroup()

fin_K <- decomp_df |>
  filter(nace_r2_code == "K", !is.na(tfp_contrib)) |>
  transmute(
    year,
    cap = cap_contrib,
    hc = hc_contrib,
    tfp = tfp_contrib,
    total = g_y
  )

fin_K_long <- fin_K |>
  select(year, cap, hc, tfp, total) |>
  pivot_longer(-year, names_to = "component", values_to = "contrib") |>
  mutate(component = recode(component,
    cap = "Capital deepening",
    hc = "Human capital",
    tfp = "TFP",
    total = "Total"
  ))

events <- data.frame(year = c(2004, 2008, 2010), event = c("EU Accession", "GFC", "Orban gov"))

p <- ggplot(fin_K_long, aes(x = year, y = contrib, colour = component, linetype = component)) +
  geom_line(linewidth = 1) +
  geom_point(size = 1.5) +
  geom_hline(yintercept = 0, linetype = "dashed", colour = "grey50") +
  geom_vline(data = events, aes(xintercept = year), linetype = "dotted", colour = "grey50", linewidth = 0.5) +
  geom_text(data = events, aes(x = year, y = Inf, label = event), vjust = -0.5, size = 2.5, colour = "grey40", inherit.aes = FALSE) +
  scale_y_continuous(expand = expansion(mult = c(0.05, 0.12))) +
  coord_cartesian(clip = "off") +
  labs(
    title = "Finance Sector (K): 3-Factor LP Growth Decomposition (1996–2011)",
    subtitle = "Pre-2008: imputed LAB_QI | alpha = 1/3",
    x = "Year", y = "Contribution (pp)",
    colour = "Component", linetype = "Component"
  ) +
  theme_minimal() +
  theme(legend.position = "bottom")

ggsave("/Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/output/figures/finance_sector_K_3f_decomposition.png", p, width = 8, height = 6, dpi = 150)
cat("Saved /Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/output/figures/finance_sector_K_3f_decomposition.png\n")