from PL_Main import translator


sentence = str(input('Please give me a sentence: '))
for i in range(0, len(sentence.split(' '))):
    print(translator(sentence.split(' ')[i]), end=' ')