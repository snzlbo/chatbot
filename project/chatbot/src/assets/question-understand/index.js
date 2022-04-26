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
    if (this.getTypeOfQuestion() == 1) {
      this.queryNumber = 1
      const keyword = this.contextText.substring(0, this.contextText.search('ажлын байрны')).trim().split('-д')
      return keyword
    }
    else {
      this.queryNumber = 404
      
    }
  }

  getQueryNumber() {
    return this.queryNumber;
  }
}

module.exports.QuestionUnderstand = QuestionUnderstand;
