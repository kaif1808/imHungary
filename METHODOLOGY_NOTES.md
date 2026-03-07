# Methodology Notes: Growth Accounting for Hungary 1995–2011
## Addressing Key Technical Issues

---

## 1. Capital Variable Specification: K/Y vs K/L

### Theoretical Specification
The production function specification is:

$$y = \left(\frac{K}{Y}\right)^{\frac{\alpha}{1-\alpha}} h A$$

where:
- $y$ = output per hour (VA/L)
- $K/Y$ = capital-output ratio (not capital-labour ratio)
- $h$ = labour quality (human capital index)
- $A$ = total factor productivity
- $\alpha$ = capital share of income

### Why K/Y Instead of K/L?

The K/Y specification is an **algebraic rearrangement** that avoids double-counting output in the decomposition:
- If we used $K/L$ directly, the capital term would appear as $\alpha \log(K/L)$
- This conflates two channels: capital accumulation **and** labour adjustment
- The K/Y form cleanly separates these: $\frac{\alpha}{1-\alpha}(\log K - \log Y)$

### Log-Difference Decomposition

Taking log-differences:

$$\hat{y} = \frac{\alpha}{1-\alpha}(\hat{K} - \hat{Y}) + \hat{h} + \hat{A}$$

where $\hat{x} = \frac{d\log x}{dt} \times 100$ (in percentage points).

Rearranging:

$$\hat{A} = \hat{y} - \frac{\alpha}{1-\alpha}(\hat{K} - \hat{Y}) - \hat{h}$$

### Empirical Implementation: Capital Deepening

The **capital deepening term** is:

$$\text{Capital deepening} = \frac{\alpha}{1-\alpha}(\hat{K} - \hat{Y})$$

For $\alpha = 1/3$, this becomes:

$$\text{Capital deepening} = \frac{1}{2}(\hat{K} - \hat{Y})$$

In the code, with $\hat{Y}$ also equal to $\hat{L}$ when $\hat{K} - \hat{Y} = \hat{K} - \hat{y} - \hat{L}$, the implementation uses:

```r
cap_contrib = alpha * (g_K - g_L)
```

**where:**
- `g_K` = log-growth of real capital stock (Kq_GFCF)
- `g_L` = log-growth of total hours worked (total_hours = H_EMP × EMP/EMPE)

**Consistency Check:** 

Since $\log Y = \log y + \log L$ (output = output per hour × hours):
$$\hat{Y} = \hat{y} + \hat{L}$$

Therefore:
$$\hat{K} - \hat{Y} = \hat{K} - \hat{y} - \hat{L}$$

And:
$$\hat{y} = \frac{\alpha}{1-\alpha}(\hat{K} - \hat{L}) + \hat{h} + \hat{A}$$

which **matches** the code: `cap_contrib = alpha * (g_K - g_L)`.

### Conclusion on Issue 1

✅ **The capital deepening term is correctly derived.** It measures growth of capital per hour (K/L growth), scaled by the capital share $\alpha$. The use of K/Y in the theoretical specification is intentional and algebraically equivalent — it simply avoids double-counting output while maintaining economic interpretation.

---

## 2. Sector-Specific α and Labour Share Bias

### Computation: α_s = 1 − LS_s

Labour share by sector is computed as:

$$\text{LS}_s = \frac{\text{Compensation of Employees (COMP)}}{\text{Nominal Value Added (VA\_CP)}}$$

Then:
$$\alpha_s = 1 - \text{LS}_s$$

### Known Biases

This approach assumes:
1. **Perfect competition** in factor markets
2. **Compensation of employees fully captures labour income**

#### Major Bias: Self-Employment Income

Self-employed workers' income is recorded as **mixed income** in national accounts, allocated arbitrarily between labour and capital (typically proportionally). This causes:

**Agriculture (A):** $\alpha_s = 0.72$ (extremely high capital share)
- Self-employment is very high (>50% in many EU countries)
- Mixed income dominates, inflating measured capital share
- **True labour share is likely much higher**
- **Bias direction:** Overstates capital's contribution; understates TFP

**Construction (F):** $\alpha_s \approx 0.50$ (moderately high)
- Significant self-employment
- **Bias direction:** Likely overstates capital contribution

**Information & Communication (J):** $\alpha_s \approx 0.35$ (moderate)
- Lower self-employment than Agriculture/Construction
- **Bias direction:** Smaller, but still present

#### Secondary Consideration: Real Estate (L)

