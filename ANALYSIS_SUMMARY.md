# Hungary Growth Accounting: Analysis Rewrite Summary

## Overview
The notebook has been substantially rewritten to provide a **comprehensive comparison of two-factor vs three-factor decomposition** across the full available time period.

---

## Key Changes

### 1. **Cell 27: Sectoral-Level Comparison**
**What's New:**
- **Two-Factor Decomposition (1995–2011)**: 
  - Available for all sectors across the full 17-year period
  - Decomposes LP growth into: **capital deepening** + **TFP+HC residual**
  - Visualization: side-by-side bar chart comparing both periods
  
- **Three-Factor Decomposition (2009–2011)**:
  - Only 2 years of LAB_QI data sufficient for meaningful HC estimates
  - Decomposes LP growth into: **capital deepening** + **labour composition (HC)** + **pure TFP**
  - Shows structural differences in growth drivers post-GFC

**Output:**
- Comparative bar chart with faceted panels (2F vs 3F)
- Summary tables for both decompositions
- Highlights sectoral differences in HC/TFP contributions

---

### 2. **Cell 35: Aggregate-Level Time Series**
**What's New:**
- **Stacked bar decomposition** showing year-by-year contributions (1995–2011)
- Two separate panels:
  - Left: 2-Factor model over full period
  - Right: 3-Factor model for 2009–2011 only
- Visualizes the **GFC shock** and recovery pattern in HC/TFP components

**Key Finding:** 
In 2009, HC contribution plummets (-2.46pp), reflecting labour market dislocation; gradually recovers by 2011 (+0.69pp)

---

### 3. **Cells 36–40: Time Series with Policy Context**
**Two Separate Visualizations:**

**Cell 36: 2-Factor LP Decomposition (1995–2011)**
- Line plot showing annual contributions to LP growth
- Overlays key events: EU accession (2004), GFC onset (2008), Orbán government (2010)
- Shows capital deepening (dashed) and TFP+HC residual (dashed) against total growth (solid)
- **Pattern:** Pre-2008 boom driven by TFP+HC (~4–5pp); crash to -3.77pp (TFP+HC) in 2009

**Cell 40: 3-Factor LP Decomposition (2009–2011)**
- Point-and-line plot for the three components + total
- Reveals composition of recovery: pure TFP vs HC gains
- Shows capital deepening plays minor role in post-crisis recovery (0.19–1.10pp)

---

## Data Availability Notes

| Component | Period | Status |
|-----------|--------|--------|
| Capital stock (Kq) | 1995–2011 | ✓ Full |
| Labour input (hours) | 1995–2011 | ✓ Full |
| Labour composition (LAB_QI) | 2008–2021 | ✗ 2008+ only |
| **2-Factor feasible** | 1995–2011 | ✓ Full 17 years |
| **3-Factor feasible** | 2009–2011 | ✗ 3 years only |

---

## Key Economic Insights

### Pre-Crisis (1995–2008)
- **Dominant driver:** TFP+HC residual (~4–5pp annually)
- **Capital deepening:** Modest contribution (~0.5–1.7pp)
- **EU accession (2004):** Structural break; sustained elevated growth through 2007

### GFC & Immediate Aftermath (2009)
- **LP collapse:** -1.62pp total
- **Capital deepening:** Paradoxically positive (+2.15pp) — labour shedding accelerates
- **TFP+HC:** Crashes to -3.77pp
- **Decomposition:** With 3-factor model: TFP (-1.31pp) + HC (-2.46pp)

### Recovery (2010–2011)
- **Gradual LP recovery:** 1.48–2.47pp
- **HC rebounds:** From -2.46pp to +0.69pp
- **Pure TFP:** Also recovers from -1.31pp to +1.54pp
- **Interpretation:** Post-crisis rehiring emphasizes higher-skill roles; productivity adaptation

---

## Files Modified
- `hungary_growth_accounting-2.ipynb`
  - Cell 27: Sectoral 2F vs 3F comparison
  - Cell 35: Aggregate stacked decomposition
  - Cells 36, 40: Time series analysis with events
  - Cell 41: New summary section

---

## Visualizations Generated
1. **Sectoral comparison** (2-Factor 1995–2011 vs 3-Factor 2009–2011)
2. **Aggregate stacked bars** (by period and year)
3. **2-Factor time series** with policy event markers
4. **3-Factor time series** (2009–2011 only)
5. Supporting tables and summary statistics
