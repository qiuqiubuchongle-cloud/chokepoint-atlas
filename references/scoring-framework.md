# Scoring Framework

Use this file when the user wants a ranked output, priority list, or a 2.0-style lane comparison.

## Goal

Turn a thesis into a clearer research priority.

## Lane Score Dimensions

Score each lane from 1-5 on these dimensions:

### 1. Constraint Score

How real is the bottleneck?

Check:

- supply concentration
- substitution difficulty
- lead time
- qualification friction

### 2. Evidence Score

How hard is the proof?

Check:

- primary-source quality
- number of confirming sources
- whether multiple companies describe the same constraint

### 3. Consensus Score

How known is this already?

High score means:

- the market is still under-focused
- the story is not fully consensus

Low score means:

- everyone already knows it

### 4. Mispricing Score

Is the role in the system larger than the current attention or valuation implies?

### 5. Catalyst Score

Are there near-term events that could force re-rating?

Examples:

- earnings
- qualification finish
- mass-production start
- capex or capacity announcement

## Output

### Lane Score

Use this for sectors or stack layers.

```text
Lane Score
- Constraint: 4/5
- Evidence: 5/5
- Consensus: 3/5
- Mispricing: 4/5
- Catalyst: 4/5
- Total view: High-priority lane
```

### Name Score

Use this after the lane is already built.

```text
Name Score
- Role in stack: bottleneck supplier
- Constraint exposure: 4/5
- Evidence quality: 3/5
- Re-rating path: 4/5
- Risk: medium-high
```

## Rule

Do not use scoring as fake precision.

The score exists to:

- compare lanes
- compare names inside one lane
- explain why one path deserves more work now

It does not exist to pretend the output is a trading signal.
