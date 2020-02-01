import twitter
import os
import textstat


parent_path = os.path.dirname(os.getcwd())
token_dir = parent_path+'\\twitter.txt'

with open(token_dir, 'r') as f:
    consumer_key = f.readline().replace('\n', '')
    consumer_secret = f.readline().replace('\n', '')
    access_token_key = f.readline().replace('\n', '')
    access_token_secret = f.readline().replace('\n', '')

class twit(twitter.Api):
    def __init__(self):
        super().__init__(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret)

    def followers_dump(self):
        pass

    def score_text(self, test_data):
        score = {}
        score['flesch_reading_ease'] = textstat.flesch_reading_ease(test_data)
        score['smog_index'] = textstat.smog_index(test_data)
        score['flesch_kincaid_grade'] = textstat.flesch_kincaid_grade(test_data)
        score['coleman_liau_index'] = textstat.coleman_liau_index(test_data)
        score['automated_readability_index'] = textstat.automated_readability_index(test_data)
        score['dale_chall_readability_score'] = textstat.dale_chall_readability_score(test_data)
        score['difficult_words'] = textstat.difficult_words(test_data)
        score['linsear_write_formula'] = textstat.linsear_write_formula(test_data)
        score['gunning_fog'] = textstat.gunning_fog(test_data)
        score['text_standard'] = textstat.text_standard(test_data)
        return score

    def score_status_text(self, screenname):
        statusdump = self.GetUserTimeline(screen_name=screenname, count=200,
                                    include_rts=False, trim_user=True)
        corpus = ''

        for status in statusdump:
            status = status.AsDict()
            status = status['text']
            corpus += ' ' + status

        return self.score_text(corpus)

    def go(self):
        print('Q to quit')
        screenname = input('Enter twitter user screenname')
        while screenname.lower() != 'q':
            print(self.score_status_text(screenname = screenname))
            screenname = input('Enter twitter user screenname')


application = twit()
print('test1')

if __name__ == '__main__':
    print('test')
    application.go()