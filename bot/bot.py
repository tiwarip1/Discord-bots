import discord
import shlex
import string
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        arguments = list(shlex.split(message.content))
        
        self.read_bitch_list()

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif arguments[-1].translate(str.maketrans('', '', string.punctuation)).lower()=='bitch' and arguments[0].lower() in ['is','am']:
            confirm = False
            for i in arguments:
                i = i.translate(str.maketrans('', '', string.punctuation)).lower()
                if i in self.bitches:
                    await message.channel.send('Yes')
                    confirm = True
            if confirm==False:
                await message.channel.send('No, but they can be if you want')
        elif arguments[0].lower()=='add' and arguments[-1].translate(str.maketrans('', '', string.punctuation)).lower()=='bitch':
            self.update_bitch_list(arguments[1])
            print(self.bitches)
            await message.channel.send('{} was added to the bitch pile'.format(arguments[1]))
        else:
            print(arguments)

    def update_bitch_list(self,addition):
        with open('bitchlog.txt','a') as f:
            f.write('{}\n'.format(addition))
            
    def read_bitch_list(self):
        self.bitches = []
        exists = os.path.isfile('bitchlog.txt')

        if exists:
            with open('bitchlog.txt','r') as f:
                for i in f:
                    self.bitches.append(i[:-1])
                    
        print(self.bitches)

client = MyClient()
client.run('NTcxMDQ3MzI5Nzg0NjYwMDQw.XMIEtg.Db2-LkVoh5PIUZNpS0OT_WifUuY')