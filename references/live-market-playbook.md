# Live Market Playbook

Use this reference when the user asks for current行情, entry zones, exit zones, stop levels, "buy now", or trade timing.

This workflow is for research and scenario planning. Do not present the result as personalized financial advice or a guaranteed buy/sell call.

## 1. Freshness Gate

Before giving a live setup, collect and show:

- ticker and exchange
- current price or last close
- timestamp and timezone
- daily range
- volume and relative volume if available
- latest earnings date or next scheduled earnings date
- latest material news, filing, guidance, or sector catalyst

Use available finance and web sources for current data. Prefer exchange data, company IR, filings, and reputable market/news sources. Cite sources when the final answer includes live claims.

If price/news data is stale, unavailable, or from an unclear timestamp, do not give current entry/exit levels. Give only a framework and say what data must be refreshed.

## 2. Autonomous Research Loop

When the user asks for autonomous or real-time research, run this loop before ranking stocks or crypto assets:

1. refresh the candidate universe from the chosen AI infrastructure or crypto lane
2. remove names with no clear role in the supply chain
3. refresh current price, volume, news, filings, earnings calendar, and peer/index context
4. grade the thesis with `evidence-scorecard.md`
5. grade the setup with price/volume/catalyst confirmation
6. keep only names with a visible catalyst or clean risk/reward map
7. output candidates as watchlist setups, active setups, or no-trade setups

Do not keep stale candidates just because they were previously interesting. A name can have a strong thesis and still be a no-trade if price is extended, liquidity is poor, or the invalidation level is unclear.

When the agent selects stocks or crypto assets itself, state:

- market universe used: US, China A-share, HK, global ADRs, crypto majors, AI/DePIN tokens, miners, or user-specified
- discovery route: supply-chain map, peer basket, screen, recent news, filings, or earnings language
- inclusion reason: why the company maps to the bottleneck
- exclusion reason: why obvious peers were skipped if relevant

For tokens, use [crypto-market-playbook.md](crypto-market-playbook.md) before producing entry/exit zones.

## 3. Thesis-To-Tape Check

Separate the long-term thesis from the current tape.

- thesis grade: A-D from `evidence-scorecard.md`
- setup grade: A-D based on price, volume, catalyst, and market regime
- market regime: risk-on, risk-off, mixed, or event-driven
- sector confirmation: leader/peer basket confirming or diverging
- catalyst window: earnings, product launch, industry event, customer capex update, regulatory news

Do not upgrade a weak thesis just because price is moving. Do not ignore a broken chart just because the thesis is attractive.

## 4. Technical Map

Use simple, explainable levels:

- prior breakout / breakdown level
- recent swing high and swing low
- 20-day and 50-day moving averages if available
- high-volume gap or base area
- obvious support / resistance from recent price action
- volume confirmation or failed breakout

Avoid overfitting with too many indicators. Prefer levels that a human trader could see on a chart.

## 5. Setup Types

Classify the setup before giving zones.

- breakout: price clears resistance with volume and sector confirmation
- pullback: thesis intact, price returns to support or moving average
- reversal: high risk; requires failed breakdown, volume, and catalyst
- post-earnings reset: wait for guidance digestion and first stable range
- no-trade: thesis may be good, but price/risk is unattractive

## 6. Entry / Add / Exit Zones

Output zones, not one exact price.

- starter zone: first area where risk/reward is acceptable
- add zone: only after confirmation, such as holding support or reclaiming resistance
- invalidation zone: where the setup is wrong
- first target: logical resistance or measured move where partial de-risking makes sense
- stretch target: only if catalyst, volume, and sector trend keep confirming

Each zone must have a reason. If no clean invalidation exists, say the setup is not clean.

## 7. Risk Template

Every live setup must include:

- maximum thesis risk: what would break the fundamental story
- maximum tape risk: what would break the price setup
- event risk: earnings, guidance, macro, customer news, regulatory headlines
- liquidity risk: especially for lower-market-cap names
- position discipline: starter/add/trim logic, not all-in logic

Do not recommend oversized positions. If asked for sizing, use risk per trade or portfolio percentage ranges, and keep speculative names smaller than proven executors.

## 8. Output Template

Use this structure:

1. data timestamp
2. one-line thesis
3. thesis grade and setup grade
4. current tape read
5. trade plan
6. invalidation
7. catalysts to watch
8. what would make the plan stale

Trade plan format:

- starter zone:
- add zone:
- no-chase zone:
- invalidation / stop zone:
- first target:
- stretch target:

If the user asks for "best stocks now", rank candidates by:

- thesis grade
- setup grade
- liquidity
- catalyst timing
- risk/reward clarity

Reject names where the thesis is strong but the current setup is poor.

If the user asks for "best crypto now", rank assets by:

- BTC/ETH regime fit
- thesis grade
- setup grade
- liquidity and venue quality
- catalyst or unlock timing
- funding/open-interest risk
- risk/reward clarity

## 9. Alert Conditions

If the user wants monitoring, define triggers instead of pretending to trade automatically:

- price trigger: reclaim, breakout, pullback, or breakdown level
- volume trigger: above-average or failed-volume move
- catalyst trigger: earnings, guidance, design win, customer capex, industry report
- thesis trigger: new evidence upgrades or downgrades the bottleneck
- invalidation trigger: support break, guidance cut, supplier substitution, lead-time easing

Each trigger should say what action it prompts: refresh research, add to watchlist, move to active setup, trim/reassess, or remove.
