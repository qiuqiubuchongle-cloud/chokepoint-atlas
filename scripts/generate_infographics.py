from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap


OUT_DIR = Path("/Users/windows/Desktop/ai-bottleneck-hunter-repo/assets")
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1600, 2200
BG_TOP = (7, 16, 24)
BG_BOTTOM = (13, 30, 42)
PANEL = (8, 18, 27)
PANEL_ALT = (10, 21, 31)
LINE = (34, 79, 102)
ACCENT = (103, 232, 255)
WHITE = (232, 244, 250)
MUTED = (150, 183, 197)
MUTED_2 = (104, 140, 157)

FONT_PATH = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"
MONO_PATH = "/System/Library/Fonts/Supplemental/Menlo.ttc"


def font(size: int):
    return ImageFont.truetype(FONT_PATH, size, index=0)


def mono(size: int):
    return ImageFont.truetype(MONO_PATH, size)


def make_canvas():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)

    for y in range(H):
        t = y / H
        r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
        g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
        b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)
        d.line((0, y, W, y), fill=(r, g, b))

    for x in range(80, W, 80):
        color = (18, 39, 54) if x % 240 else (26, 58, 76)
        d.line((x, 0, x, H), fill=color, width=1)
    for y in range(80, H, 80):
        color = (18, 39, 54) if y % 240 else (26, 58, 76)
        d.line((0, y, W, y), fill=color, width=1)

    for cx, cy, rad, color in [
        (1300, 220, 280, (40, 185, 235)),
        (260, 1880, 340, (28, 150, 210)),
    ]:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=(*color, 34))
        glow = glow.filter(ImageFilter.GaussianBlur(90))
        img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

    d = ImageDraw.Draw(img)
    d.rounded_rectangle((56, 56, W - 56, H - 56), radius=36, outline=LINE, width=2, fill=PANEL)
    return img, d


def draw_title(d, title, subtitle):
    d.text((120, 116), title, font=font(84), fill=WHITE)
    d.text((122, 214), subtitle, font=font(34), fill=ACCENT)


def draw_badge(d, text):
    box = (1170, 104, 1450, 178)
    d.rounded_rectangle(box, radius=18, outline=ACCENT, width=2, fill=(10, 32, 42))
    d.text((1198, 126), text, font=font(24), fill=ACCENT)


def wrap_lines(draw, text, max_width, fnt):
    words = list(text)
    lines = []
    current = ""
    for ch in words:
        trial = current + ch
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def paragraph(draw, x, y, text, width, fnt, fill=MUTED, line_gap=10):
    lines = []
    for block in text.split("\n"):
        if not block:
            lines.append("")
            continue
        lines.extend(wrap_lines(draw, block, width, fnt))
    step = fnt.size + line_gap
    yy = y
    for line in lines:
        draw.text((x, yy), line, font=fnt, fill=fill)
        yy += step
    return yy


def card(d, x, y, w, h, eyebrow, title, body_lines):
    d.rounded_rectangle((x, y, x + w, y + h), radius=28, outline=LINE, width=2, fill=PANEL_ALT)
    d.text((x + 28, y + 24), eyebrow, font=mono(22), fill=ACCENT)
    d.text((x + 28, y + 64), title, font=font(34), fill=WHITE)
    yy = y + 120
    for line in body_lines:
        yy = paragraph(d, x + 28, yy, line, w - 56, font(26), fill=MUTED, line_gap=8)
        yy += 10


def bullet_card(d, x, y, w, h, title, bullets, accent_title=False):
    d.rounded_rectangle((x, y, x + w, y + h), radius=28, outline=LINE, width=2, fill=PANEL_ALT)
    d.text((x + 28, y + 28), title, font=font(34), fill=ACCENT if accent_title else WHITE)
    yy = y + 96
    for bullet in bullets:
        yy = paragraph(d, x + 48, yy, "• " + bullet, w - 76, font(28), fill=MUTED, line_gap=8)
        yy += 14


def footer(d, text):
    d.text((120, 2098), text, font=font(20), fill=MUTED_2)


def infographic_methods():
    img, d = make_canvas()
    draw_title(d, "两个 AI 投研号，两个脑回路", "Serenity 盯咽喉点，Crux 画整张栈")
    draw_badge(d, "Method Comparison")

    intro = (
        "一个从机器往下拆 BOM，盯最细的卡脖子零件。"
        "\n一个先把赛道画成供应链栈，再按执行力给仓位。"
        "\n两个人的方法不同，但都不先问“谁会涨”。"
    )
    paragraph(d, 122, 292, intro, 1320, font(30), fill=MUTED, line_gap=10)

    bullet_card(
        d, 120, 470, 648, 780, "Serenity：先拆，再掐", [
            "起手不是看图，而是先指定一台具体机器：TPU pod、1.6T link、GB300 rack。",
            "核心问题：哪个零件没了，整条链就得停摆？",
            "盯二层、三层瓶颈：激光器、InP 衬底、外延、测试、连接。",
            "看集中度、替代周期、认证难度、产能锁定。",
            "喜欢抓“市值错配”：小供应商卡住大产业。"
        ],
        accent_title=True
    )

    bullet_card(
        d, 832, 470, 648, 780, "Crux：先画栈，再排位", [
            "把赛道拆成 6-9 层：需求、网络、器件、测试、代工、设备、材料。",
            "每层都贴角色：龙头、瓶颈、颠覆者、相邻硅、无聊但必需。",
            "核心不是故事，而是“谁先被付钱、谁执行最强”。",
            "横着读多家公司财报，看同一条供需线是不是同时被验证。",
            "仓位纪律比观点更重要：执行者重，早期标的轻。"
        ],
        accent_title=True
    )

    card(
        d, 120, 1328, 1360, 360, "共同底层", "他们真正相同的地方", [
            "都把市场当成一个物理系统，而不是一堆涨跌符号。",
            "都先找约束，再找公司；先看链条，再看故事。",
            "真正的差别不在“更懂 AI”，而在“更早看到哪个环节会先堵车”。"
        ]
    )

    card(
        d, 120, 1736, 1360, 240, "一句话总结", "你该学的不是他们押中了谁", [
            "而是他们怎么把“找瓶颈”这件事做成一套可重复执行的流程。"
        ]
    )
    footer(d, "Chokepoint Atlas  ·  Compare the method before you copy the names")
    return img


