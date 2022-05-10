class QuestionUnderstand {
  constructor(contextText) {
    this.contextText = contextText;
    this.queryNumber = 0;
  }

  getTypeOfQuestion(text) {
    if (this.contextText.search('ажлын байр') != -1) return 1
    else return 404
  }

  findKeyWord() {
    switch (this.getTypeOfQuestion()) {
      case 1:
        this.queryNumber = 1
        const keyword = this.contextText.substring(0, this.contextText.search('ажлын байр')).trim().split('-д')
        return keyword
        break
      default:
        this.queryNumber = 404
        return null
    }
  }

  getQueryNumber() {
    return this.queryNumber;
  }
}

module.exports.QuestionUnderstand = QuestionUnderstand;
