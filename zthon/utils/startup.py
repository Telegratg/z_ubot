# ZedThon - zthon
# Copyright (C) 2022 ZedThon . All Rights Reserved
# < https://t.me/ZedThon >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

import asyncio
import glob
import os
import sys
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils

from zthon import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import zedub
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger("إعداد الرعدثون")
cmdhr = Config.COMMAND_HAND_LER

if ENV:
    VPS_NOLOAD = ["سيرفر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هيروكو"]

bot = zedub
DEV = 1895219306


async def setup_bot():
    """
    To set up bot for zthon
    """
    try:
        await zedub.connect()
        config = await zedub(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == zedub.session.server_address:
                if zedub.session.dc_id != option.id:
                    LOGS.warning(
                        f"اصلاح الداتا {sbb_b.session.dc_id}" f" الى {option.id}"
                    )
                zedub.session.set_dc(option.id, option.ip_address, option.port)
                zedub.session.save()
                break
        bot_details = await zedub.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await zedub.start(bot_token=Config.TG_BOT_USERNAME)
        zedub.me = await zedub.get_me()
        zedub.uid = zedub.tgbot.uid = utils.get_peer_id(zedub.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(zedub.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {e}")
        sys.exit()


async def startupmessage():
    """
    رسالة التشغيل
    """
    try:
        if BOTLOG:
            Config.ZEDUBLOGO = await zedub.tgzedub.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/f821d27af168206b472ad.mp4",
                caption="**•⎆┊تـم بـدء تشغـيل سـورس زدثــون الخاص بك .. بنجاح 🧸♥️**",
                buttons=[(Button.url("𝘼𝙇𝙍𝘼𝘿𝙏𝙃𝙀𝙉 ⩫𓅛", "https://t.me/ALRADTHEN"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await zedub.check_testcases()
            message = await zedub.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**•⎆┊تـم اعـادة تشغيـل السـورس بنجــاح 🧸♥️**"
            await zedub.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await zedub.send_message(
                    msg_details[0],
                    f"{cmdhr}فحص",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    ZELZAL = zedub.me.first_name
    Malath = zedub.uid
    zel_zal = f"[{ZELZAL}](tg://user?id={Malath})"
    f"ـ {zel_zal}"
    f"•⎆┊هــذا البــوت خــاص بـ {zel_zal} يمكـنك التواصــل معـه هـنا 🧸♥️"
    zilbot = await zedub.tgbot.get_me()
    bot_name = zilbot.first_name
    botname = f"@{zilbot.username}"
    if bot_name.endswith("Assistant"):
        print("تم تشغيل البوت بنجــاح")
    else:
        try:
            await zedub.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", "ZThon")
            await asyncio.sleep(3)
            await zedub.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", f"مسـاعـد - {bot.me.first_name} ")
            await asyncio.sleep(3)
            await zedub.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await zedub.send_file("@BotFather", "zthon/zilzal/logozed.jpg")
            await asyncio.sleep(3)
            await zedub.send_message("@BotFather", "/setabouttext")
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await zedub.send_message(
                "@BotFather",
                f"- بـوت زدثــون المسـاعـد ♥️🦾 الخـاص بـ  {bot.me.first_name} ",
            )
            await asyncio.sleep(3)
            await zedub.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await zedub.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await zedub.send_message(
                "@BotFather",
                f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {zel_zal} \n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @ALRADTHEN 🌐",
            )
        except Exception as e:
            print(e)


async def add_bot_to_logger_group(chat_id):
    """
    اضافة البوت لمجموعات التخزين
    """
    bot_details = await zedub.tgbot.get_me()
    try:
        await zedub(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await zedub(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder, extfolder=None):
    """
    تحميل ملفات السورس
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"zthon/{folder}/*.py"
        plugin_path = f"zthon/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لا يمكنني تحميل {shortname} بسبب الخطأ {e}\nمجلد القاعده {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await zedub.tgzedub.send_message(
            BOTLOG_CHATID,
            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`',
        )


async def verifyLoggerGroup():
    """
    التاكد من مجموعة التخزين
    """
    flag = False
    if BOTLOG:
        try:
            entity = await zedub.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n" + str(e)
            )
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"
        photozed = await zedub.upload_file(file="zedthon/malath/Zpic.jpg")
        _, groupid = await create_supergroup(
            "كـروب السجـل زدثـــون", zedub, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("تم انشاء مجموعة التخزين بنجاح")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await zedub.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info("لا توجد صلاحيات كافية لارسال الرسائل في مجموعة التخزين")
                if entity.default_banned_rights.invite_users:
                    LOGS.info("لا توجد صلاحيات كافية لاضافة الاعضاء في مجموعة التخزين")
        except ValueError:
            LOGS.info(
                "لم يتم العثور على ايدي مجموعة التخزين تاكد من انه مكتوب بشكل صحيح "
            )
        except TypeError:
            LOGS.error(
                "صيغه ايدي مجموعة التخزين غير صالحة.تاكد من انه مكتوب بشكل صحيح "
            )
        except Exception as e:
            LOGS.error("حدث خطأ اثناء التعرف على مجموعة التخزين\n" + str(e))
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن رسـائل الخـاص.)"
        photozed = await zedub.upload_file(file="zedthon/malath/Apic.jpg")
        _, groupid = await create_supergroup(
            "كـروب التخـزين", zedub, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تم عمل مجموعة التخزين بنجاح واضافة الفارات اليه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "zthon"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)
