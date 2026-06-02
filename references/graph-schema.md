# Graph Schema

Use this file when the user wants a relationship map, project graph, system graph, or a 2.0-style output.

## Goal

Represent the thesis as a graph instead of a plain list.

## Node Types

Use these five node groups.

### 1. End System

Examples:

- `GB300 NVL72`
- `TPU pod`
- `Optimus`
- `AI factory`

### 2. Component / Function Layer

Examples:

- `laser`
- `InP substrate`
- `liquid cooling`
- `power distribution`
- `harmonic drive`
- `force-torque sensing`

### 3. Company

Examples:

- supplier
- customer
- foundry
- competitor
- test vendor

### 4. Evidence

Examples:

- earnings-call quote
- filing
- industry article
- supplier-list change

### 5. Catalyst

Examples:

- earnings date
- qualification finish
- expansion announcement
- mass-production milestone

## Edge Types

Keep the graph simple. Use:

- `supplies`
- `depends_on`
- `competes_with`
- `confirmed_by`
- `likely_benefits_from`
- `catalyzed_by`

## Minimum Graph Standard

Every strong graph should include:

1. one end system
2. two to five component layers
3. three to eight companies
4. at least two evidence nodes
5. at least one catalyst node

## Output Shape

When showing the graph in text, use:

```text
End system:
- ...

Critical components:
- ...

Companies:
- ...

Evidence links:
- Company A -> confirmed_by -> earnings-call transcript
- Component B -> depends_on -> Company C

Catalysts:
- Company C -> catalyzed_by -> qualification milestone
```

## Simple JSON Shape

```json
{
  "nodes": [
    {"id": "opt", "type": "end_system", "label": "Optimus"},
    {"id": "fts", "type": "component", "label": "force-torque sensing"},
    {"id": "vpg", "type": "company", "label": "VPG"},
    {"id": "q1call", "type": "evidence", "label": "Q1 earnings call"},
    {"id": "qual", "type": "catalyst", "label": "qualification complete"}
  ],
  "edges": [
    {"from": "opt", "to": "fts", "type": "depends_on"},
    {"from": "vpg", "to": "fts", "type": "supplies"},
    {"from": "vpg", "to": "q1call", "type": "confirmed_by"},
    {"from": "vpg", "to": "qual", "type": "catalyzed_by"}
  ]
}
```
