from telethon import TelegramClient, sync, errors
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputChannel, InputUser
from telethon.errors.rpcerrorlist import UsernameInvalidError, UserNotMutualContactError
from time import sleep
import re
import constans

while True:
    phone_number = input('Your phone number /you need to be sign in Telegram!!!/')
    is_phone_True = re.search('(\+[0-9]{12}$)', phone_number)
    try:
        phone_number == is_phone_True.group(0)
    except Exception as err:
        print(err)
        continue
    if phone_number == is_phone_True.group(0):
        client = TelegramClient('Go_on', constans.api_id, constans.api_hash).start()
        break
    continue


def main():
    flag = False
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))
    while True:
        channel_name = input('Link of channel pls, example: https://t.me/qwertyuiop1234567890, or \'-\'(without \'\') '
                             'if you need to convert 10 persons from other group (10 first persons)')
        is_correct = re.search(r'(http?s:\/\/)(t\.me)(\/[A-Za-z0-9]+)', channel_name)
        if channel_name == is_correct:
            channel = client.get_entity(channel_name)  # channel_ id or name
            users_in_channel = client.get_participants(channel_name)  # channel id or name
            print(users_in_channel)
            break
        elif channel_name == '-':
            flag = True
            break
        continue

    def from_group_ten_first_persons(group, togroup):
        flag = True
        if group == '-':
            flag = False
            return flag
        elif togroup == '-':
            flag = False
            return flag
        users = client.get_participants(group)
        channel = client.get_entity(togroup)
        for i in range(10):
            try:
                client(InviteToChannelRequest(InputChannel(channel.id, channel.access_hash),
                                                    [InputUser(users[i].id, users[i].access_hash)]))
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
                print('>>>>>9. PeerFloodError try again in 24 Hours...Yes, you in spam')
                print(err)
        return flag

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
            if not flag:
                try:
                    user = client.get_input_entity(tmp)  # (ResolveUsernameRequest(tmp))
                    print(user)
                except UsernameInvalidError as err:
                    print(err)
                    continue
                if user:
                    try:
                        sleep(31)
                        client(InviteToChannelRequest(InputChannel(channel.id, channel.access_hash),
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
                        print('>>>>>9. PeerFloodError try again in 24 Hours...Yes, you in spam')
                        print(err)
                        # sleep(86400)
            elif from_group_ten_first_persons(input('From group get partisipants or - '), input('To group or - ')):
                break
            else:
                continue
    client.disconnect()


if __name__ == '__main__':
    main()
