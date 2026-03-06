# Macroeconomics I: Lecture 3

Instructor: Alessandro Ferrari
Date: January 2026
Institution: UPF, CREI, BSE & CEPR

## Growth Accounting

99% of modern macroeconomics is "done" using theory and data

Models may be useful for:

- Getting intuitions/insights
- Measuring stuff

Growth accounting uses the structure of standard growth models to measure the sources of growth.

## Growth Accounting

Quantify the role of each production factor in the growth experience of a given country or region.

Take:

$$Y_{t}=F(K_{t},B_{t}L_{t})$$

where $Y_{t}$, $K_{t}$, and $L_{t}$ are output, capital, and labor per capita.

Given a growth rate of output per worker, how much is due to the increase in capital, labor, and productivity?

Rewrite the production function as

$$Y_{t}=A_{t}F(K_{t},L_{t})$$

where $A_{t}$ is the total factor productivity (TFP).

## Growth Accounting

Take logs and time derivatives:

$$\frac{\dot{Y}}{Y}=\frac{\dot{A}}{A}+\left(\frac{F_{K}K}{F}\right)\frac{\dot{K}}{K}+\left(\frac{F_{L}L}{F}\right)\frac{\dot{L}}{L} \Rightarrow \gamma_{Y}=\gamma_{A}+\alpha_{t}\gamma_{K}+(1-\alpha_{t})\gamma_{L}$$

where $\alpha_{t}$ is the capital share.

Everything in this equation is observable, except for $\gamma_{A}$.

But we can compute it as a residual (indeed, it is the Solow residual):

$$\gamma_{A}=\gamma_{Y}-\alpha_{t}\gamma_{K}-(1-\alpha_{t})\gamma_{L}$$

## Growth Accounting

What goes into $\gamma_{A}$? Everything except for measured capital and labor.

- Technology
- Misallocation (market efficiency, government regulation, cronyism, etc.)
- Mismeasurement of capital and labor

## Growth Accounting

Initial accounting exercises gave a very high share of growth to TFP, in the order of 70%.

This was the measure of our ignorance.

Recent measurements reduce the importance of TFP to $1/3 - 1/2$.

Problem: poor measurement of the quality of inputs.

Labor quality has increased.

- The labor force's education level has been increasing.
- A way to account for this is to weigh every person's hours by the relative wage of her education category.

Capital quality has increased even more.

- Relative price of capital equipment has declined in the last decades.
- A computer today is much faster than 30 years ago.

Need to measure capital in efficiency units, not in dollars.

## Growth Accounting

The stock of capital is not easy to measure.

One approach is to build it with the perpetual-inventory method. It basically requires applying the law of motion:

$$K_{t+1}=(1-\delta)K_{t}+I_{t}$$

We have good measures of $I_{t}$ in the national accounts. $\delta$ is easy to estimate. Then, we just need an initial estimate of $K_{0}$. This is the most complicated part. However, if we have a series for $I_{t}$ long enough, the effects of $K_{0}$ vanish.

## Growth Accounting

"Recent" measurements reduce the importance of TFP.

Still, it accounts for more than $1/3$ and in some countries by $1/2$ of output growth.

| Country | $\gamma_Y$ | $\alpha\frac{\gamma_{K}}{\gamma_{Y}}$ | $(1-\alpha) \frac{\gamma_{L}}{\gamma_{Y}}$ | $\frac{\gamma_A}{\gamma_Y}$ |
|---------|------------|--------------------------------------|------------------------------------------|---------------------------|
| **1947-1973** |||||
| US | 4.02% | 42.7% | 23.7% | 33.6% |
| UK | 3.73% | 47.2% | 0.9% | 51.9% |
| Fr | 5.42% | 41.5% | 3.9% | 54.5% |
| Ger | 6.61% | 40.6% | 2.8% | 56.6% |
| **1960-1990** |||||
| US | 3.10% | 45.2% | 41.5% | 13.2% |
| UK | 2.49% | 52.3% | -4.2% | 51.9% |
| Fr | 3.50% | 58.1% | 0.5% | 41.4% |
| Ger | 3.20% | 58.7% | -8.1% | 49.4% |

## Growth Accounting

This is useful, but it does not imply any causality.

Remember that the Solow and Ramsey models state that in the BGP all growth in capital per capita is also due to technology.

Alternative but similar framework:

$$Y_{t}=K_{t}^{\alpha}(B_{t}L_{t})^{1-\alpha} \Rightarrow \frac{Y_{t}}{N_{t}}=B_{t}\frac{L_{t}}{N_{t}}\left(\frac{K_{t}}{Y_{t}}\right)^{\frac{\alpha}{1-\alpha}}$$

Hence, the growth of output per capita $Y_{t}/N_{t}$ is decomposed in:

- growth of Solow residual
- growth of labor units per capita
- capital deepening: the increase in the capital-to-income ratio

## Growth Accounting

**Results:**

| Period | $Y/N$ | $B$ | $L/N$ | $K/Y$ |
|--------|-------|-----|-------|-------|
| 1948-2013 | 2.5 | 2.0 | 0.3 | 0.1 |
| 1948-1973 | 3.3 | 3.2 | 0.3 | -0.2 |
| 1973-1995 | 1.6 | 0.8 | 0.4 | 0.4 |
| 1995-2007 | 2.8 | 2.2 | 0.3 | 0.2 |
| 2007-2013 | 1.7 | 1.1 | 0.5 | 0.1 |

*US data. Source: Jones (2015)*

- Capital deepening of little importance: US close to BGP.
- Large importance of Solow residual.
- We observe a productivity slowdown in the 70's and 80's, also from 2007 on...

## Growth Accounting

What we have used so far is the so-called primal approach to growth accounting.

The alternative dual approach starts from the accounting equation (absent profits):

$$Y_{t}=w_{t}L_{t}+r_{t}K_{t}$$

Taking log derivatives wrt time:

$$\dot{Y}/Y=\alpha_{K}(\dot{R}/R+\dot{K}/K)+\alpha_{L}(\dot{w}/w+\dot{L}/L)$$

Which implies that we can rewrite TFP growth as:

$$\gamma_{A}=\alpha_{K}\dot{R}/R+\alpha_{L}\dot{w}/w$$

## Growth Accounting

This approach relies on national accounting identities without assumptions on social marginal products.

Should in principle coincide with the primal approach, but in practice, they are often not (Hsieh, 2002).

| Country | Primal | Dual |
|---------|--------|------|
| Hong Kong ('66-'91) | 2.3% | 2.7% |
| Singapore ('72-'90) | -0.7% | 2.2% |
| South Korea ('66-'90) | 1.7% | 1.5% |
| Taiwan ('66-'90) | 2.1% | 3.7% |

