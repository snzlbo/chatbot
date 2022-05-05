const { ActivityHandler, MessageFactory, ActivityTypes } = require('botbuilder');
const { QuestionUnderstand } = require('./src/assets/question-understand/index');
const { ApiHelper } = require('./src/assets/bot-api/index')
const { CardBuilder } = require('./src/card/index')


class EchoBot extends ActivityHandler {
    constructor() {
        super();
        const defaultAnswer =
            '💡Хүссэн байгууллагынхаа ажлын байрны мэдээллийг цаг алдалгүй аваарай. (Жишээлбэл: Голомт Банк-д Хуульч ажлын байрны дэлгэрэнгүй мэдээлэл?)'
        const noResponse =
            'Уучлаарай таны асуултад хариулт олдсонгүй. Одоогоор чатботны хариулж чадах асуулт:'
        this.onMessage(async (context, next) => {
            const question = new QuestionUnderstand(context.activity.text);
            const api = new ApiHelper(question.findKeyWord(), question.getQueryNumber())
            console.log(question.queryNumber, api.keyword)
            var responseBody = await api.responseBack()

            if (!(responseBody === undefined) && !(responseBody.length == 0)) {
                const view = new CardBuilder(responseBody);
                switch (question.getQueryNumber()) {
                    case 1:
                        await context.sendActivity({
                            attachments: [view.createAdvertisementCard()]
                        })
                        break
                    case 404:
                        await context.sendActivity(
                            MessageFactory.text('noResponse')
                        )
                }
            }
            else {
                await context.sendActivity(MessageFactory.text(noResponse, noResponse));
                await context.sendActivity(MessageFactory.text(defaultAnswer, defaultAnswer));
            }
            await next();
        });

        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            const welcomeText =
                'Сайн байна уу! Та ажлын байрны туслах чатботтой холбогдлоо. 🤗';
            for (let cnt = 0; cnt < membersAdded.length; ++cnt) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(MessageFactory.text(welcomeText, welcomeText));
                    await context.sendActivity(MessageFactory.text(defaultAnswer, defaultAnswer));
                }
            }
            await next();
        });
    }
}

module.exports.EchoBot = EchoBot;
