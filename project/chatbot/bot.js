const { ActivityHandler, MessageFactory, ActivityTypes } = require('botbuilder');
const { QuestionUnderstand } = require('./src/assets/question-understand/index');
const { ApiHelper } = require('./src/assets/bot-api/index')
const { CardBuilder } = require('./src/card/index')


class EchoBot extends ActivityHandler {
    constructor() {
        super();
        this.onMessage(async (context, next) => {
            const question = new QuestionUnderstand(context.activity.text);
            const api = new ApiHelper(question.findKeyWord(), question.getQueryNumber())
            const replyText = `Looking for: ${api.keyword}`;
            console.log(question.queryNumber, api.keyword)
            var responseBody = await api.responseBack()

            if (!(responseBody === undefined)) {
                const view = new CardBuilder(responseBody);
                if (question.getQueryNumber() == 1) {
                    await context.sendActivity({
                        attachments: [view.createAdvertisementCard()]
                    });
                }
            }

            await context.sendActivity(MessageFactory.text(replyText, replyText));
            await next();
        });

        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            const welcomeText = 'Hello and welcome!';
            for (let cnt = 0; cnt < membersAdded.length; ++cnt) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(MessageFactory.text(welcomeText, welcomeText));
                }
            }
            await next();
        });
    }
}

module.exports.EchoBot = EchoBot;