## A few observations

Consider the basic growth accounting equation:

$$\frac{\partial \log Y}{\partial t}=\frac{\partial \log F(x)}{\partial t}=\sum_{x}\frac{\partial \log F}{\partial \log x}\frac{\partial \log x}{\partial t}$$

We argued before that we can use measured income shares for the production function elasticity. Why can we do that?

Consider an optimizing firm:

$$\max_{x}\pi(x)=pF(x)-\sum_{x}w_{x}x$$

## A few observations

The profit maximization problem has FOCs of the type:

$$F_{x}p=w_{x}$$

which we can rewrite as:

$$\frac{F_{x}x}{Y}=\frac{w_{x}x}{pY}$$

The LHS is the elasticity we would like to measure, the RHS is the factor share.

What if the firm has market power?

## A few observations - Problem 1

The profit maximization is:

$$\max_{x}\pi(x)=p(x)F(x)-\sum_{x}w_{x}x$$

which implies:

$$p^{\prime}F_{x}F+pF_{x}=w_{x}$$

Which we can manipulate to:

$$\frac{\epsilon_{D}-1}{\epsilon_{D}}\frac{F_{x}x}{Y}=\frac{w_{x}x}{pY}$$

With $\epsilon_{D}$ being the elasticity of demand.

## A few observations - Problem 1

So we cannot simply take the measured factor share.

Note, however, that, by definition:

$$\mu=\frac{\epsilon_{D}}{\epsilon_{D}-1}$$

and under CRS of the production function:

$$C(Y)=\frac{pY}{\mu}$$

Hence we can recover:

$$\frac{F_{x}x}{Y}=\frac{w_{x}x}{C}$$

So the elasticity is the cost share whenever firms have profits.

## A few observations - Problem 2

Note another complication: suppose that some costs are not variable:

$$\max_{x}\pi(x)=pF(x)-\sum_{x}w_{x}x-w_{x}\Gamma$$

Suppose that $\Gamma$ is paid by hiring units of input $x$ at the price $w_{x}$.

The optimization problem from before still holds, and we obtain:

$$\frac{F_{x}x}{Y}=\frac{w_{x}x}{pY}$$

But the RHS is not the $x$ factor share, since that is given by:

$$\frac{w_{x}(x+\Gamma)}{pY}$$

## A few observations - Problem 2

Problems 1 and 2 have a similar root cause.

Going from factor share to elasticities requires that firms:

- equate REVENUE marginal products to input prices (true under perfect competition on both output AND factor markets)
- variable costs are the only costs, so when the firms make a margin calculation, we can immediately go to the full factor share

Fixing these requires strict assumptions on firm behaviour.

## A few observations - Problem 3

Note yet another thing: so far, we have been jumping seamlessly from firm-level to aggregates. This is not assumption-free.

Underlying is an assumption on "no externalities".

Namely that firms private marginal returns are equal to the social marginal returns.

Suppose there is a positive externality, then firms equate MC to private MP, but in the aggregates, Social MP is higher.

## A few observations

More problems in economies with:

- taxes
- multiple sector/inputs
- quality upgrading
- endogenous technological progress

Nonetheless, we persevere (for good reasons).

Can a country grow without improving its productivity?

[Chart: Growth Accounting for Spain (1995-2007) - showing Output growing, with Capital and Labor growing significantly faster than TFP, which slightly declines over the period]

## Development Accounting

Similar exercise, but comparing a cross-section of countries at a given point in time:

$$\log Y_{i}=\log A_{i}+\alpha \log K_{i}+(1-\alpha)\log L_{i}$$

Caselli (2005) claims that TFP differences account for more than $1/2$ of variation in income per capita between countries.

| sample | obs | $y_{90}/y_{10}$ | the xx |
|--------|-----|------------------|--------|
| Whole sample | 105 | 24.8 | 61.5% |
| OECD | 24 | 1.7 | 39.4% |
| Non OECD | 81 | 14.7 | 64.4% |

Improving capital quality measures and allowing for non Cobb-Douglas production function are important to reduce these numbers.

Where are the productivity differences coming from?

## Hall and Jones (1999, QJE)

income/worker in the USA = $35 \times$ income/worker in Niger

Hall and Jones carry out one of the "first" development accounting exercises.

Goal: understanding what part of these differences is due to:

- Efficiency in the use of factors
- Amount of factors

Conceptually:

$$\text{Income} = F(\text{Factors, Efficiency})$$

## Development accounting

Let's assume that the production function for a country $i$ is given by:

$$Y_{i}=K_{i}^{\alpha}(A_{i}H_{i})^{1-\alpha}$$

- $K_{i}$: stock of physical capital
- $H_{i}$: human capital adjusted labor factor
- $A_{i}$: labor productivity

$$H_{i}=e^{\phi(E_{i})}L_{i}$$

$E_{i}$: years of schooling

## Development accounting

We want to write the production function in terms of output per worker $y\equiv\frac{Y}{L}$.

Rewriting the production function:

$$y_{i}=\left(\frac{K_{i}}{Y_{i}}\right)^{\alpha/(1-\alpha)}h_{i}A_{i}$$

$h_{i}\equiv\frac{H_i}{L_i}$

$\frac{K_{i}}{Y_{i}}$ : capital-output ratio

This expression allows us to decompose differences in output per worker into:

- capital-output ratio
- human capital
- productivity

## Development accounting

The Penn World Tables (PWT) is one of the intensively used datasets in growth accounting (especially during the 90s and early 2000s).

Other datasets used nowadays: World development indicators, EU-KLEMS.

Hall and Jones (1999) use Penn World Tables (PWT) 5.6.

They just released version 10.01.

HJ use data on output (GDP), labor, educational attainment, and investment for the year 1988.

## Developing accounting

Remember that we want a data counterpart for:

$$h_{i}=e^{\phi(E)}$$

Barro and Lee provide relatively high-quality data for many countries-years.

HJ use the 1985 version.

These data tell us, among other things, the average number of years of schooling in a given country.

## Development accounting

To construct $\phi(E)$ we use Barro and Lee data + information on the returns of education. Using schooling $s$.

Then, for the returns, we use:

- for the first 4 years: 13.4%
- for the years 4-8: 10.1%
- for the year 9 onwards: 6.8%

Specifically:

- If $s\le4$: $\phi(s)=0.134\times s$
- If $4<s\le8$: $\phi(s)=0.134\times 4+0.101\times(s-4)$
- If $8<s$: $\phi(s)=0.134\times 4+0.101\times 4+0.068\times(s-8)$

## Development accounting