def infographic_distillation():
    img, d = make_canvas()
    draw_title(d, "我怎么把他们蒸馏成一个 Skill", "保留研究动作，删掉神棍味和直接报票冲动")
    draw_badge(d, "Distillation")

    card(
        d, 120, 300, 1360, 250, "我保留了什么", "四个必须留下的动作", [
            "1. 先指定具体机器 / 系统，而不是空谈赛道。",
            "2. 先画供应链栈，再决定瓶颈在哪一层。",
            "3. 先分证据强弱，再谈推理和想象力。",
            "4. 先给方向，再给名字，最后才谈仓位。"
        ]
    )

    steps = [
        ("01", "确认超级趋势", "不是“AI 会涨”，而是 1.6T、液冷、供电、先进封装这些真实 buildout。"),
        ("02", "指定具体机器", "GB300 NVL72、TPU pod、AI factory power train、Optimus 关节模组。"),
        ("03", "画 6-9 层供应链栈", "需求 -> 系统 -> 模块 -> 器件 -> 测试 -> 代工 -> 设备 -> 材料。"),
        ("04", "找最窄的瓶颈", "材料、认证、产能、热、电、良率，究竟卡的是哪一个。"),
        ("05", "证据交叉验证", "财报 / 电话会 / IR / 研报 / 产业新闻 / 供应商变化，同一条线必须对上。"),
        ("06", "先给方向，后给名字", "第一层只给 lane；用户继续追问，才给候选名单和低市值标的。"),
    ]
    start_y = 610
    for i, (num, title, body) in enumerate(steps):
        x = 120 if i % 2 == 0 else 832
        y = start_y + (i // 2) * 320
        card(d, x, y, 648, 260, num, title, [body])

    card(
        d, 120, 1610, 648, 270, "我删掉了什么", "不让 skill 变成表演型人格", [
            "不直接模仿两个博主的口头禅。",
            "不把推理写成既成事实。",
            "不在 thesis 之前就开始 ticker spam。"
        ]
    )
    card(
        d, 832, 1610, 648, 270, "最终产物", "这不是一个选股 prompt", [
            "它更像一个研究协议：方向 -> 栈 -> 瓶颈 -> 证据 -> 名字。",
            "目的是让 Agent 先把地图画清楚，再去谈下注。"
        ]
    )
    footer(d, "Chokepoint Atlas  ·  Distill the workflow, not the performance screenshot")
    return img


def infographic_skill():
    img, d = make_canvas()
    draw_title(d, "Chokepoint Atlas 的工作流", "一个完整的 AI 供应链瓶颈研究协议")
    draw_badge(d, "Skill Flow")

    intro = (
        "默认输出不是股票池，而是一层一层推进的研究过程。"
        "\nL1 到 L5 分工很清楚：先方向，后名单；先证据，后叙事。"
    )
    paragraph(d, 122, 292, intro, 1320, font(30), fill=MUTED, line_gap=10)

    cards = [
        ("L1", "赛道诊断", ["先给一台真实机器。", "拆 BOM，看哪个零件没了就造不出来。"]),
        ("L2", "画栈贴标签", ["把链条拆成 6-9 层。", "龙头 / 瓶颈 / 颠覆者 / 材料 / 测试分开看。"]),
        ("L3", "证据链", ["每条关键判断都分成 Confirmed / Inferred / Needs verification。", "财报和 IR 优先级最高。"]),
        ("L4", "方向判断", ["输出 lane、阶段、催化剂、打脸条件。", "这一层还不该先报股票。"]),
        ("L5", "低市值深挖", ["只有追问时才进入。", "每个名字都要写市值错配、当前阶段、为什么还太早。"]),
        ("RULE", "默认输出顺序", ["方向 -> 栈 -> 瓶颈 -> 证据 -> 名字", "如果用户上来就要小票，也得先补一段 thesis。"]),
    ]
    y0 = 500
    for idx, (eyebrow, title, lines) in enumerate(cards):
        x = 120 if idx % 2 == 0 else 832
        y = y0 + (idx // 2) * 310
        card(d, x, y, 648, 250, eyebrow, title, lines)

    card(
        d, 120, 1470, 1360, 420, "产品边界", "这个 skill 不做什么", [
            "不做短线喊单，不做情绪复读，不把社媒 rumor 当硬证据。",
            "不把早期 optionality 名字包装成执行型龙头。",
            "不强行扮演 Serenity 或 Crux，只借他们的研究动作和问题设计。"
        ]
    )
    card(
        d, 120, 1930, 1360, 150, "一句话说明书", "给别的 Agent 的最短交接", [
            "先画地图，再找堵点；先做 thesis，再谈 ticker。"
        ]
    )
    footer(d, "Chokepoint Atlas  ·  Direction first  ·  Thesis before tickers")
    return img


def main():
    outputs = {
        "infographic-01-methods.png": infographic_methods(),
        "infographic-02-distillation.png": infographic_distillation(),
        "infographic-03-skill-flow.png": infographic_skill(),
    }
    for name, img in outputs.items():
        img.save(OUT_DIR / name)
        print(OUT_DIR / name)


if __name__ == "__main__":
    main()
