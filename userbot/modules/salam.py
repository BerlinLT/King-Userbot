from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam...`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam...`")


@register(outgoing=True, pattern='^.S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Sayang,mau gak jadi pacar aku?❤️...`")


@register(outgoing=True, pattern='^.s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Sayang,mau gak jadi pacar aku?❤️...`")


@register(outgoing=True, pattern='^.J(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Gakmau ah,kamu jelek😅...`")

@register(outgoing=True, pattern='^.j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Gakmau ah,kamu jelek😅...`")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝑼𝒅𝒂𝒉 𝒕𝒂𝒖 𝒅𝒊 𝒔𝒊𝒂²𝒊𝒏 𝒎𝒂𝒔𝒊𝒉 𝒂𝒋𝒂 𝒃𝒆𝒓𝒋𝒖𝒂𝒏𝒈...`")
    
    
    @register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`kaga, gua kan ganteng`")


CMD_HELP.update({
    "salam":
    "⚡𝘾𝙈𝘿⚡`.P`\
\nPenjelasan: Untuk Memberi salam ke semua orang.\
\n\n⚡𝘾𝙈𝘿⚡`.L`\
\nPenjelasan: Untuk Menjawab Salam ke semua orang.\
\n\n⚡𝘾𝙈𝘿⚡`.S`\
\nPenjelasan: Untuk menjadi buaya🐊.\
\n\n⚡𝘾𝙈𝘿⚡`.J`\
\nPenjelasan: Untuk jdi orang jahat 😈.\
\n\n⚡𝘾𝙈𝘿⚡`.M`\
\nPenjelasan: galau 😈.\
\n\n⚡𝘾𝙈𝘿⚡`.G`\
\nPenjelasan: yg penting pede yakkann 😈."
})