Remember that we want a measure for $\frac{K_{i}}{Y_{i}}$.

$Y_{i}$ is simply GDP - good data.

However, there is usually no data for $K_{i}$.

We have to construct series of $K_{i}$ using the "perpetual inventory method":

$$K_{t}=I_{t}+(1-\delta)K_{t-1}$$

$I_{t}$ is investment, which can be easily measured in the data.

We fix $\delta$ as the depreciation rate $(=0.06)$.

$$K_{0}=\frac{I_{0}}{g+\delta}$$

## Development accounting

We measure $A_{i}$ as a residual. Very common procedure in the misallocation literature...

Once we have data for the rest of the variables, we compute for each country:

$$A_{i}=\frac{y_{i}}{\left(\frac{K_{i}}{Y_{i}}\right)^{\alpha/(1-\alpha)}h_{i}}$$

We impute to $A_{i}$ everything that our model cannot explain.

Caselli (2005): "...the measure of our ignorance".

We use $\alpha=1/3$ because that's approx. the capital share (with all the caveats from before).

## Productivity and Output per Worker

(Figure I from Hall and Jones 1999)

[Chart: Scatter plot showing Harrod-Neutral Productivity (Y-axis) vs Output per Worker (X-axis, log scale). Shows a strong positive correlation ($R^2 = 0.79$, Coeff = 0.600)]

## Development accounting

TABLE I: PRODUCTIVITY CALCULATIONS: RATIOS TO U.S. VALUES

| Country | $Y/L$ | $(K/Y)^{\alpha/(1-\alpha)}$ | $H/L$ | $A$ |
|---------|-------|------------------------------|-------|-----|
| United States | 1.000 | 1.000 | 1.000 | 1.000 |
| Canada | 0.941 | 1.002 | 0.908 | 1.034 |
| Italy | 0.834 | 1.063 | 0.650 | 1.207 |
| West Germany | 0.818 | 1.118 | 0.802 | 0.912 |
| France | 0.818 | 1.091 | 0.666 | 1.126 |
| United Kingdom | 0.727 | 0.891 | 0.808 | 1.011 |
| Hong Kong | 0.608 | 0.741 | 0.735 | 1.115 |
| Singapore | 0.606 | 1.031 | 0.545 | 1.078 |
| Japan | 0.587 | 1.119 | 0.797 | 0.658 |
| Mexico | 0.433 | 0.868 | 0.538 | 0.926 |
| Argentina | 0.418 | 0.953 | 0.676 | 0.648 |
| U.S.S.R. | 0.417 | 1.231 | 0.724 | 0.468 |
| India | 0.086 | 0.709 | 0.454 | 0.267 |
| China | 0.060 | 0.891 | 0.632 | 0.106 |
| Kenya | 0.056 | 0.747 | 0.457 | 0.165 |
| Zaire | 0.033 | 0.499 | 0.408 | 0.160 |
| Average, 127 countries: | 0.296 | 0.853 | 0.565 | 0.516 |
| Standard deviation: | 0.268 | 0.234 | 0.168 | 0.325 |
| Correlation with $Y/L$ (logs): | 1.000 | 0.624 | 0.798 | 0.889 |
| Correlation with A (logs): | 0.889 | 0.248 | 0.522 | 1.000 |

## Development accounting

Most of the income differences come from differences in $A_{i}$.

$$y_{\text{China}}=0.06\times y_{\text{USA}}$$

If China had $A_{\text{USA}}$:

$$y_{\text{China}}=0.50\times y_{\text{USA}}$$

$$y_{\text{top } 5}=31.7\times y_{\text{bottom } 5}$$

Decomposing this difference...

$$y_{\text{top } 5}=\frac{1.8}{(K/Y)^{\alpha/(1-\alpha)}}\times\frac{2.2}{h}\times\frac{8.3}{A}\times y_{\text{bottom } 5}$$

## An additional exercise: What is behind $A_{i}$?

Can we relate $A_{i}$ with any observable?

Hypothesis: Better "social infrastructure" (institutions) $\Rightarrow A_{i}\uparrow \Rightarrow y_{i}\uparrow$

Formally:

$$\log y_{i}=\gamma+\beta S_{i}+\epsilon_{i}$$

If $S$ were exogenous, we could run an OLS to estimate the effect of $S$ on $y_{i}$.

Problem: reverse causality.

$$S_{i}=\mu+\sigma \log y_{i}+X_{i}\theta+\eta_{i}$$

Higher income allows countries to improve institutions.

## An additional exercise: What is behind $A_{i}$?

Solution by HJ: Instrumental variables.

We need to find variables that:

- influence the quality of countries' institutions
- do not affect current levels of $y_{i}$ through other channels

Hall and Jones (1999) propose:

- Distance from the equator
- Percentage of the local population that speaks Western languages
- Predicted trade share (Frankel, Romer (1996))

"...Finally, we also use as an instrument the variable constructed by Frankel and Romer (1996): the (log) of predicted share of an economy, based on a gravity model of international trade that only uses a country's population and geographical features."

## An additional exercise: What is behind $A_{i}$?

How do we measure $S$ in the data?

HJ use "Government antidiversion policies (GADP)" index.

It measures the role of governments in protecting:

- Law and order
- Quality of bureaucracy
- Laws against corruption
- Laws against expropriation risk
- Contract enforcement

## Social Infrastructure and Output per Worker

(Figure II from Hall and Jones 1999)

[Chart: Scatter plot mapping Observed Index of Social Infrastructure (X-axis) against Y/L (Y-axis, log scale). Shows a clear positive trend where better social infrastructure correlates with higher output per worker]

## An additional exercise: What is behind $A_{i}$?

TABLE II: BASIC RESULTS FOR OUTPUT PER WORKER

$$\log Y/L=\alpha+\beta\tilde{S}+\tilde{\epsilon}$$

| Specification | Social infrastructure | OverID test p-value test result | Coeff test p-value test result | $\hat{\sigma}_{\tilde{\epsilon}}$ |
|--------------|----------------------|--------------------------------|-------------------------------|-----------------------------------|
| 1. Main specification | 5.1432 (.508) | .256 Accept | .812 Accept | .840 |
| 2. Instruments: Distance, Frankel-Romer | 4.998 (.567) | .208 Accept | .155 Accept | .821 |
| 3. No imputed data (79 countries) | 5.323 (.607) | .243 Accept | .905 Accept | .889 |
| 4. OLS | 3.289 (.212) | - | .002 Reject | .700 |

## An additional exercise: What is behind $A_{i}$?

TABLE IV: RESULTS FOR $\log K/Y$, $\log H/L$, and $\log A$

