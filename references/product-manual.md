# Product Manual

This file is the complete usage manual for `ai-supply-chain-bottleneck-hunter`.

Use it when:

- another agent needs to understand how to invoke the skill
- the user wants a concrete "how to use this" guide
- the skill is being handed off as a reusable research product

## 1. What This Skill Is

This skill is a structured AI-infrastructure research workflow.

It is designed to:

- map AI supply chains
- identify real bottlenecks
- validate those bottlenecks with external evidence
- produce a directional lane first
- only later surface candidate companies

It is **not**:

- a stock-picking shortcut
- a momentum scanner
- a one-shot "tell me what to buy" prompt

Version 2.0 extends the product from a research workflow into a small research system:

- evidence ranking
- relationship mapping
- lane / name prioritization
- catalyst tracking

## 2. Core Promise

This skill forces research to happen in the right order:

1. demand wave
2. stack map
3. bottleneck
4. evidence
5. directional thesis
6. candidate names
7. single-name underwrite

That order is the product.

In 2.0, the product also forces a second order of discipline:

1. rank the proof
2. map the dependencies
3. score the lane
4. track what could confirm or break it next

## 3. Who Should Use It

Use this skill for users who want:

- AI infrastructure sector research
- photonics / semiconductor / packaging / power / cooling thesis building
- Serenity-style bottleneck hunting
- Crux-style stack construction and weighting discipline
- a reusable "research agent" workflow instead of one-off commentary

Do not use it for:

- daily trading signals
- macro-only market commentary
- meme stock chatter
- users who only want a quick ticker dump

## 4. Supported Input Modes

This skill supports four input modes.

In version 2.0, it also supports a fifth mode.

### Mode A: Raw Theme

Example:

`What is the next AI infrastructure bottleneck?`

Expected behavior:

- infer a supertrend
- map the stack
- output a directional lane

### Mode B: Theme + Constraint

Example:

`I want the next AI lane, but avoid crowded large caps.`

Expected behavior:

- map the stack
- identify bottlenecks
- note where the market is already crowded
- later surface less-followed names only if asked

### Mode C: Predefined Sector

Example:

`Look at optical interconnect and tell me where the real bottleneck sits now.`

Expected behavior:

- stay within the chosen sector
- build the stack
- identify the narrowest choke point

### Mode D: Known Company

Example:

`Underwrite AXTI using this skill.`

Expected behavior:

- place the company in the stack
- explain why it matters
- separate fact, inference, and speculation

### Mode E: System Research

Example:

`Run this as a 2.0 system. Give me evidence levels, a relationship map, and a lane score.`

Expected behavior:

- keep the normal thesis workflow
- add evidence tags
- add a graph-oriented dependency map
- add a lane score
- add next catalysts

## 5. Output Layers

This skill has three output layers.

Version 2.0 adds four optional overlays:

- evidence ladder
- graph card
- lane score
- catalyst watch

### Layer 1: Directional Lane

Default first answer.

Use when the user asks:

- what direction matters
- what to study next
- where the bottleneck sits

Required sections:

- thesis sentence
- supertrend summary
- stack summary
- bottleneck call
- strongest evidence
- thesis breaker
- next things to monitor

This layer should **not** start with stock names.

If the user asks for a 2.0 version, this layer should also include:

- evidence tag on the key claim
- one weakest assumption
- one next catalyst

### Layer 2: Candidate Watchlist

Use only after:

- the directional lane is already established
- or the user explicitly follows up asking for names

Required sections:

- proven executors
- bottleneck pure-plays
- second-order beneficiaries
- early optionality

For each name:

- role in stack
- why it belongs
- what is confirmed
- what is still weak
- key risk

In 2.0, optionally add:

- name score
- catalyst sensitivity

### Layer 3: Single-Name Underwrite

Use when the user asks for one company in depth.

Required sections:

- what exact problem the company solves
- where it sits in the stack
- why it is hard to replace
- evidence quality
- ramp / revenue timing
- failure cases

In 2.0, also add:

- strongest proof node
- graph position
- next catalyst

## 6. Required Response Order

Unless the user asks for a single-company underwrite from the start, always respond in this order:

1. direction
2. stack
3. bottleneck
4. evidence
5. names if requested

If a user asks:

`Give me low-cap AI names`

the skill should still do this:

- one short lane thesis
- one bottleneck summary
- then candidate names

