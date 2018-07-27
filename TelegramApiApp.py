from telethon import TelegramClient, sync, errors
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputChannel, InputUser
from telethon.errors.rpcerrorlist import UsernameInvalidError, UserNotMutualContactError
from time import sleep
from telethon.errors.rpcerrorlist import UserIdInvalidError
import re
import constants
phone_number = '+380675141407'
client = TelegramClient('Go_on', constants.api_id, constants.api_hash).start()


def main():
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))
    while True:
        channel_name = input('Link of channel pls example: https://t.me/qwertyuiop1234567890')
        is_correct = re.search(r'(http?s:\/\/)(t\.me)(\/[A-Za-z0-9]+)', channel_name)
        if channel_name == is_correct:
            channel = client.get_entity(channel_name)  # channel_ id https://t.me/bloXrouteLabsCommunity
            users_in_channel =  client.get_participants(channel_name)  # channel id or https://t.me/ncent
            print(users_in_channel)
            break
        else:
            continue

    def is_in_group(username):
        if username in users_in_channel:
            return True
        else:
            return False

    with open('im.txt') as f:  # file with list of usernames
        for line in f:
            print(line)
            tmp = line[1:].replace('\n', '')
            print(tmp)
            try:
                user = client.get_input_entity(tmp)  # (ResolveUsernameRequest(tmp))
                print(user)
            except UsernameInvalidError as err:
                print(err)
                continue
            if user:
                try:
                    sleep(31)
                    client.invoke(InviteToChannelRequest(InputChannel(channel.id, channel.access_hash),
                                                                [InputUser(user.user_id, user.access_hash)]))
                except errors.rpcerrorlist.UserPrivacyRestrictedError as err:
                    print('>>>>0. UserPrivacyRestrictedError...')
                    print(err)
                except errors.rpcerrorlist.ChatAdminRequiredError as err:
                    print('>>>>1. ChatAdminRequiredError...')
                    print(err)
                except errors.rpcerrorlist.ChatIdInvalidError as err:
                    print('>>>>2. ChatIdInvalidError...')
                    print(err)
                except errors.rpcerrorlist.InputUserDeactivatedError as err:
                    print('>>>>3. InputUserDeactivatedError...')
                    print(err)
                except errors.rpcerrorlist.PeerIdInvalidError as err:
                    print('>>>>4. PeerIdInvalidError...')
                    print(err)
                except errors.rpcerrorlist.UserAlreadyParticipantError as err:
                    print('>>>>5. UserAlreadyParticipantError...')
                    print(err)
                except errors.rpcerrorlist.UserIdInvalidError as err:
                    print('>>>>6. UserIdInvalidError...')
                    print(err)
                except errors.rpcerrorlist.UserNotMutualContactError as err:
                    print('>>>>>7. UserNotMutualContactError...')
                    print(err)
                except errors.rpcerrorlist.UsersTooMuchError as err:
                    print('>>>>>8. UsersTooMuchError...')
                    print(err)
                except errors.rpcerrorlist.PeerFloodError as err:
                    print('>>>>>9. PeerFloodError try again in 24 Hours...Yes you in spam')
                    print(err)
                    sleep(86400)
            else:
                continue
    client.disconnect()


if __name__ == '__main__':
    main()
"""@BevzenkoA
@BobbyReggieB
@IevgeniiaKobets
@LarsMathiasRoth
@OlaSebastianSelby
@Tetiana92713958
@Volodym81570905
@Serhii88849557
@LEVINEW_QUINN
@e1ectromind 
@AndreiStefanIo1
@EricAdamPaulFrankenius
@AlfieJackson_Potter
@Prebensen2
@Knutsen79922074
@milkytwilight
@zacharynicholson
@GindemoAnton
@Marsh09331591
@Marsh09331591
@Walters97894779
@benebi
@Austin03120466
@Gdenargi
@oskar_marcus
@xMac73
@skateordie2
@barcelonaman
@lovenastyamuch
@dancetojoydivision
@Chamber31368162
@rep19
@JimmyPe91684253
@rep18
@reppo19
@rusrus82
@grant_grant
@newstuff13
@linamyakinina
@cryptogalaxy8
@Oleksii_Andrieiev
@bestby13
@proteinpoint
@scrooge13
@Kristya18
@caption1313
@Brynjar96952253
@Oliver10802973
@DavidGustav9"""