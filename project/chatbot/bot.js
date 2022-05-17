const { ActivityHandler, MessageFactory, ActivityTypes } = require('botbuilder');
const { QuestionUnderstand } = require('./src/assets/question-understand/index');
const { ApiHelper } = require('./src/assets/bot-api/index')
const { CardBuilder } = require('./src/card/index')
const welcome = require('./src/card/welcome')


class EchoBot extends ActivityHandler {
    constructor() {
        super();
        const noResponse =
            'Уучлаарай таны асуултад хариулт олдсонгүй.'
        this.onMessage(async (context, next) => {
            const question = new QuestionUnderstand(context.activity.text);
            const api = new ApiHelper(question.findKeyWord(), question.getQueryNumber())
            console.log('keyword: ' + api.keyword + ' quest: ' + question.getQueryNumber())
            var responseBody = await api.responseBack()
            console.log('response:' + responseBody)
            if (typeof (responseBody) != 'undefined') {
                if ((responseBody.length !== 0)) {
                    const view = new CardBuilder(responseBody);
                    switch (question.getQueryNumber()) {
                        case 1:
                            var content = view.createAdvertisementCard()
                            for (let index = 0; index < content.length; index++) {
                                await context.sendActivity({
                                    attachments: [content[index]]
                                })
                            }
                            break
                        case 2:
                            await context.sendActivity({
                                attachments: [view.createListCard(api.keyword)]
                            })
                            break
                        case 3:
                            var content = view.createAdvertisementCard()
                            for (let index = 0; index < content.length; index++) {
                                await context.sendActivity({
                                    attachments: [content[index]]
                                })
                            }
                            break
                        case 4:
                            await context.sendActivity({
                                attachments: [view.createSalaryListCard(api.keyword[0])]
                            })
                            break
                        case 404:
                            await context.sendActivity(
                                MessageFactory.text(noResponse, noResponse)
                            )
                            await context.sendActivity({
                                attachments: [welcome.questionsCard()]
                            });
                            break
                        default:
                            await context.sendActivity(
                                MessageFactory.text(noResponse, noResponse)
                            )
                            await context.sendActivity({
                                attachments: [welcome.questionsCard()]
                            });
                            break
                    }
                }
                else {
                    switch (question.getQueryNumber()) {
                        case 1:
                            const tempApi = new ApiHelper(api.keyword[0], 2)
                            var secondAnswer = await tempApi.responseBack()
                            const view = new CardBuilder(secondAnswer);
                            var responseText = 'Уучлаарай, ' + api.keyword[0] + ' байгууллагад' + api.keyword[1] + ' ажлын байр олдсонгүй.'
                            if (secondAnswer === undefined)
                                break
                            await context.sendActivity(
                                MessageFactory.text(responseText, responseText)
                            )
                            await context.sendActivity({
                                attachments: [view.createListCard(api.keyword[0])]
                            })
                            break
                        default:
                            await context.sendActivity(
                                MessageFactory.text('Уучлаарай таны асуултад ажлын байр олдсонгүй.')
                            )
                            await context.sendActivity({
                                attachments: [welcome.questionsCard()]
                            })
                            break
                    }
                }
            }
            else {
                await context.sendActivity(MessageFactory.text(noResponse, noResponse));
                await context.sendActivity({
                    attachments: [welcome.questionsCard()]
                });
            }
            await next();
        });

        this.onMembersAdded(async (context, next) => {
            const membersAdded = context.activity.membersAdded;
            const welcomeText =
                'Сайн байна уу! Та ажлын байрны туслах чатботтой холбогдлоо. 🤗 Хүссэн ажлын байрны мэдээллийг цаг алдалгүй аваарай';
            for (let cnt = 0; cnt < membersAdded.length; ++cnt) {
                if (membersAdded[cnt].id !== context.activity.recipient.id) {
                    await context.sendActivity(MessageFactory.text(welcomeText, welcomeText));
                    await context.sendActivity({
                        attachments: [welcome.questionsCard()]
                    });
                }
            }
            await next();
        });
    }
}

module.exports.EchoBot = EchoBot;
