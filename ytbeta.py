api_key='AIzaSyCWJmAdhtBXKCr59ao-XMvvQ8IrBM4bqis'

from googleapiclient.discovery import build

#making a youtube object 
youtube = build('youtube', 'v3', developerKey=api_key)

def run():


    print('''

=======================================Youtube===============================================

            Search For Youtube Account and select your youtube channel for detailed
                                      Statistics

=============================================================================================
    ''')


    key = input('Enter Name:  ')
    #making a request for channels by this name
    #we only tool channel which is popular by that name
    req = youtube.search().list(q= key, part= 'snippet', type= 'channel', maxResults = 3)
    res = req.execute()
    print('\n')
    print('\n')
    print('   =================================================   ')
    i = 1
    ls = list()
    for item in res['items']:
        #saving channel id to --idc--
        print('press', i, 'for this channel')
        print('\n')
        print(item['snippet']['title'], end = ' ')
        print(item['snippet']['channelId'])
        print(item['snippet']['description'])
        print('\n')
        i = i + 1
        ls.append(item['snippet']['channelId'])
        print('  ==============================================  ')

    it = int(input('>>> '))
    idc = ls[it-1]
    #making request for channel details
    #currenty only 2
    #snippet and statistics
    ch = youtube.channels().list(part = ['snippet', 'statistics', 'topicDetails'], id= idc)
    chd = ch.execute()
    for item in chd['items']:
        #printing things we need in json file
        print('\n')
        print('Title: ', item['snippet']['title'])
        print('\n')
        print('Unique Id:', idc)
        print('\n')
        print('Description: ', item['snippet']['description'])
        print('\n')
        print('Url: ', item['snippet']['customUrl'])
        print('\n')
        print('Published on: ', item['snippet']['publishedAt'])
        print('\n')
        print('country: ', item['snippet']['country'])
        print('\n')
        print('Total View Count: ', item['statistics']['viewCount'])
        print('\n')
        #print('Comment Count: ', item['statistics']['commentCount'])
        print('Subs Count: ', item['statistics']['subscriberCount'])
        print('\n')
        print('Video Count: ', item['statistics']['videoCount'])
        print('\n')
        print('==================')
        print('WikiPedia Articles that describes the Channel:')
        print('\n')
        ty = item['topicDetails']['topicCategories']
        for v in ty:
            print(v)
        print('\n')
        print('==================')
