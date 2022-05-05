const { Router } = require('express')
const useQuestionUndestand = require('./get')

const router = Router()

router.get('/', useQuestionUndestand.getQuestion)
// router.get('/:sentence', useQuestionUndestand.getQuestion)


module.exports = router