$$\text{Component} =\alpha+\beta\tilde{S}+\tilde{\epsilon}$$

| Dependent variable | $\frac{\alpha}{1-\alpha}\log K/Y$ | $\log H/L$ | $\log A$ |
|-------------------|-----------------------------------|------------|----------|
| Social infrastructure | 1.052 (.164) | 1.343 (.171) | 2.746 (.336) |
| OverID test (p) | .784 | .034 | .151 |
| Test result | Accept | Reject | Accept |
| $\hat{\sigma}_{\tilde{\epsilon}}$ | .310 | .243 | .596 |
| $\hat{\sigma}_{Depvar}$ | .320 | .290 | .727 |

## Developing accounting

- Huge income differences across countries.
- Most of these differences are accounted for by differences in TFP.
- What is the source of these differences in TFP?
- Have we diminished "the measure of our ignorance" in recent years?

## Summary

Growth/Development Accounting is a useful tool.

**IMPORTANT:** but it is not a way to investigate the causes of growth and development.

It is, as the name says, accounting.

To see this, recall our earlier result under Cobb-Douglas and labor-augmenting technological progress at rate $x$:

$$\Delta \log Y=\alpha\Delta \log K+(1-\alpha)x$$

## Summary

By growth accounting, you would conclude that the TFP growth is $\hat{\gamma}_{A}=(1-\alpha)x$.

You would also attribute $\alpha$ of the observed growth to capital-deepening.

This would be an incorrect causal statement since without $x$ no growth would occur $\Rightarrow$ need to correct for the indirect growth contribution of $x$ through endogenous factor accumulation of $K$.

In economies with human capital accumulation, we would need to correct for that too.

## What is A?

(Section Transition)

## More on A

We have so far established that, based on the development accounting exercises, a very significant portion of income per capita differences is given by differences in measured TFP.

This is a black box where we put all that we cannot properly measure.

A prominent recent literature has focused on the role of misallocation as a drag in countries' development.

For us, misallocation ends up in lower $A$.

## Misallocation

To understand the concept of misallocation, we need to first understand when it matters.

First, by allocation, we mean how we split and use finite resources.

Misallocation is generally understood to be an inefficient allocation of these resources.

Efficiency is an elusive concept, as it requires us to make assumptions about how agents turn input into output, output into utility, and how we aggregate different agents' utilities into a social welfare that we can maximize.

## Misallocation

For simplicity, let's assume away the latter issue by saying that there is a single household composed of very many individuals (atomistic).

We focus on the allocation of resources across production units (firms/plants).

When does this matter?

Suppose you have a continuum of identical firms, does the allocation of resources matter?

## Misallocation

Suppose firms have the same productivity and a production function like:

$$Y_{i}=K_{i}^{\alpha}L_{i}^{1-\alpha}$$

Suppose further that firms are competitive, make perfectly substitutable goods, and maximize their profits:

$$\pi_{i}=PY_{i}-rK_{i}-wL_{i}$$

From the usual FOC we get:

$$\frac{\alpha}{1-\alpha}\frac{w}{r}=\frac{K_{i}^{*}}{L_{i}^{*}}, \quad \forall i$$

note that the LHS is the same for all firms, so the RHS is identical.

## Misallocation

This tells us that all firms will optimally have the same amount of capital per worker, but should different firms have different amounts of capital and workers?

And, more importantly, does it matter?

Call $K^{*}/L^{*}\equiv k$ and check the aggregate production of the economy.

Since goods are perfect substitutes, total output is just the sum of individual firms' output:

$$Y=\int_{i}Y_{i}$$

## Misallocation

From the production function:

$$Y=\int_{i}K_{i}^{\alpha}L_{i}^{1-\alpha}=\int_{i}k^{\alpha}L_{i}$$

Recalling that the total amount of labor in the economy is $L$ and capital is $K$, we have that:

$$Y=k^{\alpha}\int_{i}L_{i}=k^{\alpha}L$$

Noting that I can rewrite the capital market clearing as:

$$K=\int_{i}K_{i}=\int_{i}kL_{i}$$

## Misallocation

We obtain:

$$Y=K^{\alpha}L^{1-\alpha}$$

Bottom line: if firms

- are competitive
- operate the same production function with CRS
- in the same factor markets

The allocation of resources across firms is irrelevant.

## Misallocation

The assumptions we made are all important:

- if firms are not competitive (and their market power is heterogeneous), their MRPs are going to be different and, therefore, their optimal scale.
- if firms do not operate a CRS production function, then reallocating a unit of $k$ from $i$ to $j$ changes aggregate output.
- if they operate in different production markets their $r$'s and $w$'s are different and so are their $K^{*}/L^{*}$.

## Misallocation

We can study this problem with a bit more structure by making stronger assumptions about the economy.

In doing so we follow a seminal paper by Hsieh and Klenow (2009).

Key goal: use a model to quantify cross-country differences in misallocation and answer questions like:

What would India's GDP per capita be if it had the degree of misallocation of the US?

This is equivalent to asking:

How much of the difference between US and India is driven by misallocation?

## Hsieh and Klenow (2009)

The way we go about this is first:

1. Describe the economy
2. Solve for the undistorted allocation
3. Solve the distorted allocation
4. Look at the implied measured $A$

## Hsieh and Klenow (2009)

Households have CES preferences over imperfectly substitutable varieties:

$$C=\left(\int_{i}{c_{i}}^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}, \quad \sigma>1$$

They maximize utility (consumption) subject to a budget constraint:

$$\int_{i}p_{i}C_{i}\le I$$

Define the ideal price index $P$ (cost of unit of $C$ when the household optimizes) such that:

$$PC=\int_{i}c_{i}p_{i}$$

## CES Observations

$\sigma$ governs the elasticity of substitution.

- $\sigma>1$: substitutes
- $\sigma\in(0,1)$: complements

and nests other well-known aggregators:

- $\sigma\rightarrow\infty$: perfect substitutes
- $\sigma\rightarrow0$: perfect complements
- $\sigma\rightarrow1$: Cobb-Douglas

## CES Observations

The aggregator has love-for-variety: consumers are happier to split the same consumption on more varieties.

Suppose that there is a measure $N$ of varieties ($f_{i}=N$).

Suppose the household splits consumption equally across varieties ($c_{i}=c/N, \forall i$).

Then:

$$C=\left(\int_{i}(c/N)^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}} = c/N\left(\int_{i} 1\right)^{\frac{\sigma}{\sigma-1}} = c/NN^{\frac{\sigma}{\sigma-1}}=cN^{\frac{1}{\sigma}}$$

which is increasing in $N$.

## Hsieh and Klenow (2009)