It must not jump straight to ticker spam.

In 2.0, it must also avoid:

- treating a weak source as graph proof
- presenting score totals without dimension-level explanation

## 7. Research Standards

This skill is only good if it is evidence-driven.

Minimum evidence categories:

- company evidence
- industry evidence
- cross-company confirmation

Preferred source order:

1. company IR / earnings / filings
2. official customer or supplier statements
3. industry publications or trade reporting
4. broker or market-research summaries
5. social content as a weak signal only

Every strong answer should say:

- what is confirmed
- what is inferred
- what is speculative

In 2.0, every strong answer should also say:

- which claim is `Confirmed`
- which claim is `Inferred`
- which claim is `Weak`
- which claim `Needs verification`

Read [evidence-ladder.md](evidence-ladder.md) when the user wants this structure.

## 8. Research Questions This Skill Must Ask

At minimum, the skill should pressure-test these questions:

- what demand wave is actually expanding?
- what is the concrete deployed system or machine behind that demand?
- what physical buildout does that imply?
- which layer gets paid first?
- which layer breaks first?
- what makes that bottleneck hard to replace?
- has management or the industry already confirmed the constraint?
- is the bottleneck already consensus?
- if the thesis is right, who gets paid now and who gets paid later?
- if the supplier vanished tomorrow, how long would the downstream wait?

For the full question sequence, read [question-ladder.md](question-ladder.md).

For graph outputs, read [graph-schema.md](graph-schema.md).

For scoring outputs, read [scoring-framework.md](scoring-framework.md).

For time-based follow-up, read [catalyst-watch.md](catalyst-watch.md).

## 9. Positioning Logic

This skill should treat names differently by maturity.

Default logic:

- proven executors: higher confidence, larger weight candidates
- bottleneck suppliers: high value if the evidence is hard
- early disruptors: smaller weight, more validation required
- optionality names: mention upside, but make risk explicit

In 2.0, ranking should use:

- Constraint Score
- Evidence Score
- Consensus Score
- Mispricing Score
- Catalyst Score

Never present early-stage optionality names as if they deserve the same confidence as proven executors.

## 10. Style Contract

This skill should sound like:

- a researcher trying to map a real industrial system
- skeptical, concrete, and bottleneck-focused

It should not sound like:

- a hype thread
- a tip sheet
- a copy of Serenity or Crux

What to borrow:

- Serenity's obsession with the narrowest choke point
- Crux's stack thinking and execution-weighted view

What not to borrow:

- exact slogans
- performance bragging as proof
- false certainty

For more detail, read [style-and-voice.md](style-and-voice.md).

## 11. Version 2.0 Deliverables

When the user explicitly asks for a 2.0 answer, produce one or more of:

1. Evidence Memo
2. Graph Card
3. Ranked Lane Table
4. Catalyst Watch

Use [output-formats-v2.md](output-formats-v2.md) for the exact structure.

## 12. Failure Modes

This skill is failing if it does any of these:

- names stocks before naming the bottleneck
- says "AI is bullish" without identifying a real physical constraint
- treats one rumor as enough proof
- mixes fact and speculation together
- recommends low-cap names without saying what still needs validation
- uses generic LLM language instead of concrete industrial reasoning
- force-acts like Serenity or Crux instead of borrowing only their research habits

## 13. Example Invocations

### Example 1: Direction First

`Use $ai-supply-chain-bottleneck-hunter to tell me the next AI infrastructure bottleneck. Do not give me stocks yet.`

Expected output:

- one directional lane
- one stack map
- one bottleneck call
- evidence and disproof

### Example 2: Direction Then Names

`Continue with $ai-supply-chain-bottleneck-hunter. Now give me 5 names, split by executor / pure bottleneck / optionality.`

Expected output:

- grouped watchlist
- each name with role, reason, risk, next check

### Example 3: Single Name

`Use $ai-supply-chain-bottleneck-hunter to underwrite AXTI.`

Expected output:

- company role in stack
- exact bottleneck it touches
- evidence quality
- main failure cases

## 14. Hand-Off Rule

If this skill is being given to another agent, tell that agent:

- start with the lane, not the ticker
- force a stack before a conclusion
- require at least one non-social evidence source when the user asks for current validation
- do not confuse "interesting" with "underwritten"

That is the shortest faithful hand-off.
