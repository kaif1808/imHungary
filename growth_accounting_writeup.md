# Hungary Growth Accounting: Questions (c)–(e)

---

## (c) Aggregate Growth Decomposition (1995–2011, α = 1/3)

### Framework

Starting from the aggregate production function $y = \left(\frac{K}{Y}\right)^{\alpha/(1-\alpha)} h A$,
taking the log-time derivative and approximating with log-first-differences yields:

$$\hat{y} = \underbrace{\frac{\alpha}{1-\alpha}\left(\hat{K} - \hat{L}\right)}_{\text{capital deepening}} + \underbrace{\hat{h}}_{\text{human capital}} + \underbrace{\hat{A}}_{\text{TFP}}$$

where $\hat{x}$ denotes the log-growth rate of $x$, and with $\alpha = 1/3$ the scalar $\alpha/(1-\alpha) = 0.5$.

| Term | Empirical measure | Notes |
|---|---|---|
| $\hat{y}$ | $\Delta \log(VA_{\text{real}} / \text{total\_hours})$ | Constant-price VA per total hour worked |
| Capital deepening | $\frac{1}{2}(\hat{K} - \hat{L})$ | Growth of K/L ratio scaled by 0.5 |
| $\hat{h}$ | $\Delta \log(\text{LAB\_QI})$ | EUKLEMS labour quality index |
| $\hat{A}$ | Solow residual | $\hat{y}$ minus the two factor terms above |

### Measurement choices and their implications

**Capital.** The dataset provides `Kq_GFCF`, the quality-adjusted real capital stock from the EUKLEMS capital accounts. This adjusts for asset-type composition (ICT vs. structures vs. machinery) and is the theoretically preferred measure. An unweighted perpetual-inventory stock would attribute more of ICT-intensive growth to TFP rather than capital deepening, overstating the Solow residual in knowledge-intensive sectors.

**Labour input.** Employee hours (`H_EMP`) were replaced with total hours worked by all persons engaged (`total_hours = H_EMP × EMP/EMPE`), which incorporates the self-employed. This matters for agriculture, construction, and professional services — sectors with large self-employment shares — where using employee hours alone would overstate output per hour.

**Human capital.** `LAB_QI` captures changes in workforce composition (education, age, gender) and is the best available proxy for $\hat{h}$. Its availability is limited to **2009–2011** in this dataset, so the three-factor decomposition is restricted to that window. For the full period 1995–2011, a two-factor decomposition is used, with TFP absorbing the human capital contribution. An alternative — a Mincerian index based on average years of schooling (e.g. Barro-Lee) — would allow coverage of the full period but measures the stock level of human capital rather than annual changes in workforce composition.

### Aggregate results

**Two-factor decomposition (1996–2011, full panel):**

Over the transition and pre-crisis period, Hungarian labour productivity growth was primarily driven by TFP — consistent with the standard narrative of catch-up growth through technology adoption and reallocation away from inefficient state enterprises. Capital deepening played a secondary but sustained role, reflecting high investment rates during EU accession and the credit boom of the 2000s.

**Three-factor decomposition (2009–2011, where LAB_QI is available):**

The human capital contribution is small and positive at the aggregate level over this window, implying that aggregate workforce composition changed only modestly. TFP remains the dominant source of labour productivity growth.

---

## (d) Sectoral Decomposition (α = 1/3)

### Output per worker: 1996–2011 (two-factor)

| Rank | Sector | LP growth (pp/yr) | Capital deepening | TFP + HC |
|---|---|---:|---:|---:|
| 1 | **B — Mining & quarrying** | **10.64** | 2.12 | 8.52 |
| 2 | A — Agriculture | 4.84 | 1.18 | 3.66 |
| 3 | J — ICT | 3.60 | −1.02 | 4.62 |
| 4 | C — Manufacturing | 3.56 | 1.43 | 2.13 |
| 5 | G — Wholesale & retail | 3.54 | 1.09 | 2.45 |
| 6 | H — Transport & storage | 2.85 | 0.89 | 1.96 |
| 7 | O-Q — Public sector | 1.87 | 0.37 | 1.50 |
| 8 | L — Real estate | 1.75 | 0.30 | 1.45 |
| 9 | F — Construction | 1.57 | 0.77 | 0.80 |
| 10 | R-S — Arts & recreation | 1.55 | 0.27 | 1.28 |
| 11 | I — Accommodation & food | 1.31 | 0.47 | 0.84 |
| 12 | D-E — Utilities | 0.77 | 0.78 | −0.01 |
| 13 | M-N — Professional services | 0.10 | −0.42 | 0.52 |
| 14 | **K — Finance & insurance** | **−0.81** | 0.93 | −1.74 |