The household optimization problem implies a demand schedule:

$$c_{i}=p_{i}^{-\sigma}P^{\sigma}C$$

where $P$ is:

$$P=\left(\int_{i}p_{i}^{1-\sigma}\right)^{\frac{1}{1-\sigma}}$$

This gives us a demand schedule for each variety $i$.

## Hsieh and Klenow (2009)

Firms operate a CRS Cobb-Douglas production function with heterogeneous productivities $A_{i}$:

$$y_{i}=A_{i}K_{i}^{\alpha}L_{i}^{1-\alpha}$$

They maximize profits:

$$\pi_{i}=p_{i}(y_{i})y_{i}-wL_{i}-rK_{i}$$

They compete under monopolistic competition:

- firms are monopolists of their own variety (account for how quantity choice affects the willingness to pay)
- too small to affect aggregate quantities and prices (take $w$, $r$, $P$, $Y$ as given)

## Hsieh and Klenow (2009)

By the properties of CRS production functions, we know that the marginal cost is going to be constant.

We also know how to compute the optimal input mix by minimizing expenditures.

We can focus on the quantity choice and rewrite the firm problem as:

$$\max_{p_{i}}\pi_{i}=p_{i}y_{i}(p_{i})-\frac{c}{A_{i}}y_{i}(p_{i})$$

where $c$ is the marginal cost (at the optimal input mix) for firms with productivity $A=1$.

## Hsieh and Klenow (2009)

Like earlier in the notes, we know that the firm will optimally choose:

$$p_{i}=\frac{\epsilon_{D}}{\epsilon_{D}-1}\frac{c}{A_{i}}$$

But thanks to our CES assumption, $\epsilon_{D}=\sigma$, which implies:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{c}{A_{i}}$$

We still need to determine $c$, which we can do from the cost minimization of the firm.

## Hsieh and Klenow (2009)

Consider the firm, minimizing the total cost bill subject to the production plan:

$$\min_{L_{i},K_{i}}wL_{i}+rK_{i}+\lambda[Y-A_{i}K_{i}^{\alpha}L_{i}^{1-\alpha}]$$

The FOCs are:

$$wL_{i}=\lambda(1-\alpha)y_{i}$$

$$rK_{i}=\lambda\alpha y_{i}$$

Substituting back into the PF, we obtain:

$$L_{i}=\frac{y_{i}}{A_{i}}\left(\frac{1-\alpha}{\alpha}\right)^{\alpha}\left(\frac{r}{w}\right)^{\alpha}$$

$$K_{i}=\frac{y_{i}}{A_{i}}\left(\frac{\alpha}{1-\alpha}\right)^{1-\alpha}\left(\frac{w}{r}\right)^{1-\alpha}$$

## Hsieh and Klenow (2009)

Plugging the optimal quantities into the cost function:

$$C(y_{i})=r\frac{y_{i}}{A_{i}}\left(\frac{\alpha}{1-\alpha}\right)^{1-\alpha}\left(\frac{w}{r}\right)^{1-\alpha}+w\frac{y_{i}}{A_{i}}\left(\frac{1-\alpha}{\alpha}\right)^{\alpha}\left(\frac{r}{w}\right)^{\alpha}$$

Simplifying we obtain:

$$C(y_{i})=\frac{y_{i}}{A_{i}}\left(\frac{r}{\alpha}\right)^{\alpha}\left(\frac{w}{1-\alpha}\right)^{1-\alpha}$$

Which implies that for a firm with $A_{i}=1$ the marginal cost is:

$$c=\left(\frac{r}{\alpha}\right)^{\alpha}\left(\frac{w}{1-\alpha}\right)^{1-\alpha}$$

## Hsieh and Klenow (2009)

From the pricing equation:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{1}{A_{i}}\left(\frac{r}{\alpha}\right)^{\alpha}\left(\frac{w}{1-\alpha}\right)^{1-\alpha}$$

Again, note that the only source of price differences across firms is given by the different productivities $A_{i}$.

Using the optimal pricing rule in the demand function, we can find how much each firm produces:

$$y_{i}=\left(\frac{\sigma}{\sigma-1}c\right)^{-\sigma}A_{i}^{\sigma}P^{\sigma}C$$

Where, again, the only source of size difference between firms is given by different $A$'s, mediated by the elasticity of substitution $\sigma$.

## Hsieh and Klenow (2009)

In particular, note that:

$$y_{i}\propto A_{i}^{\sigma}$$

Another important observation is that, from the profit maximization problem:

$$\max_{L_{i},K_{i}}\pi_{i}=p(y_{i})y_{i}(L_{i},K_{i})-wL_{i}-rK_{i}$$

We have that firms optimally choose to produce to the point where:

$$MRPK_{i}=(p^{\prime}y_{i}+p_{i})MPK_{i}=r$$

$$MRPL_{i}=(p^{\prime}y_{i}+p_{i})MPL_{i}=w$$

Note that the RHS is the same for all $i$.

## Hsieh and Klenow (2009)

As a consequence, firms differ in size based on productivity differences, but their MRPs are all equalized.

The MPs are NOT equalized in general when firms have market power!

## Are resources misallocated?

A social planner would want to allocate resources such that the MPs are the same across firms. Otherwise, we could take one unit of input from a low MP firm and give it to a high MP firm to obtain higher total output.

Does a planner want to reallocate in this economy?

Equivalently, are some firms too small relative to others?

## Hsieh and Klenow (2009)

We can check this by looking at the allocation that a planner would mandate.

Maximizing output in this economy implies setting:

$$\min_{\{c_{i}\}_{i}}\int_{i}\gamma_{i}c_{i}+\lambda\left[C-\left(\int_{i}{C_{i}}^{\frac{\sigma-1}{\sigma}}\right)^{\frac{\sigma}{\sigma-1}}\right]$$

where $\gamma_{i}$ is the optimal marginal cost of good $i$.

The FOC implies:

$$\gamma_{i}=\lambda c_{i}^{-\frac{1}{\sigma}}C^{\frac{1}{\sigma}}$$

## Hsieh and Klenow (2009)

The implication of this FOC is that the socially optimal share of good $i$ out of total consumption:

$$c_{i}\propto\gamma_{i}^{-\sigma}$$

The planner operates the same technology as firms, which implies that the social marginal cost must have a common component and a firm-specific component that depends negatively on $A_{i}$:

$$\gamma_{i}=\gamma/A_{i}$$

Like in the market equilibrium:

$$c_{i}\propto A_{i}^{\sigma}$$

## Hsieh and Klenow (2009)

We conclude that the market and the planner allocate the same shares across firms.

Does this mean that there is no misallocation?