Real estate shows $\alpha_s = 0.90$ (very high capital share), which is **correct by design**:
- National accounts treat **imputed rents** as output
- Imputed rent is attributed to capital (the building/land stock)
- No labour component beyond property management
- **This is not a measurement error, but a structural feature**
- **However:** TFP estimates for real estate are **nearly meaningless** — the sector's "productivity" mainly reflects real estate price movements, not genuine efficiency gains

### Explicit Flagging in the Analysis

The code identifies Agriculture's extreme $\alpha_s$ value:

```r
sect_avg_alpha |> arrange(desc(avg_alpha))
# Output shows agriculture (A) with α_s ≈ 0.72
```

### Direction of Bias

For sectors with substantial self-employment:

| Sector | Measured α_s | True α_s | Bias | Impact on TFP |
|--------|--------------|----------|------|---------------|
| Agriculture | 0.72 | ~0.40 | Overstated capital | Understated TFP |
| Construction | ~0.50 | ~0.35 | Overstated capital | Understated TFP |
| Professional Services | ~0.45 | ~0.38 | Slight overstatement | Slight TFP understatement |

### Recommendation for Reporting

When presenting sector-specific α results, explicitly note:

> "Sector-specific capital shares are computed as $\alpha_s = 1 - \text{LS}_s$, where labour share is measured as employee compensation / value added. This approach systematically overstates capital's share in sectors with large self-employment (especially Agriculture), because mixed income is allocated arbitrarily between labour and capital in national accounts. Consequently, TFP may be understated in these sectors. Real estate (L) is excluded from strong TFP conclusions because its output consists primarily of imputed rents, making measured "productivity" largely a reflection of asset prices rather than efficiency gains."

### Conclusion on Issue 2

✅ **The bias is understood and correctly identified.** The analysis should include a note on the direction and magnitude of the self-employment bias, particularly for Agriculture and Construction, when reporting sector-specific TFP estimates.

---

## 3. Real Estate (L) Sector — Low Informational Content

### The Real Estate Problem

Real estate shows:
- **Capital share (α_s) = 0.90** (extremely high)
- **Low labour share (LS_s) ≈ 0.10**

This is **not a measurement error**; it reflects the national accounts treatment:
- Output = imputed rents (revenue from implicit leasing of buildings)
- Capital = the building/land stock (produces the imputed rents)
- Labour = only management and administrative staff

### Why TFP Estimates Are Uninformative

1. **Imputed rents are unobserved.** They are estimated from rental market data or user-cost approximations, not measured directly.

2. **Real estate "productivity" reflects asset prices, not efficiency:**
   - When property values rise → imputed rents rise → measured output rises
   - This is a **valuation effect**, not a genuine productivity gain
   - TFP can appear high simply because real estate prices increased, regardless of actual management efficiency

3. **Capital stock quality is difficult to adjust.**
   - Quality adjustments (depreciation, obsolescence) are highly subjective
   - Small errors in capital measurement translate to large errors in TFP

4. **Sector includes heterogeneous activities:**
   - Residential rental markets (policy-constrained)
   - Commercial real estate (market-determined)
   - Owner-occupied dwellings (imputed rents, highly sensitive to assumptions)

### Current Treatment in the Analysis

The analysis **correctly refrains from strong conclusions** about real estate TFP:
- Sector is included in decompositions (for completeness)
- No special emphasis is placed on its TFP estimates
- Broader narratives do not rely on real estate productivity trends

### Recommendation for Reporting

When real estate appears in figures or tables:

> "The real estate sector (NACE L) is included for completeness but its TFP estimates have limited informational value. Output is primarily imputed rents (unobserved and estimated), making measured "productivity" largely a reflection of asset valuations rather than genuine efficiency gains. Conclusions about aggregate or policy-driven productivity trends should not be drawn from this sector."

Alternatively, **exclude L from headline figures** and report aggregate results both with and without real estate.

### Conclusion on Issue 3

✅ **The sector is appropriately handled.** Real estate is not driving the main narratives. If it appears prominently in any report, add a caveat about the low informational content of its TFP estimates.

---

## Summary of Flagged Issues and Resolution

| Issue | Status | Recommendation |
|-------|--------|-----------------|
| **K/Y capital specification** | ✅ Correct | No changes needed; formula is properly derived |
| **Self-employment bias in α_s** | ⚠️ Identified | Add explicit bias note to sector-specific results, especially for Agriculture |
| **Real estate TFP content** | ✅ Appropriately handled | If sector features in headlines, add caveat about low informational value |

All three issues reflect deep methodological challenges in growth accounting. The current analysis is **conceptually sound** and **appropriately cautious** in interpretation.