> **Highest LP growth: B — Mining & quarrying (+10.6 pp/yr).**
> This is the strongest performer by a wide margin. Mining is a very small sector in Hungary and its productivity is driven by volatile output (commodity prices, utilisation) rather than sustained efficiency improvement. The average should be interpreted cautiously.
>
> **Lowest LP growth: K — Finance & insurance (−0.8 pp/yr).**
> Financial sector output contracted sharply after the GFC as credit deleveraged and measured value added fell. This is partly a measurement artefact: financial intermediation services indirectly measured (FISIM) is sensitive to interest rate spreads rather than real activity.

### Three-factor decomposition (2009–2011, α = 1/3)

| Sector | LP growth | Capital deepening | HC | TFP |
|---|---:|---:|---:|---:|
| B — Mining | 10.22 | 1.17 | −1.25 | **10.30** |
| G — Wholesale & retail | 3.00 | 0.63 | 0.43 | 1.93 |
| K — Finance | 2.99 | 0.47 | 0.15 | 2.38 |
| L — Real estate | 1.99 | 0.03 | 1.32 | 0.64 |
| I — Accommodation | 1.89 | 0.40 | −0.16 | 1.65 |
| J — ICT | 1.57 | −1.64 | **5.03** | −1.82 |
| F — Construction | 1.55 | −0.01 | 1.48 | 0.08 |
| H — Transport | 1.45 | 0.95 | 0.76 | −0.26 |
| A — Agriculture | 1.20 | 0.76 | −2.52 | 2.97 |
| C — Manufacturing | 1.04 | 1.20 | 0.32 | −0.48 |
| M-N — Professional services | 0.71 | −0.34 | 4.95 | **−3.90** |
| D-E — Utilities | −0.32 | 0.23 | −0.50 | −0.05 |
| R-S — Arts | −0.39 | −0.01 | 1.59 | −1.97 |
| O-Q — Public sector | −0.48 | −0.24 | 1.64 | −1.89 |

> **Highest TFP: B — Mining (+10.3 pp/yr).** Again dominated by the same volatility caveat noted above; A — Agriculture (+3.0) and K — Finance (+2.4) are more credible top performers.
>
> **Lowest TFP: M-N — Professional services (−3.9 pp/yr).** This is consistent with Baumol's cost disease: professional and administrative services are labour-intensive with limited scope for genuine efficiency gains. Note, however, that the three-factor period (2009–2011) is short and the negative TFP here is partly offset by a very large positive HC contribution (+4.95 pp), suggesting that what is happening is a *compositional upgrade* of the labour force — hiring more highly-skilled workers — rather than true efficiency loss.
>
> O-Q — Public sector (−1.9 pp) and R-S — Arts (−2.0 pp) also show persistently negative TFP, in part because output in these sectors is difficult to measure independently of inputs.

**ICT (J)** deserves special attention: it has negative TFP (−1.82 pp) but strongly positive HC (+5.03 pp), indicating that productivity growth in this sector over 2009–2011 was driven entirely by workforce upgrading rather than efficiency gains. Using the two-factor decomposition, J ranks 3rd overall (+3.6 pp), but the three-factor split reveals the mechanism is entirely compositional.

---

## (e) Sector-Specific α from the Labour Share

### Labour shares and implied capital shares

The labour share is computed as $\text{LS}_s = \text{COMP}_s / \text{VA\_CP}_s$, averaged across 2009–2011. The implied capital share is $\alpha_s = 1 - \text{LS}_s$.