Depends on the definition.

There is no cross-sectional misallocation: the relative size of firms in the equilibrium is socially optimal.

BUT the size of firms is not socially optimal as the planner would not let firms charge a markup: all firms are too small but by the same amount (because the markup is the same thanks to CES).

## Hsieh and Klenow (2009)

Firms size is given by:

$$y_{i}=p_{i}^{-\sigma}P^{\sigma}Y=\left(\frac{\sigma}{\sigma-1}c_{i}\right)^{-\sigma}P^{\sigma}Y$$

The efficient allocation would have firm price at marginal cost.

Which implies:

$$y_{i}^{*}=c_{i}^{-\sigma}P^{\sigma}Y$$

$$\frac{y_{i}}{y_{i}^{*}}=\left(\frac{\sigma-1}{\sigma}\right)^{\sigma}<1$$

In this CES economy, the distortion is not firm-specific, which means that the whole economy is too small, but resources are correctly allocated across firms.

## Hsieh and Klenow (2009)

Side note: the inefficiency in this economy is given by the presence of pure rents: there is no technology constraint that would warrant the existence of profits.

For example, if the firms had decreasing returns to scale, some profits would be present even in the efficient allocation: $p^{*}=c<C/Y$.

You can show that if we include entry costs to set up a firm and a Free Entry condition, the economy is efficient (Dixit Stiglitz, 1977).

The profits associated with the markups are not pure rents anymore, they are quasi rents which allow firms to cover the entry costs.

## Hsieh and Klenow (2009)

How do you fix the level inefficiency?

Suppose the government introduces a tax/subsidy $\tau$ to production costs such that profits are given by:

$$\pi(y_{i})=p_{i}(y_{i})y_{i}-\frac{\tau c}{A_{i}}y_{i}$$

The optimal price of the firm is then:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{\tau c}{A_{i}}$$

If the planner sets $\tau=\frac{\sigma-1}{\sigma}$, the firm prices at marginal cost and restores the efficient levels of production.

## Hsieh and Klenow (2009)

So far:

- Barring a level inefficiency, there is no cross-sectional misallocation.
- We can compute the Solow Residual of this economy.

Start from the aggregate production function:

$$Y=AK^{\alpha}L^{1-\alpha}$$

with:

$$K=\int_{i}K_{i}$$

$$L=\int_{i}L_{i}$$

## Hsieh and Klenow (2009)

From the FOCs of the firm, we know that:

$$K_{i}=\frac{\alpha c}{rA_{i}}y_{i}$$

$$L_{i}=\frac{(1-\alpha)c}{wA_{i}}y_{i}$$

Plugging into the market-clearing conditions:

$$K=\int_{i}\frac{\alpha c}{rA_{i}}y_{i}$$

$$L=\int_{i}\frac{(1-\alpha)c}{wA_{i}}y_{i}$$

And into the aggregate PF:

$$Y=A\left(\int_{i}\frac{\alpha c}{rA_{i}}y_{i}\right)^{\alpha}\left(\int_{i}\frac{(1-\alpha)c}{wA_{i}}y_{i}\right)^{1-\alpha}$$

## Hsieh and Klenow (2009)

Solving further:

$$Y=A\int_{i}\frac{y_{i}}{A_{i}}c\left(\frac{\alpha}{r}\right)^{\alpha}\left(\frac{1-\alpha}{w}\right)^{1-\alpha}$$

Given our previous result on $c$ we get:

$$Y=A\int_{i}\frac{y_{i}}{A_{i}}$$

Reshuffling:

$$A^{-1}=\int_{i}A_{i}^{-1}\frac{y_{i}}{Y}$$

The inverse Solow residual is an output-weighted aggregate of inverse individual productivities.

## Hsieh and Klenow (2009)

We can go a step further by looking at what the output weights are.

Recall the demand function:

$$y_{i}=p_{i}^{-\sigma}P^{\sigma}Y$$

So:

$$y_{i}/Y=(p_{i}/P)^{-\sigma}$$

Given our result on $P$:

$$\frac{p_{i}}{P}=\frac{\frac{\sigma}{\sigma-1}cA_{i}^{-1}}{\left(\int_{j}\left(\frac{\sigma}{\sigma-1}cA_{j}^{-1}\right)^{1-\sigma}\right)^{\frac{1}{1-\sigma}}}$$

## Hsieh and Klenow (2009)

Simplifying, we obtain:

$$\frac{p_{i}}{P}=\frac{A_{i}^{-1}}{\left(\int_{j}A_{j}^{\sigma-1}\right)^{\frac{1}{1-\sigma}}}$$

Plugging this into the Solow Residual:

$$A^{-1}=\int_{i}A_{i}^{-1}\left(\frac{A_{i}^{-1}}{\left(\int_{j}A_{j}^{\sigma-1}\right)^{\frac{1}{1-\sigma}}}\right)^{-\sigma}$$

## Hsieh and Klenow (2009)

Simplifying:

$$A^{-1}=\int_{i}A_{i}^{-1}A_{i}^{\sigma}\left(\int_{j}A_{j}^{\sigma-1}\right)^{-\frac{\sigma}{\sigma-1}}$$

Which finally implies:

$$A=\left(\int_{i}A_{i}^{\sigma-1}\right)^{\frac{1}{\sigma-1}}$$

The Solow Residual is a geometric average of individual productivities.

Non-linear because more productive firms sell more $\Rightarrow$ higher weight.

## Hsieh and Klenow (2009)

Does our accounting framework work in this economy?

Compute the factor shares from the capital and labour expenditures.

Define the capital share as:

$$\Theta_{K}=\frac{rK}{PY}=\frac{r}{PY}\int_{i}K_{i}$$

Plugging in $K_{i}=\frac{\alpha c}{rA_{i}}y_{i}$:

$$\Theta_{K}=\frac{r}{PY}\int_{i}\frac{\alpha c}{rA_{i}}y_{i}$$

## Hsieh and Klenow (2009)

Simplifying:

$$\Theta_{K}=\frac{\alpha}{PY}\int_{i}\frac{c}{A_{i}}y_{i}$$

Recall that:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{c}{A_{i}}$$

Which implies:

$$\Theta_{K}=\frac{\alpha}{PY}\int_{i}p_{i}\frac{\sigma-1}{\sigma}y_{i}$$

and

$$\Theta_{K}=\alpha\frac{\sigma-1}{\sigma}\int_{i}\frac{p_{i}y_{i}}{PY}$$

## Hsieh and Klenow (2009)

But $p_{i}y_{i}$ is the value of sales of firm $i$, while $PY$ is the value of sales of all firms, so it has to be that:

$$\int_{i}p_{i}y_{i}=PY$$

Which implies that:

$$\Theta_{K}=\alpha\frac{\sigma-1}{\sigma}<\alpha$$

Same steps for labour give us:

$$\Theta_{L}=(1-\alpha)\frac{\sigma-1}{\sigma}<1-\alpha$$

This is an economy with profits, so the factor shares do NOT coincide with the output elasticities!

## Hsieh and Klenow (2009)

We have an economy with no cross-sectional misallocation, where the Solow Residual depends on appropriately allocating resources across firms.

We know that this matters because of the output weights in $A$.

We have also proved that those output weights are efficient since the planner and the market have the same relative firm size distribution.

We now do it all again, but with cross-sectional misallocation.

## Hsieh and Klenow (2009)

Consider a distorted problem with wedges $\tau_{i}^{K}$ and $\tau_{i}^{Y}$ such that firm $i$ maximizes:

$$\max_{y_{i},K_{i},L_{i}}(1-\tau_{i}^{Y})p_{i}(y_{i})y_{i}-wL_{i}-(1+\tau_{i}^{K})rK_{i}$$

s.t.

$$y_{i}=A_{i}K_{i}^{\alpha}L_{i}^{1-\alpha}$$

Denote $\tilde{r}_{i}=r(1+\tau_{i}^{K})$ and $\tilde{p}_{i}=p(1-\tau_{i}^{Y})$, so that we can solve basically the original problem:

$$\pi_{i}=\tilde{p}_{i}(y_{i})y_{i}-wL_{i}-\tilde{r}_{i}K_{i}$$

## Hsieh and Klenow (2009)

The FOCs are:

$$\tilde{r}_{i}=\lambda_{i}\alpha A_{i}K_{i}^{\alpha-1}L_{i}^{1-\alpha}$$

$$w=\lambda_{i}(1-\alpha)A_{i}K_{i}^{\alpha}L_{i}^{-\alpha}$$

Note immediately that the optimal capital-labour-ratio is:

$$\frac{K_{i}}{L_{i}}=\frac{\alpha}{1-\alpha}\frac{w}{r}\frac{1}{1+\tau_{i}^{K}}$$

The presence of $\tau_{i}^{K}$ distorts the incentives to hire capital relative to labour.

## Hsieh and Klenow (2009)

Firms in this economy set their MRPs as:

$$MRPL_{i}=w\frac{1}{1-\tau_{i}^{Y}}$$

$$MRPK_{i}=r\frac{1+\tau_{i}^{K}}{1-\tau_{i}^{Y}}$$

The presence of output wedges makes MRPs deviate from their marginal costs.

If the output wedges are positive, they reduce the real MRPs relative to marginal costs.

As a consequence, firms are optimally operating at a smaller scale, given their technologies and input prices.

## Hsieh and Klenow (2009)

With the same steps as before, we can find the optimal price:

$$\tilde{p}_{i}=\frac{\sigma}{\sigma-1}\frac{\tilde{c}_{i}}{A_{i}}$$

Which implies:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{\tilde{c}_{i}}{A_{i}}\frac{1}{1-\tau_{i}^{Y}}$$

To obtain the distorted marginal cost, solve the cost minimization:

$$\min_{K_{i},L_{i}}wL_{i}+\tilde{r}_{i}K_{i}+\lambda_{i}[y_{i}-A_{i}K_{i}^{\alpha}L_{i}^{1-\alpha}]$$

## Hsieh and Klenow (2009)

The FOCs say:

$$\tilde{r}_{i}=\lambda_{i}\alpha A_{i}K_{i}^{\alpha-1}L_{i}^{1-\alpha}$$

$$w=\lambda_{i}(1-\alpha)A_{i}K_{i}^{\alpha}L_{i}^{-\alpha}$$

Solving for the optimal input quantities:

$$K_{i}=\frac{\lambda_{i}\alpha y_{i}}{\tilde{r}_{i}}=\frac{\lambda_{i}\alpha y_{i}}{r(1+\tau_{i}^{K})}$$

$$L_{i}=\frac{(1-\alpha)\lambda_{i}y_{i}}{w}$$

Plugging into the PF:

$$y_{i}=A_{i}\left(\frac{\lambda_{i}\alpha y_{i}}{r(1+\tau_{i}^{K})}\right)^{\alpha}\left(\frac{(1-\alpha)\lambda_{i}y_{i}}{w}\right)^{1-\alpha}$$

## Hsieh and Klenow (2009)

Which simplifies to:

$$\lambda_{i}=A_{i}^{-1}\left(\frac{r}{\alpha}\right)^{\alpha}\left(\frac{w}{1-\alpha}\right)^{1-\alpha}(1+\tau_{i}^{K})^{\alpha}$$

But recall that $\lambda_{i}$ is the marginal cost for firm $i$, and that we defined $c$ as $\left(\frac{r}{\alpha}\right)^{\alpha}\left(\frac{w}{1-\alpha}\right)^{1-\alpha}$. Hence:

$$\lambda_{i}=A_{i}^{-1}c(1+\tau_{i}^{K})^{\alpha}$$

Which implies that the price is:

$$p_{i}=\frac{\sigma}{\sigma-1}\frac{c}{A_{i}}\frac{(1+\tau_{i}^{K})^{\alpha}}{1-\tau_{i}^{Y}}$$

## Hsieh and Klenow (2009)

We can use this in the demand function to obtain:

$$y_{i}=\left(\frac{\sigma}{\sigma-1}\frac{c}{A_{i}}\frac{(1+\tau_{i}^{K})^{\alpha}}{1-\tau_{i}^{Y}}\right)^{-\sigma}P^{\sigma}Y$$

Which implies:

$$y_{i}\propto A_{i}^{\sigma}\left(\frac{1-\tau_{i}^{Y}}{1+\tau_{i}^{K}}\right)^{\sigma}$$

The firm-level wedges distort relative output.

Since $\tau$'s are firms-specific, we have cross-sectional misallocation.

## Hsieh and Klenow (2009)

Bad news for our growth/development accounting.

From the FOCs of the minimization:

$$(1+\tau_{i}^{K})rK_{i}=\alpha\frac{c}{A_{i}}(1+\tau_{i}^{K})^{\alpha}y_{i}$$

$$wL_{i}=(1-\alpha)\frac{c}{A_{i}}(1+\tau_{i}^{K})^{\alpha}y_{i}$$

Call the labour and capital shares $\Theta_{L}$ and $\Theta_{K}$:

$$\Theta_{K}=\frac{rK}{PY}=\frac{\alpha}{\frac{\sigma}{\sigma-1}}\int_{i}\frac{1-\tau_{i}^{Y}}{1+\tau_{i}^{K}}\frac{p_{i}y_{i}}{PY}\ne\alpha$$

