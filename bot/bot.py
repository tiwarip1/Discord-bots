import discord
import shlex
import string
import os
import pandas as pd
import random
import time

from insult import make_insult

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
        elif message.content.startswith('<@571047329784660040>'):
            if arguments[1].translate(str.maketrans('', '', string.punctuation)).lower()=='insult':
                self.take_words()
                await message.channel.send('{}, you {} {} {}'.format(arguments[-1],self.used_adjective,self.used_noun,self.used_curses))
            elif arguments[1].translate(str.maketrans('', '', string.punctuation)).lower()=='old' and arguments[2].translate(str.maketrans('', '', string.punctuation)).lower()=='insult':
                words = make_insult()
                await message.channel.send('{}, you {} {} {}'.format(arguments[-1],word[0],word[1],word[2]))

        else:
            print(arguments)

    def take_words(self):
        nouns = pd.read_csv('nouns.txt')
        adjectives = pd.read_csv('adjectives.txt')
        curses = pd.read_csv('curses.txt')

        nouns_len = len(nouns.columns)
        adjectives_len = len(adjectives.columns)
        curses_len = len(curses.columns)
        self.used_noun = nouns.sample().values[0][0].lower()
        self.used_adjective = adjectives.sample().values[0][0].lower()
        self.used_curses = curses.sample().values[0][0].lower()

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
                    

client = MyClient()
client.run('NTcxMDQ3MzI5Nzg0NjYwMDQw.XMIEtg.Db2-LkVoh5PIUZNpS0OT_WifUuY')