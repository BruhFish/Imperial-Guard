import asyncio
import os

import mongoengine
from dotenv import find_dotenv, load_dotenv

from data.model.guild import Guild

load_dotenv(find_dotenv())

async def setup():
    print("STARTING DATABASE SETUP...")
    guild = Guild()

    # you should have this setup in the .env file beforehand
    guild._id          = int(os.environ.get("MAIN_GUILD_ID"))

    # If you're re-running this script to update a value, set case_id
    # to the last unused case ID or else it will start over from 1!
    guild.case_id      = 1

    # required for permissions framework!
    guild.role_administrator = 887983992194867210  # put in the role IDs for your server here
    guild.role_moderator     = 887984027846463488  # put in the role IDs for your server here
    guild.role_birthday      = 1127897252669698140  # put in the role IDs for your server here
    guild.role_sub_mod       = 887984063867150336  # put in the role IDs for your server here
    guild.role_genius        = 1117326063878537226  # put in the role IDs for your server here
    guild.role_dev           = 1127896083146748058  # put in the role IDs for your server here
    guild.role_memberone     = 1091999997106602054  # put in the role IDs for your server here
    guild.role_memberedition = 1122359281224790086  # put in the role IDs for your server here
    guild.role_memberpro     = 1091999611398410281  # put in the role IDs for your server here
    guild.role_memberplus    = 1091999548383182919  # put in the role IDs for your server here
    guild.role_memberultra   = 1122358833919037460  # put in the role IDs for your server here

    # not required if you don't want the /subnews command
    guild.role_sub_news      = 1127896392128540682  # put in the role IDs for your server here

    guild.channel_reports        = 1045873133158146098  # put in the channel IDs for your server here
    # channel where reactions will be logged
    guild.channel_emoji_log      = 887982977995386911  # put in the channel IDs for your server here
    # channel for private mod logs
    guild.channel_private        = 887982977995386911  # put in the channel IDs for your server here
    # channel where self-assignable roles will be posted
    guild.channel_reaction_roles = 887980989480075334  # put in the channel IDs for your server here
    # rules-and-info channel
    guild.channel_rules          = 887980989480075334  # put in the channel IDs for your server here
    # not required
    guild.channel_applenews      = 1092071906938728518  # put in the channel IDs for your server here
    # channel for public mod logs
    guild.channel_public         = 1124686035390046248 # put in the channel IDs for your server here
    # optional, used for /subnrnews command or something
    guild.channel_subnews        = 1046273680319201320  # put in the channel IDs for your server here
    # optional, required for /issue command
    guild.channel_common_issues  = 887982602991075378  # put in the channel IDs for your server here
    # #general, required for permissions
    guild.channel_general        =  887982441359372318 # put in the channel IDs for your server here
    # required for filter
    guild.channel_development    = 1046273182178476123  # put in the channel IDs for your server here
    # required, #bot-commands channel
    guild.channel_botspam        = 1092077564882866207  # put in the channel IDs for your server here
    # optional, needed for booster #emote-suggestions channel
    guild.channel_booster_emoji  = 1071898809149435914  # put in the channel IDs for your server here

    # you can fill these in if you want with IDs, or you ca use commands later
    guild.logging_excluded_channels = [1127910878575067226]  # put in a channel if you want (ignored in logging)
    guild.filter_excluded_channels  = [1127910878575067226]  # put in a channel if you want (ignored in filter)
    guild.filter_excluded_guilds    = [288215570996920320, 288215570996920320, 150662382874525696, 349243932447604736, 537979168064012288]  # put guild ID to whitelist in invite filter if you want

    guild.nsa_guild_id = 123 # you can leave this as is if you don't want Blootooth (message mirroring system)

    guild.save()
    print("DONE")

if __name__ == "__main__":
    if os.environ.get("DB_CONNECTION_STRING") is None:
        mongoengine.register_connection(
            host=os.environ.get("DB_HOST"), port=int(os.environ.get("DB_PORT")), alias="default", name="botty")
    else:
        mongoengine.register_connection(
            host=os.environ.get("DB_CONNECTION_STRING"), alias="default", name="botty")
    res = asyncio.get_event_loop().run_until_complete( setup() )
