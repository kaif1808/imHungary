#!/usr/bin/env Rscript
# Regenerate growth_accounting_3f_and_2f_line and lp_decomposition_aggregate_3f_and_2f figures
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
    tfp_contrib = g_y - cap_contrib - hc_contrib,
    cap_contrib_2f = cap_contrib,
    tfp_2f = g_y - cap_contrib
  ) |>
  ungroup()

# --- Growth accounting line plot ---
decomp_agg <- decomp_df |>
  filter(!is.na(tfp_contrib)) |>
  group_by(year) |>
  summarise(
    cap = mean(cap_contrib, na.rm = TRUE),
    hc = mean(hc_contrib, na.rm = TRUE),
    tfp = mean(tfp_contrib, na.rm = TRUE),
    total = mean(g_y, na.rm = TRUE),
    cap_2f = mean(cap_contrib_2f, na.rm = TRUE),
    tfp_2f = mean(tfp_2f, na.rm = TRUE),
    .groups = "drop"
  )

agg_3f <- decomp_agg |>
  select(year, cap, hc, tfp, total) |>
  pivot_longer(-year, names_to = "component", values_to = "contrib") |>
  mutate(component = recode(component, cap = "Capital", hc = "Human capital", tfp = "TFP", total = "Total"), method = "3-factor")
agg_2f <- decomp_agg |>
  select(year, cap_2f, tfp_2f, total) |>
  rename(cap = cap_2f, tfp = tfp_2f) |>
  pivot_longer(-year, names_to = "component", values_to = "contrib") |>
  mutate(component = recode(component, cap = "Capital", tfp = "Residual (HC+TFP)", total = "Total"), method = "2-factor")
agg_plot <- bind_rows(agg_3f, agg_2f)

events <- data.frame(year = c(2004, 2008, 2010), event = c("EU Accession", "GFC", "Orban gov"))
events_lab <- events |> tidyr::crossing(method = unique(agg_plot$method))

p1 <- ggplot(agg_plot, aes(x = year, y = contrib, colour = component, linetype = component)) +
  geom_line(linewidth = 1) +
  geom_point(size = 1.5) +
  geom_hline(yintercept = 0, linetype = "dashed", colour = "grey50") +
  geom_vline(data = events, aes(xintercept = year), linetype = "dotted", colour = "grey50", linewidth = 0.5) +
  geom_text(data = events_lab, aes(x = year, y = Inf, label = event), vjust = -0.5, size = 2.5, colour = "grey40", inherit.aes = FALSE) +
  facet_wrap(~ method, ncol = 1) +
  scale_y_continuous(expand = expansion(mult = c(0.05, 0.12))) +
  coord_cartesian(clip = "off") +
  labs(title = "Growth Accounting: 3-Factor vs 2-Factor (Broad Sectors)",
       subtitle = "1995–2011 | Pre-2008: imputed LAB_QI | alpha = 1/3",
       x = "Year", y = "Contribution (pp)", colour = "Component", linetype = "Component") +
  theme_minimal() +
  theme(legend.position = "bottom", plot.margin = margin(t = 20, r = 5, b = 5, l = 5))

ggsave("output/figures/growth_accounting_3f_and_2f_line.png", p1, width = 8, height = 6, dpi = 150)
cat("Saved output/figures/growth_accounting_3f_and_2f_line.png\n")

# --- LP decomposition stacked bar ---
decomp_agg_plot <- decomp_df |>
  filter(!is.na(tfp_contrib)) |>
  group_by(year) |>
  summarise(
    cap = mean(cap_contrib, na.rm = TRUE),
    hc = mean(hc_contrib, na.rm = TRUE),
    tfp = mean(tfp_contrib, na.rm = TRUE),
    total = mean(g_y, na.rm = TRUE),
    cap_2f = mean(cap_contrib_2f, na.rm = TRUE),
    tfp_2f = mean(tfp_2f, na.rm = TRUE),
    .groups = "drop"
  )

stack_3f <- decomp_agg_plot |>
  select(year, cap, hc, tfp, total) |>
  pivot_longer(cols = c(cap, hc, tfp), names_to = "component", values_to = "contribution") |>
  mutate(component = recode(component, cap = "Capital deepening", hc = "Human capital", tfp = "TFP"), method = "3-factor")
stack_2f <- decomp_agg_plot |>
  select(year, cap_2f, tfp_2f, total) |>
  pivot_longer(cols = c(cap_2f, tfp_2f), names_to = "component", values_to = "contribution") |>
  mutate(component = recode(component, cap_2f = "Capital deepening", tfp_2f = "Residual (HC+TFP)"), method = "2-factor")
stack_agg <- bind_rows(stack_3f, stack_2f)

p2 <- ggplot(stack_agg, aes(x = year, y = contribution, fill = component)) +
  geom_rect(data = data.frame(method = "3-factor", xmin = 1994.5, xmax = 2008, ymin = -Inf, ymax = Inf),
            aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
            fill = "red", alpha = 0.15, inherit.aes = FALSE) +
  geom_vline(data = data.frame(method = "3-factor", xintercept = 2008),
             aes(xintercept = xintercept), linetype = "solid", colour = "darkred", linewidth = 0.8) +
  geom_col(position = "stack") +
  geom_line(data = decomp_agg_plot |> select(year, total) |> tidyr::crossing(method = c("3-factor", "2-factor")), aes(x = year, y = total), inherit.aes = FALSE,
            colour = "black", linewidth = 0.8, linetype = "dashed") +
  geom_hline(yintercept = 0, colour = "grey50", linewidth = 0.3) +
  facet_wrap(~ method, ncol = 1) +
  scale_fill_brewer(palette = "Set2") +
  labs(title = "Hungary — LP Growth Decomposition: 3-Factor vs 2-Factor (1995–2011)",
       x = "Year", y = "Contribution (pp)", fill = "Component") +
  theme_minimal() +
  theme(legend.position = "bottom")

ggsave("/Users/kai/Documents/BSE/14E022_Macroeconomics_I/imHungary/output/figures/lp_decomposition_aggregate_3f_and_2f.png", p2, width = 8, height = 6, dpi = 150)
cat("Saved output/figures/lp_decomposition_aggregate_3f_and_2f.png\n")