$$\Theta_{L}=\frac{wL}{PY}=\frac{1-\alpha}{\frac{\sigma}{\sigma-1}}\int_{i}(1-\tau_{i}^{Y})\frac{p_{i}y_{i}}{PY}\ne1-\alpha$$

## Hsieh and Klenow (2009)

These are distorted by market power by a factor $(\sigma-1)/\sigma$. This is because $\Theta_{L}+\Theta_{K}<PY$ since there are positive profits and (you can show) the profit share is $1/\sigma$.

but they are also distorted by individual wedges.

even if we had the same $\tau^{K}$ for all firms the relative labour to capital share would be distorted.

the fact that they are firm-specific distorts them in a much harder way to undo.

## Hsieh and Klenow (2009)

Towards our stated goal of understanding how misallocation impacts measured $A$, we return to inverting the aggregate production function:

$$A=YK^{-\alpha}L^{\alpha-1}$$

To simplify the next calculations, denote TFPR of firm $i$:

$$TFPR_{i}\equiv p_{i}A_{i}=\frac{\sigma}{\sigma-1}c\frac{(1+\tau_{i}^{K})^{\alpha}}{1-\tau_{i}^{Y}}$$

And the aggregate version of the same object:

$$TFPR=PA$$

## Hsieh and Klenow (2009)

Start from the production function for the value of output:

$$PY=PAK^{\alpha}L^{1-\alpha}$$

Inverting the labour and capital shares:

$$K=\frac{\Theta_{K}PY}{r}$$

$$L=\frac{\Theta_{L}PY}{w}$$

Plugging in, we obtain:

$$PY=PA\left(\frac{\Theta_{K}PY}{r}\right)^{\alpha}\left(\frac{\Theta_{L}PY}{w}\right)^{1-\alpha}$$

Which implies:

$$PA=\left(\frac{r}{\Theta_{K}}\right)^{\alpha}\left(\frac{w}{\Theta_{L}}\right)^{1-\alpha}$$

## Hsieh and Klenow (2009)

We can work out TFPQ $A$ as $A=TFPR/P$

From the Price index:

$$P=\left(\int_{i}p_{i}^{1-\sigma}\right)^{\frac{1}{1-\sigma}}=\left(\int_{i}\left(\frac{TFPR_{i}}{A_{i}}\right)^{1-\sigma}\right)^{\frac{1}{1-\sigma}}$$

Which implies:

$$A=\left(\int_{j}\left(A_{j}\frac{TFPR}{TFPR_{j}}\right)^{\sigma-1}\right)^{\frac{1}{\sigma-1}}$$

## Hsieh and Klenow (2009)

$$A=\left(\int_{j}\left(A_{j}\frac{TFPR}{TFPR_{j}}\right)^{\sigma-1}\right)^{\frac{1}{\sigma-1}}$$

Note that TFPQ is a weighted geometric average of individual productivities.

If the undistorted marginal revenue products were equalized across firms, we would get back the undistorted economy result for aggregate TFPQ.

Since the aggregator is concave, higher dispersion in TFPR reduces aggregate productivity.

The cost of misallocation comes from the dispersion in TFPR induced by firm-specific distortions.

## Hsieh and Klenow (2009)

Through the lens of this model, we can ask counterfactual questions:

- What if India, China, and the US had the efficient firm size distribution?
- What if India and China had the dispersion in TFPR of the US?

## Hsieh and Klenow (2009)

[Chart: Density of REVENUE TFP (TFPR) showing overlapping distributions for U.S., China, and India. The U.S. distribution is tighter (less dispersion), while China and India have thicker tails and more dispersion.]

## Hsieh and Klenow (2009)

[Chart: Density of QUANTITY TFP (TFPQ) showing overlapping distributions for U.S., China, and India. The U.S. distribution is shifted further to the right, reflecting higher overall TFPQ.]

## Hsieh and Klenow (2009)

TABLE IV: TFP GAINS FROM EQUALIZING TFPR WITHIN INDUSTRIES

*Notes. Entries are $100(Y_{\text{efficient}}/Y-1)$ where:*

$$Y/Y_{\text{efficient}}=\prod_{s=1}^{S}\left[\sum_{i=1}^{M_{s}}\left(\frac{A_{si}}{A_{s}}\frac{\overline{TFPR}_{si}}{TFPR_{si}}\right)^{\sigma-1}\right]^{\theta_{s}/(\sigma-1)}$$

$$TFPR_{si}\equiv\frac{P_{si}Y_{si}}{K_{si}^{\alpha_{s}}(w_{si}L_{si})^{1-\alpha_{s}}}$$

| Country | Year 1 | % | Year 2 | % | Year 3 | % |
|---------|--------|---|--------|---|--------|---|
| China | 1998 | 115.1 | 2001 | 95.8 | 2005 | 86.6 |
| India | 1987 | 100.4 | 1991 | 102.1 | 1994 | 127.5 |
| United States | 1977 | 36.1 | 1987 | 30.7 | 1997 | 42.9 |

## Hsieh and Klenow (2009)

[Chart: Density plot for China showing the Actual vs. Efficient distributions of TFPR. The "Efficient" distribution is much tighter and centered, whereas "Actual" shows significant left and right tails, indicating misallocation.]

## Hsieh and Klenow (2009)

[Chart: Density plot for India showing the Actual vs. Efficient distributions of TFPR. Similar to China, the "Actual" distribution is flatter and wider than the desired "Efficient" tight peak.]

## Hsieh and Klenow (2009)

[Chart: Density plot for the United States showing the Actual vs. Efficient distributions of TFPR. The U.S. "Actual" distribution tracks the "Efficient" distribution much closer than China or India, though some misallocation is still visible.]

## Hsieh and Klenow (2009)

TABLE VI: TFP GAINS FROM EQUALIZING TFPR RELATIVE TO 1997 U.S. GAINS

| Country | Year 1 | % | Year 2 | % | Year 3 | % |
|---------|--------|---|--------|---|--------|---|
| China | 1998 | 50.5 | 2001 | 37.0 | 2005 | 30.5 |
| India | 1987 | 40.2 | 1991 | 41.4 | 1994 | 59.2 |

## Summary

**Unpacking A further.**

But still lots in it that should:

- Measurement error
- Adjustment costs that are not in the model
- Deviations from various assumptions (e.g., CES, CD, CRS, etc.)

These missing elements can overturn the conclusion from HK that dispersion in marginal products is necessarily bad.

With all these caveats, it is still a significant step forward in understanding what we measure as $A$!