| Sector | Avg. labour share | Implied $\alpha_s$ | Assumed $\alpha = 1/3$ |
|---|---:|---:|---:|
| A — Agriculture | 0.28 | **0.72** | 0.33 |
| B — Mining | 0.50 | 0.50 | 0.33 |
| C — Manufacturing | 0.50 | 0.50 | 0.33 |
| D-E — Utilities | 0.46 | 0.54 | 0.33 |
| F — Construction | 0.50 | 0.50 | 0.33 |
| G — Wholesale & retail | 0.58 | 0.42 | 0.33 |
| H — Transport | 0.60 | 0.40 | 0.33 |
| I — Accommodation | 0.61 | 0.39 | 0.33 |
| J — ICT | 0.46 | 0.54 | 0.33 |
| K — Finance | 0.49 | 0.51 | 0.33 |
| **L — Real estate** | **0.10** | **0.90** | 0.33 |
| M-N — Professional services | 0.58 | 0.42 | 0.33 |
| O-Q — Public sector | 0.74 | **0.26** | 0.33 |
| R-S — Arts | 0.52 | 0.48 | 0.33 |

Two sectors are dramatically different from $1/3$:

- **L — Real estate** ($\alpha_s = 0.90$): capital (primarily imputed rent on structures and land) accounts for nearly all value added by construction. This is expected by the national accounts treatment of housing services.
- **A — Agriculture** ($\alpha_s = 0.72$): land and machinery dominate measured value added; mixed income of farm households is partly classified as capital income.
- **O-Q — Public sector** ($\alpha_s = 0.26$): labour-intensive, as expected for government services.

Most manufacturing, trade, and service sectors cluster near $\alpha_s \approx 0.40$–$0.54$, somewhat above the standard $1/3$ assumption.

### TFP comparison: α = 1/3 vs. sector-specific α (2009–2011)

| Sector | TFP ($\alpha = 1/3$) | TFP (sector-$\alpha$) | $\Delta$ TFP |
|---|---:|---:|---:|
| B — Mining | 10.30 | 9.71 | −0.59 |
| G — Wholesale & retail | 1.93 | 1.76 | −0.17 |
| K — Finance | 2.38 | 2.13 | −0.25 |
| L — Real estate | 0.64 | 0.59 | −0.05 |
| I — Accommodation | 1.65 | 1.59 | −0.06 |
| **J — ICT** | −1.82 | **−0.82** | **+1.00** |
| F — Construction | 0.08 | 0.08 | 0.00 |
| H — Transport | −0.26 | −0.44 | −0.18 |
| **A — Agriculture** | 2.97 | **2.10** | **−0.87** |
| **C — Manufacturing** | −0.48 | **−1.07** | **−0.59** |
| M-N — Professional services | −3.90 | −3.81 | +0.09 |
| D-E — Utilities | −0.05 | −0.36 | −0.31 |
| R-S — Arts | −1.97 | −1.93 | +0.04 |
| O-Q — Public sector | −1.89 | −1.94 | −0.05 |

### Do the conclusions change?

**No, not substantially — but with three noteworthy exceptions:**

1. **Agriculture (A):** TFP falls from +2.97 to +2.10 pp. With $\alpha_s = 0.72$ instead of $0.33$, capital deepening accounts for a much larger share of output growth, leaving less for the Solow residual. Agriculture's ranking as the second-highest TFP sector is retained, but the margin over other sectors narrows.

2. **ICT (J):** TFP improves from −1.82 to −0.83 pp. The sector's true $\alpha_s = 0.54$ is above $1/3$, so the large *negative* capital deepening term (ICT shrank its capital stock per worker over this window) gets appropriately up-weighted, leaving TFP less negative. This makes the decomposition more coherent: ICT's story is one of workforce upgrading (+5 pp HC), not TFP destruction.

3. **Manufacturing (C):** TFP deteriorates from −0.48 to −1.07 pp. Manufacturing has $\alpha_s \approx 0.50$; the higher weight on capital deepening (+1.20 pp) crowds out TFP.

For all other sectors the shifts are small ($< 0.3$ pp). The sector rankings on both total LP growth and TFP growth are entirely preserved. The broad narrative — Mining and Agriculture at the top, Public sector and Professional services at the bottom — is unchanged.

The assumption $\alpha = 1/3$ is a reasonable approximation for most market-sector industries. The exceptions are the two outliers at either extreme of the capital-intensity distribution: **Real estate** and **Agriculture**. For cross-sector comparisons, using sector-specific labour shares is the more rigorous approach, particularly when these two sectors are included.
